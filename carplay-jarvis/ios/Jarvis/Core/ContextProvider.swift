import CoreLocation
import EventKit
import Foundation

/// Collects location and calendar context for each request. Location updates
/// run only while a conversation is active.
@MainActor
final class ContextProvider: NSObject, CLLocationManagerDelegate {
    private let locationManager = CLLocationManager()
    private let eventStore = EKEventStore()

    override init() {
        super.init()
        locationManager.delegate = self
        locationManager.desiredAccuracy = kCLLocationAccuracyHundredMeters
    }

    func startUpdating() {
        switch locationManager.authorizationStatus {
        case .authorizedWhenInUse, .authorizedAlways: locationManager.startUpdatingLocation()
        default: break
        }
    }

    func stopUpdating() {
        locationManager.stopUpdatingLocation()
    }

    func snapshot(inCar: Bool) -> DriveContext {
        let iso = ISO8601DateFormatter()
        let location = locationManager.location.flatMap { loc -> DriveContext.Location? in
            // Ignore fixes older than ten minutes; the car has moved on.
            guard -loc.timestamp.timeIntervalSinceNow < 600 else { return nil }
            return .init(
                latitude: loc.coordinate.latitude,
                longitude: loc.coordinate.longitude,
                accuracyMeters: loc.horizontalAccuracy
            )
        }
        return DriveContext(
            now: iso.string(from: Date()),
            timeZone: TimeZone.current.identifier,
            location: location,
            inCar: inCar,
            upcomingEvents: upcomingEvents().map {
                .init(title: $0.title ?? "Untitled", start: iso.string(from: $0.startDate), location: $0.location)
            }
        )
    }

    private func upcomingEvents() -> [EKEvent] {
        guard EKEventStore.authorizationStatus(for: .event) == .fullAccess else { return [] }
        let now = Date()
        let predicate = eventStore.predicateForEvents(
            withStart: now, end: now.addingTimeInterval(24 * 3600), calendars: nil
        )
        return eventStore.events(matching: predicate)
            .filter { !$0.isAllDay }
            .sorted { $0.startDate < $1.startDate }
            .prefix(5)
            .map { $0 }
    }

    nonisolated func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {}

    nonisolated func locationManager(_ manager: CLLocationManager, didFailWithError error: Error) {}
}
