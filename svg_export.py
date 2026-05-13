"""
svg_export.py — Convert any SVG to PNG/JPEG using Playwright + Pillow.
Usage:
    python svg_export.py input.svg [--out output.png] [--size 512] [--jpg]
"""
import argparse
import pathlib
from playwright.sync_api import sync_playwright
from PIL import Image
import io


def svg_to_png(svg_path: str, output: str, size: int = 512) -> None:
    svg_source = pathlib.Path(svg_path).read_text(encoding="utf-8")
    # Inline SVG so Chromium renders filters/blur correctly (img-tag blocks them)
    html = f"""<!DOCTYPE html>
<html><head><style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{size}px;height:{size}px;overflow:hidden}}
svg{{width:{size}px;height:{size}px;display:block}}
</style></head>
<body>{svg_source}</body></html>"""

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": size, "height": size})
        page.set_content(html)
        page.wait_for_timeout(800)
        png_bytes = page.screenshot(
            clip={"x": 0, "y": 0, "width": size, "height": size}
        )
        browser.close()

    out_path = pathlib.Path(output)
    if out_path.suffix.lower() in (".jpg", ".jpeg"):
        img = Image.open(io.BytesIO(png_bytes)).convert("RGB")
        img.save(str(out_path), "JPEG", quality=95)
    else:
        out_path.write_bytes(png_bytes)

    print(f"Saved {size}x{size} → {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("svg", help="Input SVG file")
    parser.add_argument("--out", default=None, help="Output file (default: same name, .png)")
    parser.add_argument("--size", type=int, default=512, help="Canvas size in px (default: 512)")
    parser.add_argument("--jpg", action="store_true", help="Save as JPEG instead of PNG")
    args = parser.parse_args()

    svg_in = pathlib.Path(args.svg)
    if args.out:
        out = args.out
    elif args.jpg:
        out = svg_in.with_suffix(".jpg")
    else:
        out = svg_in.with_suffix(".png")

    svg_to_png(str(svg_in), str(out), size=args.size)
