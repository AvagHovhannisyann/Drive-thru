#!/usr/bin/env python3
"""End-to-end test of the Blender MCP chain, driven through the MCP protocol itself.

    this script (MCP client)
        --stdio-->  mcp-for-blender server   (the exact command registered in Claude Code)
        --TCP 127.0.0.1:9876-->  add-on socket
        -->  the live Blender GUI running under Xvfb

It does not talk to Blender directly: every Blender action below is an MCP tool call,
so a pass proves the full path works, not merely that the port is open.

Steps
  1. initialize + list tools
  2. get_addon_status and get_scene_info (query the live scene)
  3. execute_blender_code: build a separate scene with a named cube, material,
     camera and light
  4. get_scene_info again: the new objects are reported back through MCP
  5. look: a viewport image through the scene camera, returned over MCP
  6. execute_blender_code: save a .blend copy and render a PNG (Cycles, CPU)
  7. check the files on disk, then re-open the .blend in a *separate* background
     Blender and confirm its contents and that the PNG is not blank
  8. execute_blender_code: remove the test scene from the live session again

Run it with the Python environment that already contains the `mcp` SDK:

    uvx --from mcp-for-blender==2.2.7 python tools/blender-mcp/mcp_e2e_test.py

Exit code 0 = every step passed. A JSON report is written next to the outputs.
"""

from __future__ import annotations

import argparse
import asyncio
import base64
import json
import os
import shlex
import struct
import subprocess
import sys
import time
from datetime import timedelta
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
PREFIX = "MCP_Test_"
SCENE = "MCP_Test_Scene"
MARKER = "BMCP_RESULT="


# --------------------------------------------------------------------------- #
# Code executed inside Blender through the execute_blender_code tool.
# --------------------------------------------------------------------------- #
BUILD_CODE = r'''
import json
import bmesh
import bpy
from mathutils import Vector

PREFIX, NAME = "MCP_Test_", "MCP_Test_Scene"
WIDTH, HEIGHT, SAMPLES = __WIDTH__, __HEIGHT__, __SAMPLES__
window = bpy.context.window_manager.windows[0]

# Start clean: drop whatever an earlier test run left behind.
old = bpy.data.scenes.get(NAME)
if old is not None:
    if window.scene == old:
        window.scene = next(s for s in bpy.data.scenes if s != old)
    bpy.data.scenes.remove(old)
for blocks in (bpy.data.objects, bpy.data.meshes, bpy.data.materials,
               bpy.data.cameras, bpy.data.lights, bpy.data.worlds):
    for block in [b for b in blocks if b.name.startswith(PREFIX)]:
        blocks.remove(block)

previous = window.scene.name
scene = bpy.data.scenes.new(NAME)          # a separate scene; the existing one is untouched
scene["bmcp_previous_scene"] = previous
# Show the new scene in the GUI *before* adding objects. Switching a window to a scene
# evaluates that scene once, before it is the window's active dependency graph; objects
# that already exist at that moment keep a stale matrix_world (camera at the origin ->
# blank `look`, get_scene_info reporting everything at 0,0,0). Objects added after the
# switch are evaluated by Blender's normal refresh when this script returns.
window.scene = scene

def aim(obj, target):
    obj.rotation_euler = (Vector(target) - obj.location).to_track_quat("-Z", "Y").to_euler()

def material(name, color, roughness):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = next(n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    bsdf.inputs["Base Color"].default_value = color
    bsdf.inputs["Roughness"].default_value = roughness
    mat.diffuse_color = color              # what the solid viewport shows
    return mat

# Named cube (2 m, resting on the ground) with a named material.
mesh = bpy.data.meshes.new(PREFIX + "CubeMesh")
bm = bmesh.new()
bmesh.ops.create_cube(bm, size=2.0)
bm.to_mesh(mesh)
bm.free()
cube = bpy.data.objects.new(PREFIX + "Cube", mesh)
cube.location = (0.0, 0.0, 1.0)
cube.rotation_euler = (0.0, 0.0, 0.5)
scene.collection.objects.link(cube)
cube.data.materials.append(material(PREFIX + "Material", (0.90, 0.22, 0.04, 1.0), 0.35))

# Ground plane so the light and shadow are visible in the render.
gmesh = bpy.data.meshes.new(PREFIX + "GroundMesh")
bm = bmesh.new()
bmesh.ops.create_grid(bm, x_segments=1, y_segments=1, size=12.0)
bm.to_mesh(gmesh)
bm.free()
ground = bpy.data.objects.new(PREFIX + "Ground", gmesh)
scene.collection.objects.link(ground)
ground.data.materials.append(material(PREFIX + "GroundMaterial", (0.55, 0.57, 0.60, 1.0), 0.8))

# Camera.
cam_data = bpy.data.cameras.new(PREFIX + "CameraData")
cam_data.lens = 50.0
camera = bpy.data.objects.new(PREFIX + "Camera", cam_data)
camera.location = (6.5, -6.5, 4.5)
aim(camera, (0.0, 0.0, 0.9))
scene.collection.objects.link(camera)
scene.camera = camera

# Light.
light_data = bpy.data.lights.new(PREFIX + "LightData", type="AREA")
light_data.energy = 600.0
light_data.size = 4.0
light = bpy.data.objects.new(PREFIX + "Light", light_data)
light.location = (4.0, -1.5, 6.0)
aim(light, (0.0, 0.0, 1.0))
scene.collection.objects.link(light)

# Soft sky-coloured world so nothing renders pitch black.
world = bpy.data.worlds.new(PREFIX + "World")
world.use_nodes = True
background = next(n for n in world.node_tree.nodes if n.type == "BACKGROUND")
background.inputs["Color"].default_value = (0.55, 0.70, 0.90, 1.0)
background.inputs["Strength"].default_value = 0.4
scene.world = world

# CPU rendering.
scene.render.engine = "CYCLES"
scene.cycles.device = "CPU"
scene.cycles.samples = SAMPLES
scene.render.resolution_x, scene.render.resolution_y = WIDTH, HEIGHT
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = "PNG"
scene.view_settings.view_transform = "Standard"   # show the material colour as authored


print("BMCP_RESULT=" + json.dumps({
    "scene": scene.name,
    "previous_scene": previous,
    "objects": {o.name: o.type for o in scene.objects},
    "cube_materials": [m.name for m in cube.data.materials],
    "cube_dimensions": [round(v, 3) for v in cube.dimensions],
    "camera": scene.camera.name,
    "engine": scene.render.engine,
    "cycles_device": scene.cycles.device,
    "resolution": [scene.render.resolution_x, scene.render.resolution_y],
    "blender": bpy.app.version_string,
    "background_mode": bpy.app.background,
}))
'''

SAVE_RENDER_CODE = r'''
import json
import os
import time
import bpy

NAME = "MCP_Test_Scene"
BLEND, PNG = __BLEND__, __PNG__
scene = bpy.data.scenes[NAME]
os.makedirs(os.path.dirname(BLEND), exist_ok=True)
for path in (BLEND, PNG):
    if os.path.exists(path):
        os.remove(path)

window = bpy.context.window_manager.windows[0]
scene.render.filepath = PNG
with bpy.context.temp_override(window=window):
    # copy=True writes the file without re-pointing the live session at it.
    bpy.ops.wm.save_as_mainfile(filepath=BLEND, copy=True, check_existing=False)
    started = time.time()
    bpy.ops.render.render(write_still=True, scene=NAME)
    seconds = time.time() - started

print("BMCP_RESULT=" + json.dumps({
    "blend": BLEND, "blend_bytes": os.path.getsize(BLEND),
    "png": PNG, "png_bytes": os.path.getsize(PNG),
    "render_seconds": round(seconds, 2),
    "engine": scene.render.engine, "device": scene.cycles.device,
    "samples": scene.cycles.samples,
    "session_file": bpy.data.filepath,
}))
'''

CLEANUP_CODE = r'''
import json
import bpy

PREFIX, NAME = "MCP_Test_", "MCP_Test_Scene"
window = bpy.context.window_manager.windows[0]
scene = bpy.data.scenes.get(NAME)
restored = None
if scene is not None:
    previous = bpy.data.scenes.get(scene.get("bmcp_previous_scene", ""))
    if previous is None:
        previous = next((s for s in bpy.data.scenes if s != scene), None)
    if previous is not None:
        window.scene = previous
        restored = previous.name
        bpy.data.scenes.remove(scene)
for blocks in (bpy.data.objects, bpy.data.meshes, bpy.data.materials,
               bpy.data.cameras, bpy.data.lights, bpy.data.worlds):
    for block in [b for b in blocks if b.name.startswith(PREFIX)]:
        blocks.remove(block)
left = [b.name for blocks in (bpy.data.scenes, bpy.data.objects, bpy.data.materials)
        for b in blocks if b.name.startswith(PREFIX)]
print("BMCP_RESULT=" + json.dumps({
    "active_scene": window.scene.name, "restored": restored,
    "scenes": [s.name for s in bpy.data.scenes], "leftover_test_data": left,
}))
'''

# Run in a separate `blender -b` process to check the saved files independently.
VERIFY_CODE = r'''
import json
import sys
import bpy
import numpy as np

extra = sys.argv[sys.argv.index("--") + 1:]
png, look = extra[0], (extra[1] if len(extra) > 1 else "")
scene = bpy.data.scenes.get("MCP_Test_Scene")
cube = bpy.data.objects.get("MCP_Test_Cube")

def rgb(path):
    img = bpy.data.images.load(path)
    return img, np.array(img.pixels[:], dtype=np.float32).reshape(-1, img.channels)[:, :3]

image, pixels = rgb(png)
look_std = None
if look:
    _look_image, look_pixels = rgb(look)
    look_std = round(float(look_pixels.std()), 4)
print("BMCP_RESULT=" + json.dumps({
    "blender": bpy.app.version_string,
    "background_mode": bpy.app.background,
    "scene_found": scene is not None,
    "objects": {o.name: o.type for o in scene.objects} if scene else {},
    "cube_materials": [m.name for m in cube.data.materials] if cube else [],
    "camera": scene.camera.name if scene and scene.camera else None,
    "png_size": list(image.size),
    "png_mean_rgb": [round(float(v), 4) for v in pixels.mean(axis=0)],
    "png_std": round(float(pixels.std()), 4),
    "png_min": round(float(pixels.min()), 4),
    "png_max": round(float(pixels.max()), 4),
    "look_std": look_std,
}))
'''


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
class Report:
    """Collects step results, prints them as they happen, and decides the exit code."""

    def __init__(self) -> None:
        self.steps: list[dict] = []

    def add(self, name: str, passed: bool, detail: str = "", **data) -> bool:
        self.steps.append({"step": name, "passed": bool(passed), "detail": detail, **data})
        print(f"{'PASS' if passed else 'FAIL'}  {name}" + (f" - {detail}" if detail else ""), flush=True)
        return bool(passed)

    @property
    def ok(self) -> bool:
        return bool(self.steps) and all(step["passed"] for step in self.steps)


def registered_command(name: str, project: Path) -> dict | None:
    """The stdio command Claude Code stores for `name` (local, then user, then project scope)."""
    def load(path: Path) -> dict:
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return {}

    config = load(Path.home() / ".claude.json")
    candidates = [
        ("local", config.get("projects", {}).get(str(project), {}).get("mcpServers", {})),
        ("user", config.get("mcpServers", {})),
        ("project", load(project / ".mcp.json").get("mcpServers", {})),
    ]
    for scope, servers in candidates:
        entry = servers.get(name)
        if entry and entry.get("command"):
            return {"scope": scope, "command": entry["command"],
                    "args": list(entry.get("args", [])), "env": dict(entry.get("env", {}))}
    return None


def text_of(result) -> str:
    return "\n".join(c.text for c in result.content if getattr(c, "type", "") == "text")


def marker_json(text: str) -> dict:
    """Parse the BMCP_RESULT=<json> line a script printed inside Blender."""
    for line in text.splitlines():
        position = line.find(MARKER)
        if position >= 0:
            return json.loads(line[position + len(MARKER):])
    raise ValueError(f"no {MARKER} line in tool output: {text[:400]!r}")


def png_header(path: Path) -> tuple[int, int]:
    """(width, height) from the IHDR chunk; raises if the file is not a PNG."""
    with path.open("rb") as handle:
        head = handle.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n" or head[12:16] != b"IHDR":
        raise ValueError("not a PNG file")
    return struct.unpack(">II", head[16:24])


def blend_magic_ok(path: Path) -> bool:
    with path.open("rb") as handle:
        head = handle.read(7)
    # Plain .blend starts with "BLENDER"; a compressed one with the zstd magic.
    return head == b"BLENDER" or head[:4] == b"\x28\xb5\x2f\xfd"


# --------------------------------------------------------------------------- #
# The test
# --------------------------------------------------------------------------- #
async def run(args: argparse.Namespace, report: Report) -> dict:
    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    blend_path = out_dir / "mcp_test_scene.blend"
    png_path = out_dir / "mcp_test_render.png"
    summary: dict = {"out_dir": str(out_dir), "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}

    if args.server_cmd:
        parts = shlex.split(args.server_cmd)
        entry = {"scope": "command line", "command": parts[0], "args": parts[1:], "env": {}}
    else:
        entry = registered_command(args.name, Path(args.project).resolve())
    if not report.add("server command", entry is not None,
                      f"{entry['command']} {' '.join(entry['args'])} ({entry['scope']} scope)" if entry
                      else f"no MCP server named '{args.name}' is registered with Claude Code - run install.sh"):
        return summary
    summary["server"] = entry

    # Claude Code starts stdio servers with its own environment plus the entry's env.
    params = StdioServerParameters(command=entry["command"], args=entry["args"],
                                   env={**os.environ, **entry["env"]})
    call_timeout = timedelta(seconds=args.timeout)

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            # 1 ---------------------------------------------------------------
            init = await session.initialize()
            info = init.serverInfo
            summary["server_info"] = {"name": info.name, "version": info.version,
                                      "protocol": init.protocolVersion}
            report.add("mcp initialize", True,
                       f"server '{info.name}' (serverInfo.version {info.version}), MCP protocol {init.protocolVersion}")

            tools = [tool.name for tool in (await session.list_tools()).tools]
            summary["tools"] = tools
            needed = {"get_addon_status", "get_scene_info", "execute_blender_code", "look"}
            report.add("mcp list_tools", needed <= set(tools),
                       f"{len(tools)} tools: {', '.join(tools)}")

            async def call(tool: str, arguments: dict):
                return await session.call_tool(tool, arguments, read_timeout_seconds=call_timeout)

            async def run_code(step: str, code: str) -> dict | None:
                result = await call("execute_blender_code", {"code": code})
                text = text_of(result)
                if result.isError or not text.startswith("Code executed successfully"):
                    report.add(step, False, text[:1500])
                    return None
                return marker_json(text)

            # 2 ---------------------------------------------------------------
            result = await call("get_addon_status", {})
            status_text = text_of(result)
            summary["addon_status"] = status_text
            report.add("tool get_addon_status", not result.isError and "Blender" in status_text,
                       " | ".join(status_text.splitlines()[:3])[:300])

            result = await call("get_scene_info", {"fields": ["location", "size", "settings"]})
            before_text = text_of(result)
            summary["scene_before"] = before_text
            report.add("tool get_scene_info (live scene)", not result.isError and bool(before_text.strip()),
                       " | ".join(before_text.splitlines()[:2])[:300])

            # 3 ---------------------------------------------------------------
            build = await run_code("tool execute_blender_code (build test scene)",
                                   BUILD_CODE.replace("__WIDTH__", str(args.width))
                                             .replace("__HEIGHT__", str(args.height))
                                             .replace("__SAMPLES__", str(args.samples)))
            if build is None:
                return summary
            summary["build"] = build
            objects = build["objects"]
            report.add("tool execute_blender_code (build test scene)",
                       build["scene"] == SCENE
                       and objects.get(PREFIX + "Cube") == "MESH"
                       and objects.get(PREFIX + "Camera") == "CAMERA"
                       and objects.get(PREFIX + "Light") == "LIGHT"
                       and build["cube_materials"] == [PREFIX + "Material"]
                       and build["background_mode"] is False,
                       f"scene {build['scene']} (kept '{build['previous_scene']}' untouched); "
                       f"cube material {build['cube_materials']}; camera {build['camera']}; "
                       f"engine {build['engine']}/{build['cycles_device']}; Blender {build['blender']} GUI")

            # 4 ---------------------------------------------------------------
            result = await call("get_scene_info", {"query": PREFIX, "fields": ["location", "size", "materials", "details"]})
            after_text = text_of(result)
            summary["scene_after"] = after_text
            report.add("tool get_scene_info (test scene)",
                       not result.isError
                       and all(n in after_text for n in (PREFIX + "Cube", PREFIX + "Camera", PREFIX + "Light", PREFIX + "Material"))
                       and "(6.5, -6.5, 4.5)" in after_text and "(0.0, 0.0, 1.0)" in after_text,
                       " | ".join(after_text.splitlines()[:6])[:500])

            # 5 ---------------------------------------------------------------
            result = await call("look", {"mode": "camera", "shading": "solid", "max_size": 640})
            images = [c for c in result.content if getattr(c, "type", "") == "image"]
            if images and not result.isError:
                raw = base64.b64decode(images[0].data)
                extension = {"image/png": "png", "image/jpeg": "jpg", "image/webp": "webp"}.get(images[0].mimeType, "bin")
                look_path = out_dir / f"mcp_test_look.{extension}"
                look_path.write_bytes(raw)
                summary["look"] = {"path": str(look_path), "bytes": len(raw), "mime": images[0].mimeType,
                                   "caption": text_of(result)[:300]}
                report.add("tool look (viewport via camera)", len(raw) > 2000,
                           f"{images[0].mimeType}, {len(raw)} bytes -> {look_path}; {summary['look']['caption']}")
            else:
                report.add("tool look (viewport via camera)", False, text_of(result)[:800])

            # 6 ---------------------------------------------------------------
            saved = await run_code("tool execute_blender_code (save .blend + render PNG)",
                                   SAVE_RENDER_CODE.replace("__BLEND__", repr(str(blend_path)))
                                                   .replace("__PNG__", repr(str(png_path))))
            if saved is not None:
                summary["save_render"] = saved
                report.add("tool execute_blender_code (save .blend + render PNG)",
                           saved["blend_bytes"] > 0 and saved["png_bytes"] > 0 and saved["device"] == "CPU",
                           f"render {saved['render_seconds']} s on {saved['engine']}/{saved['device']} "
                           f"@ {saved['samples']} samples; .blend {saved['blend_bytes']} B; PNG {saved['png_bytes']} B")

            # 8 (always attempted, so the live session is left as it was) ------
            if not args.keep_scene:
                cleaned = await run_code("tool execute_blender_code (remove test scene)", CLEANUP_CODE)
                if cleaned is not None:
                    summary["cleanup"] = cleaned
                    report.add("tool execute_blender_code (remove test scene)",
                               not cleaned["leftover_test_data"] and cleaned["active_scene"] != SCENE,
                               f"active scene back to '{cleaned['active_scene']}', scenes {cleaned['scenes']}")

    # 7 ----- files on disk, checked from outside the live Blender ------------
    blend_ok = blend_path.is_file() and blend_path.stat().st_size > 10_000 and blend_magic_ok(blend_path)
    report.add("file .blend exists", blend_ok,
               f"{blend_path} ({blend_path.stat().st_size if blend_path.exists() else 0} bytes)")
    try:
        width, height = png_header(png_path)
        png_ok = (width, height) == (args.width, args.height) and png_path.stat().st_size > 5_000
        report.add("file PNG exists", png_ok, f"{png_path} ({png_path.stat().st_size} bytes, {width}x{height})")
    except (OSError, ValueError) as exc:
        png_ok = report.add("file PNG exists", False, f"{png_path}: {exc}")

    if blend_ok and png_ok:
        blender = args.blender
        proc = subprocess.run(
            [blender, "--background", "--factory-startup", str(blend_path),
             "--python-expr", VERIFY_CODE, "--", str(png_path),
             *([summary["look"]["path"]] if summary.get("look", {}).get("mime") == "image/png" else [])],
            capture_output=True, text=True, timeout=300,
        )
        try:
            verify = marker_json(proc.stdout)
        except ValueError:
            report.add("independent check (separate background Blender)", False,
                       (proc.stdout + proc.stderr)[-800:])
        else:
            summary["verify"] = verify
            objects = verify["objects"]
            report.add("independent check: .blend contents", verify["scene_found"]
                       and objects.get(PREFIX + "Cube") == "MESH"
                       and objects.get(PREFIX + "Camera") == "CAMERA"
                       and objects.get(PREFIX + "Light") == "LIGHT"
                       and verify["cube_materials"] == [PREFIX + "Material"]
                       and verify["background_mode"] is True,
                       f"re-opened in blender -b {verify['blender']}: objects {sorted(objects)}, "
                       f"cube material {verify['cube_materials']}, camera {verify['camera']}")
            report.add("independent check: PNG is a real image",
                       verify["png_size"] == [args.width, args.height] and verify["png_std"] > 0.03
                       and verify["png_max"] > 0.3,
                       f"{verify['png_size'][0]}x{verify['png_size'][1]}, mean RGB {verify['png_mean_rgb']}, "
                       f"std {verify['png_std']}, range {verify['png_min']}-{verify['png_max']}")
            if verify.get("look_std") is not None:
                report.add("independent check: viewport image is not blank", verify["look_std"] > 0.03,
                           f"pixel std {verify['look_std']} (a uniform image would be 0)")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--name", default=os.environ.get("BMCP_MCP_NAME", "blender"),
                        help="name of the MCP server registered with Claude Code (default: blender)")
    parser.add_argument("--project", default=str(REPO_ROOT),
                        help="project directory the server is registered for (default: repository root)")
    parser.add_argument("--server-cmd", default="",
                        help="test this stdio command instead of the registered one")
    parser.add_argument("--out-dir", default=os.path.join(os.environ.get("BMCP_HOME", "/opt/blender-mcp"), "test-output"))
    parser.add_argument("--blender", default=os.environ.get("BMCP_BLENDER_BIN", "/opt/blender-dl/current/blender"),
                        help="Blender binary for the separate background verification")
    parser.add_argument("--width", type=int, default=960)
    parser.add_argument("--height", type=int, default=540)
    parser.add_argument("--samples", type=int, default=48)
    parser.add_argument("--timeout", type=int, default=240, help="seconds allowed per MCP tool call")
    parser.add_argument("--keep-scene", action="store_true", help="leave MCP_Test_Scene in the live session")
    args = parser.parse_args()

    report = Report()
    summary: dict = {}
    try:
        summary = asyncio.run(run(args, report))
    except Exception as exc:  # connection refused, timeouts, protocol errors, ...
        report.add("unexpected error", False, f"{type(exc).__name__}: {exc}")
    summary["steps"] = report.steps
    summary["passed"] = report.ok
    summary["finished_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    report_path = Path(args.out_dir) / "mcp_e2e_report.json"
    try:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
        print(f"report: {report_path}")
    except OSError as exc:
        print(f"could not write {report_path}: {exc}", file=sys.stderr)

    passed = sum(step["passed"] for step in report.steps)
    print(f"RESULT: {'PASS' if report.ok else 'FAIL'} ({passed}/{len(report.steps)} steps)")
    return 0 if report.ok else 1


if __name__ == "__main__":
    sys.exit(main())
