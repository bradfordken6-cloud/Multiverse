# Crystallic workspace

Place MultiverseOS visual assets in `images/`. The dashboard reads **only** this
folder and exposes the discovered files through `/api/v1/crystallic/images`.

Supported image types are AVIF, GIF, JPEG, PNG, SVG, and WebP. Add new stages to
`pages/` and register them in `PAGES` in `app.py` so they remain part of the
intentional MultiverseOS navigation flow.
