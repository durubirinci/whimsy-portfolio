"""Build a single self-contained HTML file (images inlined as data URIs).

Usage: python3 src/build_single_file.py  ->  dist/portfolio.html
The normal site is index.html + assets/; this is only for sharing one file.
"""
import base64, os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(root, "src", "index.template.html")).read()
for name, ext, mime in [("downtown", "webp", "image/webp"), ("uptown", "webp", "image/webp"),
                        ("school", "webp", "image/webp"), ("room", "webp", "image/webp"),
                        ("mission", "webp", "image/webp"), ("toolbar", "webp", "image/webp"),
                        ("avatar", "png", "image/png"), ("head", "png", "image/png")]:
    data = base64.b64encode(open(os.path.join(root, "assets", f"{name}.{ext}"), "rb").read()).decode()
    src = src.replace("{{%s}}" % name, f"data:{mime};base64,{data}")
assert "{{" not in src
os.makedirs(os.path.join(root, "dist"), exist_ok=True)
open(os.path.join(root, "dist", "portfolio.html"), "w").write(src)
print("wrote dist/portfolio.html")
