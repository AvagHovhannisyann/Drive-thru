import AVFoundation
import Speech

/// Audio session policy for CarPlay voice apps: play-and-record, default mode,
/// no mixing, and active only while a conversation is running.
enum AudioSessionController {
    static func activate() throws {
        let session = AVAudioSession.sharedInstance()
        try session.setCategory(.playAndRecord, mode: .default, options: [.allowBluetoothHFP, .defaultToSpeaker])
        try session.setActive(true)
    }

    static func deactivate() {
        // Lets music or podcasts the driver was playing resume.
        try? AVAudioSession.sharedInstance().setActive(false, options: .notifyOthersOnDeactivation)
    }
}

/// Streams the microphone into Apple's speech recogniser and returns once the
/// driver stops talking.
@MainActor
final class SpeechListener {
    enum Failure: LocalizedError {
        case unavailable(String)
        var errorDescription: String? {
            if case let .unavailable(reason) = self { return reason }
            return nil
        }
    }

    private let audioEngine = AVAudioEngine()
    private var request: SFSpeechAudioBufferRecognitionRequest?
    private var task: SFSpeechRecognitionTask?
    private var watchdog: Task<Void, Never>?
    private var continuation: CheckedContinuation<String?, Error>?
    /// Identifies the current `listen` call so late callbacks from a cancelled one are dropped.
    private var session = UUID()

    private var transcript = ""
    private var startedAt = Date()
    private var lastChangeAt = Date()

    /// Called with the partial transcript as the driver speaks.
    var onPartial: ((String) -> Void)?

    /// Returns what the driver said, or nil if they said nothing before `noSpeechTimeout`.
    func listen(
        locale: Locale,
        endOfSpeechSilence: TimeInterval = 1.2,
        noSpeechTimeout: TimeInterval = 8,
        maxDuration: TimeInterval = 30
    ) async throws -> String? {
        cancel()
        guard let recognizer = SFSpeechRecognizer(locale: locale) else {
            throw Failure.unavailable("Speech recognition doesn't support \(locale.identifier).")
        }
        guard recognizer.isAvailable else { throw Failure.unavailable("Speech recognition is unavailable right now.") }

        let request = SFSpeechAudioBufferRecognitionRequest()
        request.shouldReportPartialResults = true
        request.addsPunctuation = true
        if recognizer.supportsOnDeviceRecognition { request.requiresOnDeviceRecognition = true }
        self.request = request

        let input = audioEngine.inputNode
        input.removeTap(onBus: 0)
        input.installTap(onBus: 0, bufferSize: 1024, format: input.outputFormat(forBus: 0)) { @Sendable buffer, _ in
            request.append(buffer)
        }
        audioEngine.prepare()
        try audioEngine.start()

        transcript = ""
        startedAt = Date()
        lastChangeAt = Date()
        let session = UUID()
        self.session = session

        return try await withCheckedThrowingContinuation { continuation in
            self.continuation = continuation
            self.task = recognizer.recognitionTask(with: request) { @Sendable [weak self] result, error in
                let text = result?.bestTranscription.formattedString
                let isFinal = result?.isFinal ?? false
                let failed = error != nil && result == nil
                Task { @MainActor in
                    guard let self, self.session == session else { return }
                    self.handle(text: text, isFinal: isFinal, failed: failed)
                }
            }
            self.watchdog = Task { @MainActor [weak self] in
                while !Task.isCancelled {
                    try? await Task.sleep(for: .milliseconds(150))
                    self?.checkTimeouts(silence: endOfSpeechSilence, noSpeech: noSpeechTimeout, max: maxDuration)
                }
            }
        }
    }

    /// Stops listening; a pending `listen` returns nil.
    func cancel() {
        finish(nil)
    }

    private func handle(text: String?, isFinal: Bool, failed: Bool) {
        if let text, text != transcript {
            transcript = text
            lastChangeAt = Date()
            onPartial?(text)
        }
        if isFinal || failed { finish(transcript) }
    }

    private func checkTimeouts(silence: TimeInterval, noSpeech: TimeInterval, max: TimeInterval) {
        let now = Date()
        if transcript.isEmpty {
            if now.timeIntervalSince(startedAt) > noSpeech { finish(nil) }
        } else if now.timeIntervalSince(lastChangeAt) > silence || now.timeIntervalSince(startedAt) > max {
            finish(transcript)
        }
    }

    private func finish(_ text: String?) {
        watchdog?.cancel()
        watchdog = nil
        if audioEngine.isRunning { audioEngine.stop() }
        audioEngine.inputNode.removeTap(onBus: 0)
        request?.endAudio()
        request = nil
        task?.cancel()
        task = nil

        guard let continuation else { return }
        self.continuation = nil
        let trimmed = text?.trimmingCharacters(in: .whitespacesAndNewlines) ?? ""
        continuation.resume(returning: trimmed.isEmpty ? nil : trimmed)
    }
}

/// Text-to-speech that can be awaited and interrupted.
@MainActor
final class SpeechSpeaker: NSObject, AVSpeechSynthesizerDelegate {
    private let synthesizer = AVSpeechSynthesizer()
    private var current: ObjectIdentifier?
    private var continuation: CheckedContinuation<Void, Never>?

    override init() {
        super.init()
        synthesizer.delegate = self
    }

    func speak(_ text: String, language: String, voiceIdentifier: String) async {
        stop()
        let utterance = AVSpeechUtterance(string: text)
        utterance.voice = AVSpeechSynthesisVoice(identifier: voiceIdentifier)
            ?? AVSpeechSynthesisVoice(language: language)
        utterance.prefersAssistiveTechnologySettings = false
        current = ObjectIdentifier(utterance)
        await withCheckedContinuation { continuation in
            self.continuation = continuation
            synthesizer.speak(utterance)
        }
    }

    func stop() {
        if synthesizer.isSpeaking { synthesizer.stopSpeaking(at: .immediate) }
        complete(nil)
    }

    /// Resumes the waiting caller. Callbacks for an older utterance are ignored
    /// so a late `didCancel` can't cut the next sentence short.
    private func complete(_ id: ObjectIdentifier?) {
        if let id, id != current { return }
        current = nil
        continuation?.resume()
        continuation = nil
    }

    nonisolated func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didFinish utterance: AVSpeechUtterance) {
        let id = ObjectIdentifier(utterance)
        Task { @MainActor in self.complete(id) }
    }

    nonisolated func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didCancel utterance: AVSpeechUtterance) {
        let id = ObjectIdentifier(utterance)
        Task { @MainActor in self.complete(id) }
    }
}

/// Short synthesised cues: a chirp when Jarvis starts listening and a soft
/// pulse while it is thinking, so the driver never has to look at the screen.
@MainActor
final class Earcons {
    private let engine = AVAudioEngine()
    private let player = AVAudioPlayerNode()
    private let format = AVAudioFormat(standardFormatWithSampleRate: 44_100, channels: 1)!
    private lazy var listenCue = tone([(880, 0.07), (0, 0.03), (1320, 0.09)], volume: 0.35)
    private lazy var thinkingPulse = tone([(523, 0.12), (0, 0.9)], volume: 0.12)

    init() {
        engine.attach(player)
        engine.connect(player, to: engine.mainMixerNode, format: format)
    }

    /// Plays the listening cue and returns when it has finished.
    func playListenCue() async {
        guard start() else { return }
        await withCheckedContinuation { continuation in
            player.scheduleBuffer(listenCue, at: nil, options: .interrupts, completionCallbackType: .dataPlayedBack) { @Sendable _ in
                continuation.resume()
            }
            player.play()
        }
    }

    func startThinking() {
        guard start() else { return }
        player.scheduleBuffer(thinkingPulse, at: nil, options: [.loops, .interrupts], completionHandler: nil)
        player.play()
    }

    func stop() {
        player.stop()
        if engine.isRunning { engine.stop() }
    }

    private func start() -> Bool {
        if engine.isRunning { return true }
        do {
            try engine.start()
            return true
        } catch {
            return false
        }
    }

    /// Builds a buffer from (frequency Hz, seconds) segments; 0 Hz is silence.
    private func tone(_ segments: [(Double, Double)], volume: Float) -> AVAudioPCMBuffer {
        let rate = format.sampleRate
        let frames = AVAudioFrameCount(segments.reduce(0) { $0 + Int($1.1 * rate) })
        let buffer = AVAudioPCMBuffer(pcmFormat: format, frameCapacity: frames)!
        buffer.frameLength = frames
        let samples = buffer.floatChannelData![0]
        var index = 0
        for (frequency, seconds) in segments {
            let count = Int(seconds * rate)
            let fade = min(count / 4, Int(0.01 * rate))
            for i in 0..<count {
                var value: Float = 0
                if frequency > 0 {
                    let envelope = Float(min(1, Double(min(i, count - 1 - i)) / Double(max(fade, 1))))
                    value = sin(Float(2 * Double.pi * frequency * Double(i) / rate)) * volume * envelope
                }
                samples[index + i] = value
            }
            index += count
        }
        return buffer
    }
}
