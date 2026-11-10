"""filmkit - helpers for building and rendering film shots in Blender 5.2 (Cycles on CPU).

Import from a shot script that Blender runs:

    import sys; sys.path.insert(0, "/home/user/Drive-thru/tools/film/blender")
    import filmkit as fk

Everything here was checked against Blender 5.2.4. Conventions:
  * metres, Z up, time in SECONDS on one master clock; `fk.frame(t)` converts to a frame
  * nodes are found by type, never by (localised) name
  * nothing depends on the UI, so the same script runs in `blender -b` and in the live session
"""

from __future__ import annotations

import math
import os
from typing import Callable, Iterable, Sequence

import bmesh
import bpy
from bpy_extras import anim_utils
from mathutils import Vector

FONTS = os.environ.get("FILM_HOME", "/opt/film-studio") + "/fonts"

# --------------------------------------------------------------------------- time


def scene() -> bpy.types.Scene:
    return bpy.context.scene


def frame(seconds: float, sc: bpy.types.Scene | None = None) -> int:
    """Frame number for a time on the master clock (t = 0 is frame 1)."""
    sc = sc or scene()
    return int(round(seconds * sc.render.fps / sc.render.fps_base)) + 1


def set_range(duration: float, sc: bpy.types.Scene | None = None) -> None:
    sc = sc or scene()
    sc.frame_start, sc.frame_end = 1, frame(duration, sc) - 1


# --------------------------------------------------------------------------- scene and render


def reset(fps: int = 24, res: tuple[int, int] = (1920, 1080), name: str = "Film") -> bpy.types.Scene:
    """Empty file with one scene. Keeps no default cube, light or camera."""
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    sc.name = name
    sc.render.fps, sc.render.fps_base = fps, 1.0
    sc.render.resolution_x, sc.render.resolution_y = res
    sc.render.resolution_percentage = 100
    sc.unit_settings.system = "METRIC"
    return sc


def cycles(samples: int = 128, threshold: float = 0.02, denoise: bool = True, bounces: int = 8,
           diffuse: int = 4, glossy: int = 4, transmission: int = 8, clamp_indirect: float = 8.0,
           blur_glossy: float = 0.5, persistent: bool = True, motion_blur: bool = False,
           shutter: float = 0.5, sc: bpy.types.Scene | None = None) -> None:
    """Cycles on CPU with adaptive sampling and OpenImageDenoise (albedo + normal guided)."""
    sc = sc or scene()
    sc.render.engine = "CYCLES"
    c = sc.cycles
    c.device = "CPU"
    c.samples = samples
    c.use_adaptive_sampling = True
    c.adaptive_threshold = threshold
    c.adaptive_min_samples = max(16, samples // 8)
    c.use_denoising = denoise
    if denoise:
        c.denoiser = "OPENIMAGEDENOISE"
        c.denoising_input_passes = "RGB_ALBEDO_NORMAL"
        c.denoising_prefilter = "ACCURATE"
    c.max_bounces = bounces
    c.diffuse_bounces, c.glossy_bounces, c.transmission_bounces = diffuse, glossy, transmission
    c.transparent_max_bounces = 8
    c.sample_clamp_indirect = clamp_indirect
    c.blur_glossy = blur_glossy
    c.caustics_reflective = c.caustics_refractive = False
    c.use_light_tree = True
    sc.render.use_persistent_data = persistent
    sc.render.use_motion_blur = motion_blur
    sc.render.motion_blur_shutter = shutter
    sc.render.threads_mode = "AUTO"


def color(view: str = "AgX", look: str = "AgX - Medium High Contrast", exposure: float = 0.0,
          gamma: float = 1.0, sc: bpy.types.Scene | None = None) -> None:
    sc = sc or scene()
    sc.display_settings.display_device = "sRGB"
    sc.view_settings.view_transform = view
    sc.view_settings.look = look
    sc.view_settings.exposure = exposure
    sc.view_settings.gamma = gamma


def output_png(path: str, depth: int = 8, sc: bpy.types.Scene | None = None) -> None:
    """`path` ends with a name and `####` for the frame number, for example //frames/a_####."""
    sc = sc or scene()
    s = sc.render.image_settings
    s.media_type = "IMAGE"          # 5.0+: set before file_format
    s.file_format = "PNG"
    s.color_mode = "RGB"
    s.color_depth = str(depth)
    s.compression = 15
    sc.render.filepath = path


def output_exr(path: str, multilayer: bool = True, sc: bpy.types.Scene | None = None) -> None:
    sc = sc or scene()
    s = sc.render.image_settings
    s.media_type = "MULTI_LAYER_IMAGE" if multilayer else "IMAGE"
    s.file_format = "OPEN_EXR_MULTILAYER" if multilayer else "OPEN_EXR"
    s.color_depth = "16"
    s.exr_codec = "DWAA"
    sc.render.filepath = path


def collection(name: str, parent: bpy.types.Collection | None = None) -> bpy.types.Collection:
    coll = bpy.data.collections.get(name)
    if coll is None:
        coll = bpy.data.collections.new(name)
        (parent or scene().collection).children.link(coll)
    return coll


def link(obj: bpy.types.Object, coll: bpy.types.Collection | None = None) -> bpy.types.Object:
    (coll or scene().collection).objects.link(obj)
    return obj


# --------------------------------------------------------------------------- geometry


def _mesh_object(name: str, bm: bmesh.types.BMesh, coll=None, mat=None, smooth_angle: float | None = 35.0):
    mesh = bpy.data.meshes.new(name)
    bm.to_mesh(mesh)
    bm.free()
    obj = link(bpy.data.objects.new(name, mesh), coll)
    if mat is not None:
        mesh.materials.append(mat)
    if smooth_angle is not None:
        smooth(obj, smooth_angle)
    return obj


def smooth(obj: bpy.types.Object, angle: float = 35.0) -> None:
    """Smooth shading with sharp edges above `angle` degrees (replaces auto smooth)."""
    mesh = obj.data
    mesh.polygons.foreach_set("use_smooth", [True] * len(mesh.polygons))
    mesh.set_sharp_from_angle(angle=math.radians(angle))
    mesh.update()


def bevel(obj: bpy.types.Object, width: float, segments: int = 3, angle: float = 30.0) -> bpy.types.Object:
    """Rounded edges. Almost every man-made edge needs one to catch a highlight."""
    mod = obj.modifiers.new("Bevel", "BEVEL")
    mod.width, mod.segments = width, segments
    mod.limit_method = "ANGLE"
    mod.angle_limit = math.radians(angle)
    mod.harden_normals = True
    return obj


def box(name: str, size: Sequence[float], loc: Sequence[float] = (0, 0, 0), bevel_width: float = 0.0,
        segments: int = 3, mat=None, coll=None, rot: Sequence[float] = (0, 0, 0)) -> bpy.types.Object:
    """Box of full size (x, y, z), centred on `loc`."""
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, vec=Vector(size), verts=bm.verts)
    obj = _mesh_object(name, bm, coll, mat, smooth_angle=35.0)
    obj.location, obj.rotation_euler = loc, rot
    if bevel_width > 0:
        bevel(obj, bevel_width, segments)
    return obj


def cylinder(name: str, radius: float, depth: float, loc: Sequence[float] = (0, 0, 0), verts: int = 48,
             bevel_width: float = 0.0, mat=None, coll=None, rot: Sequence[float] = (0, 0, 0),
             radius_top: float | None = None) -> bpy.types.Object:
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=verts, radius1=radius,
                          radius2=radius if radius_top is None else radius_top, depth=depth)
    obj = _mesh_object(name, bm, coll, mat)
    obj.location, obj.rotation_euler = loc, rot
    if bevel_width > 0:
        bevel(obj, bevel_width, 3)
    return obj


def sphere(name: str, radius: float, loc: Sequence[float] = (0, 0, 0), segments: int = 48, mat=None,
           coll=None, scale: Sequence[float] = (1, 1, 1)) -> bpy.types.Object:
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=segments, v_segments=segments // 2, radius=radius)
    obj = _mesh_object(name, bm, coll, mat, smooth_angle=180.0)
    obj.location, obj.scale = loc, scale
    return obj


def lathe(name: str, profile: Iterable[tuple[float, float]], segments: int = 64, loc=(0, 0, 0), mat=None,
          coll=None, thickness: float = 0.0, subsurf: int = 0) -> bpy.types.Object:
    """Revolve a (radius, height) profile around Z: mugs, pots, lamp shades, vases, bottles."""
    bm = bmesh.new()
    points = list(profile)
    verts = [bm.verts.new((r, 0.0, z)) for r, z in points]
    edges = [bm.edges.new((a, b)) for a, b in zip(verts, verts[1:])]
    bmesh.ops.spin(bm, geom=verts + edges, cent=(0, 0, 0), axis=(0, 0, 1), angle=math.tau,
                   steps=segments, use_duplicate=False)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-6)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    obj = _mesh_object(name, bm, coll, mat, smooth_angle=60.0)
    obj.location = loc
    if thickness > 0:
        mod = obj.modifiers.new("Solidify", "SOLIDIFY")
        mod.thickness, mod.offset = thickness, 0.0
    if subsurf:
        mod = obj.modifiers.new("Subdivision", "SUBSURF")
        mod.levels = mod.render_levels = subsurf
    return obj


def plane(name: str, size: Sequence[float], loc=(0, 0, 0), rot=(0, 0, 0), mat=None, coll=None) -> bpy.types.Object:
    bm = bmesh.new()
    bmesh.ops.create_grid(bm, x_segments=1, y_segments=1, size=0.5)
    bmesh.ops.scale(bm, vec=Vector((size[0], size[1], 1.0)), verts=bm.verts)
    uv = bm.loops.layers.uv.new("UVMap")
    for face in bm.faces:
        for loop in face.loops:
            loop[uv].uv = (loop.vert.co.x / size[0] + 0.5, loop.vert.co.y / size[1] + 0.5)
    obj = _mesh_object(name, bm, coll, mat, smooth_angle=None)
    obj.location, obj.rotation_euler = loc, rot
    return obj


def rod(name: str, a: Sequence[float], b: Sequence[float], radius: float, verts: int = 24, mat=None,
        coll=None) -> bpy.types.Object:
    """Cylinder from point a to point b: lamp arms, legs, rails, cables in straight runs."""
    va, vb = Vector(a), Vector(b)
    obj = cylinder(name, radius, (vb - va).length, loc=(va + vb) / 2, verts=verts, mat=mat, coll=coll)
    obj.rotation_euler = (vb - va).to_track_quat("Z", "Y").to_euler()
    return obj


def torus_arc(name: str, major: float, minor: float, start: float = 0.0, end: float = 360.0, segments: int = 32,
              ring: int = 12, loc=(0, 0, 0), rot=(0, 0, 0), mat=None, coll=None) -> bpy.types.Object:
    """Part of a torus in the local XZ plane (angles in degrees, 0 = +X, 90 = +Z): handles, hooks, rings."""
    bm = bmesh.new()
    rings = []
    for i in range(segments + 1):
        a = math.radians(start + (end - start) * i / segments)
        centre = Vector((major * math.cos(a), 0.0, major * math.sin(a)))
        radial = centre.normalized()
        rings.append([bm.verts.new(centre + minor * (math.cos(t) * radial + math.sin(t) * Vector((0, 1, 0))))
                      for t in [j * math.tau / ring for j in range(ring)]])
    for r0, r1 in zip(rings, rings[1:]):
        for j in range(ring):
            bm.faces.new((r0[j], r0[(j + 1) % ring], r1[(j + 1) % ring], r1[j]))
    if abs(end - start) < 360:
        bm.faces.new(rings[0][::-1])
        bm.faces.new(rings[-1])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    obj = _mesh_object(name, bm, coll, mat, smooth_angle=60.0)
    obj.location, obj.rotation_euler = loc, rot
    return obj


def text(name: str, body: str, font: str | None = None, size: float = 0.1, extrude: float = 0.0, loc=(0, 0, 0),
         rot=(0, 0, 0), mat=None, coll=None, align: str = "CENTER") -> bpy.types.Object:
    """Text object. `font` is a path, or 'Family/Family-400.ttf' relative to the fonts folder."""
    curve = bpy.data.curves.new(name, "FONT")
    curve.body, curve.size, curve.extrude = body, size, extrude
    curve.align_x, curve.align_y = align, "CENTER"
    if font:
        curve.font = bpy.data.fonts.load(font if os.path.isabs(font) else os.path.join(FONTS, font), check_existing=True)
    obj = link(bpy.data.objects.new(name, curve), coll)
    obj.location, obj.rotation_euler = loc, rot
    if mat is not None:
        curve.materials.append(mat)
    return obj


def parent(child: bpy.types.Object, to: bpy.types.Object, keep_world: bool = False) -> bpy.types.Object:
    child.parent = to
    if keep_world:
        child.matrix_parent_inverse = to.matrix_world.inverted()
    return child


def empty(name: str, loc=(0, 0, 0), coll=None) -> bpy.types.Object:
    obj = link(bpy.data.objects.new(name, None), coll)
    obj.location = loc
    obj.empty_display_size = 0.05
    return obj


# --------------------------------------------------------------------------- materials


def principled(mat: bpy.types.Material) -> bpy.types.ShaderNode:
    return next(n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED")


def material(name: str, color: Sequence[float] = (0.8, 0.8, 0.8), rough: float = 0.5, metallic: float = 0.0,
             **inputs: float | Sequence[float]) -> bpy.types.Material:
    """Principled material. Extra inputs by socket name with spaces as underscores,
    for example coat_weight=1, sheen_weight=0.5, transmission_weight=1, emission_strength=5."""
    mat = bpy.data.materials.new(name)
    bsdf = principled(mat)
    bsdf.inputs["Base Color"].default_value = (*color[:3], 1.0)
    bsdf.inputs["Roughness"].default_value = rough
    bsdf.inputs["Metallic"].default_value = metallic
    lookup = {s.name.lower().replace(" ", "_"): s for s in bsdf.inputs}
    for key, value in inputs.items():
        sock = lookup[key]
        sock.default_value = (*value[:3], 1.0) if isinstance(value, (tuple, list)) else value
    mat.diffuse_color = (*color[:3], 1.0)   # viewport only
    return mat


def emission(name: str, color: Sequence[float] = (1, 1, 1), strength: float = 5.0) -> bpy.types.Material:
    return material(name, (0, 0, 0), rough=0.4, emission_color=color, emission_strength=strength)


def _node(tree, kind: str, **props):
    node = tree.nodes.new(kind)
    for key, value in props.items():
        setattr(node, key, value)
    return node


def add_surface_noise(mat: bpy.types.Material, scale: float = 40.0, bump: float = 0.15, rough_var: float = 0.12,
                      color_var: float = 0.06, detail: float = 6.0, object_space: bool = True) -> bpy.types.Material:
    """Break up a flat material: slight colour and roughness variation plus fine bump.
    Perfectly uniform surfaces are the quickest way to look computer-generated."""
    tree = mat.node_tree
    bsdf = principled(mat)
    coords = _node(tree, "ShaderNodeTexCoord")
    noise = _node(tree, "ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = scale
    noise.inputs["Detail"].default_value = detail
    tree.links.new(coords.outputs["Object" if object_space else "Generated"], noise.inputs["Vector"])
    base = tuple(bsdf.inputs["Base Color"].default_value)
    if color_var > 0:
        mix = _node(tree, "ShaderNodeMix", data_type="RGBA", blend_type="MULTIPLY")
        ramp = _node(tree, "ShaderNodeMapRange")
        ramp.inputs["To Min"].default_value = 1.0 - color_var
        ramp.inputs["To Max"].default_value = 1.0 + color_var
        tree.links.new(noise.outputs["Fac"], ramp.inputs["Value"])
        mul = _node(tree, "ShaderNodeVectorMath", operation="SCALE")
        mul.inputs[0].default_value = base[:3]
        tree.links.new(ramp.outputs["Result"], mul.inputs["Scale"])
        tree.links.new(mul.outputs["Vector"], bsdf.inputs["Base Color"])
        tree.nodes.remove(mix)
    if rough_var > 0:
        rough = bsdf.inputs["Roughness"].default_value
        rr = _node(tree, "ShaderNodeMapRange")
        rr.inputs["To Min"].default_value = max(0.0, rough - rough_var)
        rr.inputs["To Max"].default_value = min(1.0, rough + rough_var)
        tree.links.new(noise.outputs["Fac"], rr.inputs["Value"])
        tree.links.new(rr.outputs["Result"], bsdf.inputs["Roughness"])
    if bump > 0:
        fine = _node(tree, "ShaderNodeTexNoise")
        fine.inputs["Scale"].default_value = scale * 8
        fine.inputs["Detail"].default_value = 8.0
        tree.links.new(coords.outputs["Object" if object_space else "Generated"], fine.inputs["Vector"])
        bump_node = _node(tree, "ShaderNodeBump")
        bump_node.inputs["Strength"].default_value = bump
        bump_node.inputs["Distance"].default_value = 0.002
        tree.links.new(fine.outputs["Fac"], bump_node.inputs["Height"])
        tree.links.new(bump_node.outputs["Normal"], bsdf.inputs["Normal"])
    return mat


def wood(name: str, dark: Sequence[float] = (0.13, 0.065, 0.03), light: Sequence[float] = (0.27, 0.14, 0.065),
         grain_scale: float = 5.0, stretch: float = 12.0, rough: float = 0.42, axis: str = "X",
         coat: float = 0.25, bump: float = 0.2, banding: float = 0.3) -> bpy.types.Material:
    """Procedural wood. Broad stretched noise sets the tone, distorted bands add growth lines,
    a very fine fibre layer drives roughness and bump. `axis` is the grain direction (object space)."""
    mat = material(name, light, rough=rough, coat_weight=coat, coat_roughness=0.25)
    tree, bsdf = mat.node_tree, principled(mat)
    coords = _node(tree, "ShaderNodeTexCoord")
    mapping = _node(tree, "ShaderNodeMapping")
    squeeze = [1.0, 1.0, 1.0]
    squeeze["XYZ".index(axis)] = 1.0 / stretch
    mapping.inputs["Scale"].default_value = squeeze
    tree.links.new(coords.outputs["Object"], mapping.inputs["Vector"])
    tone = _node(tree, "ShaderNodeTexNoise")
    tone.inputs["Scale"].default_value = grain_scale
    tone.inputs["Detail"].default_value = 4.0
    tone.inputs["Roughness"].default_value = 0.62
    tone.inputs["Distortion"].default_value = 1.1
    tree.links.new(mapping.outputs["Vector"], tone.inputs["Vector"])
    across = "XYZ"[("XYZ".index(axis) + 1) % 3]
    lines = _node(tree, "ShaderNodeTexWave", wave_type="BANDS", bands_direction=across, wave_profile="SAW")
    lines.inputs["Scale"].default_value = grain_scale * 2.4
    lines.inputs["Distortion"].default_value = 7.0
    lines.inputs["Detail"].default_value = 2.0
    lines.inputs["Detail Scale"].default_value = 1.6
    tree.links.new(mapping.outputs["Vector"], lines.inputs["Vector"])
    blend = _node(tree, "ShaderNodeMix", data_type="FLOAT")
    blend.inputs["Factor"].default_value = banding
    tree.links.new(tone.outputs["Fac"], blend.inputs["A"])
    tree.links.new(lines.outputs["Fac"], blend.inputs["B"])
    ramp = _node(tree, "ShaderNodeValToRGB")
    mid = tuple((d + l) / 2 * 1.06 for d, l in zip(dark, light))
    ramp.color_ramp.elements[0].position, ramp.color_ramp.elements[0].color = 0.28, (*dark, 1)
    ramp.color_ramp.elements[1].position, ramp.color_ramp.elements[1].color = 0.74, (*light, 1)
    middle = ramp.color_ramp.elements.new(0.5)
    middle.color = (*mid, 1)
    tree.links.new(blend.outputs["Result"], ramp.inputs["Fac"])
    tree.links.new(ramp.outputs["Color"], bsdf.inputs["Base Color"])
    fibre_map = _node(tree, "ShaderNodeMapping")
    fine = [1.0, 1.0, 1.0]
    fine["XYZ".index(axis)] = 1.0 / (stretch * 4)
    fibre_map.inputs["Scale"].default_value = fine
    tree.links.new(coords.outputs["Object"], fibre_map.inputs["Vector"])
    fibre = _node(tree, "ShaderNodeTexNoise")
    fibre.inputs["Scale"].default_value = grain_scale * 60
    fibre.inputs["Detail"].default_value = 3.0
    tree.links.new(fibre_map.outputs["Vector"], fibre.inputs["Vector"])
    rr = _node(tree, "ShaderNodeMapRange")
    rr.inputs["To Min"].default_value, rr.inputs["To Max"].default_value = rough - 0.07, rough + 0.12
    tree.links.new(fibre.outputs["Fac"], rr.inputs["Value"])
    tree.links.new(rr.outputs["Result"], bsdf.inputs["Roughness"])
    bump_node = _node(tree, "ShaderNodeBump")
    bump_node.inputs["Strength"].default_value = bump
    bump_node.inputs["Distance"].default_value = 0.0012
    tree.links.new(fibre.outputs["Fac"], bump_node.inputs["Height"])
    tree.links.new(bump_node.outputs["Normal"], bsdf.inputs["Normal"])
    return mat


def screen_material(name: str, image_path: str, strength: float = 2.2, frames: int = 1, start_frame: int = 1,
                    offset: int = 0, gloss: float = 0.12) -> bpy.types.Material:
    """Emissive display. `image_path` is one image, or the first file of a numbered sequence
    (name_0001.png) when `frames` > 1; frame `start_frame` of the film shows the first image."""
    mat = material(name, (0.01, 0.01, 0.012), rough=gloss, coat_weight=1.0, coat_roughness=0.03)
    tree, bsdf = mat.node_tree, principled(mat)
    image = bpy.data.images.load(image_path, check_existing=True)
    tex = _node(tree, "ShaderNodeTexImage", image=image, extension="CLIP", interpolation="Cubic")
    if frames > 1:
        image.source = "SEQUENCE"
        user = tex.image_user
        user.frame_duration, user.frame_start, user.frame_offset = frames, start_frame, offset
        user.use_auto_refresh = True
        user.use_cyclic = False
    tree.links.new(tex.outputs["Color"], bsdf.inputs["Emission Color"])
    bsdf.inputs["Emission Strength"].default_value = strength
    return mat


def glass(name: str, color=(1, 1, 1), rough: float = 0.0, ior: float = 1.45, thin: bool = False) -> bpy.types.Material:
    mat = material(name, color, rough=rough, transmission_weight=1.0, ior=ior)
    if thin:
        principled(mat).inputs["Thin Wall"].default_value = True   # window panes: no refraction cost
    return mat


# --------------------------------------------------------------------------- lights and world


def look_at(obj: bpy.types.Object, target: Sequence[float]) -> None:
    direction = Vector(target) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def _light(name: str, kind: str, loc, target, power: float, color, temperature, group, coll) -> bpy.types.Object:
    data = bpy.data.lights.new(name, kind)
    data.energy = power
    if temperature:
        data.use_temperature, data.temperature = True, temperature
    if color is not None:
        data.color = color
    obj = link(bpy.data.objects.new(name, data), coll)
    obj.location = loc
    if target is not None:
        look_at(obj, target)
    if group:
        lightgroup(group)
        obj.lightgroup = group
    return obj


def area(name: str, loc, target, size: float | tuple[float, float] = 1.0, power: float = 100.0, color=None,
         temperature: float | None = None, spread: float = math.pi, group: str = "", coll=None) -> bpy.types.Object:
    obj = _light(name, "AREA", loc, target, power, color, temperature, group, coll)
    if isinstance(size, (tuple, list)):
        obj.data.shape, obj.data.size, obj.data.size_y = "RECTANGLE", size[0], size[1]
    else:
        obj.data.shape, obj.data.size = "DISK", size
    obj.data.spread = spread
    return obj


def point(name: str, loc, power: float = 50.0, radius: float = 0.03, color=None, temperature=None, group: str = "",
          coll=None) -> bpy.types.Object:
    obj = _light(name, "POINT", loc, None, power, color, temperature, group, coll)
    obj.data.shadow_soft_size = radius
    return obj


def spot(name: str, loc, target, power: float = 200.0, angle: float = 60.0, blend: float = 0.4, radius: float = 0.02,
         color=None, temperature=None, group: str = "", coll=None) -> bpy.types.Object:
    obj = _light(name, "SPOT", loc, target, power, color, temperature, group, coll)
    obj.data.spot_size, obj.data.spot_blend, obj.data.shadow_soft_size = math.radians(angle), blend, radius
    return obj


def sun(name: str, elevation: float, azimuth: float, strength: float = 4.0, angle: float = 1.0, color=None,
        temperature=None, group: str = "", coll=None) -> bpy.types.Object:
    """Sun light. Elevation above the horizon and compass azimuth (0 = +Y, clockwise) in degrees."""
    obj = _light(name, "SUN", (0, 0, 5), None, strength, color, temperature, group, coll)
    obj.data.angle = math.radians(angle)
    el, az = math.radians(elevation), math.radians(azimuth)
    toward_sun = Vector((math.sin(az) * math.cos(el), math.cos(az) * math.cos(el), math.sin(el)))
    obj.rotation_euler = (-toward_sun).to_track_quat("-Z", "Y").to_euler()
    return obj


def lightgroup(name: str, view_layer: bpy.types.ViewLayer | None = None) -> str:
    """Light groups give one render pass per group, so light levels can be changed after rendering."""
    layer = view_layer or bpy.context.view_layer
    if name not in [g.name for g in layer.lightgroups]:
        layer.lightgroups.add(name=name)
    return name


def world_sky(elevation: float = 20.0, azimuth: float = 120.0, strength: float = 0.25, sun_disc: bool = False,
              group: str = "", sc: bpy.types.Scene | None = None) -> bpy.types.World:
    """Physical sky as the world. Pair it with fk.sun(...) at the same angles for a crisp sun."""
    sc = sc or scene()
    world = sc.world or bpy.data.worlds.new("World")
    sc.world = world
    tree = world.node_tree
    background = next(n for n in tree.nodes if n.type == "BACKGROUND")
    sky = _node(tree, "ShaderNodeTexSky", sky_type="MULTIPLE_SCATTERING")
    sky.sun_elevation = math.radians(max(elevation, -5.0))
    sky.sun_rotation = math.radians(azimuth)
    sky.sun_disc = sun_disc
    tree.links.new(sky.outputs["Color"], background.inputs["Color"])
    background.inputs["Strength"].default_value = strength
    if group:
        lightgroup(group)
        world.lightgroup = group
    return world


def world_color(color=(0.02, 0.025, 0.04), strength: float = 1.0, group: str = "",
                sc: bpy.types.Scene | None = None) -> bpy.types.World:
    sc = sc or scene()
    world = sc.world or bpy.data.worlds.new("World")
    sc.world = world
    background = next(n for n in world.node_tree.nodes if n.type == "BACKGROUND")
    background.inputs["Color"].default_value = (*color, 1.0)
    background.inputs["Strength"].default_value = strength
    if group:
        lightgroup(group)
        world.lightgroup = group
    return world


def world_hdri(path: str, strength: float = 1.0, rotation: float = 0.0, group: str = "",
               sc: bpy.types.Scene | None = None) -> bpy.types.World:
    """Equirectangular HDRI. Blender ships eight small ones in datafiles/studiolights/world/."""
    sc = sc or scene()
    world = sc.world or bpy.data.worlds.new("World")
    sc.world = world
    tree = world.node_tree
    background = next(n for n in tree.nodes if n.type == "BACKGROUND")
    env = _node(tree, "ShaderNodeTexEnvironment", image=bpy.data.images.load(path, check_existing=True))
    mapping = _node(tree, "ShaderNodeMapping")
    mapping.inputs["Rotation"].default_value = (0, 0, math.radians(rotation))
    coords = _node(tree, "ShaderNodeTexCoord")
    tree.links.new(coords.outputs["Generated"], mapping.inputs["Vector"])
    tree.links.new(mapping.outputs["Vector"], env.inputs["Vector"])
    tree.links.new(env.outputs["Color"], background.inputs["Color"])
    background.inputs["Strength"].default_value = strength
    if group:
        lightgroup(group)
        world.lightgroup = group
    return world


# --------------------------------------------------------------------------- camera


def camera(name: str, loc, target, lens: float = 50.0, fstop: float | None = None, focus=None,
           sensor: float = 36.0, coll=None) -> bpy.types.Object:
    """Full-frame camera. `focus` is an object or a distance in metres; `fstop` None = no depth of field."""
    data = bpy.data.cameras.new(name)
    data.lens, data.sensor_width = lens, sensor
    data.clip_start, data.clip_end = 0.01, 200.0
    obj = link(bpy.data.objects.new(name, data), coll)
    obj.location = loc
    look_at(obj, target)
    if fstop is not None:
        data.dof.use_dof = True
        data.dof.aperture_fstop = fstop
        data.dof.aperture_blades = 9
        if isinstance(focus, bpy.types.Object):
            data.dof.focus_object = focus
        else:
            data.dof.focus_distance = focus if focus else (Vector(target) - Vector(loc)).length
    return obj


def cut_to(cam: bpy.types.Object, seconds: float, sc: bpy.types.Scene | None = None) -> None:
    """Make `cam` the active camera from this time on (timeline marker bound to the camera)."""
    sc = sc or scene()
    marker = sc.timeline_markers.new(cam.name, frame=frame(seconds, sc))
    marker.camera = cam
    if sc.camera is None or seconds <= 0:
        sc.camera = cam


# --------------------------------------------------------------------------- animation


def fcurves(block: bpy.types.ID) -> list[bpy.types.FCurve]:
    """All F-curves animating a data-block (slotted actions: they live in a channelbag)."""
    data = block.animation_data
    if not data or not data.action or not data.action_slot:
        return []
    bag = anim_utils.action_get_channelbag_for_slot(data.action, data.action_slot)
    return list(bag.fcurves) if bag else []


def key(block: bpy.types.ID, path: str, seconds: float, value=None, index: int = -1, interp: str = "BEZIER",
        easing: str = "AUTO", handles: str = "AUTO_CLAMPED") -> None:
    """Keyframe `path` at a time in seconds. `interp`: BEZIER, LINEAR, CONSTANT, SINE, QUAD,
    CUBIC, QUART, QUINT, EXPO, CIRC, BACK, BOUNCE, ELASTIC; `easing`: AUTO, EASE_IN, EASE_OUT, EASE_IN_OUT.
    The interpolation applies from this key to the next one."""
    f = frame(seconds)
    if value is not None:
        target, _, prop = path.rpartition(".")
        owner = block.path_resolve(target) if target else block
        if index >= 0:
            getattr(owner, prop)[index] = value
        else:
            setattr(owner, prop, value)
    block.keyframe_insert(path, index=index, frame=f)
    for curve in fcurves(block):
        if curve.data_path == path and (index < 0 or curve.array_index == index):
            for point in curve.keyframe_points:
                if abs(point.co.x - f) < 0.5:
                    point.interpolation, point.easing = interp, easing
                    point.handle_left_type = point.handle_right_type = handles
            curve.update()


def bake(block: bpy.types.ID, path: str, fn: Callable[[float], float | Sequence[float]], t0: float, t1: float,
         index: int = -1) -> None:
    """Sample fn(t) on every frame between t0 and t1 (seconds) and key the result linearly.
    Use for motion that is easier to write as a formula: hops, springs, orbits, hand-held drift."""
    target, _, prop = path.rpartition(".")
    owner = block.path_resolve(target) if target else block
    fps = scene().render.fps
    for f in range(frame(t0), frame(t1) + 1):
        value = fn((f - 1) / fps)
        if index >= 0:
            getattr(owner, prop)[index] = value
        else:
            setattr(owner, prop, value)
        block.keyframe_insert(path, index=index, frame=f)
    for curve in fcurves(block):
        if curve.data_path == path and (index < 0 or curve.array_index == index):
            for point in curve.keyframe_points:
                point.interpolation = "LINEAR"


def smoothstep(x: float) -> float:
    x = min(1.0, max(0.0, x))
    return x * x * (3 - 2 * x)


def ease_out_cubic(x: float) -> float:
    x = min(1.0, max(0.0, x))
    return 1 - (1 - x) ** 3


def ease_in_out_cubic(x: float) -> float:
    x = min(1.0, max(0.0, x))
    return 4 * x ** 3 if x < 0.5 else 1 - (-2 * x + 2) ** 3 / 2


def hop(t: float, start: float, duration: float, height: float, squash: float = 0.25) -> tuple[float, float]:
    """One hop with anticipation, stretch in the air and squash on landing.
    Returns (height above ground, vertical scale); scale the other two axes by 1/sqrt(scale)."""
    u = (t - start) / duration
    if u <= 0 or u >= 1.25:
        return 0.0, 1.0
    if u < 0.18:                       # anticipation: crouch
        return 0.0, 1.0 - squash * math.sin(u / 0.18 * math.pi / 2)
    if u < 0.88:                       # flight: parabola, stretched while moving fast
        v = (u - 0.18) / 0.70
        z = height * 4 * v * (1 - v)
        speed = abs(1 - 2 * v)
        return z, 1.0 + squash * 0.8 * speed
    if u < 1.0:                        # landing: squash
        v = (u - 0.88) / 0.12
        return 0.0, 1.0 - squash * math.sin(v * math.pi / 2)
    v = (u - 1.0) / 0.25               # settle with one small overshoot
    return 0.0, 1.0 - squash * (1 - v) * math.cos(v * math.pi * 1.5)


# --------------------------------------------------------------------------- render


def render_still(path: str, frame_number: int | None = None, sc: bpy.types.Scene | None = None) -> float:
    """Render one frame to `path` (extension added by Blender). Returns seconds taken."""
    import time
    sc = sc or scene()
    if frame_number is not None:
        sc.frame_set(frame_number)
        for marker in sorted(sc.timeline_markers, key=lambda m: m.frame):   # honour camera cuts
            if marker.camera and marker.frame <= frame_number:
                sc.camera = marker.camera
    sc.render.filepath = path
    started = time.time()
    bpy.ops.render.render(write_still=True, scene=sc.name)
    return time.time() - started


def save(path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=path, check_existing=False)


# --------------------------------------------------------------------------- plates (render once, light in comp)


def plate_meta(sc: bpy.types.Scene | None = None, track: Sequence[str] = ()) -> dict:
    """Camera facts and, for each object name in `track` (planes made with fk.plane), the pixel
    position of its four corners (top-left, top-right, bottom-right, bottom-left in UV terms),
    its distance from the camera and the blur-circle diameter there. The compositor uses this to
    put images on screens and posters after rendering."""
    from bpy_extras.object_utils import world_to_camera_view
    sc = sc or scene()
    cam = sc.camera
    scale = sc.render.resolution_percentage / 100
    width, height = int(sc.render.resolution_x * scale), int(sc.render.resolution_y * scale)
    meta = {"frame": sc.frame_current, "width": width, "height": height, "camera": cam.name,
            "lens": cam.data.lens, "fstop": cam.data.dof.aperture_fstop if cam.data.dof.use_dof else None,
            "lightgroups": [g.name for g in bpy.context.view_layer.lightgroups], "quads": {}}
    depsgraph = bpy.context.evaluated_depsgraph_get()
    focus = None
    if cam.data.dof.use_dof:
        target = cam.data.dof.focus_object
        focus = ((target.matrix_world.translation - cam.matrix_world.translation).dot(
            cam.matrix_world.to_quaternion() @ Vector((0, 0, -1))) if target else cam.data.dof.focus_distance)
    for name in track:
        obj = bpy.data.objects[name].evaluated_get(depsgraph)
        mesh = obj.data
        uv = mesh.uv_layers.active.data
        corners = {}
        for loop in mesh.loops:
            u, v = uv[loop.index].uv
            world = obj.matrix_world @ mesh.vertices[loop.vertex_index].co
            x, y, depth = world_to_camera_view(sc, cam, world)
            corners[(round(u), round(v))] = [x * width, (1 - y) * height, depth]
        ordered = [corners[key] for key in ((0, 1), (1, 1), (1, 0), (0, 0))]
        depth = sum(c[2] for c in ordered) / 4
        coc = 0.0
        if focus and cam.data.dof.use_dof:
            f = cam.data.lens / 1000
            coc_m = abs(f * f * (depth - focus) / (cam.data.dof.aperture_fstop * depth * (focus - f)))
            coc = coc_m / (cam.data.sensor_width / 1000) * width
        meta["quads"][name] = {"corners": [c[:2] for c in ordered], "depth": depth, "blur_px": coc}
    return meta


def render_plate(path: str, samples: int = 256, threshold: float = 0.01, track: Sequence[str] = (),
                 region: Sequence[float] | None = None, sc: bpy.types.Scene | None = None) -> float:
    """Render the current frame as a multilayer EXR with one pass per light group and the
    denoising guide passes, plus <path>.json from plate_meta(). No denoising here: the compositor
    denoises each light group separately. `region` = (x0, y0, x1, y1) as fractions of the frame
    (origin bottom-left) renders only that part: use it for the frames where something small moves."""
    import json
    import time
    sc = sc or scene()
    layer = bpy.context.view_layer
    c = sc.cycles
    previous = (c.samples, c.adaptive_threshold, c.use_denoising, sc.render.use_border)
    c.samples, c.adaptive_threshold, c.use_denoising = samples, threshold, False
    c.adaptive_min_samples = max(16, samples // 4)
    layer.cycles.denoising_store_passes = True
    layer.use_pass_z = True
    sc.render.use_border = region is not None
    sc.render.use_crop_to_border = False
    if region is not None:
        sc.render.border_min_x, sc.render.border_min_y, sc.render.border_max_x, sc.render.border_max_y = region
    s = sc.render.image_settings
    s.media_type = "MULTI_LAYER_IMAGE"
    s.file_format = "OPEN_EXR_MULTILAYER"
    s.color_depth, s.exr_codec = "16", "ZIP"
    sc.render.filepath = path
    sc.render.use_file_extension = True
    started = time.time()
    bpy.ops.render.render(write_still=True, scene=sc.name)
    seconds = time.time() - started
    meta = plate_meta(sc, track)
    meta.update(samples=samples, render_seconds=round(seconds, 1), region=list(region) if region else None)
    with open(path + ".json", "w") as handle:
        json.dump(meta, handle, indent=1)
    c.samples, c.adaptive_threshold, c.use_denoising, sc.render.use_border = previous
    return seconds
