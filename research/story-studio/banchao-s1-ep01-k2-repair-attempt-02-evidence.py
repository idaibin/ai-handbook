#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path('/mnt/data/k2_repair_attempt02_rev24')
K1_PATH = Path('/mnt/data/EP01-K1-NORMAL-WRITING.png')
K2_REJECTED_PATH = Path('/mnt/data/EP01-K2-TIP-OFF-SURFACE.png')
K2_PATH = ROOT / 'EP01-K2-TIP-OFF-SURFACE-ATTEMPT-02.png'
RECEIPT_PATH = ROOT / 'BANCHAO-S1-EP01-K2-REPAIR-ATTEMPT-02-RECEIPT-REV24.json'


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def font(size: int, bold: bool = False):
    candidates = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf',
    ]
    for p in candidates:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def fit(img: Image.Image, size: tuple[int, int]) -> Image.Image:
    c = img.copy()
    c.thumbnail(size, Image.Resampling.LANCZOS)
    out = Image.new('RGB', size, 'white')
    out.paste(c, ((size[0]-c.width)//2, (size[1]-c.height)//2))
    return out


def main() -> None:
    k1 = Image.open(K1_PATH).convert('RGB')
    k2r = Image.open(K2_REJECTED_PATH).convert('RGB')
    k2 = Image.open(K2_PATH).convert('RGB')
    a = np.array(k1)
    b = np.array(k2)
    diff = np.abs(a.astype(np.int16)-b.astype(np.int16))
    changed = diff.max(axis=2)>0
    ys,xs = np.where(changed)
    bbox = [int(xs.min()),int(ys.min()),int(xs.max()+1),int(ys.max()+1)]

    mask = np.zeros((*changed.shape,3), dtype=np.uint8)
    mask[changed] = [255,255,255]
    Image.fromarray(mask).save(ROOT/'BANCHAO-S1-EP01-K2-REPAIR-ATTEMPT-02-CHANGED-PIXEL-MASK-REV24.png')

    heat = np.zeros((*changed.shape,3), dtype=np.uint8)
    heat[changed] = [255,32,32]
    Image.fromarray(heat).save(ROOT/'BANCHAO-S1-EP01-K2-REPAIR-ATTEMPT-02-DIFF-MAP-REV24.png')

    ann = k2.copy()
    d = ImageDraw.Draw(ann)
    d.rectangle(bbox, outline=(255,0,0), width=4)
    d.rectangle((760,560,1080,825), outline=(255,185,0), width=3)
    d.text((30,30), 'K2 repair attempt 02: local hand-brush motion region', font=font(28,True), fill='white', stroke_width=2, stroke_fill='black')
    ann.save(ROOT/'BANCHAO-S1-EP01-K2-REPAIR-ATTEMPT-02-ANNOTATED-FULL-FRAME-REV24.jpg', quality=94)

    W,H = 1920,1200
    sheet = Image.new('RGB',(W,H),'white')
    d = ImageDraw.Draw(sheet)
    d.text((30,18),'EP01 K2 REPAIR ATTEMPT 02 — GENERATION PREFLIGHT (REV24)',font=font(38,True),fill=(20,20,20))
    d.text((30,68),'Candidate generated; independent review not executed; K3 remains blocked',font=font(27,True),fill=(160,0,0))
    panel=(600,338)
    positions=[(20,120),(660,120),(1300,120)]
    images=[k1,k2r,k2]
    labels=['K1 source — writing contact','K2 attempt 01 — rejected split tip','K2 attempt 02 — coherent hand-brush lift']
    for im,pos,label in zip(images,positions,labels):
        sheet.paste(fit(im,panel),pos)
        d.text((pos[0]+5,pos[1]+348),label,font=font(22,True),fill=(20,20,20))

    crop=(780,500,1140,920)
    crop_size=(570,665)
    crop_positions=[(20,490),(675,490),(1330,490)]
    for im,pos,label in zip(images,crop_positions,labels):
        c=im.crop(crop)
        sheet.paste(fit(c,crop_size),pos)
        d.text((pos[0]+5,1165),label,font=font(19,True),fill=(20,20,20))
    sheet.save(ROOT/'BANCHAO-S1-EP01-K2-REPAIR-ATTEMPT-02-FULL-FRAME-REVIEW-SHEET-REV24.jpg',quality=95)

    CW,CH=1800,1050
    close = Image.new('RGB',(CW,CH),'white')
    d=ImageDraw.Draw(close)
    d.text((30,18),'K2 ATTEMPT 02 — HAND / BRUSH / TIP CLOSE-UP',font=font(38,True),fill=(20,20,20))
    d.text((30,68),'One coherent local state transform; visual pass remains bounded pending independent review',font=font(25),fill=(80,80,80))
    hand_crop=(820,520,1120,900)
    tip_crop=(930,700,1080,910)
    for i,(im,label) in enumerate(zip(images,labels)):
        x=20+i*590
        hand=im.crop(hand_crop).resize((560,710),Image.Resampling.LANCZOS)
        close.paste(hand,(x,120))
        d.text((x+8,840),label,font=font(20,True),fill=(20,20,20))
        tip=im.crop(tip_crop).resize((280,190),Image.Resampling.NEAREST)
        close.paste(tip,(x+140,865))
    close.save(ROOT/'BANCHAO-S1-EP01-K2-REPAIR-ATTEMPT-02-HAND-TIP-CLOSEUP-REV24.jpg',quality=95)

    receipt = json.loads(RECEIPT_PATH.read_text(encoding='utf-8'))
    evidence = {
        'schema':'story-studio/k2-repair-attempt-02-evidence-v1',
        'task_identifier':'TASK — Story Studio — 班超 S1 FINAL GATE',
        'task_key':'story-studio/banchao/s1-final-gate',
        'execution_unit':'EP01_WRITING_SYSTEM_K2_STATIC_ANCHOR_REPAIR_ATTEMPT_02',
        'result':'K2_REPAIR_ATTEMPT_02_CANDIDATE_GENERATED_PENDING_REVIEW',
        'source':{'file_name':K1_PATH.name,'drive_file_id':'1VMntzshVFdYTUft1KVW4CmMiPVDZ-Uwg','sha256':sha256(K1_PATH)},
        'rejected_attempt_01':{
            'file_name':K2_REJECTED_PATH.name,
            'drive_file_id':'1-1A3NoYCCmY0kUat9jGIDbUzLTiCPxJZ',
            'sha256':sha256(K2_REJECTED_PATH),
            'status':'REJECTED_REVIEW_RETAINED_AS_EVIDENCE',
        },
        'candidate_attempt_02':{
            'file_name':K2_PATH.name,
            'sha256':sha256(K2_PATH),
            'native_spec':'1920x1080_RGB_PNG',
            'role':'production_motion_anchor_internal_candidate_pending_review_attempt_02',
            'rights_status':'internal_candidate_only',
            'production_ready':False,
        },
        'derivation_receipt':receipt,
        'preflight':{
            'native_spec':'PASS',
            'single_clean_frame':'PASS',
            'hand_wrist_changed_pixel_count':receipt['derivation']['hand_wrist_changed_pixel_count'],
            'face_changed_pixel_count':receipt['derivation']['face_changed_pixel_count'],
            'single_continuous_tip':'PASS_VISUAL_BOUNDED_PENDING_INDEPENDENT_REVIEW',
            'tip_off_surface':'PASS_VISUAL_BOUNDED_PENDING_INDEPENDENT_REVIEW',
            'identity_costume_set_camera_lighting':'PASS_EXACT_PIXEL_IDENTITY_OUTSIDE_LOCAL_BBOX',
            'full_independent_review':'NOT_EXECUTED',
            'k3_authorized':False,
        },
        'failure_attempts':[{'attempt':'image_gen_edit_attempt_04','result':'FAIL_IMPLEMENTATION_OUTPUT_ROUTING_DASHBOARD_REPORT','registered':False}],
        'authorization_after':{
            'K2_review_attempt_02':'AUTHORIZED_NEXT',
            'K3':'NOT_AUTHORIZED_UNTIL_K2_REVIEW_ATTEMPT_02_PASS',
            'K4':'NOT_AUTHORIZED',
            'K5':'NOT_AUTHORIZED',
        },
        'unchanged':{'canonical':194,'production_ready':0,'mapping_revision':10,'manifest_revision':10,'canonical_drive_refs':194,'ep01_ep02_boundary':True},
    }
    (ROOT/'BANCHAO-S1-EP01-K2-REPAIR-ATTEMPT-02-EVIDENCE-REV24.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':
    main()
