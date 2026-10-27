import AVFoundation
import Speech
import SwiftUI

struct SettingsView: View {
    @ObservedObject private var settings = AppSettings.shared
    @ObservedObject private var permissions = Permissions.shared
    @Environment(\.dismiss) private var dismiss

    private var voices: [AVSpeechSynthesisVoice] {
        AVSpeechSynthesisVoice.speechVoices()
            .filter { $0.language == settings.localeIdentifier }
            .sorted { ($0.quality.rawValue, $0.name) > ($1.quality.rawValue, $1.name) }
    }

    private var recognitionLocales: [String] {
        SFSpeechRecognizer.supportedLocales().map { $0.identifier(.bcp47) }.sorted()
    }

    var body: some View {
        NavigationStack {
            Form {
                Section {
                    TextField("https://<project>.supabase.co/functions/v1/jarvis", text: $settings.backendURL)
                        .textContentType(.URL)
                        .keyboardType(.URL)
                        .textInputAutocapitalization(.never)
                        .autocorrectionDisabled()
                    SecureField("Shared secret", text: $settings.sharedSecret)
                } header: {
                    Text("Server")
                } footer: {
                    Text("The edge function URL and the JARVIS_SHARED_SECRET you set when deploying it.")
                }

                Section("Voice") {
                    Picker("Language", selection: $settings.localeIdentifier) {
                        ForEach(recognitionLocales, id: \.self) { id in
                            Text(Locale.current.localizedString(forIdentifier: id) ?? id).tag(id)
                        }
                    }
                    Picker("Jarvis voice", selection: $settings.voiceIdentifier) {
                        Text("System default").tag("")
                        ForEach(voices, id: \.identifier) { voice in
                            Text(voice.quality == .premium ? "\(voice.name) (premium)" : voice.name).tag(voice.identifier)
                        }
                    }
                    Toggle("Keep listening after answers", isOn: $settings.followUpListening)
                }

                Section {
                    PermissionRow(title: "Speech recognition", granted: permissions.speech)
                    PermissionRow(title: "Microphone", granted: permissions.microphone)
                    PermissionRow(title: "Location (weather, nearby places)", granted: permissions.location)
                    PermissionRow(title: "Calendar (your next events)", granted: permissions.calendar)
                    PermissionRow(title: "Contacts (calling by name)", granted: permissions.contacts)
                    Button("Request permissions") { Task { await permissions.requestAll() } }
                } header: {
                    Text("Permissions")
                } footer: {
                    Text("Grant these on the phone before driving; prompts can't be answered on the car screen. Anything denied earlier must be changed in the Settings app.")
                }
            }
            .navigationTitle("Settings")
            .toolbar { Button("Done") { dismiss() } }
        }
    }
}

private struct PermissionRow: View {
    let title: String
    let granted: Bool

    var body: some View {
        LabeledContent(title) {
            Image(systemName: granted ? "checkmark.circle.fill" : "xmark.circle")
                .foregroundStyle(granted ? Color.green : Color.secondary)
        }
    }
}
