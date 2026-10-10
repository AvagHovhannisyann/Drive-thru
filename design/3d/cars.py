"""
cars.py -- procedural, real-world-proportioned road vehicles for the drive-thru Cycles scene
===========================================================================================

Interface
---------
    import cars
    cars.CAR_KINDS  -> ["sedan", "suv", "hatch", "ev", "van", "lada"]
    empty = cars.make_car(name, kind, color, x, y, heading,
                          lights_on=False, link_fn=None, mats=None,
                          z=0.03, steer=0.0, metallic=None, plate=None, seed=None)

* ``kind``    one of CAR_KINDS (unknown kinds fall back to "sedan").
               sedan = Toyota Camry XV70 / Mercedes E-class class   (4.885 x 1.840 x 1.445 m)
               suv   = Toyota RAV4 / Lexus RX class                 (4.750 x 1.880 x 1.690 m)
               hatch = Hyundai i30 / Kia Ceed class                 (4.340 x 1.795 x 1.455 m)
               ev    = BYD Seal / Tesla Model 3 class (glass roof)  (4.780 x 1.860 x 1.440 m)
               van   = Ford Transit / Mercedes Sprinter L2H2 class  (5.530 x 2.060 x 2.550 m)
               lada  = VAZ-2107 "Zhiguli" (chrome bumpers, 13" wheels) (4.145 x 1.620 x 1.440 m)
* ``color``   linear RGB tuple of the body paint.  Metallic is auto-detected (greys, silvers and
               dark saturated colours become metallic) unless ``metallic`` is given.
* ``x, y``    footprint centre (world metres), ``heading`` in degrees (0 = car points +X),
               ``z`` ground height (default 0.03 = site asphalt top used by build_scene).
* ``lights_on`` switches head/tail/DRL emission on and adds two forward spot lamps.
* ``link_fn``  callable(ob, collection_name) used to link every created object (pass
               build_scene.link).  Default links into a "vehicles" collection of the scene.
* ``mats``    optional dict overriding any module material by key (see MAT_KEYS); missing keys
               are created here, prefixed "car_" to avoid clashes with scene materials.
* returns the parent Empty; body / wheels / lamps are parented to it (local coordinates:
  +X forward, +Y left, Z up, origin at the centre of the footprint on the ground).

Construction
------------
Lower body: bmesh loft through ~50 cross-sections (filleted 9-point half sections with a crisp
shoulder crease, tumble-under rocker, crowned deck), plan-view rounded corners and radial end caps
with rake/bulge, made manifold and cut by a boolean (MANIFOLD solver, EXACT fallback) to give
recessed wheel arches with black liners.  Greenhouse: separate loft with A/B/C(/D) pillars in body
paint, tumblehome, belt seal, window frames and see-through tinted glass (fresnel glossy over
tinted transparent) with a simple interior (seats, head-rests, dash, wheel).  Details are
BVH-projected onto the body: wrap-around head/tail-light clusters (lens + LED strip), grilles,
black bumper/cladding parts, door shut lines, handles, cowl, number plates (Armenian 520 x 112 mm
with flag, "AM" and a generated registration), mirrors, roof rails / chrome bumpers per kind.
Wheels: revolved tyres with bulged sidewalls, alloy rims (10-spoke / twin / 5-spoke / aero /
steel+hubcap), brake discs and callipers.  Geometry is cached per kind (shared mesh datablocks,
per-object material slots), so 30 cars cost about as much as six.  ~7-10k faces per car, no
subdivision modifiers.
"""
import bpy
import bmesh
import math
import random
import bisect
from mathutils import Vector
from mathutils.bvhtree import BVHTree

CAR_KINDS = ["sedan", "suv", "hatch", "ev", "van", "lada"]

# material slot order of the body mesh (all slots are overridden per object)
SLOTS = ["paint", "glass", "trim", "gloss", "chrome", "grille", "head", "drl", "tail", "plate",
         "interior", "well", "gap", "mirror", "under", "amber", "glass_opaque", "seat"]
SI = {k: i for i, k in enumerate(SLOTS)}
WSLOTS = ["tyre", "rim", "brake", "caliper", "hub_dark", "hubcap"]
WI = {k: i for i, k in enumerate(WSLOTS)}
MAT_KEYS = sorted(set(SLOTS + WSLOTS + ["head_on", "head_off", "drl_on", "drl_off", "tail_on", "tail_off",
                                        "rim_steel", "rim_dark"]) - {"paint", "plate", "head", "drl", "tail"})


# ======================================================================================
# small maths helpers
# ======================================================================================
class Curve:
    """Monotone cubic (Fritsch-Carlson / PCHIP) interpolation through (x, y) keys, clamped ends."""

    def __init__(self, pts):
        pts = sorted(pts)
        self.x = [float(p[0]) for p in pts]
        self.y = [float(p[1]) for p in pts]
        n = len(pts)
        if n == 1:
            self.x.append(self.x[0] + 1.0); self.y.append(self.y[0]); n = 2
        h = [self.x[i + 1] - self.x[i] for i in range(n - 1)]
        d = [(self.y[i + 1] - self.y[i]) / h[i] for i in range(n - 1)]
        m = [0.0] * n
        m[0], m[-1] = d[0], d[-1]
        for i in range(1, n - 1):
            if d[i - 1] * d[i] <= 0:
                m[i] = 0.0
            else:
                w1 = 2 * h[i] + h[i - 1]
                w2 = h[i] + 2 * h[i - 1]
                m[i] = (w1 + w2) / (w1 / d[i - 1] + w2 / d[i])
        self.h, self.m = h, m

    def __call__(self, x):
        xs = self.x
        if x <= xs[0]:
            return self.y[0]
        if x >= xs[-1]:
            return self.y[-1]
        i = bisect.bisect_right(xs, x) - 1
        h = self.h[i]
        t = (x - xs[i]) / h
        t2, t3 = t * t, t * t * t
        return ((2 * t3 - 3 * t2 + 1) * self.y[i] + (t3 - 2 * t2 + t) * h * self.m[i]
                + (-2 * t3 + 3 * t2) * self.y[i + 1] + (t3 - t2) * h * self.m[i + 1])


def _fillet(pts, radii, segs):
    """Replace interior corners of a 2D polyline by quadratic-Bezier fillets.
    Returns (points, s) where s[i] is the fractional control-polyline parameter of each point."""
    out = [tuple(pts[0])]
    par = [0.0]
    for i in range(1, len(pts) - 1):
        P, A, B = Vector(pts[i]), Vector(pts[i - 1]), Vector(pts[i + 1])
        da, db = A - P, B - P
        la, lb = da.length, db.length
        da.normalize(); db.normalize()
        ang = math.acos(max(-1.0, min(1.0, da.dot(db))))
        t = radii[i - 1] / max(math.tan(ang / 2), 1e-4)
        t = min(max(t, 0.002), 0.45 * min(la, lb))
        T1, T2 = P + da * t, P + db * t
        n = segs[i - 1]
        for k in range(n + 1):
            u = k / n
            Q = T1 * (1 - u) ** 2 + P * (2 * u * (1 - u)) + T2 * (u * u)
            out.append((Q.x, Q.y))
            par.append(i + (u - 0.5) * 0.5)
    out.append(tuple(pts[-1]))
    par.append(len(pts) - 1.0)
    return out, par


def _smooth01(t):
    t = min(1.0, max(0.0, t))
    return t * t * (3 - 2 * t)


# ======================================================================================
# vehicle specifications (real-world dimensions; xf = distance from the front bumper)
# ======================================================================================
_R_DEF = [0.03, 0.04, 0.10, 0.30, 0.008, 0.035, 0.40]   # fillet radii C1..C7
_SEGS = [1, 2, 2, 2, 2, 3, 2]

SPECS = {
    # ---------------------------------------------------------------- Toyota Camry XV70 class
    "sedan": dict(
        L=4.885, W=1.84, H=1.445, wb=2.825, fo=0.975, R=0.334, rim=0.2286, tw=0.235, gap=0.045,
        rc_f=0.42, rc_r=0.30, bulge_f=0.035, bulge_r=0.03,
        bot=[(0, 0.27), (0.10, 0.215), (0.35, 0.175), (0.8, 0.16), (1.4, 0.15), (3.4, 0.15), (4.0, 0.16),
             (4.5, 0.215), (4.885, 0.33)],
        deck=[(0, 0.645), (0.05, 0.715), (0.13, 0.77), (0.35, 0.815), (0.8, 0.865), (1.25, 0.912), (1.58, 0.94),
              (2.4, 0.955), (3.4, 0.99), (3.92, 1.035), (4.2, 1.055), (4.62, 1.05), (4.76, 1.035), (4.885, 0.985)],
        belt=[(0, 0.625), (0.12, 0.70), (0.5, 0.795), (1.0, 0.878), (1.58, 0.935), (2.5, 0.965), (3.5, 1.01),
              (3.95, 1.03), (4.4, 1.035), (4.885, 0.965)],
        sh=[(0, 0.555), (0.15, 0.64), (0.6, 0.735), (1.2, 0.805), (2.5, 0.855), (3.8, 0.895), (4.4, 0.905),
            (4.885, 0.86)],
        tumble=[(0, 0.08), (0.6, 0.07), (1.6, 0.068), (3.9, 0.075), (4.885, 0.09)],
        hwf=[(0, 0.965), (0.5, 0.985), (1.2, 0.997), (2.6, 1.0), (3.8, 1.0), (4.4, 0.99), (4.885, 0.975)],
        crown=0.025,
        rake_f=[(0.15, -0.07), (0.25, -0.02), (0.38, 0.0), (0.50, -0.012), (0.62, -0.045), (0.80, -0.10)],
        rake_r=[(0.25, -0.06), (0.40, -0.01), (0.55, 0.0), (0.80, -0.015), (0.95, -0.04), (1.1, -0.08)],
        gh=dict(cowl=1.58, ws_top=2.50, roof_rear=3.30, tail=3.92,
                top=[(1.58, 0.985), (1.85, 1.115), (2.15, 1.27), (2.40, 1.385), (2.56, 1.425), (2.85, 1.445),
                     (3.12, 1.432), (3.32, 1.395), (3.60, 1.245), (3.92, 1.075)],
                rail=[(1.58, 0.94), (1.95, 1.10), (2.30, 1.275), (2.60, 1.37), (2.9, 1.388), (3.2, 1.365),
                      (3.42, 1.29), (3.70, 1.14), (3.92, 1.045)],
                tgh=[(1.58, 0.03), (2.3, 0.14), (2.6, 0.165), (3.2, 0.165), (3.6, 0.11), (3.92, 0.05)],
                bpil=(2.63, 2.72), dlo_end=3.47, windows=[(1.58, 2.63), (2.72, 3.47), (3.50, 3.66)],
                frame="chrome", belt_mat="chrome", bpil_mat="paint", roof_glass=False),
        wheel="multi", rim_mat="rim",
        lights="camry", mirror=(0.12, 0.21, 0.13),
    ),
    # ---------------------------------------------------------------- BYD Seal / Tesla Model 3 class
    "ev": dict(
        L=4.78, W=1.86, H=1.44, wb=2.90, fo=0.86, R=0.338, rim=0.2413, tw=0.235, gap=0.04,
        rc_f=0.46, rc_r=0.34, bulge_f=0.05, bulge_r=0.03,
        bot=[(0, 0.25), (0.10, 0.195), (0.35, 0.16), (0.8, 0.14), (3.5, 0.14), (4.1, 0.17), (4.5, 0.24),
             (4.78, 0.36)],
        deck=[(0, 0.56), (0.05, 0.63), (0.14, 0.68), (0.4, 0.72), (0.8, 0.77), (1.15, 0.83), (1.40, 0.875),
              (2.4, 0.93), (3.6, 1.0), (4.1, 1.045), (4.45, 1.062), (4.62, 1.068), (4.70, 1.06), (4.78, 1.0)],
        belt=[(0, 0.545), (0.12, 0.62), (0.5, 0.715), (1.0, 0.815), (1.40, 0.868), (2.5, 0.925), (3.6, 0.985),
              (4.2, 1.035), (4.5, 1.048), (4.78, 0.985)],
        sh=[(0, 0.47), (0.2, 0.57), (0.8, 0.70), (2.0, 0.795), (3.8, 0.86), (4.5, 0.88), (4.78, 0.84)],
        tumble=[(0, 0.09), (0.8, 0.075), (1.5, 0.07), (3.9, 0.085), (4.78, 0.10)],
        hwf=[(0, 0.955), (0.5, 0.98), (1.2, 0.995), (2.6, 1.0), (3.8, 1.0), (4.4, 0.99), (4.78, 0.975)],
        crown=0.03,
        rake_f=[(0.15, -0.05), (0.25, -0.01), (0.33, 0.0), (0.45, -0.02), (0.56, -0.06), (0.70, -0.11)],
        rake_r=[(0.30, -0.06), (0.45, -0.01), (0.60, 0.0), (0.85, -0.02), (1.0, -0.06), (1.1, -0.09)],
        gh=dict(cowl=1.40, ws_top=2.42, roof_rear=3.05, tail=4.28,
                top=[(1.40, 0.92), (1.70, 1.055), (2.0, 1.20), (2.25, 1.33), (2.45, 1.40), (2.75, 1.44),
                     (3.05, 1.425), (3.35, 1.36), (3.70, 1.25), (4.0, 1.155), (4.28, 1.085)],
                rail=[(1.40, 0.872), (1.8, 1.06), (2.2, 1.265), (2.5, 1.355), (2.8, 1.382), (3.1, 1.36),
                      (3.5, 1.25), (3.85, 1.125), (4.1, 1.07), (4.28, 1.05)],
                tgh=[(1.40, 0.03), (2.2, 0.14), (2.6, 0.17), (3.2, 0.17), (3.8, 0.12), (4.28, 0.05)],
                bpil=(2.52, 2.62), dlo_end=3.92, windows=[(1.40, 2.52), (2.62, 3.55), (3.58, 3.92)],
                frame="trim", belt_mat="trim", bpil_mat="gloss", roof_glass=True),
        wheel="aero", rim_mat="rim_dark",
        lights="ev", mirror=(0.12, 0.20, 0.12), flush_handles=True,
    ),
    # ---------------------------------------------------------------- Toyota RAV4 / Lexus RX class
    "suv": dict(
        L=4.75, W=1.88, H=1.69, wb=2.75, fo=0.95, R=0.370, rim=0.2413, tw=0.235, gap=0.06,
        rc_f=0.42, rc_r=0.24, bulge_f=0.04, bulge_r=0.02,
        bot=[(0, 0.40), (0.12, 0.32), (0.4, 0.255), (0.8, 0.21), (3.9, 0.21), (4.3, 0.26), (4.75, 0.42)],
        deck=[(0, 0.865), (0.05, 0.94), (0.15, 0.995), (0.4, 1.035), (0.9, 1.07), (1.35, 1.108), (1.55, 1.125),
              (2.5, 1.15), (4.0, 1.19), (4.45, 1.20), (4.62, 1.192), (4.75, 1.13)],
        belt=[(0, 0.845), (0.12, 0.92), (0.6, 1.015), (1.55, 1.118), (3.0, 1.155), (4.3, 1.185), (4.62, 1.18),
              (4.75, 1.11)],
        sh=[(0, 0.77), (0.25, 0.86), (1.0, 0.965), (2.5, 1.025), (4.2, 1.075), (4.75, 1.02)],
        tumble=[(0, 0.08), (0.6, 0.07), (1.6, 0.07), (4.2, 0.075), (4.75, 0.08)],
        hwf=[(0, 0.965), (0.5, 0.985), (1.2, 0.997), (2.6, 1.0), (3.8, 1.0), (4.4, 0.995), (4.75, 0.985)],
        crown=0.025,
        rake_f=[(0.30, -0.08), (0.42, -0.02), (0.55, 0.0), (0.70, -0.015), (0.85, -0.05), (1.0, -0.10)],
        rake_r=[(0.35, -0.05), (0.50, -0.01), (0.65, 0.0), (0.95, -0.01), (1.1, -0.03), (1.2, -0.06)],
        gh=dict(cowl=1.55, ws_top=2.40, roof_rear=4.40, tail=4.64,
                top=[(1.55, 1.165), (1.85, 1.315), (2.15, 1.47), (2.40, 1.60), (2.60, 1.655), (3.0, 1.69),
                     (3.6, 1.685), (4.1, 1.665), (4.35, 1.64), (4.50, 1.53), (4.64, 1.215)],
                rail=[(1.55, 1.12), (1.95, 1.325), (2.3, 1.50), (2.6, 1.585), (3.2, 1.61), (3.9, 1.595),
                      (4.3, 1.56), (4.48, 1.46), (4.64, 1.20)],
                tgh=[(1.55, 0.03), (2.3, 0.13), (2.6, 0.15), (4.2, 0.15), (4.64, 0.12)],
                bpil=(2.70, 2.79), dlo_end=3.62, windows=[(1.55, 2.70), (2.79, 3.62), (3.72, 4.20)],
                frame="trim", belt_mat="chrome", bpil_mat="gloss", roof_glass=False),
        wheel="twin", rim_mat="rim",
        lights="rav4", mirror=(0.13, 0.22, 0.15), roof_rails=True, cladding=True,
    ),
    # ---------------------------------------------------------------- Hyundai i30 / Kia Ceed class
    "hatch": dict(
        L=4.34, W=1.795, H=1.455, wb=2.65, fo=0.88, R=0.317, rim=0.2159, tw=0.225, gap=0.042,
        rc_f=0.40, rc_r=0.26, bulge_f=0.035, bulge_r=0.02,
        bot=[(0, 0.26), (0.10, 0.20), (0.35, 0.165), (0.8, 0.145), (3.2, 0.145), (3.8, 0.17), (4.1, 0.22),
             (4.34, 0.33)],
        deck=[(0, 0.625), (0.05, 0.70), (0.13, 0.755), (0.4, 0.80), (0.9, 0.86), (1.3, 0.905), (1.45, 0.925),
              (2.4, 0.95), (3.6, 1.005), (3.95, 1.025), (4.16, 1.03), (4.26, 1.015), (4.34, 0.955)],
        belt=[(0, 0.605), (0.12, 0.69), (0.5, 0.785), (1.0, 0.865), (1.45, 0.92), (2.6, 0.955), (3.5, 0.995),
              (4.0, 1.022), (4.16, 1.025), (4.34, 0.94)],
        sh=[(0, 0.545), (0.2, 0.63), (0.8, 0.745), (2.0, 0.825), (3.6, 0.885), (4.34, 0.86)],
        tumble=[(0, 0.08), (0.6, 0.07), (1.5, 0.068), (3.8, 0.075), (4.34, 0.085)],
        hwf=[(0, 0.965), (0.5, 0.985), (1.2, 0.997), (2.6, 1.0), (3.5, 1.0), (4.0, 0.99), (4.34, 0.975)],
        crown=0.025,
        rake_f=[(0.15, -0.07), (0.25, -0.02), (0.37, 0.0), (0.50, -0.012), (0.62, -0.045), (0.80, -0.10)],
        rake_r=[(0.25, -0.05), (0.40, -0.01), (0.55, 0.0), (0.80, -0.01), (0.95, -0.03), (1.05, -0.06)],
        gh=dict(cowl=1.45, ws_top=2.35, roof_rear=3.70, tail=4.17,
                top=[(1.45, 0.968), (1.75, 1.12), (2.05, 1.28), (2.30, 1.39), (2.50, 1.435), (2.9, 1.455),
                     (3.4, 1.445), (3.70, 1.42), (3.95, 1.275), (4.17, 1.05)],
                rail=[(1.45, 0.925), (1.85, 1.125), (2.2, 1.295), (2.5, 1.378), (3.0, 1.398), (3.45, 1.385),
                      (3.75, 1.33), (3.98, 1.18), (4.17, 1.035)],
                tgh=[(1.45, 0.03), (2.2, 0.14), (2.5, 0.16), (3.5, 0.16), (3.9, 0.12), (4.17, 0.07)],
                bpil=(2.56, 2.64), dlo_end=3.50, windows=[(1.45, 2.56), (2.64, 3.50)],
                frame="trim", belt_mat="trim", bpil_mat="gloss", roof_glass=False),
        wheel="five", rim_mat="rim",
        lights="i30", mirror=(0.12, 0.20, 0.13),
    ),
    # ---------------------------------------------------------------- Ford Transit / Sprinter L2H2
    "van": dict(
        L=5.53, W=2.06, H=2.55, wb=3.30, fo=0.95, R=0.356, rim=0.2032, tw=0.235, gap=0.06,
        rc_f=0.32, rc_r=0.08, bulge_f=0.04, bulge_r=0.0,
        bot=[(0, 0.37), (0.12, 0.31), (0.4, 0.245), (0.8, 0.20), (4.6, 0.20), (5.3, 0.30), (5.53, 0.42)],
        deck=[(0, 0.90), (0.06, 0.975), (0.18, 1.035), (0.5, 1.085), (0.80, 1.13), (0.95, 1.17), (1.10, 1.32),
              (1.35, 1.58), (1.60, 1.835), (1.80, 2.02), (1.95, 2.15), (2.15, 2.30), (2.40, 2.405), (2.9, 2.475),
              (4.5, 2.50), (5.35, 2.50), (5.45, 2.48), (5.53, 2.40)],
        belt=[(0, 0.88), (0.15, 0.99), (0.5, 1.065), (0.95, 1.14), (1.2, 1.37), (1.5, 1.685), (1.8, 1.955),
              (2.1, 2.16), (2.4, 2.30), (2.9, 2.38), (5.4, 2.40), (5.53, 2.33)],
        sh=[(0, 0.80), (0.3, 0.92), (0.95, 1.055), (1.5, 1.11), (5.53, 1.12)],
        tumble=[(0, 0.10), (0.95, 0.10), (1.6, 0.12), (2.4, 0.13), (5.53, 0.12)],
        hwf=[(0, 0.95), (0.6, 0.975), (1.4, 0.99), (2.2, 1.0), (5.53, 1.0)],
        crown=0.055, radii=[0.03, 0.05, 0.10, 0.4, 0.02, 0.10, 0.5],
        rake_f=[(0.30, -0.06), (0.45, -0.01), (0.60, 0.0), (0.80, -0.02), (0.95, -0.06), (1.10, -0.12)],
        rake_r=[(0.3, 0.0), (2.6, 0.0)],
        gh=None,
        wheel="steel", rim_mat="rim_steel",
        lights="van", mirror=(0.16, 0.30, 0.30), van=True,
    ),
    # ---------------------------------------------------------------- VAZ-2107
    "lada": dict(
        L=4.03, W=1.62, H=1.44, wb=2.424, fo=0.74, R=0.288, rim=0.1651, tw=0.175, gap=0.05,
        rc_f=0.10, rc_r=0.09, bulge_f=0.01, bulge_r=0.01, Lbumper=0.06,
        bot=[(0, 0.32), (0.08, 0.27), (0.3, 0.205), (0.65, 0.18), (3.3, 0.18), (3.7, 0.22), (4.03, 0.32)],
        deck=[(0, 0.80), (0.025, 0.835), (0.07, 0.852), (0.7, 0.866), (1.36, 0.875), (2.3, 0.882), (2.95, 0.925),
              (3.22, 0.952), (3.85, 0.955), (3.97, 0.95), (4.03, 0.915)],
        belt=[(0, 0.79), (0.05, 0.832), (1.36, 0.862), (2.5, 0.872), (3.22, 0.94), (3.9, 0.945), (4.03, 0.905)],
        sh=[(0, 0.735), (0.1, 0.775), (1.36, 0.795), (3.0, 0.825), (4.03, 0.84)],
        tumble=[(0, 0.045), (4.03, 0.045)],
        hwf=[(0, 0.99), (0.4, 1.0), (3.6, 1.0), (4.03, 0.99)],
        crown=0.015, radii=[0.02, 0.025, 0.05, 0.25, 0.006, 0.02, 0.4],
        rake_f=[(0.30, -0.02), (0.40, 0.0), (0.70, 0.0), (0.85, -0.02)],
        rake_r=[(0.30, -0.02), (0.40, 0.0), (0.80, 0.0), (0.95, -0.015)],
        gh=dict(cowl=1.36, ws_top=2.10, roof_rear=3.00, tail=3.24,
                top=[(1.36, 0.892), (1.62, 1.07), (1.88, 1.245), (2.10, 1.375), (2.28, 1.405), (2.7, 1.415),
                     (2.98, 1.40), (3.10, 1.30), (3.24, 0.968)],
                rail=[(1.36, 0.87), (1.68, 1.08), (1.98, 1.28), (2.18, 1.35), (2.7, 1.368), (2.96, 1.35),
                      (3.10, 1.24), (3.24, 0.955)],
                tgh=[(1.36, 0.03), (2.1, 0.11), (2.95, 0.11), (3.24, 0.06)],
                bpil=(2.27, 2.36), dlo_end=2.97, windows=[(1.36, 2.27), (2.36, 2.97)],
                frame="chrome", belt_mat="chrome", bpil_mat="paint", roof_glass=False),
        wheel="lada", rim_mat="rim_steel",
        lights="lada", mirror=(0.10, 0.14, 0.09), bumpers="chrome",
    ),
}


def _prep(kind):
    S = dict(SPECS[kind])
    S["kind"] = kind
    for k in ("bot", "deck", "belt", "sh", "tumble", "hwf"):
        S[k + "_c"] = Curve(S[k])
    S["rake_f_c"] = Curve(S["rake_f"])
    S["rake_r_c"] = Curve(S["rake_r"])
    S.setdefault("radii", _R_DEF)
    g = S.get("gh")
    if g:
        g = dict(g)
        g["top_c"] = Curve(g["top"]); g["rail_c"] = Curve(g["rail"]); g["tgh_c"] = Curve(g["tgh"])
        S["gh"] = g
    S["hw"] = S["W"] / 2
    S["xa_f"] = S["L"] / 2 - S["fo"]             # front axle x (car local)
    S["xa_r"] = S["xa_f"] - S["wb"]              # rear axle x
    S["ra"] = S["R"] + S["gap"]                   # arch radius
    S["yw"] = S["hw"] - 0.025 - S["tw"] / 2      # wheel centre |y|
    return S


def _X(S, xf):
    return S["L"] / 2 - xf


# ======================================================================================
# lower body loft
# ======================================================================================
def _half_section(S, xf, hw):
    """Filleted half cross-section (y >= 0) at station xf. Returns (pts, par)."""
    zb = S["bot_c"](xf)
    zsh = S["sh_c"](xf)
    zbe = S["belt_c"](xf)
    zd = S["deck_c"](xf)
    tum = S["tumble_c"](xf)
    cr = S["crown"]
    k = max(0.25, hw / S["hw"])
    zsh = max(zsh, zb + 0.08)
    zbe = max(zbe, zsh + 0.03)
    ztop = max(zd + cr, zbe + 0.008)
    z3 = zb + min(0.12, 0.3 * (zsh - zb))
    zmid = zb + 0.6 * (zsh - zb)
    yb = max(hw - tum, 0.25 * hw)
    pts = [(0.0, zb), (hw - 0.20 * k, zb), (hw - 0.035, zb + 0.03), (hw - 0.025, z3), (hw - 0.007, zmid),
           (hw, zsh), (yb, zbe), (0.55 * yb, ztop - 0.25 * (ztop - zbe) * 0.55 ** 2 * 0 - cr * 0.3), (0.0, ztop)]
    return _fillet(pts, S["radii"], _SEGS)


def _lower_stations(S):
    L, rcf, rcr = S["L"], S["rc_f"], S["rc_r"]
    nc = 7
    st = []
    for k in range(nc + 1):                         # front corner: theta 90 -> 0
        th = math.pi / 2 * (1 - k / nc)
        xf = rcf * (1 - math.sin(th))
        st.append((xf, S["hw"] * S["hwf_c"](rcf) - rcf * (1 - math.cos(th))))
    x0, x1 = rcf, L - rcr
    keys = []
    g = S.get("gh")
    if g:
        keys += [g["cowl"], g["tail"]]
    n_mid = int(math.ceil((x1 - x0) / 0.105))
    mids = [x0 + (x1 - x0) * i / n_mid for i in range(1, n_mid)]
    mids = [m for m in mids if all(abs(m - kk) > 0.03 for kk in keys)] + [kk for kk in keys if x0 < kk < x1]
    for xf in sorted(mids):
        st.append((xf, S["hw"] * S["hwf_c"](xf)))
    for k in range(nc + 1):                         # rear corner: theta 0 -> 90
        th = math.pi / 2 * k / nc
        xf = L - rcr * (1 - math.cos(th)) if False else (L - rcr) + rcr * math.sin(th)
        st.append((xf, S["hw"] * S["hwf_c"](L - rcr) - rcr * (1 - math.cos(th))))
    return st


def _lower_body_mesh(S):
    L = S["L"]
    st = _lower_stations(S)
    g = S.get("gh")
    rings, ring_xf = [], []
    verts = []
    half_par = None
    for (xf, hw) in st:
        pts, par = _half_section(S, xf, hw)
        half_par = par
        n = len(pts)
        x = _X(S, xf)
        ring = []
        for j in range(n):
            ring.append(len(verts)); verts.append([x, pts[j][0], pts[j][1]])
        for j in range(n - 2, 0, -1):
            ring.append(len(verts)); verts.append([x, -pts[j][0], pts[j][1]])
        rings.append(ring); ring_xf.append(xf)
    n = len(half_par)
    rl = 2 * n - 2

    def half_edge(j):
        return j if j < n - 1 else 2 * n - 3 - j

    zone = [int(math.floor((half_par[e] + half_par[e + 1]) / 2)) for e in range(n - 1)]
    faces, fmat = [], []
    clad = S.get("cladding") or S.get("van")
    for s in range(len(rings) - 1):
        A, B = rings[s], rings[s + 1]
        xfm = 0.5 * (ring_xf[s] + ring_xf[s + 1])
        for j in range(rl):
            jn = (j + 1) % rl
            faces.append((A[j], B[j], B[jn], A[jn]))
            zn = zone[half_edge(j)]
            m = "paint"
            if zn <= 1:
                m = "under"
            elif zn == 2 and clad:
                m = "trim"
            elif zn >= 6 and g and g["cowl"] + 0.02 < xfm < g["tail"] - 0.02:
                m = "interior"
            fmat.append(SI[m])

    # radial end caps (front = ring 0, rear = last ring)
    def cap(ring, end):
        pts = [Vector(verts[i]) for i in ring]
        zc = sum(p.z for p in pts) / len(pts)
        x_end = pts[0].x
        bul = S["bulge_f"] if end > 0 else S["bulge_r"]
        prev = ring
        for s_ in (0.72, 0.42):
            cur = []
            for p in pts:
                cur.append(len(verts))
                verts.append([x_end + end * bul * (1 - s_ * s_), p.y * s_, zc + (p.z - zc) * s_])
            for j in range(rl):
                jn = (j + 1) % rl
                faces.append((prev[j], prev[jn], cur[jn], cur[j])); fmat.append(SI["paint"])
            prev = cur
        c = len(verts); verts.append([x_end + end * bul, 0.0, zc])
        for j in range(rl):
            faces.append((prev[j], prev[(j + 1) % rl], c)); fmat.append(SI["paint"])

    cap(rings[0], +1)
    cap(rings[-1], -1)
    # rake shear near the ends + Lbumper shift
    for v in verts:
        xf = L / 2 - v[0]
        ff = _smooth01(1 - xf / 0.6)
        fr = _smooth01(1 - (L - xf) / 0.6)
        if ff > 0:
            v[0] += S["rake_f_c"](v[2]) * ff
        if fr > 0:
            v[0] -= S["rake_r_c"](v[2]) * fr
    bm = bmesh.new()
    bv = [bm.verts.new(v) for v in verts]
    for f, m in zip(faces, fmat):
        try:
            ff = bm.faces.new([bv[i] for i in f])
            ff.material_index = m
            ff.smooth = True
        except ValueError:
            pass
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-5)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new("_car_body_tmp")
    bm.to_mesh(me)
    bm.free()
    return me


def _arch_cutter_mesh(S):
    bm = bmesh.new()
    seg = 48
    for xa in (S["xa_f"], S["xa_r"]):
        for side in (1, -1):
            yi = side * (S["yw"] - S["tw"] / 2 - 0.045)
            yo = side * (S["hw"] + 0.4)
            zc = S["R"] + 0.012
            r = S["ra"]
            ring_i, ring_o = [], []
            for k in range(seg):
                a = 2 * math.pi * k / seg
                ring_i.append(bm.verts.new((xa + r * math.cos(a), yi, zc + r * math.sin(a))))
                ring_o.append(bm.verts.new((xa + r * math.cos(a), yo, zc + r * math.sin(a))))
            for k in range(seg):
                kn = (k + 1) % seg
                bm.faces.new((ring_i[k], ring_i[kn], ring_o[kn], ring_o[k]))
            bm.faces.new(ring_i[::-1])
            bm.faces.new(ring_o)
    for f in bm.faces:
        f.material_index = SI["well"]
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new("_car_cut_tmp")
    bm.to_mesh(me)
    bm.free()
    return me


def _boolean_arches(S, body_me):
    cut_me = _arch_cutter_mesh(S)
    sc = bpy.context.scene
    ob = bpy.data.objects.new("_car_tmp_body", body_me)
    cu = bpy.data.objects.new("_car_tmp_cut", cut_me)
    sc.collection.objects.link(ob)
    sc.collection.objects.link(cu)
    mod = ob.modifiers.new("arch", "BOOLEAN")
    mod.operation = "DIFFERENCE"
    mod.object = cu
    res = None
    for solver in ("MANIFOLD", "EXACT", "FAST"):
        try:
            mod.solver = solver
        except Exception:
            continue
        dg = bpy.context.evaluated_depsgraph_get()
        dg.update()
        r = bpy.data.meshes.new_from_object(ob.evaluated_get(dg))
        if len(r.polygons) > 0.8 * len(body_me.polygons) and len(r.polygons) != len(body_me.polygons):
            res = r
            break
        bpy.data.meshes.remove(r)
    if res is None:
        res = body_me.copy()
    bpy.data.objects.remove(ob)
    bpy.data.objects.remove(cu)
    bpy.data.meshes.remove(cut_me)
    bpy.data.meshes.remove(body_me)
    return res


# ======================================================================================
# geometry accumulation helpers
# ======================================================================================
class _Acc:
    """Adds geometry into a bmesh with material indices and optional UVs."""

    def __init__(self, bm):
        self.bm = bm
        self.uv = bm.loops.layers.uv.verify()

    def face(self, pts, mat, uvs=None, smooth=True):
        vs = [self.bm.verts.new(p) for p in pts]
        try:
            f = self.bm.faces.new(vs)
        except ValueError:
            for v in vs:
                self.bm.verts.remove(v)
            return None
        f.material_index = SI.get(mat, 0) if isinstance(mat, str) else mat
        f.smooth = smooth
        if uvs:
            for lp, uv in zip(f.loops, uvs):
                lp[self.uv].uv = uv
        return f

    def grid(self, P, mat, uvfn=None, smooth=True, closed_u=False):
        """P[i][j] grid of 3D points (i along u, j along v) -> quads with shared verts."""
        nu, nv = len(P), len(P[0])
        V = [[self.bm.verts.new(P[i][j]) for j in range(nv)] for i in range(nu)]
        out = []
        iu = nu if closed_u else nu - 1
        for i in range(iu):
            i2 = (i + 1) % nu
            for j in range(nv - 1):
                try:
                    f = self.bm.faces.new((V[i][j], V[i2][j], V[i2][j + 1], V[i][j + 1]))
                except ValueError:
                    continue
                f.material_index = SI.get(mat, 0) if isinstance(mat, str) else mat
                f.smooth = smooth
                if uvfn:
                    for lp, (a, b) in zip(f.loops, ((i, j), (i2, j), (i2, j + 1), (i, j + 1))):
                        lp[self.uv].uv = uvfn(a, b)
                out.append(f)
        return out

    def box(self, c, ax, ay, az, sx, sy, sz, mat, bevel=0.0, smooth=False):
        """Oriented box: centre c, unit axes ax/ay/az, full sizes sx/sy/sz."""
        c = Vector(c); ax, ay, az = Vector(ax), Vector(ay), Vector(az)
        res = bmesh.ops.create_cube(self.bm, size=1.0)
        vs = res["verts"]
        for v in vs:
            p = v.co.copy()
            v.co = c + ax * (p.x * sx) + ay * (p.y * sy) + az * (p.z * sz)
        fs = list({f for v in vs for f in v.link_faces})
        for f in fs:
            f.material_index = SI.get(mat, 0) if isinstance(mat, str) else mat
            f.smooth = smooth
        if bevel > 0:
            es = list({e for v in vs for e in v.link_edges})
            r = bmesh.ops.bevel(self.bm, geom=vs + es, offset=bevel, segments=2, affect="EDGES", profile=0.5)
            for f in r.get("faces", []):
                f.material_index = SI.get(mat, 0) if isinstance(mat, str) else mat
                f.smooth = True
        return vs


# ======================================================================================
# greenhouse
# ======================================================================================
def _greenhouse(S, acc):
    g = S["gh"]
    if not g:
        return
    keys = [g["cowl"], g["ws_top"], g["roof_rear"], g["tail"], g["bpil"][0], g["bpil"][1], g["dlo_end"]]
    for a, b in g["windows"]:
        keys += [a, b]
    keys = sorted(set(round(k, 4) for k in keys if g["cowl"] <= k <= g["tail"]))
    xs = [keys[0]]
    for a, b in zip(keys[:-1], keys[1:]):
        n = max(1, int(math.ceil((b - a) / 0.09)))
        xs += [a + (b - a) * i / n for i in range(1, n + 1)]
    cr = S["crown"]
    sections = []
    for xf in xs:
        hw = S["hw"] * S["hwf_c"](xf)
        tum = S["tumble_c"](xf)
        yb = hw - tum - 0.028
        zb = S["belt_c"](xf) - 0.022
        ends = abs(xf - g["cowl"]) < 1e-4 or abs(xf - g["tail"]) < 1e-4
        zr = g["rail_c"](xf)
        zt = g["top_c"](xf)
        if ends:
            zr = zb + 0.012
            zt = min(zt, S["deck_c"](xf) + cr - 0.012)
        zr = max(zr, zb + 0.012)
        yr = yb - g["tgh_c"](xf)
        h = zr - zb
        f1 = min(0.3, 0.045 / h) if h > 0.05 else 0.25
        f3 = 1 - (min(0.3, 0.035 / h) if h > 0.05 else 0.25)
        side = []
        for fr in (0.0, f1, 0.5, f3, 1.0):
            side.append((yb + (yr - yb) * fr ** 1.15, zb + fr * h))
        zedge = min(zr + 0.028, zt - 0.003)
        zedge = max(zedge, zr + 0.002)
        ye = yr - 0.03

        def roofz(y):
            t = min(1.0, max(0.0, y / ye)) if ye > 1e-3 else 1.0
            return zt - (zt - zedge) * t * t

        pw = 0.07
        top = [(yr - 0.012, zr + 0.6 * (zedge - zr)), (ye - pw, roofz(ye - pw)), (0.58 * (ye - pw), roofz(0.58 * (ye - pw))),
               (0.27 * (ye - pw), roofz(0.27 * (ye - pw))), (0.0, zt)]
        half = side + top
        sections.append((xf, half))
    nh = len(sections[0][1])
    # vertex grid: ring around (+y side bottom -> centre -> -y side bottom), open at the bottom
    P = []
    for xf, half in sections:
        x = _X(S, xf)
        ring = [(x, y, z) for (y, z) in half] + [(x, -y, z) for (y, z) in reversed(half[:-1])]
        P.append(ring)
    nr = len(P[0])
    bm = acc.bm
    V = [[bm.verts.new(p) for p in ring] for ring in P]

    def seg_of(j):            # ring edge j -> half segment index
        return j if j < nh - 1 else (nr - 2 - j)

    def in_win(xm):
        return any(a + 1e-4 < xm < b - 1e-4 for a, b in g["windows"])

    for s in range(len(P) - 1):
        xm = 0.5 * (sections[s][0] + sections[s + 1][0])
        for j in range(nr - 1):
            sg = seg_of(j)
            if sg == 0:
                m = g["belt_mat"] if in_win(xm) else "paint"
            elif sg in (1, 2):
                if in_win(xm):
                    m = "glass"
                elif g["bpil"][0] - 1e-4 < xm < g["bpil"][1] + 1e-4:
                    m = g["bpil_mat"]
                else:
                    m = "paint"
            elif sg == 3:
                m = g["frame"] if in_win(xm) else ("paint" if not (g["bpil"][0] < xm < g["bpil"][1]) else g["bpil_mat"])
            elif sg in (4, 5):
                m = "paint"
            else:
                if xm < g["ws_top"]:
                    m = "glass"
                elif xm < g["roof_rear"]:
                    m = "glass" if g["roof_glass"] else "paint"
                else:
                    m = "glass"
            a, b, c, d = V[s][j], V[s][j + 1], V[s + 1][j + 1], V[s + 1][j]
            try:
                f = bm.faces.new((a, d, c, b))
            except ValueError:
                continue
            f.material_index = SI[m]
            f.smooth = True


# ======================================================================================
# projection of details onto the body (BVH ray casting)
# ======================================================================================
class _Proj:
    def __init__(self, S, bvh):
        self.S, self.bvh = S, bvh
        L, hw = S["L"], S["hw"]
        self.cf = (L / 2 - S["rc_f"], hw * S["hwf_c"](S["rc_f"]) - S["rc_f"])
        self.cr = (-L / 2 + S["rc_r"], hw * S["hwf_c"](L - S["rc_r"]) - S["rc_r"])

    def ray(self, kind, a, b, side=1):
        S = self.S
        far = 6.0
        if kind == "front":
            return Vector((far, a, b)), Vector((-1, 0, 0))
        if kind == "rear":
            return Vector((-far, a, b)), Vector((1, 0, 0))
        if kind == "side":           # a = xf, b = z
            return Vector((_X(S, a), side * far, b)), Vector((0, -side, 0))
        if kind == "top":            # a = xf, b = y
            return Vector((_X(S, a), b, far)), Vector((0, 0, -1))
        if kind in ("cf", "cr"):     # a = theta (deg), b = z
            cx, cy = self.cf if kind == "cf" else self.cr
            e = 1 if kind == "cf" else -1
            th = math.radians(a)
            d = Vector((e * math.cos(th), side * math.sin(th), 0))
            o = Vector((e * abs(cx), side * cy, b)) + d * far
            return o, -d
        raise ValueError(kind)

    def hit(self, kind, a, b, side=1):
        o, d = self.ray(kind, a, b, side)
        loc, nor, idx, dist = self.bvh.ray_cast(o, d, 20.0)
        if loc is None:
            return None, None
        if nor.dot(d) > 0:
            nor = -nor
        return loc, nor


def _patch(acc, pj, kind, quad, mat, res=(6, 2), off=0.003, side=1, uv=False):
    (a0, b0), (a1, b1), (a2, b2), (a3, b3) = quad
    nu, nv = res
    P = []
    for i in range(nu + 1):
        u = i / nu
        row = []
        for j in range(nv + 1):
            v = j / nv
            a = (1 - u) * (1 - v) * a0 + u * (1 - v) * a1 + u * v * a2 + (1 - u) * v * a3
            b = (1 - u) * (1 - v) * b0 + u * (1 - v) * b1 + u * v * b2 + (1 - u) * v * b3
            loc, nor = pj.hit(kind, a, b, side)
            if loc is None:
                return None
            row.append(loc + nor * off)
        P.append(row)
    if side < 0 and kind in ("side", "cf", "cr"):
        P = P[::-1]
    return acc.grid(P, mat, uvfn=(lambda i, j: (i / nu, j / nv)) if uv else None)


def _strip(acc, pj, kind, pts, w, mat, off=0.0015, side=1, step=0.08):
    """Thin projected ribbon along a polyline given in projection coordinates."""
    dense = []
    for (a0, b0), (a1, b1) in zip(pts[:-1], pts[1:]):
        n = max(1, int(math.hypot(a1 - a0, b1 - b0) / step))
        for k in range(n):
            t = k / n
            dense.append((a0 + (a1 - a0) * t, b0 + (b1 - b0) * t))
    dense.append(pts[-1])
    P = []
    for k, (a, b) in enumerate(dense):
        k0, k1 = max(0, k - 1), min(len(dense) - 1, k + 1)
        da, db = dense[k1][0] - dense[k0][0], dense[k1][1] - dense[k0][1]
        ln = math.hypot(da, db) or 1.0
        na, nb = -db / ln * w / 2, da / ln * w / 2
        row = []
        for s in (-1, 1):
            loc, nor = pj.hit(kind, a + s * na, b + s * nb, side)
            if loc is None:
                return None
            row.append(loc + nor * off)
        P.append(row)
    if side < 0:
        P = [r[::-1] for r in P]
    return acc.grid(P, mat)


def _plate(acc, pj, end, zc, yc=0.0, w=0.52, h=0.112):
    kind = "front" if end > 0 else "rear"
    xs = []
    for dy in (-w / 2, 0, w / 2):
        for dz in (-h / 2, h / 2):
            loc, nor = pj.hit(kind, yc + dy, zc + dz)
            if loc is None:
                return
            xs.append(loc.x)
    x = (max(xs) + 0.012) if end > 0 else (min(xs) - 0.012)
    y0, y1 = yc - w / 2, yc + w / 2
    z0, z1 = zc - h / 2, zc + h / 2
    m = 0.012
    xb = x - end * 0.004
    if end > 0:
        acc.face([(xb, y1 + m, z0 - m), (xb, y0 - m, z0 - m), (xb, y0 - m, z1 + m), (xb, y1 + m, z1 + m)], "trim", smooth=False)
        acc.face([(x, y1, z0), (x, y0, z0), (x, y0, z1), (x, y1, z1)], "plate",
                 uvs=[(0, 0), (1, 0), (1, 1), (0, 1)], smooth=False)
    else:
        acc.face([(xb, y0 - m, z0 - m), (xb, y1 + m, z0 - m), (xb, y1 + m, z1 + m), (xb, y0 - m, z1 + m)], "trim", smooth=False)
        acc.face([(x, y0, z0), (x, y1, z0), (x, y1, z1), (x, y0, z1)], "plate",
                 uvs=[(0, 0), (1, 0), (1, 1), (0, 1)], smooth=False)


def _sym(fn, *a, **k):
    for s in (1, -1):
        fn(*a, side=s, **k)


# ---------------------------------------------------------------- per-kind light / grille sets
def _lights(S, acc, pj):
    lk = S["lights"]
    P = lambda kind, quad, mat, res=(8, 2), off=0.003, mirror=True: (
        [_patch(acc, pj, kind, quad, mat, res, off, side=s) for s in ((1, -1) if mirror else (1,))])
    F = lambda quad, mat, res=(6, 2), off=0.003: _patch(acc, pj, "front", quad, mat, res, off)
    Rr = lambda quad, mat, res=(6, 2), off=0.003: _patch(acc, pj, "rear", quad, mat, res, off)
    mirq = lambda q: [(-a, b) for (a, b) in reversed(q)]
    if lk == "camry":
        P("cf", [(-24, 0.615), (74, 0.655), (66, 0.728), (-24, 0.682)], "head", (12, 3))
        P("cf", [(-22, 0.618), (60, 0.648), (60, 0.660), (-22, 0.630)], "drl", (10, 1), 0.0045)
        F([(-0.33, 0.62), (0.33, 0.62), (0.28, 0.672), (-0.28, 0.672)], "grille", (6, 2))
        F([(-0.33, 0.672), (0.33, 0.672), (0.28, 0.682), (-0.28, 0.682)], "chrome", (6, 1), 0.0035)
        F([(-0.58, 0.24), (0.58, 0.24), (0.52, 0.52), (-0.52, 0.52)], "grille", (8, 3))
        P("cf", [(8, 0.25), (52, 0.29), (48, 0.48), (2, 0.52)], "grille", (5, 3))
        F([(-0.72, 0.205), (0.72, 0.205), (0.72, 0.235), (-0.72, 0.235)], "trim", (8, 1))
        _plate(acc, pj, 1, 0.40)
        P("cr", [(-42, 0.86), (68, 0.885), (66, 0.99), (-42, 0.978)], "tail", (12, 3))
        P("cr", [(-40, 0.905), (60, 0.92), (60, 0.935), (-40, 0.92)], "drl", (10, 1), 0.0045)
        Rr([(-0.40, 0.935), (0.40, 0.935), (0.40, 0.95), (-0.40, 0.95)], "chrome", (8, 1))
        _plate(acc, pj, -1, 0.80)
        Rr([(-0.78, 0.33), (0.78, 0.33), (0.72, 0.42), (-0.72, 0.42)], "trim", (8, 1))
        P("cr", [(0, 0.44), (40, 0.45), (40, 0.475), (0, 0.465)], "tail", (4, 1))
        for s in (1, -1):
            Rr([(s * 0.43, 0.345), (s * 0.66, 0.345), (s * 0.66, 0.39), (s * 0.43, 0.39)] if s > 0 else
               [(-0.66, 0.345), (-0.43, 0.345), (-0.43, 0.39), (-0.66, 0.39)], "chrome", (3, 1), 0.004)
    elif lk == "ev":
        P("cf", [(-18, 0.585), (78, 0.62), (72, 0.665), (-18, 0.625)], "head", (12, 2))
        P("cf", [(-16, 0.63), (70, 0.655), (70, 0.663), (-16, 0.638)], "drl", (10, 1), 0.0045)
        F([(-0.42, 0.25), (0.42, 0.25), (0.38, 0.33), (-0.38, 0.33)], "grille", (6, 1))
        P("cf", [(10, 0.25), (45, 0.27), (40, 0.40), (5, 0.42)], "gloss", (4, 2))
        _plate(acc, pj, 1, 0.42)
        Rr([(-0.62, 0.95), (0.62, 0.95), (0.62, 0.965), (-0.62, 0.965)], "tail", (12, 1), 0.004)
        P("cr", [(-36, 0.925), (66, 0.94), (64, 1.00), (-36, 0.99)], "tail", (12, 2))
        P("cr", [(-34, 0.955), (60, 0.965), (60, 0.975), (-34, 0.966)], "drl", (10, 1), 0.0045)
        _plate(acc, pj, -1, 0.60)
        Rr([(-0.80, 0.36), (0.80, 0.36), (0.74, 0.47), (-0.74, 0.47)], "gloss", (8, 1))
    elif lk == "rav4":
        P("cf", [(-20, 0.83), (72, 0.86), (66, 0.94), (-20, 0.91)], "head", (12, 3))
        P("cf", [(-18, 0.835), (66, 0.86), (66, 0.873), (-18, 0.848)], "drl", (10, 1), 0.0045)
        F([(-0.42, 0.56), (0.42, 0.56), (0.36, 0.84), (-0.36, 0.84)], "grille", (6, 3))
        F([(-0.38, 0.84), (0.38, 0.84), (0.34, 0.93), (-0.34, 0.93)], "grille", (6, 1))
        F([(-0.78, 0.33), (0.78, 0.33), (0.74, 0.56), (-0.74, 0.56)], "trim", (8, 2), 0.0025)
        P("cf", [(10, 0.36), (55, 0.40), (50, 0.56), (5, 0.56)], "trim", (5, 2), 0.0025)
        F([(-0.40, 0.36), (0.40, 0.36), (0.40, 0.40), (-0.40, 0.40)], "chrome", (6, 1), 0.0035)
        _plate(acc, pj, 1, 0.47)
        P("cr", [(-35, 1.03), (70, 1.05), (68, 1.15), (-35, 1.12)], "tail", (12, 3))
        P("cr", [(-33, 1.07), (62, 1.085), (62, 1.098), (-33, 1.083)], "drl", (10, 1), 0.0045)
        Rr([(-0.82, 0.36), (0.82, 0.36), (0.80, 0.56), (-0.80, 0.56)], "trim", (8, 2), 0.0025)
        P("cr", [(0, 0.40), (70, 0.42), (70, 0.56), (0, 0.56)], "trim", (6, 2), 0.0025)
        _plate(acc, pj, -1, 0.82)
        Rr([(-0.36, 0.95), (0.36, 0.95), (0.36, 0.965), (-0.36, 0.965)], "chrome", (6, 1))
    elif lk == "i30":
        P("cf", [(-26, 0.60), (70, 0.64), (62, 0.71), (-26, 0.67)], "head", (12, 3))
        P("cf", [(-24, 0.605), (58, 0.635), (58, 0.648), (-24, 0.618)], "drl", (10, 1), 0.0045)
        F([(-0.46, 0.27), (0.46, 0.27), (0.38, 0.56), (-0.38, 0.56)], "grille", (7, 3))
        F([(-0.40, 0.555), (0.40, 0.555), (0.38, 0.57), (-0.38, 0.57)], "chrome", (6, 1), 0.0035)
        P("cf", [(10, 0.25), (50, 0.28), (45, 0.42), (5, 0.45)], "gloss", (4, 2))
        F([(-0.70, 0.205), (0.70, 0.205), (0.70, 0.24), (-0.70, 0.24)], "trim", (8, 1))
        _plate(acc, pj, 1, 0.41)
        P("cr", [(-30, 0.885), (72, 0.905), (70, 0.985), (-30, 0.975)], "tail", (12, 3))
        P("cr", [(-28, 0.93), (62, 0.94), (62, 0.952), (-28, 0.943)], "drl", (10, 1), 0.0045)
        _plate(acc, pj, -1, 0.72)
        Rr([(-0.75, 0.33), (0.75, 0.33), (0.70, 0.42), (-0.70, 0.42)], "trim", (8, 1))
        P("cr", [(0, 0.45), (40, 0.46), (40, 0.48), (0, 0.47)], "tail", (4, 1))
    elif lk == "van":
        P("cf", [(-30, 0.90), (55, 0.93), (50, 1.06), (-30, 1.04)], "head", (10, 3))
        P("cf", [(-28, 0.905), (50, 0.93), (50, 0.945), (-28, 0.92)], "drl", (8, 1), 0.0045)
        F([(-0.52, 0.66), (0.52, 0.66), (0.50, 0.95), (-0.50, 0.95)], "grille", (8, 3))
        F([(-0.56, 0.95), (0.56, 0.95), (0.54, 0.975), (-0.54, 0.975)], "chrome", (8, 1), 0.0035)
        F([(-0.86, 0.33), (0.86, 0.33), (0.86, 0.66), (-0.86, 0.66)], "trim", (10, 2), 0.0025)
        P("cf", [(0, 0.35), (85, 0.36), (85, 0.66), (0, 0.66)], "trim", (8, 2), 0.0025)
        _plate(acc, pj, 1, 0.47)
        P("cr", [(-5, 0.98), (60, 0.98), (60, 1.40), (-5, 1.40)], "tail", (4, 4))
        P("cr", [(-5, 1.15), (60, 1.15), (60, 1.25), (-5, 1.25)], "amber", (4, 1), 0.0045)
        Rr([(-0.98, 0.36), (0.98, 0.36), (0.98, 0.60), (-0.98, 0.60)], "trim", (10, 2), 0.0025)
        _plate(acc, pj, -1, 0.75)
        Rr([(-0.25, 2.40), (0.25, 2.40), (0.25, 2.43), (-0.25, 2.43)], "tail", (4, 1))
    elif lk == "lada":
        for s in (1, -1):
            q = [(0.43, 0.62), (0.72, 0.62), (0.72, 0.76), (0.43, 0.76)]
            if s < 0:
                q = mirq(q)
            F(q, "chrome", (3, 2), 0.003)
            qi = [(0.45, 0.635), (0.70, 0.635), (0.70, 0.745), (0.45, 0.745)]
            if s < 0:
                qi = mirq(qi)
            F(qi, "head", (3, 2), 0.004)
        F([(-0.42, 0.62), (0.42, 0.62), (0.42, 0.76), (-0.42, 0.76)], "grille", (6, 2), 0.003)
        for i in range(9):
            yy = -0.40 + i * 0.1
            F([(yy - 0.006, 0.625), (yy + 0.006, 0.625), (yy + 0.006, 0.755), (yy - 0.006, 0.755)], "chrome", (1, 1), 0.0045)
        F([(-0.42, 0.755), (0.42, 0.755), (0.42, 0.765), (-0.42, 0.765)], "chrome", (6, 1), 0.0045)
        for s in (1, -1):
            q = [(0.42, 0.78), (0.76, 0.78), (0.76, 0.93), (0.42, 0.93)]
            if s < 0:
                q = mirq(q)
            Rr(q, "tail", (4, 2), 0.003)
            qa = [(0.62, 0.785), (0.75, 0.785), (0.75, 0.925), (0.62, 0.925)]
            qw = [(0.53, 0.785), (0.61, 0.785), (0.61, 0.925), (0.53, 0.925)]
            if s < 0:
                qa, qw = mirq(qa), mirq(qw)
            Rr(qa, "amber", (2, 2), 0.0045)
            Rr(qw, "chrome", (2, 2), 0.0045)
        _plate(acc, pj, -1, 0.66)
    # side repeaters / markers are omitted (sub-pixel at architectural distances)


def _door_lines(S, acc, pj):
    g = S.get("gh")
    zb = S["bot_c"](2.0)
    z_low = zb + 0.14
    xa_fr = S["fo"] + S["ra"]
    xa_rf = S["fo"] + S["wb"] - S["ra"]
    arch_top = S["R"] + 0.012 + S["ra"]
    w = 0.006
    for side in (1, -1):
        if g:
            bl = g["belt_c"](0) if False else None
            zbe = lambda xf: S["belt_c"](xf) - 0.035
            xd0 = max(g["cowl"] - 0.04, xa_fr + 0.04)
            xbl = 0.5 * (g["bpil"][0] + g["bpil"][1])
            xr = g["dlo_end"] + 0.03
            lines = [[(xd0 + 0.06, zbe(xd0 + 0.06)), (xd0, z_low + 0.02)],
                     [(xbl, zbe(xbl)), (xbl, z_low)]]
            if xr < xa_rf - 0.05:
                lines.append([(xr, zbe(xr)), (xr, arch_top + 0.02), (xa_rf - 0.05, S["R"] + 0.15), (xa_rf - 0.05, z_low)])
            else:
                lines.append([(xr, zbe(xr)), (xr, arch_top + 0.03)])
            lines.append([(xd0, z_low), (min(xa_rf - 0.05, xr), z_low)])
            for ln in lines:
                _strip(acc, pj, "side", ln, w, "gap", side=side)
            # handles
            if not S.get("flush_handles"):
                for xh in (xbl - 0.22, g["dlo_end"] - 0.17):
                    zh = S["belt_c"](xh) - 0.10
                    loc, nor = pj.hit("side", xh, zh, side)
                    if loc is not None:
                        tng = Vector((-1, 0, 0))
                        acc.box(loc + nor * 0.012, tng, nor, Vector((0, 0, 1)), 0.17, 0.022, 0.028,
                                "chrome" if S["kind"] in ("lada", "sedan") else "paint", bevel=0.006)
            else:
                for xh in (xbl - 0.22, g["dlo_end"] - 0.17):
                    zh = S["belt_c"](xh) - 0.10
                    _patch(acc, pj, "side", [(xh - 0.085, zh - 0.012), (xh + 0.085, zh - 0.012), (xh + 0.085, zh + 0.012),
                                             (xh - 0.085, zh + 0.012)], "gloss", (2, 1), 0.002, side=side)
        else:  # van: cab door, sliding door (right side), rear doors
            L = S["L"]
            xc0, xc1 = 1.05, 2.05
            lines = [[(xc0, 1.30), (xc0, z_low + 0.02)], [(xc1, 2.28), (xc1, z_low)], [(xc0, z_low), (xc1, z_low)],
                     [(xc0 + 0.08, 2.0), (xc1 - 0.02, 2.25)]]
            if side < 0:
                lines += [[(2.12, 2.28), (2.12, z_low)], [(3.40, 2.28), (3.40, z_low)], [(2.12, 2.28), (3.40, 2.28)],
                          [(2.12, z_low), (3.40, z_low)]]
            for ln in lines:
                _strip(acc, pj, "side", ln, w, "gap", side=side)
            # side protection strip
            _patch(acc, pj, "side", [(0.55, 0.47), (L - 0.30, 0.47), (L - 0.30, 0.58), (0.55, 0.58)], "trim", (14, 1),
                   0.004, side=side)
            for xh in (xc1 - 0.18,) + ((3.25,) if side < 0 else ()):
                loc, nor = pj.hit("side", xh, 1.05, side)
                if loc is not None:
                    acc.box(loc + nor * 0.015, Vector((-1, 0, 0)), nor, Vector((0, 0, 1)), 0.20, 0.03, 0.04, "trim", bevel=0.006)


def _cowl_and_shuts(S, acc, pj):
    g = S.get("gh")
    if not g:
        return
    c = g["cowl"]
    yb = S["hw"] * S["hwf_c"](c) - S["tumble_c"](c) - 0.04
    _patch(acc, pj, "top", [(c - 0.09, -yb), (c - 0.09, yb), (c + 0.005, yb), (c + 0.005, -yb)], "trim", (1, 8), 0.004)
    for side in (1, -1):
        yh = lambda xf: side * (S["hw"] * S["hwf_c"](xf) - S["tumble_c"](xf) - 0.035)
        _strip(acc, pj, "top", [(0.14, yh(0.14)), (0.8, yh(0.8)), (c - 0.09, yh(c - 0.09))], 0.005, "gap")
        if S["kind"] in ("sedan", "lada"):
            t0 = g["tail"] + 0.05
            _strip(acc, pj, "top", [(t0, yh(t0)), (S["L"] - 0.12, yh(S["L"] - 0.12))], 0.005, "gap")
    if S["kind"] in ("sedan", "lada"):
        t0 = g["tail"] + 0.05
        yb2 = S["hw"] - S["tumble_c"](t0) - 0.035
        _strip(acc, pj, "top", [(t0, -yb2), (t0, yb2)], 0.005, "gap")


def _van_windows(S, acc, pj):
    # windscreen (front projection), black surround first
    acc_q = lambda kind, q, m, res, off, side=1: _patch(acc, pj, kind, q, m, res, off, side=side)
    acc_q("front", [(-0.86, 1.26), (0.86, 1.26), (0.80, 2.07), (-0.80, 2.07)], "trim", (8, 6), 0.003)
    acc_q("front", [(-0.82, 1.29), (0.82, 1.29), (0.76, 2.03), (-0.76, 2.03)], "glass_opaque", (8, 6), 0.005)
    for s in (1, -1):
        acc_q("side", [(1.12, 1.27), (1.98, 1.27), (1.98, 2.05), (1.30, 2.05)], "trim", (5, 4), 0.003, side=s)
        acc_q("side", [(1.15, 1.30), (1.95, 1.30), (1.95, 2.02), (1.33, 2.02)], "glass_opaque", (5, 4), 0.005, side=s)
    for s in (1, -1):
        q = [(0.06, 1.40), (0.82, 1.40), (0.82, 2.05), (0.06, 2.05)]
        if s < 0:
            q = [(-0.82, 1.40), (-0.06, 1.40), (-0.06, 2.05), (-0.82, 2.05)]
        acc_q("rear", q, "glass_opaque", (3, 3), 0.004)
    _strip(acc, pj, "rear", [(0.0, 2.33), (0.0, 0.62)], 0.008, "gap")


def _cladding(S, acc, pj):
    """Black wheel-arch mouldings + rocker cladding (SUV)."""
    ra = S["ra"]
    zc = S["R"] + 0.012
    for xa in (S["xa_f"], S["xa_r"]):
        xf_c = S["L"] / 2 - xa
        for side in (1, -1):
            P = []
            nseg = 16
            for k in range(nseg + 1):
                a = math.radians(-12 + (180 + 24) * k / nseg)
                row = []
                for rr in (ra + 0.004, ra + 0.065):
                    xf = xf_c - rr * math.cos(a)
                    z = zc + rr * math.sin(a)
                    loc, nor = pj.hit("side", xf, z, side)
                    if loc is None or abs(loc.y) < S["hw"] - 0.12:
                        row = None
                        break
                    row.append(loc + nor * 0.008)
                if row is None:
                    continue
                P.append(row)
            if len(P) > 2:
                if side < 0:
                    P = [r[::-1] for r in P]
                acc.grid(P, "trim")


def _mirrors(S, acc):
    g = S.get("gh")
    dx, dy, dz = S["mirror"]
    if g:
        xf = g["cowl"] + 0.16
        zb = S["belt_c"](xf) + 0.02
    else:
        xf = 1.20
        zb = 1.45
    x = _X(S, xf)
    hw = S["hw"] * S["hwf_c"](xf)
    for side in (1, -1):
        yb = hw - S["tumble_c"](xf) * 0.6
        # arm
        acc.box((x, side * (yb + 0.05), zb + 0.02), (1, 0, 0), (0, 1, 0), (0, 0, 1), 0.06, 0.12, 0.035, "trim", bevel=0.008)
        # housing
        cy = side * (yb + 0.06 + dy / 2)
        cz = zb + 0.02 + dz / 2
        vs = acc.box((x, cy, cz), (1, 0, 0), (0, 1, 0), (0, 0, 1), dx, dy, dz,
                     "paint" if not S.get("van") else "trim", bevel=min(dx, dz) * 0.35)
        # mirror glass (rear face)
        xm = x - dx / 2 - 0.001
        ym0, ym1 = cy - side * (dy / 2 - 0.02), cy + side * (dy / 2 - 0.02)
        z0, z1 = cz - dz / 2 + 0.018, cz + dz / 2 - 0.018
        q = [(xm, ym0, z0), (xm, ym1, z0), (xm, ym1, z1), (xm, ym0, z1)]
        if side > 0:
            q = q[::-1]
        acc.face(q, "mirror", smooth=False)


def _interior(S, acc):
    g = S.get("gh")
    if not g:
        return
    up = Vector((0, 0, 1)); fw = Vector((1, 0, 0)); lt = Vector((0, 1, 0))
    belt = lambda xf: S["belt_c"](xf)
    xb = 0.5 * (g["bpil"][0] + g["bpil"][1])
    # dashboard
    xd = g["cowl"] + 0.32
    zd = belt(xd)
    hw = S["hw"] - S["tumble_c"](xd) - 0.08
    acc.box((_X(S, xd), 0, zd - 0.02), fw, lt, up, 0.45, 2 * hw, 0.14, "interior", bevel=0.03)
    # steering wheel (left-hand drive -> driver on +y)
    cx, cy, cz = _X(S, xd + 0.28), 0.37, zd + 0.06
    n, r, t = 14, 0.19, 0.022
    ax = Vector((math.cos(math.radians(62)), 0, math.sin(math.radians(62))))   # wheel normal tilted
    e1 = Vector((0, 1, 0)); e2 = ax.cross(e1).normalized()
    P = []
    for i in range(n):
        a = 2 * math.pi * i / n
        c = Vector((cx, cy, cz)) + (e1 * math.cos(a) + e2 * math.sin(a)) * r
        rd = (e1 * math.cos(a) + e2 * math.sin(a))
        P.append([c + (rd * math.cos(b) + ax * math.sin(b)) * t for b in (0, 2.1, 4.2)])
    for i in range(n):
        P[i].append(P[i][0])
    acc.grid(P, "interior", closed_u=True)
    # seats
    rows = [xb + 0.18]
    if g["dlo_end"] - xb > 0.7:
        rows.append(min(g["dlo_end"] + 0.02, g["roof_rear"] + 0.15))
    for i, xs in enumerate(rows):
        x = _X(S, xs)
        zt = g["rail_c"](xs) - 0.20
        z0 = belt(xs) - 0.25
        ys = (0.37, -0.37) if i == 0 else (0.42, 0.0, -0.42)
        for y in ys:
            sw = 0.50 if i == 0 else 0.42
            acc.box((x - 0.02, y, 0.5 * (z0 + zt)), (math.cos(0.22), 0, math.sin(0.22)), lt,
                    (-math.sin(0.22), 0, math.cos(0.22)), 0.12, sw, zt - z0, "seat", bevel=0.035)
            acc.box((x - 0.06, y, zt + 0.11), fw, lt, up, 0.10, 0.26, 0.17, "seat", bevel=0.035)


def _roof_rails(S, acc):
    g = S["gh"]
    x0, x1 = g["ws_top"] + 0.30, g["roof_rear"] - 0.05
    n = 8
    for side in (1, -1):
        P = []
        for i in range(n + 1):
            xf = x0 + (x1 - x0) * i / n
            yr = S["hw"] * S["hwf_c"](xf) - S["tumble_c"](xf) - 0.028 - g["tgh_c"](xf) - 0.10
            zt = g["top_c"](xf)
            ze = g["rail_c"](xf) + 0.028
            ye = yr + 0.07
            t = min(1, yr / ye)
            z = zt - (zt - ze) * t * t + 0.055
            x = _X(S, xf)
            y = side * yr
            P.append([(x, y - 0.018, z - 0.016), (x, y + 0.018, z - 0.016), (x, y + 0.018, z + 0.016), (x, y - 0.018, z + 0.016)])
        for r in P:
            r.append(r[0])
        acc.grid(P, "chrome" if S["kind"] == "suv" else "trim")
        for xf in (x0 + 0.04, x1 - 0.04):
            yr = S["hw"] * S["hwf_c"](xf) - S["tumble_c"](xf) - 0.028 - g["tgh_c"](xf) - 0.10
            zt = g["top_c"](xf) - 0.01
            acc.box((_X(S, xf), side * yr, zt + 0.025), (1, 0, 0), (0, 1, 0), (0, 0, 1), 0.07, 0.04, 0.06, "trim")


def _bumper_bars(S, acc, pj):
    """VAZ-2107 chrome bumpers with black rubber strip."""
    for end in (1, -1):
        zc = 0.47 if end > 0 else 0.48
        kind = "front" if end > 0 else "rear"
        loc, nor = pj.hit(kind, 0.0, zc)
        if loc is None:
            continue
        x = loc.x + end * 0.045
        P = []
        n = 10
        for i in range(n + 1):
            u = -1 + 2 * i / n
            y = u * (S["hw"] + 0.01)
            sweep = -end * 0.10 * max(0.0, abs(u) - 0.75) / 0.25
            xx = x + sweep
            P.append([(xx - end * 0.03, y, zc - 0.07), (xx, y, zc - 0.06), (xx + end * 0.012, y, zc), (xx, y, zc + 0.06),
                      (xx - end * 0.03, y, zc + 0.07)])
        if end < 0:
            P = P[::-1]
        acc.grid(P, "chrome")
        Pr = [[(r[1][0] + end * 0.014, r[1][1], zc - 0.018), (r[1][0] + end * 0.014, r[1][1], zc + 0.018)] for r in P]
        acc.grid(Pr, "trim")


# ======================================================================================
# body mesh (cached per kind)
# ======================================================================================
_MESH_CACHE = {}
_MAT_CACHE = {}
_IMG_CACHE = {}


def _alive(idb):
    try:
        idb.name
        return True
    except (ReferenceError, AttributeError):
        return False


def _fix_well_materials(S, me):
    """Assign the liner material to faces lying on the arch cutter surfaces (solver independent)."""
    zc = S["R"] + 0.012
    ra = S["ra"]
    yi = S["yw"] - S["tw"] / 2 - 0.045
    idx = SI["well"]
    for p in me.polygons:
        c = p.center
        for xa in (S["xa_f"], S["xa_r"]):
            d = math.hypot(c.x - xa, c.z - zc)
            if abs(d - ra) < 0.004 and abs(c.y) > yi - 0.002:
                p.material_index = idx
            elif abs(abs(c.y) - yi) < 0.002 and d < ra + 0.002:
                p.material_index = idx


def _build_body_mesh(kind):
    S = _prep(kind)
    me0 = _lower_body_mesh(S)
    me1 = _boolean_arches(S, me0)
    _fix_well_materials(S, me1)
    bm = bmesh.new()
    bm.from_mesh(me1)
    bpy.data.meshes.remove(me1)
    bvh = BVHTree.FromBMesh(bm)
    acc = _Acc(bm)
    pj = _Proj(S, bvh)
    _greenhouse(S, acc)
    _lights(S, acc, pj)
    _door_lines(S, acc, pj)
    _cowl_and_shuts(S, acc, pj)
    if S.get("van"):
        _van_windows(S, acc, pj)
    if S.get("cladding"):
        _cladding(S, acc, pj)
    if S.get("roof_rails"):
        _roof_rails(S, acc)
    if S.get("bumpers"):
        _bumper_bars(S, acc, pj)
    _mirrors(S, acc)
    _interior(S, acc)
    me = bpy.data.meshes.new(f"car_{kind}_body")
    bm.to_mesh(me)
    bm.free()
    for p in me.polygons:
        if p.material_index not in (SI["plate"],):
            p.use_smooth = True
    try:
        me.set_sharp_from_angle(angle=math.radians(40))
    except Exception:
        pass
    me.use_fake_user = False
    return me, S


# ======================================================================================
# wheels
# ======================================================================================
def _revolve(acc, prof, mat, seg=32, smooth=True):
    """prof: list of (y, r) revolved about the Y axis."""
    P = []
    for k in range(seg):
        a = 2 * math.pi * k / seg
        ca, sa = math.cos(a), math.sin(a)
        P.append([(r * ca, y, r * sa) for (y, r) in prof])
    return acc.grid(P, WI[mat], smooth=smooth, closed_u=True)


def _disc(acc, y, r, mat, seg=32, facing=1):
    pts = [(r * math.cos(2 * math.pi * k / seg), y, r * math.sin(2 * math.pi * k / seg)) for k in range(seg)]
    if facing < 0:
        pts = pts[::-1]
    f = acc.face(pts, WI[mat], smooth=False)
    return f


def _spoke(acc, phi, r0, r1, w0, w1, yf0, yf1, th, mat):
    n = 4
    P = []
    for i in range(n + 1):
        t = i / n
        r = r0 + (r1 - r0) * t
        w = w0 + (w1 - w0) * t
        yf = yf0 + (yf1 - yf0) * (t ** 0.7)
        cx, cz = r * math.cos(phi), r * math.sin(phi)
        tx, tz = -math.sin(phi), math.cos(phi)
        hw = w / 2
        # cross-section: back-left, front-left (chamfer), front-right, back-right
        P.append([(cx - tx * hw, yf - th, cz - tz * hw), (cx - tx * hw * 0.8, yf, cz - tz * hw * 0.8),
                  (cx + tx * hw * 0.8, yf, cz + tz * hw * 0.8), (cx + tx * hw, yf - th, cz + tz * hw)])
    for r in P:
        r.append(r[0])
    acc.grid(P, WI[mat], smooth=False)


def _build_wheel_mesh(style, R, rim, tw):
    bm = bmesh.new()
    acc = _Acc(bm)
    sw = R - rim
    h = tw / 2
    tyre = [(-h + 0.012, rim + 0.004), (-h - 0.001, rim + 0.28 * sw), (-h - 0.004, rim + 0.62 * sw),
            (-h + 0.004, R - 0.022), (-h + 0.022, R - 0.004), (-0.06, R - 0.001), (0.0, R), (0.06, R - 0.001),
            (h - 0.022, R - 0.004), (h - 0.004, R - 0.022), (h + 0.004, rim + 0.62 * sw), (h + 0.001, rim + 0.28 * sw),
            (h - 0.012, rim + 0.004)]
    _revolve(acc, tyre, "tyre", 36)
    yf = h - 0.016
    rs = rim - 0.014
    lip = [(-h + 0.015, rs - 0.004), (yf - 0.03, rs - 0.004), (yf - 0.004, rs), (yf, rim - 0.002), (yf - 0.008, rim + 0.006)]
    _revolve(acc, lip, "rim" if style not in ("steel", "lada") else "rim", 36)
    _disc(acc, -h + 0.03, rs, "hub_dark", 24, facing=1)
    # brake disc + caliper
    yb = -0.005
    _revolve(acc, [(yb, rim - 0.05), (yb, 0.07)], "brake", 24, smooth=False)
    a = math.radians(150)
    rc = rim - 0.065
    acc.box((rc * math.cos(a), yb + 0.03, rc * math.sin(a)), (math.cos(a), 0, math.sin(a)), (0, 1, 0),
            (-math.sin(a), 0, math.cos(a)), 0.05, 0.05, 0.13, WI["caliper"], bevel=0.008)
    yh = yf - 0.045
    rh = 0.072
    if style in ("multi", "twin", "five", "aero"):
        if style == "multi":
            spokes = [(2 * math.pi * k / 10, 0.030, 0.038) for k in range(10)]
        elif style == "twin":
            spokes = []
            for k in range(6):
                b = 2 * math.pi * k / 6
                spokes += [(b - 0.085, 0.020, 0.026), (b + 0.085, 0.020, 0.026)]
        elif style == "five":
            spokes = [(2 * math.pi * k / 5, 0.050, 0.085) for k in range(5)]
        else:
            spokes = [(2 * math.pi * k / 5, 0.085, 0.20) for k in range(5)]
        for (phi, w0, w1) in spokes:
            _spoke(acc, phi, rh - 0.01, rs + 0.004, w0, w1, yh + 0.004, yf - 0.002, 0.024, "rim")
        # hub
        _revolve(acc, [(yh - 0.02, rh), (yh + 0.006, rh), (yh + 0.008, rh - 0.01)], "rim", 24, smooth=True)
        _disc(acc, yh + 0.008, rh - 0.01, "rim", 24)
        _disc(acc, yh + 0.011, 0.028, "hub_dark", 16)
        if style == "aero":
            # outer aero ring
            _revolve(acc, [(yf - 0.004, rs + 0.002), (yf - 0.002, rs - 0.035)], "rim", 36, smooth=False)
    else:
        # stamped steel disc (dished) with vent holes
        dish = [(yf - 0.004, rs + 0.002), (yf - 0.012, rs - 0.03), (yh - 0.01, rim * 0.62), (yh - 0.004, rim * 0.45),
                (yh + 0.004, 0.06)]
        _revolve(acc, [(y, r) for (y, r) in dish], "rim", 36, smooth=True)
        nh = 8 if style == "steel" else 4
        for k in range(nh):
            a = 2 * math.pi * (k + 0.5) / nh
            rr = rim * 0.70
            pts = []
            for q in range(8):
                b = 2 * math.pi * q / 8
                pts.append((rr * math.cos(a) + 0.022 * math.cos(b), yf - 0.022, rr * math.sin(a) + 0.022 * math.sin(b)))
            acc.face(pts, WI["hub_dark"], smooth=False)
        if style == "steel":
            _revolve(acc, [(yh + 0.004, 0.085), (yh + 0.03, 0.075), (yh + 0.04, 0.04), (yh + 0.042, 0.001)], "hubcap", 24)
        else:
            _revolve(acc, [(yh + 0.004, 0.105), (yh + 0.025, 0.095), (yh + 0.045, 0.06), (yh + 0.05, 0.001)], "hubcap", 24)
    bmesh.ops.recalc_face_normals(bm, faces=[f for f in bm.faces if f.material_index == WI["tyre"]])
    me = bpy.data.meshes.new(f"car_wheel_{style}")
    bm.to_mesh(me)
    bm.free()
    try:
        me.set_sharp_from_angle(angle=math.radians(40))
    except Exception:
        pass
    return me


# ======================================================================================
# materials
# ======================================================================================
def _bsdf(m):
    return m.node_tree.nodes["Principled BSDF"]


def _principled(name, color, rough=0.5, metal=0.0, coat=0.0, coat_rough=0.03, emission=None, estr=0.0, spec=0.5,
                transmission=0.0, ior=1.45):
    m = bpy.data.materials.get(name)
    if m is not None and m.use_nodes:
        return m
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    b = _bsdf(m)
    b.inputs["Base Color"].default_value = (*color, 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    b.inputs["Coat Weight"].default_value = coat
    b.inputs["Coat Roughness"].default_value = coat_rough
    b.inputs["Specular IOR Level"].default_value = spec
    b.inputs["Transmission Weight"].default_value = transmission
    b.inputs["IOR"].default_value = ior
    if emission is not None:
        b.inputs["Emission Color"].default_value = (*emission, 1)
        b.inputs["Emission Strength"].default_value = estr
    m.diffuse_color = (*color, 1)
    return m


def _glass(name, tint=(0.16, 0.18, 0.18)):
    m = bpy.data.materials.get(name)
    if m is not None:
        return m
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    N, Lk = nt.nodes, nt.links
    for n in list(N):
        if n.type != "OUTPUT_MATERIAL":
            N.remove(n)
    out = [n for n in N if n.type == "OUTPUT_MATERIAL"][0]
    tr = N.new("ShaderNodeBsdfTransparent"); tr.inputs[0].default_value = (*tint, 1)
    gl = N.new("ShaderNodeBsdfGlossy"); gl.inputs["Roughness"].default_value = 0.02
    gl.inputs["Color"].default_value = (1, 1, 1, 1)
    fr = N.new("ShaderNodeFresnel"); fr.inputs["IOR"].default_value = 1.52
    # boost reflectance a little (laminated + coated glass, dark interior behind)
    mr = N.new("ShaderNodeMapRange"); mr.inputs[3].default_value = 0.06; mr.inputs[4].default_value = 1.0
    Lk.new(fr.outputs[0], mr.inputs[0])
    mx = N.new("ShaderNodeMixShader")
    Lk.new(mr.outputs[0], mx.inputs[0]); Lk.new(tr.outputs[0], mx.inputs[1]); Lk.new(gl.outputs[0], mx.inputs[2])
    Lk.new(mx.outputs[0], out.inputs["Surface"])
    m.diffuse_color = (0.05, 0.06, 0.07, 1)
    m.blend_method = "BLEND" if hasattr(m, "blend_method") else None
    return m


def _grille(name):
    m = bpy.data.materials.get(name)
    if m is not None:
        return m
    m = _principled(name, (0.02, 0.021, 0.022), rough=0.35, coat=0.3)
    nt = m.node_tree
    N, Lk = nt.nodes, nt.links
    tc = N.new("ShaderNodeTexCoord")
    br = N.new("ShaderNodeTexBrick")
    br.inputs["Scale"].default_value = 28.0
    br.inputs["Mortar Size"].default_value = 0.25
    br.inputs["Color1"].default_value = (0.0, 0.0, 0.0, 1)
    br.inputs["Color2"].default_value = (0.0, 0.0, 0.0, 1)
    br.inputs["Mortar"].default_value = (1, 1, 1, 1)
    mp = N.new("ShaderNodeMapping"); mp.inputs["Rotation"].default_value = (math.radians(90), 0, math.radians(90))
    Lk.new(tc.outputs["Object"], mp.inputs[0]); Lk.new(mp.outputs[0], br.inputs["Vector"])
    mx = N.new("ShaderNodeMix"); mx.data_type = "RGBA"
    Lk.new(br.outputs["Fac"], mx.inputs[0])
    mx.inputs[6].default_value = (0.004, 0.004, 0.005, 1); mx.inputs[7].default_value = (0.05, 0.05, 0.055, 1)
    Lk.new(mx.outputs[2], _bsdf(m).inputs["Base Color"])
    bp = N.new("ShaderNodeBump"); bp.inputs["Strength"].default_value = 0.6; bp.inputs["Distance"].default_value = 0.004
    Lk.new(br.outputs["Fac"], bp.inputs["Height"]); Lk.new(bp.outputs[0], _bsdf(m).inputs["Normal"])
    return m


def _materials(mats=None):
    M = _MAT_CACHE
    if not M or not all(_alive(v) for v in M.values()):
        M.clear()
        M["glass"] = _glass("car_glass")
        M["trim"] = _principled("car_trim_black", (0.018, 0.018, 0.019), rough=0.55)
        M["gloss"] = _principled("car_trim_gloss", (0.006, 0.006, 0.007), rough=0.08, coat=1.0)
        M["chrome"] = _principled("car_chrome", (0.85, 0.86, 0.88), rough=0.06, metal=1.0)
        M["grille"] = _grille("car_grille")
        M["interior"] = _principled("car_interior", (0.022, 0.021, 0.02), rough=0.8)
        M["seat"] = _principled("car_seat", (0.035, 0.032, 0.03), rough=0.75)
        M["well"] = _principled("car_wheel_well", (0.012, 0.012, 0.012), rough=0.9)
        M["gap"] = _principled("car_panel_gap", (0.004, 0.004, 0.004), rough=0.9)
        M["mirror"] = _principled("car_mirror_glass", (0.7, 0.72, 0.75), rough=0.03, metal=1.0)
        M["under"] = _principled("car_underbody", (0.02, 0.02, 0.02), rough=0.85)
        M["amber"] = _principled("car_amber", (0.55, 0.22, 0.01), rough=0.1, coat=1.0, emission=(1.0, 0.4, 0.02), estr=0.0)
        M["glass_opaque"] = _principled("car_glass_opaque", (0.012, 0.014, 0.016), rough=0.03, coat=1.0, spec=1.0)
        M["head_off"] = _principled("car_headlamp", (0.55, 0.57, 0.6), rough=0.12, metal=0.85, coat=1.0, coat_rough=0.0,
                                    emission=(1.0, 0.95, 0.88), estr=0.0)
        M["head_on"] = _principled("car_headlamp_on", (0.9, 0.9, 0.9), rough=0.12, metal=0.5, coat=1.0,
                                   emission=(1.0, 0.95, 0.88), estr=45.0)
        M["drl_off"] = _principled("car_drl", (0.75, 0.76, 0.78), rough=0.15, coat=1.0, emission=(1.0, 0.98, 0.95), estr=0.0)
        M["drl_on"] = _principled("car_drl_on", (0.9, 0.9, 0.9), rough=0.15, coat=1.0, emission=(1.0, 0.98, 0.95), estr=25.0)
        M["tail_off"] = _principled("car_taillamp", (0.30, 0.008, 0.01), rough=0.08, coat=1.0, emission=(1.0, 0.02, 0.01), estr=0.0)
        M["tail_on"] = _principled("car_taillamp_on", (0.45, 0.01, 0.01), rough=0.08, coat=1.0, emission=(1.0, 0.03, 0.01), estr=10.0)
        M["tyre"] = _principled("car_tyre", (0.018, 0.018, 0.018), rough=0.82, spec=0.3)
        M["rim"] = _principled("car_rim_alloy", (0.62, 0.63, 0.65), rough=0.22, metal=1.0)
        M["rim_dark"] = _principled("car_rim_dark", (0.06, 0.062, 0.066), rough=0.3, metal=0.9, coat=0.5)
        M["rim_steel"] = _principled("car_rim_steel", (0.10, 0.10, 0.105), rough=0.45, metal=0.4)
        M["brake"] = _principled("car_brake_disc", (0.28, 0.27, 0.26), rough=0.4, metal=1.0)
        M["caliper"] = _principled("car_caliper", (0.05, 0.05, 0.055), rough=0.5, metal=0.3)
        M["hub_dark"] = _principled("car_hub_dark", (0.008, 0.008, 0.008), rough=0.8)
        M["hubcap"] = _principled("car_hubcap", (0.75, 0.76, 0.78), rough=0.12, metal=1.0)
    out = dict(M)
    if mats:
        for k, v in mats.items():
            if v is not None:
                out[k] = v
    return out


def _paint(color, metallic=None, flakes=False):
    r, g, b = [max(0.0, min(1.0, c)) for c in color[:3]]
    mx, mn = max(r, g, b), min(r, g, b)
    sat = (mx - mn) / (mx + 1e-6)
    if metallic is None:
        metallic = (sat < 0.25 and 0.08 < mx < 0.7) or (sat >= 0.25 and 0.03 < mx < 0.3)
    name = "car_paint_%02x%02x%02x%s" % (int(r * 255), int(g * 255), int(b * 255), "m" if metallic else "s")
    m = bpy.data.materials.get(name)
    if m is not None:
        return m
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    N, Lk = nt.nodes, nt.links
    bs = N["Principled BSDF"]
    out = N["Material Output"]
    bs.inputs["Base Color"].default_value = (r, g, b, 1)
    bs.inputs["Metallic"].default_value = 0.8 if metallic else 0.0
    bs.inputs["Roughness"].default_value = 0.32 if metallic else 0.2
    bs.inputs["Coat Weight"].default_value = 1.0
    bs.inputs["Coat Roughness"].default_value = 0.025
    bs.inputs["Coat IOR"].default_value = 1.5
    bs.inputs["Specular IOR Level"].default_value = 0.5
    if metallic and flakes:
        vo = N.new("ShaderNodeTexVoronoi"); vo.inputs["Scale"].default_value = 2500.0
        tc = N.new("ShaderNodeTexCoord"); Lk.new(tc.outputs["Object"], vo.inputs["Vector"])
        bp = N.new("ShaderNodeBump"); bp.inputs["Strength"].default_value = 0.08
        Lk.new(vo.outputs["Distance"], bp.inputs["Height"]); Lk.new(bp.outputs[0], bs.inputs["Normal"])
    # back faces (inside of the roof seen through glass) read as headliner
    geo = N.new("ShaderNodeNewGeometry")
    dif = N.new("ShaderNodeBsdfDiffuse"); dif.inputs[0].default_value = (0.09, 0.085, 0.08, 1)
    mix = N.new("ShaderNodeMixShader")
    Lk.new(geo.outputs["Backfacing"], mix.inputs[0])
    Lk.new(bs.outputs[0], mix.inputs[1]); Lk.new(dif.outputs[0], mix.inputs[2])
    Lk.new(mix.outputs[0], out.inputs["Surface"])
    m.diffuse_color = (r, g, b, 1)
    return m


# ---------------------------------------------------------------- Armenian number plates
_FONT = {
    '0': ["01110", "10001", "10011", "10101", "11001", "10001", "01110"],
    '1': ["00100", "01100", "00100", "00100", "00100", "00100", "01110"],
    '2': ["01110", "10001", "00001", "00010", "00100", "01000", "11111"],
    '3': ["11110", "00001", "00001", "01110", "00001", "00001", "11110"],
    '4': ["00010", "00110", "01010", "10010", "11111", "00010", "00010"],
    '5': ["11111", "10000", "11110", "00001", "00001", "10001", "01110"],
    '6': ["00110", "01000", "10000", "11110", "10001", "10001", "01110"],
    '7': ["11111", "00001", "00010", "00100", "01000", "01000", "01000"],
    '8': ["01110", "10001", "10001", "01110", "10001", "10001", "01110"],
    '9': ["01110", "10001", "10001", "01111", "00001", "00010", "01100"],
    'A': ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    'B': ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
    'C': ["01110", "10001", "10000", "10000", "10000", "10001", "01110"],
    'D': ["11100", "10010", "10001", "10001", "10001", "10010", "11100"],
    'E': ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    'H': ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
    'K': ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
    'L': ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    'M': ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
    'N': ["10001", "10001", "11001", "10101", "10011", "10001", "10001"],
    'O': ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    'P': ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
    'R': ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    'S': ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
    'T': ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    'U': ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    'X': ["10001", "10001", "01010", "00100", "01010", "10001", "10001"],
    'Z': ["11111", "00001", "00010", "00100", "01000", "10000", "11111"],
}
_PL_LET = "ABCDEHKLMNOPRSTUXZ"


def plate_text(seed):
    r = random.Random(seed)
    return "%02d %s%s %03d" % (r.randint(1, 99), r.choice(_PL_LET), r.choice(_PL_LET), r.randint(1, 999))


def _plate_image(text):
    W, H = 256, 56
    key = "car_plate_img_" + text.replace(" ", "_")
    im = bpy.data.images.get(key)
    if im is not None:
        return im
    px = [0.92] * (W * H * 4)
    for i in range(W * H):
        px[i * 4 + 3] = 1.0

    def put(x, y, c):          # y from top
        if 0 <= x < W and 0 <= y < H:
            k = ((H - 1 - y) * W + x) * 4
            px[k], px[k + 1], px[k + 2] = c

    def rect(x0, y0, x1, y1, c):
        for yy in range(y0, y1):
            for xx in range(x0, x1):
                put(xx, yy, c)

    blk = (0.01, 0.01, 0.012)
    rect(0, 0, W, 2, blk); rect(0, H - 2, W, H, blk); rect(0, 0, 2, H, blk); rect(W - 2, 0, W, H, blk)
    # flag + AM
    rect(7, 8, 41, 15, (0.72, 0.02, 0.03)); rect(7, 15, 41, 22, (0.0, 0.12, 0.5)); rect(7, 22, 41, 29, (0.95, 0.45, 0.0))

    def glyph(ch, x, y, sx, sy):
        g = _FONT.get(ch)
        if not g:
            return
        for gy, row in enumerate(g):
            for gx, bit in enumerate(row):
                if bit == "1":
                    rect(x + gx * sx, y + gy * sy, x + (gx + 1) * sx, y + (gy + 1) * sy, blk)

    glyph("A", 10, 34, 2, 2); glyph("M", 24, 34, 2, 2)
    x = 52
    for ch in text:
        if ch == " ":
            x += 9
            continue
        glyph(ch, x, 7, 4, 6)
        x += 24
    im = bpy.data.images.new(key, W, H, alpha=False)
    im.pixels.foreach_set(px)
    im.update()
    try:
        im.pack()
    except Exception:
        pass
    return im


def _plate_material(text):
    name = "car_plate_" + text.replace(" ", "_")
    m = bpy.data.materials.get(name)
    if m is not None:
        return m
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    it = nt.nodes.new("ShaderNodeTexImage")
    it.image = _plate_image(text)
    it.interpolation = "Linear"
    uv = nt.nodes.new("ShaderNodeUVMap")
    nt.links.new(uv.outputs[0], it.inputs[0])
    b = _bsdf(m)
    nt.links.new(it.outputs[0], b.inputs["Base Color"])
    b.inputs["Roughness"].default_value = 0.35
    b.inputs["Coat Weight"].default_value = 0.3
    m.diffuse_color = (0.9, 0.9, 0.9, 1)
    return m


# ======================================================================================
# public API
# ======================================================================================
def _default_link(ob, cname):
    sc = bpy.context.scene
    c = bpy.data.collections.get(cname)
    if c is None:
        c = bpy.data.collections.new(cname)
        sc.collection.children.link(c)
    elif c.name not in sc.collection.children and c not in sc.collection.children_recursive:
        sc.collection.children.link(c)
    c.objects.link(ob)
    return ob


def _kind_assets(kind):
    ent = _MESH_CACHE.get(kind)
    if ent and _alive(ent[0]) and _alive(ent[1]):
        return ent
    me, S = _build_body_mesh(kind)
    wkey = (S["wheel"], S["R"], S["rim"], S["tw"])
    wm = None
    for k2, e2 in _MESH_CACHE.items():
        if e2 and e2[3] == wkey and _alive(e2[1]):
            wm = e2[1]
    if wm is None:
        wm = _build_wheel_mesh(S["wheel"], S["R"], S["rim"], S["tw"])
    ent = (me, wm, S, wkey)
    _MESH_CACHE[kind] = ent
    return ent


def face_count(kind):
    """Faces of one complete car of this kind (body + 4 wheels)."""
    me, wm, S, _ = _kind_assets(kind)
    return len(me.polygons) + 4 * len(wm.polygons)


def make_car(name, kind, color, x, y, heading, lights_on=False, link_fn=None, mats=None,
             z=0.03, steer=0.0, metallic=None, plate=None, seed=None):
    """Create a car; returns the parent Empty (see module docstring)."""
    if kind not in SPECS:
        kind = "sedan"
    link_fn = link_fn or _default_link
    me, wm, S, _ = _kind_assets(kind)
    M = _materials(mats)
    rnd = random.Random(seed if seed is not None else name)
    paint = (mats or {}).get("paint") or _paint(color, metallic)
    ptxt = plate or plate_text(rnd.random())
    slot_mat = dict(M)
    slot_mat["paint"] = paint
    slot_mat["head"] = M["head_on"] if lights_on else M["head_off"]
    slot_mat["drl"] = M["drl_on"] if lights_on else M["drl_off"]
    slot_mat["tail"] = M["tail_on"] if lights_on else M["tail_off"]
    slot_mat["plate"] = (mats or {}).get("plate") or _plate_material(ptxt)
    if len(me.materials) == 0:
        for k in SLOTS:
            me.materials.append(slot_mat.get(k))
    if len(wm.materials) == 0:
        for k in WSLOTS:
            wm.materials.append(M.get(k))

    e = bpy.data.objects.new(name, None)
    e.empty_display_type = "PLAIN_AXES"
    e.empty_display_size = 0.5
    link_fn(e, "vehicles")
    body = bpy.data.objects.new(name + "_body", me)
    link_fn(body, "vehicles")
    body.parent = e
    for i, k in enumerate(SLOTS):
        body.material_slots[i].link = "OBJECT"
        body.material_slots[i].material = slot_mat.get(k)
    rim_mat = M.get(S.get("rim_mat", "rim"), M["rim"])
    wmat = {k: M.get(k) for k in WSLOTS}
    wmat["rim"] = rim_mat
    for xa, fr in ((S["xa_f"], True), (S["xa_r"], False)):
        for side in (1, -1):
            w = bpy.data.objects.new(f"{name}_wheel_{'f' if fr else 'r'}{'l' if side > 0 else 'r'}", wm)
            link_fn(w, "vehicles")
            w.parent = e
            w.location = (xa, side * S["yw"], S["R"] - 0.008)
            rz = (0.0 if side > 0 else math.pi) + (math.radians(steer) if fr else 0.0)
            w.rotation_euler = (0.0, rnd.uniform(0, 2 * math.pi), rz)
            for i, k in enumerate(WSLOTS):
                w.material_slots[i].link = "OBJECT"
                w.material_slots[i].material = wmat[k]
    if lights_on:
        zl = S["deck_c"](0.1) - 0.08
        for side in (1, -1):
            ld = bpy.data.lights.new(f"{name}_beam", "SPOT")
            ld.energy = 140.0
            ld.color = (1.0, 0.93, 0.82)
            ld.spot_size = math.radians(75)
            ld.spot_blend = 0.6
            ld.shadow_soft_size = 0.04
            lo = bpy.data.objects.new(f"{name}_beam_{'l' if side > 0 else 'r'}", ld)
            link_fn(lo, "vehicles")
            lo.parent = e
            lo.location = (S["L"] / 2 - 0.05, side * (S["hw"] - 0.32), zl)
            lo.rotation_euler = (0.0, math.radians(90 + 8), 0.0)   # -Z axis -> +X, tilted 8 deg down
    e.location = (x, y, z)
    e.rotation_euler = (0, 0, math.radians(heading))
    return e
