import AVFoundation
import Combine
import Contacts
import CoreLocation
import EventKit
import Speech

/// Asks for everything Jarvis uses, once, from the phone UI. In the car there
/// is no way to answer a permission prompt, so this must happen beforehand.
@MainActor
final class Permissions: NSObject, ObservableObject, CLLocationManagerDelegate {
    static let shared = Permissions()

    @Published private(set) var speech = false
    @Published private(set) var microphone = false
    @Published private(set) var location = false
    @Published private(set) var calendar = false
    @Published private(set) var contacts = false

    /// Speech and microphone are required; the rest only add context.
    var canTalk: Bool { speech && microphone }

    private let locationManager = CLLocationManager()

    override private init() {
        super.init()
        locationManager.delegate = self
        refresh()
    }

    func refresh() {
        speech = SFSpeechRecognizer.authorizationStatus() == .authorized
        microphone = AVAudioApplication.shared.recordPermission == .granted
        location = [.authorizedWhenInUse, .authorizedAlways].contains(locationManager.authorizationStatus)
        calendar = EKEventStore.authorizationStatus(for: .event) == .fullAccess
        contacts = CNContactStore.authorizationStatus(for: .contacts) == .authorized
    }

    func requestAll() async {
        _ = await Self.requestSpeech()
        _ = await AVAudioApplication.requestRecordPermission()
        if locationManager.authorizationStatus == .notDetermined {
            locationManager.requestWhenInUseAuthorization()
        }
        _ = try? await EKEventStore().requestFullAccessToEvents()
        _ = try? await CNContactStore().requestAccess(for: .contacts)
        refresh()
    }

    /// The callback arrives on a background queue, so this must not be main-actor isolated.
    private nonisolated static func requestSpeech() async -> SFSpeechRecognizerAuthorizationStatus {
        await withCheckedContinuation { continuation in
            SFSpeechRecognizer.requestAuthorization { continuation.resume(returning: $0) }
        }
    }

    nonisolated func locationManagerDidChangeAuthorization(_ manager: CLLocationManager) {
        Task { @MainActor in self.refresh() }
    }
}
