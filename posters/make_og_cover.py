# -*- coding: utf-8 -*-
"""ওজি-কভার (FB/WhatsApp শেয়ার প্রিভিউ) — 1200x630"""
from PIL import Image, ImageDraw, ImageFont
import os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "assets", "og-cover.png")
F = os.path.join(HERE, "..", "assets", "fonts")
B = os.path.join(F, "HindSiliguri-Bold.ttf"); S = os.path.join(F, "HindSiliguri-SemiBold.ttf"); R = os.path.join(F, "HindSiliguri-Regular.ttf")
def font(p, n): return ImageFont.truetype(p, n)

W, H = 1200, 630
img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
for y in range(H):
    t = y / H
    d.line([(0, y), (W, y)], fill=(int(5 + 13 * t), int(63 + 81 * t * .55), int(54 + 73 * t * .6)))
ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
od.ellipse([W - 300, -170, W + 130, 260], fill=(232, 161, 28, 235))
od.ellipse([W - 210, H - 150, W + 190, H + 250], fill=(217, 242, 236, 26))
od.ellipse([-90, H - 120, 90, H + 60], fill=(232, 161, 28, 22))
img = Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB"); d = ImageDraw.Draw(img)

d.text((80, 70), "TAQWA TOUCH FOUNDATION", font=font(S, 28), fill=(190, 224, 218))
d.text((80, 122), "তাকওয়া টাচ", font=font(B, 70), fill=(255, 255, 255))
d.text((80, 208), "ফাউন্ডেশন", font=font(B, 70), fill=(255, 255, 255))
d.text((80, 316), "তাকওয়ার ছোঁয়ায়, বদলে যাক জীবন ও সমাজ", font=font(S, 34), fill=(242, 181, 68))
d.line([(80, 372), (240, 372)], fill=(232, 161, 28), width=6)
d.text((80, 396), "রাস্তাঘাট উন্নয়ন • অসহায়দের সহায়তা • পরিচ্ছন্নতা • সচেতনতা", font=font(R, 25), fill=(214, 240, 236))
d.text((80, 444), "গোলাপনগর, ভেড়ামারা, কুষ্টিয়া  •  হটলাইন : ০১৬০৭-২১৫৪২১", font=font(R, 24), fill=(214, 240, 236))
d.rounded_rectangle([80, 486, 80 + 470, 486 + 54], radius=27, fill=(255, 255, 255))
d.text((80 + 235, 513), "taqwa-touch-foundation.github.io/site", font=font(S, 22), fill=(5, 63, 54), anchor="mm")
img.save(OUT, "PNG", optimize=True)
print("✓ og-cover.png", os.path.getsize(OUT) // 1024, "KB")
