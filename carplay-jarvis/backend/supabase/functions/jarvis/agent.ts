// The Jarvis agent loop: one driver utterance in, one spoken reply (plus any
// device actions) out.
//
// Conversation history is returned to the phone as an opaque JSON string and
// sent back unchanged on the next turn. It is only ever appended to, never
// trimmed or edited, because Claude's thinking blocks are bound to the exact
// history that produced them.

import type Anthropic from "@anthropic-ai/sdk";
import {
  type Coordinates,
  DEVICE_ACTION_TOOLS,
  type DeviceAction,
  getWeather,
  toDeviceAction,
  TOOLS,
} from "./tools.ts";

export interface CalendarEvent {
  title: string;
  start: string; // ISO 8601
  location?: string;
}

export interface DriveContext {
  now: string; // ISO 8601
  timeZone: string; // IANA, e.g. "Asia/Yerevan"
  location?: Coordinates & { accuracyMeters?: number };
  inCar: boolean;
  upcomingEvents?: CalendarEvent[];
}

export interface AgentRequest {
  input: string;
  history?: string;
  context: DriveContext;
}

export interface AgentResult {
  reply: string;
  actions: DeviceAction[];
  history: string;
}

export interface AgentOptions {
  model: string;
  /** Injected so tests can stub the API. */
  createMessage: (
    params: Anthropic.Beta.MessageCreateParamsNonStreaming,
  ) => Promise<Anthropic.Beta.BetaMessage>;
  fetchImpl?: typeof fetch;
}

// Models that accept the server-side `fallbacks: "default"` parameter.
const FALLBACK_MODELS = new Set(["claude-opus-5-5", "claude-opus-5", "claude-fable-5-1", "claude-sonnet-5-5"]);
const MAX_ROUNDS = 6;

const SYSTEM_PROMPT = `You are Jarvis, a personal voice assistant. The user is usually driving and talks to you through CarPlay; everything you write is read aloud by a text-to-speech voice and nothing is shown on screen.

How to answer:
- Latency-sensitive; begin your visible answer immediately.
- Speak like a calm, capable assistant: one to three short sentences unless the driver asks for detail.
- Plain spoken language only. No markdown, lists, emoji, URLs, or symbols the voice would read out. Say numbers the way a person would ("about twenty minutes", "eighteen degrees").
- Answer in the language the driver used.
- If the request is ambiguous, ask one short question instead of guessing.

Tools:
- get_weather for weather, web_search for news, facts, opening hours, prices, scores and anything time-sensitive. Never claim to have searched when you did not.
- start_navigation and place_call run on the driver's phone after you finish speaking. When you use one, also say what you are doing ("Starting directions to the airport.").
- end_conversation when the driver is done; then reply with a brief sign-off.
- The <context> block in each driver turn carries the local time, the driver's position and upcoming calendar events. Use it; don't recite it.

Safety:
- The driver's attention belongs on the road. Keep it brief, never ask them to look at or touch the phone, and suggest pulling over for anything that needs reading or typing.`;

function formatContext(ctx: DriveContext): string {
  const tz = isValidTimeZone(ctx.timeZone) ? ctx.timeZone : "UTC";
  const when = (iso: string, opts: Intl.DateTimeFormatOptions) => {
    const d = new Date(iso);
    return Number.isNaN(d.getTime()) ? iso : new Intl.DateTimeFormat("en-GB", { timeZone: tz, ...opts }).format(d);
  };
  const lines = [
    `Local time: ${when(ctx.now, { dateStyle: "full", timeStyle: "short" })} (${tz})`,
    ctx.location
      ? `Driver position: ${ctx.location.latitude.toFixed(5)}, ${ctx.location.longitude.toFixed(5)}` +
        (ctx.location.accuracyMeters != null ? ` (±${Math.round(ctx.location.accuracyMeters)} m)` : "")
      : "Driver position: unavailable",
    `In the car: ${ctx.inCar ? "yes" : "no (using the phone)"}`,
  ];
  const events = ctx.upcomingEvents ?? [];
  if (events.length > 0) {
    lines.push("Upcoming calendar events:");
    for (const e of events.slice(0, 5)) {
      lines.push(
        `- ${when(e.start, { weekday: "short", hour: "2-digit", minute: "2-digit" })} ${e.title}` +
          (e.location ? ` at ${e.location}` : ""),
      );
    }
  } else {
    lines.push("Upcoming calendar events: none in the next 24 hours, or calendar access is off");
  }
  return `<context>\n${lines.join("\n")}\n</context>`;
}

function isValidTimeZone(tz: string): boolean {
  try {
    new Intl.DateTimeFormat("en", { timeZone: tz });
    return true;
  } catch {
    return false;
  }
}

function spokenText(content: Anthropic.Beta.BetaContentBlock[]): string {
  return content
    .filter((b): b is Anthropic.Beta.BetaTextBlock => b.type === "text")
    .map((b) => b.text)
    .join(" ")
    .replace(/\s+/g, " ")
    .trim();
}

export async function runAgent(req: AgentRequest, opts: AgentOptions): Promise<AgentResult> {
  const fetchImpl = opts.fetchImpl ?? fetch;
  const messages: Anthropic.Beta.BetaMessageParam[] = req.history ? JSON.parse(req.history) : [];
  messages.push({
    role: "user",
    content: [{ type: "text", text: `${formatContext(req.context)}\n\n${req.input}` }],
  });

  const useFallbacks = FALLBACK_MODELS.has(opts.model);
  const actions: DeviceAction[] = [];
  let reply = "";

  for (let round = 0; round < MAX_ROUNDS; round++) {
    const params: Anthropic.Beta.MessageCreateParamsNonStreaming = {
      model: opts.model,
      max_tokens: 8000,
      system: [{ type: "text", text: SYSTEM_PROMPT, cache_control: { type: "ephemeral" } }],
      tools: TOOLS,
      output_config: { effort: "low" },
      messages,
      ...(useFallbacks ? { betas: ["server-side-fallback-2026-07-01"], fallbacks: "default" as const } : {}),
    };

    const response = await opts.createMessage(params);
    // Echo the assistant turn back verbatim, thinking and fallback blocks included.
    messages.push({ role: "assistant", content: response.content as Anthropic.Beta.BetaContentBlockParam[] });

    if (response.stop_reason === "refusal") {
      reply = "Sorry, I can't help with that one.";
      break;
    }
    if (response.stop_reason === "pause_turn") {
      // A long server-side web search paused; re-sending resumes it.
      continue;
    }
    if (response.stop_reason === "tool_use") {
      const results: Anthropic.Beta.BetaToolResultBlockParam[] = [];
      for (const block of response.content) {
        if (block.type !== "tool_use") continue;
        const input = (block.input ?? {}) as Record<string, unknown>;
        try {
          if (DEVICE_ACTION_TOOLS.has(block.name)) {
            const action = toDeviceAction(block.name, input);
            if (!action) throw new Error("missing destination or contact");
            actions.push(action);
            results.push({
              type: "tool_result",
              tool_use_id: block.id,
              content: action.type === "end_conversation"
                ? "Conversation will end after your reply."
                : "Queued. It runs on the driver's phone right after you finish speaking.",
            });
          } else if (block.name === "get_weather") {
            const place = typeof input.place === "string" ? input.place : "";
            results.push({
              type: "tool_result",
              tool_use_id: block.id,
              content: await getWeather(place, req.context.location, fetchImpl),
            });
          } else {
            throw new Error(`unknown tool ${block.name}`);
          }
        } catch (err) {
          results.push({
            type: "tool_result",
            tool_use_id: block.id,
            is_error: true,
            content: err instanceof Error ? err.message : String(err),
          });
        }
      }
      // All results go back in a single user turn.
      messages.push({ role: "user", content: results });
      continue;
    }

    reply = spokenText(response.content);
    break;
  }

  if (reply === "") {
    reply = actions.some((a) => a.type === "end_conversation") ? "Okay." : "Sorry, I lost my train of thought. Could you say that again?";
  }
  return { reply, actions, history: JSON.stringify(messages) };
}
