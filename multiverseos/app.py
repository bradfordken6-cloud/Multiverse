"""MultiverseOS: the single entry point for the Crystallic workspace.

Only files inside ``multiverseos/crystallic`` are treated as workspace assets.
This prevents the dashboard from accidentally indexing the wider repository.
"""

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

APP_ROOT = Path(__file__).resolve().parent
CRYSTALLIC_ROOT = APP_ROOT / "crystallic"
IMAGE_ROOT = CRYSTALLIC_ROOT / "images"
PAGES = {"index": "index.html", "index2": "index2.html", "index3": "index3.html"}
IMAGE_SUFFIXES = {".avif", ".gif", ".jpeg", ".jpg", ".png", ".svg", ".webp"}

app = FastAPI(title="MultiverseOS", version="1.0.0")
app.mount("/crystallic", StaticFiles(directory=CRYSTALLIC_ROOT), name="crystallic")


def crystallic_images() -> list[dict[str, str]]:
    """Return a stable, relative manifest of images in the designated folder."""
    return [
        {"name": image.name, "url": f"/crystallic/images/{image.name}"}
        for image in sorted(IMAGE_ROOT.iterdir())
        if image.is_file() and image.suffix.lower() in IMAGE_SUFFIXES
    ]


@app.get("/health")
def health():
    return {"status": "ok", "service": "multiverseos", "image_count": len(crystallic_images())}


@app.get("/api/v1/crystallic/images")
def image_manifest():
    return {"root": "multiverseos/crystallic/images", "count": len(crystallic_images()), "images": crystallic_images()}


@app.get("/")
@app.get("/index")
def index():
    return FileResponse(APP_ROOT / "pages" / PAGES["index"])


@app.get("/{page_name}")
def page(page_name: str):
    page_file = PAGES.get(page_name)
    if page_file is None:
        raise HTTPException(status_code=404, detail="MultiverseOS page not found")
    return FileResponse(APP_ROOT / "pages" / page_file)
