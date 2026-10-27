// Supabase Edge Function: POST /functions/v1/jarvis
//
// Request:  { input: string, history?: string, context: DriveContext }
// Response: { reply: string, actions: DeviceAction[], history: string }
//
// Secrets (supabase secrets set ...):
//   ANTHROPIC_API_KEY      required
//   JARVIS_SHARED_SECRET   required; the app sends it in the x-jarvis-key header
//   JARVIS_MODEL           optional, defaults to claude-opus-5-5

import Anthropic from "@anthropic-ai/sdk";
import { type DriveContext, runAgent } from "./agent.ts";

const MAX_INPUT_CHARS = 2_000;
const MAX_HISTORY_BYTES = 500_000;

const client = new Anthropic({
  apiKey: Deno.env.get("ANTHROPIC_API_KEY"),
  maxRetries: 1,
  timeout: 45_000,
});
const model = Deno.env.get("JARVIS_MODEL") ?? "claude-opus-5-5";
const sharedSecret = Deno.env.get("JARVIS_SHARED_SECRET") ?? "";

function json(status: number, body: unknown): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "content-type": "application/json" },
  });
}

function timingSafeEqual(a: string, b: string): boolean {
  const ea = new TextEncoder().encode(a);
  const eb = new TextEncoder().encode(b);
  let diff = ea.length ^ eb.length;
  for (let i = 0; i < Math.max(ea.length, eb.length); i++) diff |= (ea[i] ?? 0) ^ (eb[i] ?? 0);
  return diff === 0;
}

function parseContext(raw: unknown): DriveContext | null {
  if (typeof raw !== "object" || raw === null) return null;
  const c = raw as Record<string, unknown>;
  if (typeof c.now !== "string" || typeof c.timeZone !== "string") return null;
  const loc = c.location as Record<string, unknown> | undefined;
  const events = Array.isArray(c.upcomingEvents) ? c.upcomingEvents : [];
  return {
    now: c.now,
    timeZone: c.timeZone,
    inCar: c.inCar === true,
    location: loc && typeof loc.latitude === "number" && typeof loc.longitude === "number"
      ? {
        latitude: loc.latitude,
        longitude: loc.longitude,
        accuracyMeters: typeof loc.accuracyMeters === "number" ? loc.accuracyMeters : undefined,
      }
      : undefined,
    upcomingEvents: events
      .filter((e): e is Record<string, unknown> => typeof e === "object" && e !== null)
      .filter((e) => typeof e.title === "string" && typeof e.start === "string")
      .map((e) => ({
        title: String(e.title).slice(0, 200),
        start: String(e.start),
        location: typeof e.location === "string" ? e.location.slice(0, 200) : undefined,
      })),
  };
}

Deno.serve(async (req) => {
  if (req.method !== "POST") return json(405, { error: "POST only" });
  if (!sharedSecret || !timingSafeEqual(req.headers.get("x-jarvis-key") ?? "", sharedSecret)) {
    return json(401, { error: "unauthorized" });
  }

  let body: Record<string, unknown>;
  try {
    body = await req.json();
  } catch {
    return json(400, { error: "body must be JSON" });
  }
  const input = typeof body.input === "string" ? body.input.trim() : "";
  const context = parseContext(body.context);
  if (input === "" || input.length > MAX_INPUT_CHARS || !context) {
    return json(400, { error: "need input (1-2000 chars) and context {now, timeZone}" });
  }
  let history = typeof body.history === "string" && body.history !== "" ? body.history : undefined;
  if (history && history.length > MAX_HISTORY_BYTES) history = undefined; // start a fresh conversation

  try {
    const result = await runAgent(
      { input, history, context },
      { model, createMessage: (params) => client.beta.messages.create(params) },
    );
    return json(200, result);
  } catch (err) {
    if (err instanceof Anthropic.RateLimitError) return json(429, { error: "rate limited, try again shortly" });
    if (err instanceof Anthropic.BadRequestError) {
      console.error("bad request to Claude", err.message);
      return json(502, { error: "Claude rejected the request", resetHistory: true });
    }
    if (err instanceof Anthropic.APIError) {
      console.error("Claude API error", err.status, err.message);
      return json(502, { error: "Claude is unavailable right now" });
    }
    if (err instanceof SyntaxError) return json(400, { error: "history is not valid JSON", resetHistory: true });
    console.error("jarvis failure", err);
    return json(500, { error: "internal error" });
  }
});
