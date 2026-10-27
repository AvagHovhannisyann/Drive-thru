import SwiftUI

struct ContentView: View {
    @ObservedObject private var engine = ConversationEngine.shared
    @ObservedObject private var settings = AppSettings.shared
    @ObservedObject private var permissions = Permissions.shared
    @State private var showingSettings = false

    var body: some View {
        NavigationStack {
            VStack(spacing: 0) {
                if !settings.isConfigured || !permissions.canTalk {
                    setupBanner
                }
                transcript
                talkButton
                    .padding(.vertical, 28)
            }
            .navigationTitle("Jarvis")
            .toolbar {
                Button { showingSettings = true } label: { Image(systemName: "gearshape") }
                    .accessibilityLabel("Settings")
            }
            .sheet(isPresented: $showingSettings) { SettingsView() }
            .onAppear { permissions.refresh() }
        }
    }

    private var setupBanner: some View {
        VStack(alignment: .leading, spacing: 8) {
            if !settings.isConfigured {
                Label("Add your Jarvis server in Settings.", systemImage: "server.rack")
            }
            if !permissions.canTalk {
                Button {
                    Task { await permissions.requestAll() }
                } label: {
                    Label("Allow microphone and speech recognition", systemImage: "mic")
                }
            }
        }
        .font(.callout)
        .frame(maxWidth: .infinity, alignment: .leading)
        .padding()
        .background(.yellow.opacity(0.15))
    }

    private var transcript: some View {
        ScrollViewReader { proxy in
            List {
                ForEach(engine.lines) { line in
                    LineView(line: line).id(line.id)
                }
                if !engine.partialTranscript.isEmpty {
                    Text(engine.partialTranscript)
                        .foregroundStyle(.secondary)
                        .italic()
                        .id("partial")
                }
            }
            .listStyle(.plain)
            .overlay {
                if engine.lines.isEmpty {
                    ContentUnavailableView(
                        "Ready when you are",
                        systemImage: "car",
                        description: Text("Tap the button, or open Jarvis on your CarPlay screen.")
                    )
                }
            }
            .onChange(of: engine.lines) {
                if let last = engine.lines.last { withAnimation { proxy.scrollTo(last.id, anchor: .bottom) } }
            }
        }
    }

    private var talkButton: some View {
        Button(action: engine.toggle) {
            ZStack {
                Circle()
                    .fill(engine.phase.isActive ? Color.red.gradient : Color.accentColor.gradient)
                    .frame(width: 96, height: 96)
                    .shadow(radius: engine.phase == .listening ? 16 : 4)
                    .scaleEffect(engine.phase == .listening ? 1.08 : 1)
                    .animation(
                        engine.phase == .listening
                            ? .easeInOut(duration: 0.7).repeatForever(autoreverses: true)
                            : .default,
                        value: engine.phase
                    )
                Image(systemName: engine.phase.isActive ? "stop.fill" : "waveform")
                    .font(.system(size: 36, weight: .semibold))
                    .foregroundStyle(.white)
            }
        }
        .buttonStyle(.plain)
        .accessibilityLabel(engine.phase.isActive ? "Stop Jarvis" : "Talk to Jarvis")
        .overlay(alignment: .bottom) {
            Text(statusText)
                .font(.footnote)
                .foregroundStyle(.secondary)
                .offset(y: 24)
        }
    }

    private var statusText: String {
        switch engine.phase {
        case .idle: return "Tap to talk"
        case .listening: return "Listening…"
        case .thinking: return "Thinking…"
        case .speaking: return "Speaking…"
        }
    }
}

private struct LineView: View {
    let line: ConversationEngine.Line

    var body: some View {
        switch line.speaker {
        case .driver:
            Text(line.text)
                .frame(maxWidth: .infinity, alignment: .trailing)
                .foregroundStyle(.primary)
        case .jarvis:
            Text(line.text)
                .frame(maxWidth: .infinity, alignment: .leading)
                .foregroundStyle(Color.accentColor)
        case .system:
            Label(line.text, systemImage: "exclamationmark.triangle")
                .font(.footnote)
                .foregroundStyle(.orange)
        }
    }
}
