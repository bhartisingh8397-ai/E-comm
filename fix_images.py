import shutil
import os

src_dir = r"C:\Users\bharti\\.gemini\\antigravity\\brain\\0b984440-1902-4055-a7be-e2b815945298"
dst_dir = r"c:\Users\bharti\Desktop\E-comm\static\images"

mapping = {
    "logo_png_1775045255941.png": "logo.png",
    "hero_jpg_1775045280131.png": "hero.jpg",
    "watch_png_1775045302469.png": "watch.png",
    "headphones_png_1775045328052.png": "headphones.png",
    "laptop_png_1775045356794.png": "laptop.png"
}

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

for src_name, dst_name in mapping.items():
    src_path = os.path.join(src_dir, src_name)
    dst_path = os.path.join(dst_dir, dst_name)
    if os.path.exists(src_path):
        shutil.copy(src_path, dst_path)
        print(f"Copied {src_name} to {dst_name}")
    else:
        print(f"Source not found: {src_path}")
