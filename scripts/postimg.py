#!/usr/bin/env python3
"""DigitalBrain 글 이미지 생성기. 외부 사진 없이 글의 검증된 수치로 카드를 그린다.

  python3 scripts/postimg.py cover   spec.json out.png   # 1200x630 커버 카드 (OG 이미지 겸용)
  python3 scripts/postimg.py compare spec.json out.png   # 두 제품 수치 비교 막대 차트

의존: pillow (`pip install pillow`), scripts/fonts/NotoSansKR-{400,700}.ttf (SIL OFL)
"""
import json, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FONTS = Path(__file__).resolve().parent / "fonts"
BG, TILE, BORDER = (29, 30, 32), (40, 41, 45), (58, 59, 63)
FG, SEC, TER, ACCENT = (232, 232, 234), (160, 161, 165), (110, 111, 116), (47, 111, 237)
W, H = 1200, 630
SITE = "leeyunjai.github.io"

def font(weight, size):
    return ImageFont.truetype(str(FONTS / f"NotoSansKR-{weight}.ttf"), size)

def wrap(draw, text, f, max_w):
    """단어 단위로 줄바꿈하되, 한 단어가 너무 길면 글자 단위로 자른다."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=f) <= max_w:
            cur = trial; continue
        if cur: lines.append(cur); cur = ""
        if draw.textlength(word, font=f) <= max_w:
            cur = word; continue
        for ch in word:                       # 긴 단어(한글 붙어쓰기)는 글자 단위
            if draw.textlength(cur + ch, font=f) <= max_w: cur += ch
            else: lines.append(cur); cur = ch
    if cur: lines.append(cur)
    return lines

def fit(draw, text, f, max_w):
    """넘치면 말줄임표로 자른다."""
    if draw.textlength(text, font=f) <= max_w: return text
    while text and draw.textlength(text + "…", font=f) > max_w: text = text[:-1]
    return text.rstrip() + "…"

def mark(draw, x, y, size=44):
    """헤더와 같은 D 마크."""
    draw.rounded_rectangle([x, y, x + size, y + size], radius=size * 0.22, fill=ACCENT)
    f = font(700, int(size * 0.68))
    tw = draw.textlength("D", font=f)
    draw.text((x + (size - tw) / 2, y + size * 0.08), "D", font=f, fill=(255, 255, 255))

def brand(draw, x, y):
    mark(draw, x, y)
    draw.text((x + 58, y + 2), "DigitalBrain", font=font(700, 34), fill=FG)

def cover(spec, out):
    img = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(img)
    pad = 72
    brand(d, pad, 60)
    # 상단 오른쪽: 날짜
    if spec.get("date"):
        f = font(400, 24); tw = d.textlength(spec["date"], font=f)
        d.text((W - pad - tw, 70), spec["date"], font=f, fill=SEC)
    # 제목: 2줄까지, 넘치면 폰트 축소
    for size in (62, 56, 50, 44):
        f = font(700, size); lines = wrap(d, spec["title"], f, W - pad * 2)
        if len(lines) <= 2: break
    lines = lines[:2]
    # 킥커 + 제목 블록을 헤더(약 130)와 타일(440) 사이에서 세로 가운데 정렬
    block = (48 if spec.get("kicker") else 0) + len(lines) * int(size * 1.28)
    y = 140 + max(0, (410 - 140 - block) // 2)
    if spec.get("kicker"):
        d.text((pad, y), spec["kicker"], font=font(700, 26), fill=ACCENT); y += 48
    for ln in lines:
        d.text((pad, y), ln, font=f, fill=FG); y += int(size * 1.28)
    # 하단 스탯 타일 (최대 4개)
    stats = spec.get("stats", [])[:4]
    if stats:
        n = len(stats); gap = 18
        tw_ = (W - pad * 2 - gap * (n - 1)) // n
        ty = H - 72 - 118
        for i, s in enumerate(stats):
            x = pad + i * (tw_ + gap)
            d.rounded_rectangle([x, ty, x + tw_, ty + 118], radius=12, fill=TILE, outline=BORDER)
            vf = font(700, 38)
            # 값이 타일보다 길면 축소
            for vs in (38, 32, 28, 24):
                vf = font(700, vs)
                if d.textlength(s["value"], font=vf) <= tw_ - 40: break
            d.text((x + 20, ty + 18), s["value"], font=vf, fill=FG)
            lf = font(400, 20)
            d.text((x + 20, ty + 72), fit(d, s.get("label", ""), lf, tw_ - 40), font=lf, fill=SEC)
    # 하단 사이트 표기
    f = font(400, 20); tw = d.textlength(SITE, font=f)
    d.text((W - pad - tw, H - 48), SITE, font=f, fill=TER)
    img.save(out, optimize=True)

def compare(spec, out):
    rows = spec["rows"]; n = len(rows)
    h = 200 + n * 92 + 90
    img = Image.new("RGB", (W, h), BG); d = ImageDraw.Draw(img)
    pad = 72
    brand(d, pad, 52)
    d.text((pad, 128), spec["title"], font=font(700, 40), fill=FG)
    # 범례 (오른쪽 위)
    lf = font(400, 22); lx = W - pad
    for name, col in ((spec["b"], TER), (spec["a"], ACCENT)):
        tw = d.textlength(name, font=lf); lx -= tw
        d.text((lx, 62), name, font=lf, fill=SEC); lx -= 30
        d.rounded_rectangle([lx, 68, lx + 18, 86], radius=4, fill=col); lx -= 26
    y = 200
    label_w, bar_x = 300, pad + 300
    bar_w = W - pad - bar_x - 130
    for r in rows:
        d.text((pad, y + 22), r["label"], font=font(400, 24), fill=SEC)
        mx = max(float(r["a"]), float(r["b"])) or 1.0
        unit = r.get("unit", "")
        for k, (val, col, dy) in enumerate(((r["a"], ACCENT, 0), (r["b"], TER, 34))):
            w_ = int(bar_w * float(val) / mx)
            d.rounded_rectangle([bar_x, y + dy, bar_x + max(w_, 6), y + dy + 24], radius=6, fill=col)
            txt = f"{val:g}{unit}" if isinstance(val, (int, float)) else f"{val}{unit}"
            d.text((bar_x + w_ + 14, y + dy - 2), txt, font=font(700 if k == 0 else 400, 22), fill=FG if k == 0 else SEC)
        y += 92
        d.line([pad, y - 14, W - pad, y - 14], fill=BORDER, width=1)
    if spec.get("note"):
        d.text((pad, h - 60), spec["note"], font=font(400, 20), fill=TER)
    f = font(400, 20); tw = d.textlength(SITE, font=f)
    d.text((W - pad - tw, h - 60), SITE, font=f, fill=TER)
    img.save(out, optimize=True)

if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] not in ("cover", "compare"):
        sys.exit(__doc__)
    spec = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    Path(sys.argv[3]).parent.mkdir(parents=True, exist_ok=True)
    (cover if sys.argv[1] == "cover" else compare)(spec, sys.argv[3])
    print("wrote", sys.argv[3])
