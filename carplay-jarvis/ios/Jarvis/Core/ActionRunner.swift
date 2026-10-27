import CarPlay
import Contacts
import UIKit

/// Runs the device actions Claude asked for: directions and phone calls.
@MainActor
struct ActionRunner {
    /// Set while CarPlay is connected so URLs open on the car screen.
    weak var carPlayScene: CPTemplateApplicationScene?

    /// Returns a sentence to speak if an action could not be carried out.
    func perform(_ action: JarvisAPI.Action) async -> String? {
        switch action.type {
        case .navigate:
            guard let url = mapsURL(for: action) else { return "I couldn't work out where to navigate to." }
            open(url)
            return nil
        case .call:
            let number: String?
            if let phoneNumber = action.phoneNumber {
                number = phoneNumber
            } else if let contact = action.contact {
                number = await Self.lookUpPhoneNumber(named: contact)
            } else {
                number = nil
            }
            guard let number, let url = URL(string: "tel:\(number.filter { $0.isNumber || $0 == "+" })") else {
                return "I couldn't find a number for \(action.contact ?? "that contact")."
            }
            open(url)
            return nil
        case .endConversation:
            return nil
        }
    }

    private func mapsURL(for action: JarvisAPI.Action) -> URL? {
        var components = URLComponents(string: "maps://")!
        let destination: String
        if let lat = action.latitude, let lon = action.longitude {
            destination = "\(lat),\(lon)"
        } else if let text = action.destination, !text.isEmpty {
            destination = text
        } else {
            return nil
        }
        components.queryItems = [
            URLQueryItem(name: "daddr", value: destination),
            URLQueryItem(name: "dirflg", value: "d"),
        ]
        return components.url
    }

    private func open(_ url: URL) {
        if let carPlayScene {
            carPlayScene.open(url, options: nil, completionHandler: nil)
        } else {
            UIApplication.shared.open(url)
        }
    }

    /// Best match by name: prefers mobile numbers.
    private static func lookUpPhoneNumber(named name: String) async -> String? {
        guard CNContactStore.authorizationStatus(for: .contacts) == .authorized else { return nil }
        return await Task.detached(priority: .userInitiated) { () -> String? in
            let store = CNContactStore()
            let keys = [CNContactPhoneNumbersKey, CNContactGivenNameKey, CNContactFamilyNameKey] as [CNKeyDescriptor]
            let predicate = CNContact.predicateForContacts(matchingName: name)
            guard let contacts = try? store.unifiedContacts(matching: predicate, keysToFetch: keys) else { return nil }
            let numbers = contacts.flatMap(\.phoneNumbers)
            let mobile = numbers.first { $0.label == CNLabelPhoneNumberMobile || $0.label == CNLabelPhoneNumberiPhone }
            return (mobile ?? numbers.first)?.value.stringValue
        }.value
    }
}
