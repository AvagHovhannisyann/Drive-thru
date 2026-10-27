import CarPlay
import Combine
import UIKit

/// CarPlay UI: a short list to start a conversation, then the system Voice
/// Control template while Jarvis listens, thinks and speaks. Replies are
/// spoken only; Apple's guidelines for voice-based conversational apps don't
/// allow showing answer text or images on the car screen.
@MainActor
final class CarPlaySceneDelegate: UIResponder, CPTemplateApplicationSceneDelegate {
    private var interfaceController: CPInterfaceController?
    private var voiceTemplate: CPVoiceControlTemplate?
    /// True while a present animation is running; CarPlay allows one modal at a time.
    private var isPresenting = false
    private var phaseObserver: AnyCancellable?

    private let engine = ConversationEngine.shared

    private enum StateID {
        static let listening = "listening"
        static let thinking = "thinking"
        static let speaking = "speaking"
    }

    /// Preset requests shown under the main button.
    private let quickAsks: [(title: String, symbol: String, prompt: String)] = [
        ("Brief me", "sun.max", "Give me a quick briefing: weather here, my next event, and anything I should know."),
        ("Next meeting", "calendar", "What's my next meeting and when do I need to leave?"),
        ("Find fuel", "fuelpump", "Navigate to the nearest gas station."),
        ("Find coffee", "cup.and.saucer", "Navigate to a good coffee place nearby."),
    ]

    // MARK: CPTemplateApplicationSceneDelegate

    func templateApplicationScene(
        _ templateApplicationScene: CPTemplateApplicationScene,
        didConnect interfaceController: CPInterfaceController
    ) {
        self.interfaceController = interfaceController
        engine.carPlayScene = templateApplicationScene
        interfaceController.setRootTemplate(makeRootTemplate(), animated: false) { _, _ in }

        phaseObserver = engine.$phase
            .removeDuplicates()
            .receive(on: RunLoop.main)
            .sink { [weak self] phase in self?.render(phase) }

        // Voice-based conversational apps must open in voice mode.
        engine.start()
    }

    func templateApplicationScene(
        _ templateApplicationScene: CPTemplateApplicationScene,
        didDisconnectInterfaceController interfaceController: CPInterfaceController
    ) {
        engine.stop()
        engine.carPlayScene = nil
        phaseObserver = nil
        voiceTemplate = nil
        self.interfaceController = nil
    }

    // MARK: Templates

    private func makeRootTemplate() -> CPListTemplate {
        let talk = CPListItem(
            text: "Talk to Jarvis",
            detailText: "Ask anything, get directions, call someone",
            image: UIImage(systemName: "waveform.circle.fill")
        )
        talk.handler = { [weak self] _, completion in
            self?.engine.start()
            completion()
        }

        let asks = quickAsks.map { ask -> CPListItem in
            let item = CPListItem(text: ask.title, detailText: nil, image: UIImage(systemName: ask.symbol))
            item.handler = { [weak self] _, completion in
                self?.engine.start(prompt: ask.prompt)
                completion()
            }
            return item
        }

        return CPListTemplate(
            title: "Jarvis",
            sections: [
                CPListSection(items: [talk]),
                CPListSection(items: asks, header: "Quick asks", sectionIndexTitle: nil),
            ]
        )
    }

    private func makeVoiceTemplate() -> CPVoiceControlTemplate {
        let states = [
            CPVoiceControlState(
                identifier: StateID.listening,
                titleVariants: ["Listening…", "Listening"],
                image: UIImage(systemName: "waveform"),
                repeats: true
            ),
            CPVoiceControlState(
                identifier: StateID.thinking,
                titleVariants: ["Thinking…", "Thinking"],
                image: UIImage(systemName: "ellipsis"),
                repeats: true
            ),
            CPVoiceControlState(
                identifier: StateID.speaking,
                titleVariants: ["Jarvis", "Jarvis"],
                image: UIImage(systemName: "speaker.wave.2.fill"),
                repeats: true
            ),
        ]
        return CPVoiceControlTemplate(voiceControlStates: states)
    }

    /// Shows the voice template while a conversation runs and dismisses it after.
    private func render(_ phase: ConversationEngine.Phase) {
        guard let interfaceController else { return }

        let stateID: String
        switch phase {
        case .idle:
            // If a present is still animating, its completion calls render again.
            guard let shown = voiceTemplate, !isPresenting else { return }
            voiceTemplate = nil
            // Dismissing with nothing presented raises an exception unless a completion is given.
            if interfaceController.presentedTemplate === shown {
                interfaceController.dismissTemplate(animated: true) { _, _ in }
            }
            return
        case .listening: stateID = StateID.listening
        case .thinking: stateID = StateID.thinking
        case .speaking: stateID = StateID.speaking
        }

        if let voiceTemplate {
            voiceTemplate.activateVoiceControlState(withIdentifier: stateID)
        } else if !isPresenting {
            let template = makeVoiceTemplate()
            voiceTemplate = template
            isPresenting = true
            template.activateVoiceControlState(withIdentifier: stateID)
            interfaceController.presentTemplate(template, animated: true) { [weak self] success, _ in
                guard let self else { return }
                self.isPresenting = false
                if !success { self.voiceTemplate = nil }
                // The phase may have moved on during the animation.
                self.render(self.engine.phase)
            }
        }
    }
}
