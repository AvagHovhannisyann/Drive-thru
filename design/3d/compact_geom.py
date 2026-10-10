"""Geometry of CHAMPA Compact (shared by compact_scene.py and design/drawings/make_compact_plan.py; no bpy)."""
BLD = dict(x0=48.0, x1=60.0, y0=22.0, y1=29.5, ffl=0.15)           # 90 m2 pavilion
ROOF = dict(x0=46.6, x1=61.6, y0=19.6, y1=31.4, t=0.32,
            z_nw=3.85, z_ne=4.35, z_sw=4.25, z_se=5.75)               # small hypar, rises to the approach (SE)
TOWER = dict(x=62.4, y=20.6, w=1.4, d=1.4, h=7.5)
LANE_X, LANE_Y, LANE_W = 66.6, 31.75, 3.4                             # east leg x, north leg y, width
WEST_X = 43.4                                                          # exit leg
ORDER = (64.55, 22.0)                                                  # menu board (driver's left when heading north)
WINDOW_X = 54.0                                                        # pickup window on north facade
HOST = dict(canopy=(5.0, 8.0, 31.0, 21.0), canopy_z=5.6, shop=(4.0, 29.0, 19.0, 38.5))




def roof_z(x, y):
    u = (x - ROOF["x0"]) / (ROOF["x1"] - ROOF["x0"])
    v = (y - ROOF["y0"]) / (ROOF["y1"] - ROOF["y0"])
    return (ROOF["z_sw"] * (1 - u) * (1 - v) + ROOF["z_se"] * u * (1 - v) + ROOF["z_nw"] * (1 - u) * v + ROOF["z_ne"] * u * v)
