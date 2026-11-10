#!/usr/bin/env python3
"""Call one tool of the registered Blender MCP server from the terminal.

A real MCP client: it starts the stdio server exactly as Claude Code would (same
command, same environment) and speaks the MCP protocol to it. Use it when a session
has no native `mcp__blender__*` tools loaded, or to script and debug the bridge.

    PY="uvx --from mcp-for-blender==2.2.7 python tools/blender-mcp/mcp_call.py"
    $PY --list                                         # tools the server offers
    $PY get_scene_info '{"fields": ["location", "size", "settings"]}'
    $PY execute_blender_code --code 'import bpy; print(bpy.app.version_string)'
    $PY execute_blender_code --code-file my_script.py
    $PY look '{"mode": "camera", "max_size": 800}' --save-images /opt/blender-mcp/tmp

Text results go to stdout; images are written to --save-images (default: current
directory) and their paths printed. Exit code 0 = the tool call succeeded.
"""

from __future__ import annotations

import argparse
import asyncio
import base64
import json
import os
import shlex
import sys
import time
from datetime import timedelta
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def registered_command(name: str, project: Path) -> dict | None:
    """The stdio command Claude Code stores for `name` (local, then user, then project scope)."""
    def load(path: Path) -> dict:
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return {}

    config = load(Path.home() / ".claude.json")
    for servers in (
        config.get("projects", {}).get(str(project), {}).get("mcpServers", {}),
        config.get("mcpServers", {}),
        load(project / ".mcp.json").get("mcpServers", {}),
    ):
        entry = servers.get(name)
        if entry and entry.get("command"):
            return {"command": entry["command"], "args": list(entry.get("args", [])),
                    "env": dict(entry.get("env", {}))}
    return None


async def run(args: argparse.Namespace) -> int:
    if args.server_cmd:
        parts = shlex.split(args.server_cmd)
        entry = {"command": parts[0], "args": parts[1:], "env": {}}
    else:
        entry = registered_command(args.name, Path(args.project).resolve())
    if entry is None:
        print(f"no MCP server named '{args.name}' is registered with Claude Code "
              f"(run tools/blender-mcp/install.sh) and no --server-cmd was given", file=sys.stderr)
        return 2

    arguments: dict = json.loads(args.arguments) if args.arguments else {}
    if args.code_file:
        arguments["code"] = Path(args.code_file).read_text(encoding="utf-8")
    elif args.code is not None:
        arguments["code"] = args.code

    params = StdioServerParameters(command=entry["command"], args=entry["args"],
                                   env={**os.environ, **entry["env"]})
    # The server logs to stderr; keep it out of the way unless asked for.
    errlog = sys.stderr if args.verbose else open(os.devnull, "w")
    async with stdio_client(params, errlog=errlog) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            if args.list:
                for tool in (await session.list_tools()).tools:
                    summary = (tool.description or "").strip().splitlines()[0] if tool.description else ""
                    print(f"{tool.name:28} {summary[:110]}")
                return 0

            result = await session.call_tool(
                args.tool, arguments, read_timeout_seconds=timedelta(seconds=args.timeout))
            image_dir = Path(args.save_images)
            for index, item in enumerate(result.content):
                kind = getattr(item, "type", "")
                if kind == "text":
                    print(item.text)
                elif kind == "image":
                    extension = {"image/png": "png", "image/jpeg": "jpg", "image/webp": "webp"}.get(item.mimeType, "bin")
                    image_dir.mkdir(parents=True, exist_ok=True)
                    path = image_dir / f"{args.tool}_{time.strftime('%Y%m%d-%H%M%S')}_{index}.{extension}"
                    path.write_bytes(base64.b64decode(item.data))
                    print(f"[image saved: {path} ({path.stat().st_size} bytes, {item.mimeType})]")
                else:
                    print(f"[{kind or 'unknown'} content omitted]")
            return 1 if result.isError else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("tool", nargs="?", help="tool name, e.g. get_scene_info")
    parser.add_argument("arguments", nargs="?", default="", help="tool arguments as a JSON object")
    parser.add_argument("--code", help="shortcut for execute_blender_code: the Python source")
    parser.add_argument("--code-file", help="shortcut for execute_blender_code: read the source from a file")
    parser.add_argument("--list", action="store_true", help="list the server's tools and exit")
    parser.add_argument("--save-images", default=".", help="directory for images a tool returns")
    parser.add_argument("--timeout", type=int, default=240, help="seconds allowed for the call")
    parser.add_argument("--name", default=os.environ.get("BMCP_MCP_NAME", "blender"))
    parser.add_argument("--project", default=str(REPO_ROOT))
    parser.add_argument("--server-cmd", default="", help="use this stdio command instead of the registered one")
    parser.add_argument("--verbose", action="store_true", help="show the server's log output")
    args = parser.parse_args()
    if not args.list and not args.tool:
        parser.error("give a tool name or --list")
    try:
        return asyncio.run(run(args))
    except Exception as exc:  # connection refused, timeout, protocol error
        print(f"MCP call failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
