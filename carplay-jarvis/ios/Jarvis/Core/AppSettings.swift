import Combine
import Foundation
import Security
import Speech

/// User-editable settings. The backend secret lives in the Keychain; everything
/// else in UserDefaults.
@MainActor
final class AppSettings: ObservableObject {
    static let shared = AppSettings()

    private let defaults = UserDefaults.standard

    /// Full URL of the edge function, e.g. https://abcd.supabase.co/functions/v1/jarvis
    @Published var backendURL: String { didSet { defaults.set(backendURL, forKey: Keys.backendURL) } }
    @Published var sharedSecret: String { didSet { Keychain.set(sharedSecret, for: Keys.sharedSecret) } }
    /// Speech-recognition and voice language, e.g. "en-US".
    @Published var localeIdentifier: String { didSet { defaults.set(localeIdentifier, forKey: Keys.locale) } }
    /// Empty means the system default voice for `localeIdentifier`.
    @Published var voiceIdentifier: String { didSet { defaults.set(voiceIdentifier, forKey: Keys.voice) } }
    /// Keep listening for a follow-up after each answer.
    @Published var followUpListening: Bool { didSet { defaults.set(followUpListening, forKey: Keys.followUp) } }

    var isConfigured: Bool { URL(string: backendURL)?.scheme == "https" && !sharedSecret.isEmpty }

    private init() {
        backendURL = defaults.string(forKey: Keys.backendURL) ?? ""
        sharedSecret = Keychain.get(Keys.sharedSecret) ?? ""
        localeIdentifier = defaults.string(forKey: Keys.locale) ?? Self.defaultLocale()
        voiceIdentifier = defaults.string(forKey: Keys.voice) ?? ""
        followUpListening = defaults.object(forKey: Keys.followUp) as? Bool ?? true
    }

    /// The phone's language if Apple's recogniser supports it, otherwise US English.
    private static func defaultLocale() -> String {
        let preferred = Locale.current.identifier(.bcp47)
        let supported = SFSpeechRecognizer.supportedLocales().map { $0.identifier(.bcp47) }
        return supported.contains(preferred) ? preferred : "en-US"
    }

    private enum Keys {
        static let backendURL = "backendURL"
        static let sharedSecret = "jarvis.sharedSecret"
        static let locale = "localeIdentifier"
        static let voice = "voiceIdentifier"
        static let followUp = "followUpListening"
    }
}

private enum Keychain {
    static func set(_ value: String, for key: String) {
        let query: [String: Any] = [kSecClass as String: kSecClassGenericPassword, kSecAttrAccount as String: key]
        SecItemDelete(query as CFDictionary)
        guard !value.isEmpty else { return }
        var item = query
        item[kSecValueData as String] = Data(value.utf8)
        // Readable while the phone is locked, which is the normal state in the car.
        item[kSecAttrAccessible as String] = kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly
        SecItemAdd(item as CFDictionary, nil)
    }

    static func get(_ key: String) -> String? {
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrAccount as String: key,
            kSecReturnData as String: true,
            kSecMatchLimit as String: kSecMatchLimitOne,
        ]
        var result: AnyObject?
        guard SecItemCopyMatching(query as CFDictionary, &result) == errSecSuccess, let data = result as? Data else {
            return nil
        }
        return String(data: data, encoding: .utf8)
    }
}
