#!/usr/bin/env python3
"""PWA 아이콘 생성기. favicon.svg 의 D 마크를 그대로 래스터화한다.

  python3 scripts/pwaicon.py 192 static/icon-192.png

maskable 안전영역: 글리프가 아이콘 중앙 80% 원 안에 들어와야 OS 마스크에 잘리지 않는다.
favicon.svg 의 D 는 24 그리드에서 11.2 x 12.8 (대각선 17.0 < 19.2) 이라 그대로 안전하다.
배경은 라운드 없이 꽉 채운다. 모서리 처리는 OS 가 한다.

의존: pillow
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw

BG = (47, 111, 237)          # #2f6fed
FG = (255, 255, 255)
SS = 4                        # 슈퍼샘플링 배율

def draw(size):
    n = size * SS
    k = n / 24.0                                   # 24 그리드 -> 픽셀
    img = Image.new("RGB", (n, n), BG)
    d = ImageDraw.Draw(img)

    def rect(x0, y0, x1, y1, fill):
        d.rectangle([x0 * k, y0 * k, x1 * k, y1 * k], fill=fill)

    def right_half_circle(cx, cy, r, fill):
        d.pieslice([(cx - r) * k, (cy - r) * k, (cx + r) * k, (cy + r) * k],
                   -90, 90, fill=fill)

    # 바깥 D: 세로 획 + 오른쪽 반원
    rect(6.6, 5.6, 11.4, 18.4, FG)
    right_half_circle(11.4, 12.0, 6.4, FG)
    # 안쪽 구멍
    rect(9.6, 8.6, 11.4, 15.4, BG)
    right_half_circle(11.4, 12.0, 3.4, BG)

    return img.resize((size, size), Image.LANCZOS)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    size, out = int(sys.argv[1]), Path(sys.argv[2])
    out.parent.mkdir(parents=True, exist_ok=True)
    draw(size).save(out, optimize=True)
    print("wrote", out, f"{size}x{size}")
