"""Runs inside Blender for tools/film/render_farm.py: render a frame range, skipping frames that exist.

Several workers can share one range: each writes a placeholder for the frame it takes
(use_placeholder) and never overwrites (use_overwrite = False), so no frame is rendered twice.
"""
import json
import sys
import time

import bpy

args = sys.argv[sys.argv.index("--") + 1:]
opt = lambda name, default=None: args[args.index(name) + 1] if name in args else default  # noqa: E731
sc = bpy.context.scene
sc.frame_start, sc.frame_end = int(opt("--start")), int(opt("--end"))
sc.render.filepath = opt("--out")
sc.render.use_placeholder, sc.render.use_overwrite = True, False
sc.render.use_file_extension = True
if opt("--threads"):
    sc.render.threads_mode, sc.render.threads = "FIXED", int(opt("--threads"))
if opt("--samples"):
    sc.cycles.samples = int(opt("--samples"))
if opt("--scale"):
    sc.render.resolution_percentage = int(opt("--scale"))
s = sc.render.image_settings
if opt("--format", "PNG") == "EXR":
    s.media_type, s.file_format, s.color_depth, s.exr_codec = "IMAGE", "OPEN_EXR", "16", "ZIP"
else:
    s.media_type, s.file_format, s.color_mode, s.color_depth = "IMAGE", "PNG", "RGB", opt("--depth", "8")
log = open(opt("--log"), "a", buffering=1)
started = {}
bpy.app.handlers.render_pre.append(lambda scene, *_: started.__setitem__(scene.frame_current, time.time()))
bpy.app.handlers.render_post.append(lambda scene, *_: log.write(json.dumps(
    {"frame": scene.frame_current, "seconds": round(time.time() - started.get(scene.frame_current, time.time()), 2),
     "worker": opt("--worker", "0")}) + "\n"))
bpy.ops.render.render(animation=True)
