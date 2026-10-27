// Tool definitions and server-side executors for Jarvis.
//
// Two kinds of tools:
//   - server tools: executed here (weather) or by Anthropic (web search);
//   - device actions: Claude asks for them, we queue them, and the iPhone runs
//     them after Jarvis has finished speaking (navigation, phone calls, ending
//     the conversation). The phone owns these because only it can open Maps on
//     the CarPlay screen or look up the user's contacts.

import type Anthropic from "@anthropic-ai/sdk";

export type DeviceAction =
  | { type: "navigate"; destination: string; latitude?: number; longitude?: number }
  | { type: "call"; contact?: string; phoneNumber?: string }
  | { type: "end_conversation" };

export interface Coordinates {
  latitude: number;
  longitude: number;
}

export const DEVICE_ACTION_TOOLS = new Set(["start_navigation", "place_call", "end_conversation"]);

// Kept in a fixed order so the tool block of the prompt stays cacheable.
export const TOOLS: Anthropic.Beta.BetaToolUnion[] = [
  {
    type: "web_search_20260209",
    name: "web_search",
    max_uses: 3,
  },
  {
    name: "get_weather",
    description:
      "Current conditions and today/tomorrow forecast. Omit `place` to use the driver's current location.",
    strict: true,
    input_schema: {
      type: "object",
      properties: {
        place: {
          type: "string",
          description: "City or place name, e.g. 'Dilijan'. Empty string means the driver's location.",
        },
      },
      required: ["place"],
      additionalProperties: false,
    },
  },
  {
    name: "start_navigation",
    description:
      "Start Apple Maps turn-by-turn directions on the car screen. Use a specific address, a named place, or a category search such as 'nearest gas station'. This ends the conversation so Maps can take over.",
    strict: true,
    input_schema: {
      type: "object",
      properties: {
        destination: { type: "string", description: "Address, place name, or search phrase." },
      },
      required: ["destination"],
      additionalProperties: false,
    },
  },
  {
    name: "place_call",
    description:
      "Call someone from the driver's contacts by name, or a phone number. This ends the conversation.",
    strict: true,
    input_schema: {
      type: "object",
      properties: {
        contact: { type: "string", description: "Contact name as the driver said it, or empty." },
        phone_number: { type: "string", description: "Phone number in international format, or empty." },
      },
      required: ["contact", "phone_number"],
      additionalProperties: false,
    },
  },
  {
    name: "end_conversation",
    description: "Call when the driver is done (says thanks, goodbye, that's all, stop).",
    strict: true,
    input_schema: { type: "object", properties: {}, required: [], additionalProperties: false },
  },
];

/** Turns a device-action tool call into the action the phone will run. */
export function toDeviceAction(name: string, input: Record<string, unknown>): DeviceAction | null {
  const str = (v: unknown) => (typeof v === "string" && v.trim() !== "" ? v.trim() : undefined);
  switch (name) {
    case "start_navigation": {
      const destination = str(input.destination);
      return destination ? { type: "navigate", destination } : null;
    }
    case "place_call": {
      const contact = str(input.contact);
      const phoneNumber = str(input.phone_number);
      return contact || phoneNumber ? { type: "call", contact, phoneNumber } : null;
    }
    case "end_conversation":
      return { type: "end_conversation" };
    default:
      return null;
  }
}

// Open-Meteo: free, no API key. https://open-meteo.com/en/docs
const WEATHER_CODES: Record<number, string> = {
  0: "clear sky", 1: "mainly clear", 2: "partly cloudy", 3: "overcast", 45: "fog", 48: "freezing fog",
  51: "light drizzle", 53: "drizzle", 55: "heavy drizzle", 61: "light rain", 63: "rain", 65: "heavy rain",
  66: "freezing rain", 67: "heavy freezing rain", 71: "light snow", 73: "snow", 75: "heavy snow",
  77: "snow grains", 80: "rain showers", 81: "heavy rain showers", 82: "violent rain showers",
  85: "snow showers", 86: "heavy snow showers", 95: "thunderstorm", 96: "thunderstorm with hail",
  99: "severe thunderstorm with hail",
};

export async function getWeather(
  place: string,
  driverLocation: Coordinates | undefined,
  fetchImpl: typeof fetch = fetch,
): Promise<string> {
  let coords = driverLocation;
  let label = "the driver's location";
  if (place.trim() !== "") {
    const geo = await fetchImpl(
      `https://geocoding-api.open-meteo.com/v1/search?count=1&name=${encodeURIComponent(place)}`,
    );
    if (!geo.ok) throw new Error(`geocoding failed: HTTP ${geo.status}`);
    const hit = (await geo.json()).results?.[0];
    if (!hit) return JSON.stringify({ error: `No place found named "${place}".` });
    coords = { latitude: hit.latitude, longitude: hit.longitude };
    label = [hit.name, hit.admin1, hit.country].filter(Boolean).join(", ");
  }
  if (!coords) return JSON.stringify({ error: "The driver's location is unavailable; ask which city." });

  const url = "https://api.open-meteo.com/v1/forecast?" + new URLSearchParams({
    latitude: String(coords.latitude),
    longitude: String(coords.longitude),
    current: "temperature_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m",
    daily: "weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max",
    timezone: "auto",
    forecast_days: "2",
  });
  const res = await fetchImpl(url);
  if (!res.ok) throw new Error(`weather failed: HTTP ${res.status}`);
  const w = await res.json();
  const day = (i: number) => ({
    conditions: WEATHER_CODES[w.daily.weather_code[i]] ?? "unknown",
    high_c: w.daily.temperature_2m_max[i],
    low_c: w.daily.temperature_2m_min[i],
    precipitation_chance_pct: w.daily.precipitation_probability_max[i],
  });
  return JSON.stringify({
    place: label,
    now: {
      conditions: WEATHER_CODES[w.current.weather_code] ?? "unknown",
      temperature_c: w.current.temperature_2m,
      feels_like_c: w.current.apparent_temperature,
      wind_kmh: w.current.wind_speed_10m,
      precipitation_mm: w.current.precipitation,
    },
    today: day(0),
    tomorrow: day(1),
  });
}
