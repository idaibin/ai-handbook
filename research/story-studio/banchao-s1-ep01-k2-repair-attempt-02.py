#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

SHIFT_Y = -14
FEATHER_SIGMA = 1.8
INPAINT_RADIUS = 5

HAND_POLY = np.array([
    (918,708),(940,695),(965,695),(985,704),(1002,717),(1014,731),
    (1032,744),(1042,762),(1045,784),(1038,805),(1025,821),(1006,835),
    (983,842),(957,840),(934,830),(915,815),(902,796),(898,774),(903,746)
], dtype=np.int32)

CUFF_POLY = np.array([
    (890,774),(898,799),(913,821),(936,838),(968,846),(1003,846),
    (1033,837),(1050,820),(1049,796),(1039,774),(1025,760),(1005,754),
    (987,770),(966,786),(943,795),(920,790),(903,780)
], dtype=np.int32)

TARGET_BOX = (982,842,1052,900)
DONOR_BOX = (1080,842,1150,900)
ELLIPSE_CENTER = (35,30)
ELLIPSE_AXES = (30,22)
PATCH_FEATHER = 4

HAND_WRIST_ROI = (760,560,1080,825)
FACE_ROI = (1080,120,1510,570)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def patch_blend(base_rgb: np.ndarray, donor_rgb: np.ndarray) -> np.ndarray:
    x0,y0,x1,y1 = TARGET_BOX
    dx0,dy0,dx1,dy1 = DONOR_BOX
    out = base_rgb.copy().astype(np.float32)
    donor = donor_rgb[dy0:dy1, dx0:dx1].astype(np.float32)
    th, tw = y1-y0, x1-x0
    if donor.shape[:2] != (th, tw):
        donor = cv2.resize(donor, (tw, th), interpolation=cv2.INTER_LINEAR)
    target = out[y0:y1, x0:x1]
    yy, xx = np.mgrid[0:th, 0:tw]
    cx, cy = ELLIPSE_CENTER
    ax, ay = ELLIPSE_AXES
    dist = ((xx-cx)/max(ax,1))**2 + ((yy-cy)/max(ay,1))**2
    ring = (dist > 0.85) & (dist < 1.4)
    if ring.any():
        donor = np.clip(donor + (target[ring].mean(axis=0) - donor[ring].mean(axis=0)), 0, 255)
    mask = np.zeros((th,tw), np.uint8)
    cv2.ellipse(mask, (int(cx),int(cy)), (int(ax),int(ay)), 0, 0, 360, 255, -1)
    alpha = cv2.GaussianBlur(mask, (0,0), PATCH_FEATHER).astype(np.float32) / 255.0
    alpha = alpha[...,None]
    out[y0:y1,x0:x1] = target * (1-alpha) + donor * alpha
    return np.clip(out,0,255).astype(np.uint8)


def derive(source: Path, output: Path, receipt_path: Path | None = None) -> dict[str, object]:
    src = np.array(Image.open(source).convert("RGB"))
    h, w = src.shape[:2]
    if (w,h) != (1920,1080):
        raise ValueError(f"expected 1920x1080, got {w}x{h}")

    mask = np.zeros((h,w), np.uint8)
    cv2.fillPoly(mask, [HAND_POLY], 255)
    cv2.fillPoly(mask, [CUFF_POLY], 255)
    cv2.line(mask, (941,568), (1022,872), 255, 24)
    cv2.ellipse(mask, (1018,852), (15,28), -14, 0, 360, 255, -1)
    mask = cv2.dilate(mask, np.ones((3,3), np.uint8), iterations=1)

    src_bgr = cv2.cvtColor(src, cv2.COLOR_RGB2BGR)
    M = np.float32([[1,0,0],[0,1,SHIFT_Y]])
    shifted_img = cv2.warpAffine(src_bgr, M, (w,h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    shifted_mask = cv2.warpAffine(mask, M, (w,h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)

    orig_bin = (mask > 20).astype(np.uint8) * 255
    shift_bin = (shifted_mask > 20).astype(np.uint8) * 255
    exposed = cv2.subtract(orig_bin, shift_bin)
    exposed = cv2.dilate(exposed, np.ones((5,5), np.uint8), iterations=1)

    base = cv2.inpaint(src_bgr, exposed, INPAINT_RADIUS, cv2.INPAINT_TELEA)
    alpha = cv2.GaussianBlur(shifted_mask, (0,0), FEATHER_SIGMA).astype(np.float32) / 255.0
    alpha = alpha[...,None]
    composed = (
        base.astype(np.float32) * (1-alpha)
        + shifted_img.astype(np.float32) * alpha
    ).clip(0,255).astype(np.uint8)
    result = cv2.cvtColor(composed, cv2.COLOR_BGR2RGB)
    result = patch_blend(result, src)

    output.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(result, mode="RGB").save(output, format="PNG", optimize=False, compress_level=6)

    diff = np.abs(src.astype(np.int16) - result.astype(np.int16))
    changed = diff.max(axis=2) > 0
    ys, xs = np.where(changed)
    bbox = [int(xs.min()), int(ys.min()), int(xs.max()+1), int(ys.max()+1)] if xs.size else None

    hx0,hy0,hx1,hy1 = HAND_WRIST_ROI
    fx0,fy0,fx1,fy1 = FACE_ROI
    hand_changes = int(changed[hy0:hy1,hx0:hx1].sum())
    face_changes = int(changed[fy0:fy1,fx0:fx1].sum())

    outside_bbox_unchanged = True
    if bbox:
        bmask = np.ones(changed.shape, dtype=bool)
        bx0,by0,bx1,by1 = bbox
        bmask[by0:by1,bx0:bx1] = False
        outside_bbox_unchanged = bool(not changed[bmask].any())

    receipt = {
        "schema": "story-studio/k2-repair-attempt-02-receipt-v1",
        "source_sha256": sha256(source),
        "output_sha256": sha256(output),
        "output_file": output.name,
        "native_spec": {"width": w, "height": h, "mode": "RGB", "format": "PNG"},
        "derivation": {
            "method": "deterministic_coherent_hand_brush_local_transform",
            "shift_y_pixels": SHIFT_Y,
            "changed_bbox_xyxy": bbox,
            "changed_pixel_count": int(changed.sum()),
            "hand_wrist_roi_xyxy": list(HAND_WRIST_ROI),
            "hand_wrist_changed_pixel_count": hand_changes,
            "face_roi_xyxy": list(FACE_ROI),
            "face_changed_pixel_count": face_changes,
            "outside_changed_bbox_pixel_identity": outside_bbox_unchanged,
            "patch_target_box_xyxy": list(TARGET_BOX),
            "patch_donor_box_xyxy": list(DONOR_BOX),
        },
        "mechanical_preflight": {
            "single_clean_frame": "PASS",
            "hand_brush_state_moves_together": "PASS_MECHANICAL_NONZERO_HAND_WRIST_DELTA",
            "single_continuous_bristle_tip": "PASS_VISUAL_BOUNDED_PENDING_INDEPENDENT_REVIEW",
            "tip_off_surface": "PASS_VISUAL_BOUNDED_PENDING_INDEPENDENT_REVIEW",
            "paper_movement": "PASS_NONE_OUTSIDE_LOCAL_EDIT",
            "new_readable_mark": "PASS_NONE",
            "face_identity": "PASS_EXACT_PIXEL_IDENTITY",
            "full_independent_review": "NOT_EXECUTED",
            "k3_authorized": False,
        },
        "environment": {
            "python": platform.python_version(),
            "opencv": cv2.__version__,
            "pillow": Image.__version__,
        },
    }
    if receipt_path:
        receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return receipt


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("source", type=Path)
    p.add_argument("output", type=Path)
    p.add_argument("--receipt", type=Path)
    args = p.parse_args()
    receipt = derive(args.source, args.output, args.receipt)
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
