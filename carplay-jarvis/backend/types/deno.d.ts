// Minimal Deno globals so `tsc` can type-check the edge function under Node.
// Deno provides the real definitions at runtime.
declare namespace Deno {
  const env: { get(key: string): string | undefined };
  function serve(handler: (req: Request) => Response | Promise<Response>): unknown;
}
