// Offline tests for the agent loop: the Claude API and Open-Meteo are stubbed.
// Run with `npm test`.

import assert from "node:assert/strict";
import { test } from "node:test";
import type Anthropic from "@anthropic-ai/sdk";
import { runAgent } from "../supabase/functions/jarvis/agent.ts";

const context = {
  now: "2026-10-27T14:30:00Z",
  timeZone: "Asia/Yerevan",
  inCar: true,
  location: { latitude: 40.1776, longitude: 44.5126, accuracyMeters: 12 },
  upcomingEvents: [{ title: "Dinner with Ani", start: "2026-10-27T16:00:00Z", location: "Lavash" }],
};

function message(
  stop_reason: Anthropic.Beta.BetaStopReason,
  content: unknown[],
): Anthropic.Beta.BetaMessage {
  return { id: "msg", type: "message", role: "assistant", model: "claude-opus-5-5", stop_reason, content } as
    unknown as Anthropic.Beta.BetaMessage;
}

const weatherFetch: typeof fetch = async (url) => {
  assert.match(String(url), /api\.open-meteo\.com/);
  return new Response(JSON.stringify({
    current: { temperature_2m: 14, apparent_temperature: 12, precipitation: 0, weather_code: 2, wind_speed_10m: 9 },
    daily: {
      weather_code: [61, 0],
      temperature_2m_max: [16, 18],
      temperature_2m_min: [7, 6],
      precipitation_probability_max: [70, 5],
    },
  }));
};

test("runs server tools, queues device actions, returns spoken reply and append-only history", async () => {
  const calls: Anthropic.Beta.MessageCreateParamsNonStreaming[] = [];
  const responses = [
    message("tool_use", [
      { type: "thinking", thinking: "", signature: "sig-1" },
      { type: "tool_use", id: "t1", name: "get_weather", input: { place: "" } },
      { type: "tool_use", id: "t2", name: "start_navigation", input: { destination: "Lavash Restaurant" } },
    ]),
    message("end_turn", [{ type: "text", text: "It's fourteen degrees and cloudy.\n Starting directions to Lavash." }]),
  ];
  const result = await runAgent(
    { input: "What's the weather, and take me to dinner", context },
    {
      model: "claude-opus-5-5",
      fetchImpl: weatherFetch,
      createMessage: async (params) => {
        calls.push(structuredClone(params));
        return responses.shift()!;
      },
    },
  );

  assert.equal(result.reply, "It's fourteen degrees and cloudy. Starting directions to Lavash.");
  assert.deepEqual(result.actions, [{ type: "navigate", destination: "Lavash Restaurant" }]);

  // Fallbacks are on for Opus 5.5 and the context block reaches the model.
  assert.equal(calls[0].fallbacks, "default");
  assert.deepEqual(calls[0].betas, ["server-side-fallback-2026-07-01"]);
  const firstUser = JSON.stringify(calls[0].messages[0]);
  assert.match(firstUser, /Asia\/Yerevan/);
  assert.match(firstUser, /Dinner with Ani/);

  // Both tool results go back in one user turn, and the thinking block is echoed unchanged.
  const second = calls[1].messages;
  assert.equal(second.length, 3);
  assert.deepEqual((second[1].content as unknown[])[0], { type: "thinking", thinking: "", signature: "sig-1" });
  const results = second[2].content as Anthropic.Beta.BetaToolResultBlockParam[];
  assert.deepEqual(results.map((r) => r.tool_use_id), ["t1", "t2"]);
  assert.match(String(results[0].content), /"temperature_c":14/);

  // The returned history extends what was sent, so the next turn is append-only.
  const history = JSON.parse(result.history);
  assert.equal(history.length, 4);
  assert.deepEqual(history.slice(0, 3), second);
});

test("continues an existing conversation and resumes pause_turn without a new user message", async () => {
  const prior = JSON.stringify([
    { role: "user", content: [{ type: "text", text: "hi" }] },
    { role: "assistant", content: [{ type: "text", text: "Hello." }] },
  ]);
  const seen: number[] = [];
  const responses = [
    message("pause_turn", [{ type: "server_tool_use", id: "s1", name: "web_search", input: { query: "x" } }]),
    message("end_turn", [{ type: "text", text: "Ararat won two nil." }]),
  ];
  const result = await runAgent(
    { input: "How did Ararat do?", history: prior, context },
    {
      model: "claude-haiku-5-5",
      createMessage: async (params) => {
        seen.push(params.messages.length);
        assert.equal(params.fallbacks, undefined); // Haiku has no server-side fallback
        return responses.shift()!;
      },
    },
  );
  assert.deepEqual(seen, [3, 4]); // second call only adds the paused assistant turn
  assert.equal(result.reply, "Ararat won two nil.");
  assert.equal(JSON.parse(result.history).length, 5);
});

test("tool errors are reported to Claude, not thrown", async () => {
  const responses = [
    message("tool_use", [{ type: "tool_use", id: "t1", name: "place_call", input: { contact: "", phone_number: "" } }]),
    message("tool_use", [{ type: "tool_use", id: "t2", name: "end_conversation", input: {} }]),
    message("end_turn", []),
  ];
  let lastParams: Anthropic.Beta.MessageCreateParamsNonStreaming | undefined;
  const result = await runAgent(
    { input: "call", context },
    {
      model: "claude-opus-5-5",
      createMessage: async (params) => {
        lastParams = params;
        return responses.shift()!;
      },
    },
  );
  const errorTurn = lastParams!.messages[2].content as Anthropic.Beta.BetaToolResultBlockParam[];
  assert.equal(errorTurn[0].is_error, true);
  assert.deepEqual(result.actions, [{ type: "end_conversation" }]);
  assert.equal(result.reply, "Okay.");
});
