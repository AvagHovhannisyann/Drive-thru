"""Blender startup script for the persistent MCP service.

Run by supervise.sh as:   blender ... --python blender_startup.py

On Blender's main thread it
  1. enables the "MCP for Blender" add-on (module ``blender_mcp``),
  2. pins the add-on's listener to loopback and to the configured port,
  3. starts the add-on's socket server through the add-on's own operator,
  4. re-checks every few seconds and repairs 1-3 when a script reset Blender
     (``bpy.ops.wm.read_factory_settings()`` disables every add-on, for example),
  5. writes ``run/blender-status.json`` so status.sh can report from outside.

No sidebar click is involved. The names below were read from the installed add-on
(mcp-for-blender 2.2.7: add-on ``bl_info`` version 1.8, protocol 15), not guessed:

  operator           bpy.ops.blendermcp.start_server() / stop_server()
  server instance    bpy.types.blendermcp_server          (.running .host .port)
  listener address   AddonPreferences.bind_address  (+ allow_remote_connections)
  listener port      Scene.blendermcp_port
  auto-start flag    Scene.blendermcp_auto_start_server

Configuration comes from environment variables set by supervise.sh (see config.env).
"""

import contextlib
import ipaddress
import json
import os
import sys
import time
import traceback

import addon_utils
import bpy
from bpy.app.handlers import persistent

ADDON = os.environ.get("BMCP_ADDON_MODULE", "blender_mcp")
HOST = os.environ.get("BMCP_HOST", "127.0.0.1")
PORT = int(os.environ.get("BMCP_PORT", "9876"))
STATUS_FILE = os.environ.get("BMCP_STATUS_FILE", "")
INTERVAL = max(1.0, float(os.environ.get("BMCP_WATCHDOG_INTERVAL", "5")))
DEFAULT_ENGINE = os.environ.get("BMCP_DEFAULT_ENGINE", "CYCLES").strip().upper()
HAS_GPU = os.environ.get("BMCP_HAS_GPU", "0") == "1"

# Factory-default engines that are replaced on an unsaved scene when there is no GPU.
_EEVEE_ENGINES = {"BLENDER_EEVEE_NEXT", "BLENDER_EEVEE"}

_state = {
    "started_at": time.time(),
    "healthy_once": False,   # the socket has been up at least once
    "repairs": 0,            # times the watchdog had to re-enable / restart after that
    "last_error": "",
    "prefs_saved": False,
    "apply_defaults": True,  # apply CPU render defaults on the next tick
    "gpu_info": None,
}


def log(message):
    stamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    print(f"[{stamp}] [bmcp-startup] {message}", flush=True)


def _is_loopback(host):
    try:
        return ipaddress.IPv4Address(host).is_loopback
    except ValueError:
        return False


def _window_override():
    """Operators need a window; timers run without one, so borrow the first window."""
    windows = getattr(bpy.context.window_manager, "windows", None)
    if windows:
        return bpy.context.temp_override(window=windows[0])
    return contextlib.nullcontext()


def _addon_enabled():
    try:
        _loaded_default, loaded_state = addon_utils.check(ADDON)
    except Exception:
        return False
    return bool(loaded_state) and ADDON in bpy.context.preferences.addons


def _ensure_addon():
    """Enable the add-on and pin its listener settings. True if anything changed."""
    changed = False
    if not _addon_enabled():
        errors = []
        log(f"enabling add-on '{ADDON}'")
        module = addon_utils.enable(
            ADDON, default_set=True, persistent=True, handle_error=errors.append
        )
        if module is None or not _addon_enabled():
            detail = f": {errors[0]!r}" if errors else ""
            raise RuntimeError(
                f"could not enable add-on module '{ADDON}'{detail} - is it installed in "
                f"{bpy.utils.user_resource('SCRIPTS', path='addons')}? (run install.sh)"
            )
        changed = True

    prefs = bpy.context.preferences.addons[ADDON].preferences
    if prefs.bind_address != HOST:
        prefs.bind_address = HOST
        changed = True
    if prefs.allow_remote_connections:
        prefs.allow_remote_connections = False
        changed = True
    return changed


def _ensure_server():
    """Start the add-on's socket server on HOST:PORT. True if it had to be (re)started."""
    scene = bpy.context.scene
    if scene is None:
        raise RuntimeError("no scene in context yet")
    if scene.blendermcp_port != PORT:
        scene.blendermcp_port = PORT
    if not scene.blendermcp_auto_start_server:
        scene.blendermcp_auto_start_server = True

    server = getattr(bpy.types, "blendermcp_server", None)
    if server is not None and server.running:
        if int(server.port) == PORT and str(server.host) == HOST:
            return False
        log(f"server listens on {server.host}:{server.port}, expected {HOST}:{PORT} - restarting it")
        bpy.ops.blendermcp.stop_server()

    result = bpy.ops.blendermcp.start_server()
    server = getattr(bpy.types, "blendermcp_server", None)
    running = bool(server is not None and server.running)
    log(f"bpy.ops.blendermcp.start_server() -> {sorted(result)}; running={running} on {HOST}:{PORT}")
    if not running:
        raise RuntimeError(f"add-on socket server did not start on {HOST}:{PORT} (port in use?)")
    return True


def _apply_render_defaults():
    """Without a GPU, render the unsaved default scene with Cycles on the CPU.

    Only touches scenes of an unsaved file that still use the factory EEVEE engine;
    a saved .blend keeps whatever its author chose.
    """
    if HAS_GPU or DEFAULT_ENGINE in ("", "KEEP") or bpy.data.filepath:
        return
    for scene in bpy.data.scenes:
        if scene.render.engine not in _EEVEE_ENGINES:
            continue
        previous = scene.render.engine
        try:
            scene.render.engine = DEFAULT_ENGINE
        except TypeError as exc:
            log(f"cannot set render engine {DEFAULT_ENGINE!r}: {exc}")
            return
        if DEFAULT_ENGINE == "CYCLES":
            scene.cycles.device = "CPU"
        log(f"no GPU: scene '{scene.name}' render engine {previous} -> {scene.render.engine} (CPU)")


def _gpu_info():
    if _state["gpu_info"] is None:
        try:
            import gpu

            _state["gpu_info"] = {
                "backend": gpu.platform.backend_type_get(),
                "vendor": gpu.platform.vendor_get(),
                "renderer": gpu.platform.renderer_get(),
                "version": gpu.platform.version_get(),
            }
        except Exception as exc:  # no GPU context yet
            return {"error": repr(exc)}
    return _state["gpu_info"]


def _write_status(ok, error=""):
    if not STATUS_FILE:
        return
    server = getattr(bpy.types, "blendermcp_server", None)
    module = sys.modules.get(ADDON)
    scene = bpy.context.scene
    addon_entry = bpy.context.preferences.addons.get(ADDON)
    prefs = addon_entry.preferences if addon_entry else None
    status = {
        "ok": bool(ok),
        "error": error,
        "timestamp": time.time(),
        "time_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "pid": os.getpid(),
        "uptime_seconds": round(time.time() - _state["started_at"], 1),
        "blender_version": bpy.app.version_string,
        "blender_build_hash": bpy.app.build_hash.decode("ascii", "replace"),
        "blender_binary": bpy.app.binary_path,
        "background": bpy.app.background,
        "windows": len(getattr(bpy.context.window_manager, "windows", [])),
        "addon_module": ADDON,
        "addon_enabled": _addon_enabled(),
        "addon_file": getattr(module, "__file__", None),
        "addon_version": list(getattr(module, "bl_info", {}).get("version", [])) if module else None,
        "addon_protocol": getattr(module, "ADDON_PROTOCOL_VERSION", None),
        "server_running": bool(server is not None and server.running),
        "server_host": getattr(server, "host", None),
        "server_port": getattr(server, "port", None),
        "bind_address": getattr(prefs, "bind_address", None),
        "allow_remote_connections": getattr(prefs, "allow_remote_connections", None),
        "telemetry_consent": getattr(prefs, "telemetry_consent", None),
        "online_access": bpy.app.online_access,
        "gpu": _gpu_info(),
        "has_gpu": HAS_GPU,
        "blend_file": bpy.data.filepath,
        "scene": getattr(scene, "name", None),
        "render_engine": scene.render.engine if scene else None,
        "cycles_device": scene.cycles.device if scene and hasattr(scene, "cycles") else None,
        "watchdog_interval": INTERVAL,
        "watchdog_repairs": _state["repairs"],
        "user_scripts": bpy.utils.user_resource("SCRIPTS"),
    }
    tmp = STATUS_FILE + ".tmp"
    try:
        with open(tmp, "w", encoding="utf-8") as handle:
            json.dump(status, handle, indent=1, sort_keys=True)
        os.replace(tmp, STATUS_FILE)
    except OSError as exc:
        log(f"cannot write status file {STATUS_FILE}: {exc}")


def _tick():
    """One health pass: add-on enabled, socket up, defaults applied, status written."""
    try:
        with _window_override():
            changed = _ensure_addon()
            changed = _ensure_server() or changed
            if _state["apply_defaults"]:
                _state["apply_defaults"] = False
                _apply_render_defaults()
            if changed and _state["healthy_once"]:
                _state["repairs"] += 1
                log(f"watchdog repaired the MCP socket (repair #{_state['repairs']})")
            if changed and not _state["prefs_saved"]:
                # Remember the add-on in this service's private preferences so that
                # File > New (wm.read_homefile) keeps it enabled.
                try:
                    bpy.ops.wm.save_userpref()
                    _state["prefs_saved"] = True
                except Exception as exc:
                    log(f"could not save preferences (non-fatal): {exc!r}")
        if not _state["healthy_once"]:
            _state["healthy_once"] = True
            log(f"MCP add-on socket is up on {HOST}:{PORT} (Blender {bpy.app.version_string}, pid {os.getpid()})")
        _state["last_error"] = ""
        _write_status(True)
    except Exception as exc:
        message = f"{type(exc).__name__}: {exc}"
        if message != _state["last_error"]:  # log each distinct failure once
            _state["last_error"] = message
            log(f"health pass failed: {message}")
            traceback.print_exc()
        try:
            _write_status(False, message)
        except Exception:
            pass


def _watchdog():
    _tick()
    return INTERVAL


def _tick_once():
    _tick()
    return None


@persistent
def _on_load_post(*_args):
    """A file was loaded: re-apply defaults and check the socket promptly."""
    _state["apply_defaults"] = True
    if not bpy.app.timers.is_registered(_tick_once):
        bpy.app.timers.register(_tick_once, first_interval=0.3, persistent=True)


def main():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(line_buffering=True)
        except Exception:
            pass

    if bpy.app.background:
        log("background mode (blender -b): the add-on cannot serve commands without a "
            "window, nothing to do. Use start.sh for the live MCP service.")
        return
    if not _is_loopback(HOST):
        log(f"refusing to start: BMCP_HOST={HOST!r} is not a loopback address")
        sys.exit(3)

    log(f"startup: Blender {bpy.app.version_string} pid {os.getpid()}, add-on '{ADDON}', "
        f"target {HOST}:{PORT}, user scripts {bpy.utils.user_resource('SCRIPTS')}")
    if _on_load_post not in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(_on_load_post)
    bpy.app.timers.register(_watchdog, first_interval=1.0, persistent=True)


main()
