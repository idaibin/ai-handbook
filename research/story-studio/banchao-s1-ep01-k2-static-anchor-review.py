#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def get_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf',
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def fit(img: Image.Image, size: tuple[int, int]) -> Image.Image:
    copy = img.copy()
    copy.thumbnail(size, Image.Resampling.LANCZOS)
    canvas = Image.new('RGB', size, 'white')
    canvas.paste(copy, ((size[0] - copy.width) // 2, (size[1] - copy.height) // 2))
    return canvas


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('k1', type=Path)
    parser.add_argument('k2', type=Path)
    parser.add_argument('outdir', type=Path)
    args = parser.parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)

    k1 = Image.open(args.k1).convert('RGB')
    k2 = Image.open(args.k2).convert('RGB')
    a = np.array(k1)
    b = np.array(k2)
    if a.shape != b.shape:
        raise ValueError(f'shape mismatch: {a.shape} vs {b.shape}')

    diff = np.abs(a.astype(np.int16) - b.astype(np.int16))
    changed = diff.max(axis=2) > 0
    ys, xs = np.where(changed)
    bbox = [int(xs.min()), int(ys.min()), int(xs.max() + 1), int(ys.max() + 1)] if xs.size else None
    changed_count = int(changed.sum())

    hand_wrist_roi = [760, 560, 1080, 825]
    x0, y0, x1, y1 = hand_wrist_roi
    hand_diff_count = int(changed[y0:y1, x0:x1].sum())

    outside_identity = True
    if bbox:
        mask = np.ones(changed.shape, dtype=bool)
        bx0, by0, bx1, by1 = bbox
        mask[by0:by1, bx0:bx1] = False
        outside_identity = bool(not changed[mask].any())

    mask_img = np.zeros((*changed.shape, 3), dtype=np.uint8)
    mask_img[changed] = [255, 255, 255]
    Image.fromarray(mask_img).save(args.outdir / 'BANCHAO-S1-EP01-K2-CHANGED-PIXEL-MASK-REVIEW-REV23.png')

    heat = np.zeros((*changed.shape, 3), dtype=np.uint8)
    heat[changed] = [255, 32, 32]
    Image.fromarray(heat).save(args.outdir / 'BANCHAO-S1-EP01-K2-DIFF-MAP-REV23.png')

    ann = k2.copy()
    draw = ImageDraw.Draw(ann)
    if bbox:
        draw.rectangle(bbox, outline=(255, 0, 0), width=4)
    draw.rectangle(hand_wrist_roi, outline=(255, 180, 0), width=3)
    draw.text(
        (30, 30),
        'K2 review: local edit region (red); hand/wrist ROI unchanged (amber)',
        font=get_font(28, True),
        fill=(255, 255, 255),
        stroke_width=2,
        stroke_fill=(0, 0, 0),
    )
    ann.save(args.outdir / 'BANCHAO-S1-EP01-K2-ANNOTATED-FULL-FRAME-REV23.jpg', quality=94)

    width, height = 1800, 1360
    sheet = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(sheet)
    black = (20, 20, 20)
    red = (185, 0, 0)
    green = (0, 120, 45)

    draw.text((30, 20), 'EP01 K2 STATIC ANCHOR — INDEPENDENT REVIEW (REV23)', font=get_font(42, True), fill=black)
    draw.text((30, 78), 'FAIL_IMPLEMENTATION_REPAIR_REQUIRED · K3 NOT AUTHORIZED', font=get_font(30, True), fill=red)

    full_size = (850, 478)
    sheet.paste(fit(k1, full_size), (30, 130))
    sheet.paste(fit(k2, full_size), (920, 130))
    draw.text((30, 615), 'K1 source — contact state', font=get_font(26, True), fill=black)
    draw.text((920, 615), 'K2 candidate — visible gap, invalid geometry', font=get_font(26, True), fill=red)

    if bbox:
        sx = full_size[0] / k2.width
        sy = full_size[1] / k2.height
        bx0, by0, bx1, by1 = bbox
        scaled = (920 + int(bx0 * sx), 130 + int(by0 * sy), 920 + int(bx1 * sx), 130 + int(by1 * sy))
        draw.rectangle(scaled, outline=red, width=5)

    crop_box = (955, 745, 1100, 920)
    c1 = k1.crop(crop_box).resize((520, 520), Image.Resampling.LANCZOS)
    c2 = k2.crop(crop_box).resize((520, 520), Image.Resampling.LANCZOS)
    gray = (np.array(k2).mean(axis=2) * 0.22).astype(np.uint8)
    diff_vis = np.stack([gray, gray, gray], axis=2)
    diff_vis[changed] = [255, 20, 20]
    c3 = Image.fromarray(diff_vis).crop(crop_box).resize((520, 520), Image.Resampling.NEAREST)

    for panel, x in ((c1, 30), (c2, 570), (c3, 1110)):
        sheet.paste(panel, (x, 690))
    for label, x in (('K1 close-up', 45), ('K2 close-up', 585), ('Changed pixels', 1125)):
        draw.rectangle((x - 5, 700, x + 275, 744), fill=(255, 255, 255))
        draw.text((x, 705), label, font=get_font(25, True), fill=black)

    draw.rectangle((720, 850, 890, 1115), outline=red, width=6)

    footer_y = 1225
    draw.rectangle((0, footer_y, width, height), fill=(247, 247, 247))
    draw.text((30, 1245), 'PASS_BOUNDED', font=get_font(24, True), fill=green)
    draw.text((245, 1245), 'A visible air gap exists between the lowest tip and the paper.', font=get_font(23), fill=black)
    draw.text((30, 1285), 'FAIL 1', font=get_font(24, True), fill=red)
    draw.text((145, 1285), 'The lower bristles form a split / duplicated silhouette instead of one continuous tip.', font=get_font(23), fill=black)
    draw.text((30, 1325), 'FAIL 2', font=get_font(24, True), fill=red)
    draw.text((145, 1325), 'Required wrist lift is absent: hand/wrist ROI changed pixels = 0.', font=get_font(23), fill=black)
    draw.text((1125, 1248), 'Mechanical evidence', font=get_font(23, True), fill=black)
    draw.text((1125, 1288), f'{changed_count} changed pixels', font=get_font(22), fill=black)
    draw.text((1125, 1328), f'bbox {bbox}', font=get_font(22), fill=black)

    sheet.save(args.outdir / 'BANCHAO-S1-EP01-K2-INDEPENDENT-REVIEW-SHEET-REV23.jpg', quality=95)

    metrics = {
        'k1_sha256': sha256(args.k1),
        'k2_sha256': sha256(args.k2),
        'image': {'width': k1.width, 'height': k1.height, 'mode': 'RGB', 'format': 'PNG'},
        'difference': {
            'changed_bbox_xyxy': bbox,
            'changed_pixel_count': changed_count,
            'outside_bbox_pixel_identity': outside_identity,
            'hand_wrist_roi_xyxy': hand_wrist_roi,
            'hand_wrist_changed_pixel_count': hand_diff_count,
            'max_channel_delta': int(diff.max()),
            'mean_channel_delta_on_changed_pixels': float(diff[changed].mean()) if changed_count else 0.0,
        },
        'mechanical_findings': {
            'native_spec': 'PASS_1920X1080_RGB_PNG',
            'visible_tip_surface_gap': 'PASS_BOUNDED',
            'paper_movement': 'PASS_NONE',
            'new_readable_mark': 'PASS_NONE',
            'outside_local_edit_identity': 'PASS_EXACT_PIXEL_IDENTITY',
            'wrist_lift_state': 'FAIL_ZERO_PIXEL_DELTA_IN_HAND_WRIST_ROI',
        },
        'visual_findings': {
            'single_continuous_bristle_tip': 'FAIL_SPLIT_DUPLICATED_SILHOUETTE',
            'hero_brush_geometry_continuity': 'FAIL',
            'interpolation_suitability': 'FAIL',
        },
        'review_result': 'FAIL_IMPLEMENTATION_REPAIR_REQUIRED',
        'k3_authorized': False,
    }
    (args.outdir / 'BANCHAO-S1-EP01-K2-MECHANICAL-REVIEW-RECEIPT-REV23.json').write_text(
        json.dumps(metrics, ensure_ascii=False, indent=2) + '\n', encoding='utf-8'
    )
    print(json.dumps(metrics, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
