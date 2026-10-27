import Foundation

/// Client for the Jarvis edge function (backend/supabase/functions/jarvis).
struct JarvisAPI {
    struct Request: Encodable {
        let input: String
        /// Opaque conversation state from the previous response, sent back byte-for-byte.
        let history: String?
        let context: DriveContext
    }

    struct Response: Decodable {
        let reply: String
        let actions: [Action]
        let history: String
    }

    struct Action: Decodable, Equatable {
        enum Kind: String, Decodable {
            case navigate, call
            case endConversation = "end_conversation"
        }

        let type: Kind
        let destination: String?
        let latitude: Double?
        let longitude: Double?
        let contact: String?
        let phoneNumber: String?
    }

    struct ServerError: Decodable {
        let error: String
        let resetHistory: Bool?
    }

    enum Failure: LocalizedError {
        case notConfigured
        case server(status: Int, message: String, resetHistory: Bool)

        var errorDescription: String? {
            switch self {
            case .notConfigured: return "Jarvis isn't set up yet. Add the server address in the app's settings."
            case let .server(_, message, _): return message
            }
        }
    }

    let endpoint: URL
    let sharedSecret: String

    @MainActor
    init(settings: AppSettings) throws {
        guard settings.isConfigured, let url = URL(string: settings.backendURL) else { throw Failure.notConfigured }
        endpoint = url
        sharedSecret = settings.sharedSecret
    }

    func send(_ body: Request) async throws -> Response {
        var request = URLRequest(url: endpoint, timeoutInterval: 50)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.setValue(sharedSecret, forHTTPHeaderField: "x-jarvis-key")
        request.httpBody = try JSONEncoder().encode(body)

        let (data, response) = try await URLSession.shared.data(for: request)
        let status = (response as? HTTPURLResponse)?.statusCode ?? 0
        guard status == 200 else {
            let detail = try? JSONDecoder().decode(ServerError.self, from: data)
            throw Failure.server(
                status: status,
                message: detail?.error ?? "Server error \(status)",
                resetHistory: detail?.resetHistory ?? false
            )
        }
        return try JSONDecoder().decode(Response.self, from: data)
    }
}

/// What Jarvis knows about the drive, sent with every utterance.
struct DriveContext: Encodable {
    struct Location: Encodable {
        let latitude: Double
        let longitude: Double
        let accuracyMeters: Double
    }

    struct Event: Encodable {
        let title: String
        let start: String
        let location: String?
    }

    let now: String
    let timeZone: String
    let location: Location?
    let inCar: Bool
    let upcomingEvents: [Event]
}
