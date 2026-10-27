import CarPlay
import Combine
import Foundation

/// The hands-free loop shared by the phone UI and CarPlay:
/// listen -> think (backend) -> speak -> run actions -> listen again.
@MainActor
final class ConversationEngine: ObservableObject {
    static let shared = ConversationEngine()

    enum Phase: Equatable {
        case idle, listening, thinking, speaking

        var isActive: Bool { self != .idle }
    }

    struct Line: Identifiable, Equatable {
        enum Speaker { case driver, jarvis, system }
        let id = UUID()
        let speaker: Speaker
        let text: String
    }

    @Published private(set) var phase: Phase = .idle
    @Published private(set) var lines: [Line] = []
    @Published private(set) var partialTranscript = ""

    /// Set by the CarPlay scene delegate while the car is connected.
    weak var carPlayScene: CPTemplateApplicationScene?

    private let listener = SpeechListener()
    private let speaker = SpeechSpeaker()
    private let earcons = Earcons()
    private let context = ContextProvider()
    private let settings = AppSettings.shared
    private var loop: Task<Void, Never>?

    /// Opaque backend state for the current conversation; dropped when it ends.
    private var history: String?

    private static let stopPhrases: Set<String> = [
        "stop", "cancel", "never mind", "nevermind", "that's all", "thats all", "thank you", "thanks",
        "goodbye", "bye", "no thanks", "nothing",
    ]

    private init() {
        listener.onPartial = { [weak self] text in self?.partialTranscript = text }
    }

    /// Starts a conversation. With `prompt`, Jarvis answers it first instead of listening.
    func start(prompt: String? = nil) {
        guard loop == nil else { return }
        loop = Task { [weak self] in
            await self?.run(firstPrompt: prompt)
        }
    }

    func stop() {
        loop?.cancel()
        listener.cancel()
        speaker.stop()
        earcons.stop() // also completes a pending listen cue
    }

    func toggle() {
        phase.isActive ? stop() : start()
    }

    // MARK: - Loop

    private func run(firstPrompt: String?) async {
        history = nil
        var pendingPrompt = firstPrompt
        var deferredActions: [JarvisAPI.Action] = []
        context.startUpdating()

        do {
            let api = try JarvisAPI(settings: settings)
            try AudioSessionController.activate()

            conversation: while !Task.isCancelled {
                let utterance: String
                if let prompt = pendingPrompt {
                    utterance = prompt
                    pendingPrompt = nil
                } else {
                    phase = .listening
                    partialTranscript = ""
                    await earcons.playListenCue()
                    earcons.stop()
                    guard !Task.isCancelled,
                          let heard = try await listener.listen(locale: Locale(identifier: settings.localeIdentifier))
                    else { break }
                    utterance = heard
                }
                partialTranscript = ""
                append(.driver, utterance)

                if Self.isStopPhrase(utterance) {
                    await say("Okay.")
                    break
                }

                phase = .thinking
                earcons.startThinking()
                let response: JarvisAPI.Response
                do {
                    response = try await api.send(.init(
                        input: utterance,
                        history: history,
                        context: context.snapshot(inCar: carPlayScene != nil)
                    ))
                } catch let JarvisAPI.Failure.server(_, _, resetHistory) where resetHistory {
                    history = nil
                    earcons.stop()
                    await say("Sorry, something went wrong. Let's start over. What do you need?")
                    continue
                }
                earcons.stop()
                guard !Task.isCancelled else { break }
                history = response.history

                await say(response.reply)

                for action in response.actions {
                    switch action.type {
                    case .endConversation:
                        break conversation
                    case .navigate, .call:
                        // Maps and Phone take over the audio, so finish first and run these after.
                        deferredActions.append(action)
                    }
                }
                if !deferredActions.isEmpty || !settings.followUpListening { break }
            }
        } catch _ where Task.isCancelled {
            // Stopped by the driver; URLSession reports this as URLError.cancelled.
        } catch {
            earcons.stop()
            let message = (error as? LocalizedError)?.errorDescription ?? "I couldn't reach the server."
            append(.system, message)
            if (try? AudioSessionController.activate()) != nil {
                await say(message)
            }
        }

        listener.cancel()
        speaker.stop()
        earcons.stop()
        context.stopUpdating()
        AudioSessionController.deactivate()
        history = nil
        phase = .idle
        loop = nil

        let runner = ActionRunner(carPlayScene: carPlayScene)
        for action in deferredActions {
            if let problem = await runner.perform(action) {
                append(.system, problem)
            }
        }
    }

    private func say(_ text: String) async {
        guard !text.isEmpty, !Task.isCancelled else { return }
        phase = .speaking
        append(.jarvis, text)
        await speaker.speak(
            text,
            language: settings.localeIdentifier,
            voiceIdentifier: settings.voiceIdentifier
        )
    }

    private func append(_ speaker: Line.Speaker, _ text: String) {
        lines.append(Line(speaker: speaker, text: text))
        if lines.count > 100 { lines.removeFirst(lines.count - 100) }
    }

    static func isStopPhrase(_ text: String) -> Bool {
        let normalized = text.lowercased()
            .trimmingCharacters(in: .punctuationCharacters.union(.whitespaces))
            .replacingOccurrences(of: "’", with: "'")
        let withoutName = normalized.replacingOccurrences(of: ", jarvis", with: "")
            .replacingOccurrences(of: " jarvis", with: "")
        return stopPhrases.contains(normalized) || stopPhrases.contains(withoutName)
    }
}
