"""Download the CC0 Poly Haven HDRIs, PBR textures and models used by the Blender scenes (run once)."""
import json, urllib.request, os, sys
UA={"User-Agent":"drive-thru-study/1.0"}
def get(u): return json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=UA)).read())
def dl(url, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path): return
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA)) as r, open(path,'wb') as f: f.write(r.read())
base = "/home/user/Drive-thru/design/3d/assets"
hdris = ["kloofendal_48d_partly_cloudy_puresky","qwantani_late_afternoon_puresky","qwantani_dusk_2_puresky","kloofendal_43d_clear_puresky"]
for h in hdris:
    f = get(f"https://api.polyhaven.com/files/{h}")
    dl(f['hdri']['4k']['hdr']['url'], f"{base}/hdri/{h}_4k.hdr"); print("hdri", h)
textures = ["asphalt_02","large_sandstone_blocks_01","red_sandstone_wall","oak_wood_planks","concrete_floor_02","brick_pavement_02","aerial_grass_rock","gravel","brushed_concrete","grass_path_2","worn_asphalt"]
for t in textures:
    f = get(f"https://api.polyhaven.com/files/{t}")
    for m in ["Diffuse","nor_gl","Rough","Displacement","AO"]:
        if m in f and '2k' in f[m]:
            fmt = 'jpg' if 'jpg' in f[m]['2k'] else list(f[m]['2k'].keys())[0]
            dl(f[m]['2k'][fmt]['url'], f"{base}/tex/{t}/{t}_{m}.{fmt}")
    print("tex", t)
models = ["island_tree_01","island_tree_02","jacaranda_tree","tree_small_02","shrub_01","shrub_02","shrub_03","shrub_04","grass_medium_01","grass_medium_02","planter_box_01","outdoor_table_chair_set_01","street_lamp_01","metal_trash_can","pine_tree_01","modular_street_seating","potted_plant_02"]
for mname in models:
    try:
        f = get(f"https://api.polyhaven.com/files/{mname}")
        b = f['blend']['1k']['blend']
        dl(b['url'], f"{base}/models/{mname}/{mname}_1k.blend")
        for rel, inc in b.get('include',{}).items():
            dl(inc['url'], f"{base}/models/{mname}/{rel}")
        print("model", mname)
    except Exception as e:
        print("FAIL", mname, e)
