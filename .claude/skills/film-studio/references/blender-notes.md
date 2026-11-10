# Blender 5.2 notes verified on this machine

The full 4.x -> 5.2 table is in `.claude/skills/blender-core/references/api-changes-5x.md`. These are the
points that broke or surprised scripts written here; each was checked against Blender 5.2.4.

| Topic | What works |
|---|---|
| Light groups | `view_layer.lightgroups.add(name="sun")` (there is no `.new`); then `object.lightgroup = "sun"` for lights AND emissive meshes, `world.lightgroup = "sky"`. |
| Light group passes | Render-layer outputs are named `Combined_<group>`. They are NOT denoised by the render denoiser; denoise each one afterwards (`tools/film/comp.py prepare`). |
| Multilayer EXR | Written as a multi-PART file: one part per pass (`ViewLayer.Combined_sun`, `ViewLayer.Denoising Albedo`, ...). Read with `OpenEXR.File(path).parts`, not `.channels()` of the first part. |
| Output format | Set `image_settings.media_type` (`IMAGE` / `MULTI_LAYER_IMAGE` / `VIDEO`) BEFORE `file_format`. |
| Colour | Views: Standard, AgX, Khronos PBR Neutral, ACES 1.3/2.0, Filmic. Looks carry the view name: `AgX - Medium High Contrast`. Read valid values from the error text of a wrong assignment. |
| Sky | `ShaderNodeTexSky.sky_type`: `MULTIPLE_SCATTERING` (new default), `SINGLE_SCATTERING`, `PREETHAM`, `HOSEK_WILKIE`. |
| Lights | `light.use_temperature = True; light.temperature = 2700` replaces hand-made blackbody colours. |
| Materials | New materials and worlds already have node trees; `use_nodes = True` is deprecated. Principled sockets: `Coat Weight`, `Sheen Weight`, `Transmission Weight`, `Emission Color`, `Thin Wall` (cheap window glass). |
| Smooth shading | `mesh.set_sharp_from_angle(angle=...)` after setting `use_smooth` on the polygons (auto smooth is gone). |
| Animation | Actions are slotted: F-curves live in a channelbag. `bpy_extras.anim_utils.action_get_channelbag_for_slot(action, slot).fcurves`. `keyframe_insert` still creates everything. |
| Compositor | `scene.compositing_node_group`, no Composite node, File Output uses `directory` / `file_name` / `file_output_items`. This toolkit does not use the Blender compositor: finishing is done in `comp.py`. |
| Depsgraph | Create objects AFTER the window shows the scene they belong to, or call `view_layer.update()` before reading `matrix_world`. |
| Background mode | `blender -b --factory-startup --python script.py -- args` for clean builds. EEVEE needs a GPU even in background: do not use it here. |
| Render region | `use_border` + `border_min_x/..` render part of the frame; with `use_crop_to_border = False` the file keeps the full size and the rest is transparent black. |
| Timing | Do not parse render progress from the log (format changed in 5.0); measure with `time.time()` around `bpy.ops.render.render` or with `render_pre` / `render_post` handlers. |
| Bundled HDRIs | `/opt/blender-dl/current/5.2/datafiles/studiolights/world/{city,courtyard,forest,interior,night,studio,sunrise,sunset}.exr` (small, CC0): usable for reflections and soft ambient light with `fk.world_hdri`. |
| Extensions from the command line | `blender --online-mode --command extension sync`, then `... extension install id1,id2 --enable` (ONE comma-separated argument). The whole install fails if any id is unknown for this version or already installed; `tools/film/install.sh` installs only missing ones. Set `BLENDER_USER_RESOURCES=/opt/blender-mcp/userdata` so the live service sees them, and restart the service. |
| glTF models | `bpy.ops.import_scene.gltf(filepath=...)`; Poly Haven models are in metres at real size. |
| OCIO outside Blender | `PyOpenColorIO` with `/opt/blender-dl/current/5.2/datafiles/colormanagement/config.ocio` reproduces Blender's display transform on numpy arrays. |

## Cost facts (4 vCPU, no GPU)

- Fixed cost per render call: about 1.5 s (scene sync, BVH) for a small set.
- Shading is about a quarter of the time; ray traversal and bounces are the rest. Simplifying materials
  buys little; fewer samples, fewer pixels and fewer frames buy everything.
- Options measured on an interior lit through a window (480x270, 128 samples): fast GI approximation
  -26 %, 64 samples with a looser threshold -50 %, two diffuse bounces instead of four -7 %,
  path guiding +12 % (slower), light tree off -8 %, window glass on or off: no difference.
- OpenImageDenoise on a 960x540 pass: about 0.4 s. It is never the bottleneck.
