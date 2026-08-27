#!/usr/bin/env python3
"""Create EP01 K2 static motion-anchor candidate from K1 with a bounded deterministic local edit.

The operation changes only the visible lower bristle-tip/contact region. It removes the
contact pixels from the writing surface, reconstructs the paper locally with OpenCV
Telea inpainting, and moves the existing tapered tip upward by 10 pixels. It does not
alter the Canon source, character identity, costume, set, camera, lighting, paper plane,
or any other prop.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

POLYGON_CENTER = [(1024, 838), (1026, 845), (1028, 852), (1030, 859), (1033, 868)]
POLYGON_WIDTHS = [6, 6, 5, 3, 1]
SHIFT_PIXELS = 10
INPAINT_RADIUS = 5
FEATHER_SIGMA = 1.2


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def derive(source: Path, output: Path) -> dict[str, object]:
    src = np.array(Image.open(source).convert("RGB"))
    height, width = src.shape[:2]
    if (width, height) != (1920, 1080):
        raise ValueError(f"Expected 1920x1080 source, got {width}x{height}")

    left: list[tuple[int, int]] = []
    right: list[tuple[int, int]] = []
    for (x, y), half_width in zip(POLYGON_CENTER, POLYGON_WIDTHS, strict=True):
        left.append((x - half_width, y))
        right.append((x + half_width, y))
    polygon = np.array(left + right[::-1], dtype=np.int32)

    mask = np.zeros((height, width), dtype=np.uint8)
    cv2.fillPoly(mask, [polygon], 255)
    alpha = cv2.GaussianBlur(mask, (0, 0), FEATHER_SIGMA).astype(np.float32) / 255.0

    yy = np.indices(mask.shape)[0]
    remove = np.zeros_like(mask)
    remove[(mask > 0) & (yy >= 850)] = 255
    remove = cv2.dilate(remove, np.ones((5, 5), dtype=np.uint8), iterations=1)

    base_bgr = cv2.inpaint(cv2.cvtColor(src, cv2.COLOR_RGB2BGR), remove, INPAINT_RADIUS, cv2.INPAINT_TELEA)
    base = cv2.cvtColor(base_bgr, cv2.COLOR_BGR2RGB)

    shifted_alpha = np.zeros_like(alpha)
    shifted_pixels = np.zeros_like(src, dtype=np.float32)
    shifted_alpha[:-SHIFT_PIXELS, :] = alpha[SHIFT_PIXELS:, :]
    shifted_pixels[:-SHIFT_PIXELS, :, :] = src[SHIFT_PIXELS:, :, :]

    a = shifted_alpha[..., None]
    result = np.clip(base.astype(np.float32) * (1.0 - a) + shifted_pixels * a, 0, 255).astype(np.uint8)

    output.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(result, mode="RGB").save(output, format="PNG", optimize=False, compress_level=6)

    diff = np.abs(src.astype(np.int16) - result.astype(np.int16))
    changed_mask = diff.max(axis=2) > 0
    ys, xs = np.where(changed_mask)
    if xs.size == 0:
        bbox = None
    else:
        bbox = [int(xs.min()), int(ys.min()), int(xs.max() + 1), int(ys.max() + 1)]

    return {
        "source_sha256": sha256(source),
        "output_sha256": sha256(output),
        "width": width,
        "height": height,
        "mode": "RGB",
        "format": "PNG",
        "shift_pixels": SHIFT_PIXELS,
        "changed_pixel_count": int(changed_mask.sum()),
        "changed_bbox_xyxy": bbox,
        "max_channel_delta": int(diff.max()),
        "mean_channel_delta_changed_pixels": float(diff[changed_mask].mean()),
        "outside_bbox_unchanged": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    receipt = derive(args.source, args.output)
    if args.receipt:
        args.receipt.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
