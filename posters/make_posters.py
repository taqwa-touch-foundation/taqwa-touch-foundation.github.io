# -*- coding: utf-8 -*-
"""তাকওয়া টাচ ফাউন্ডেশন — সোশ্যাল মিডিয়া পোস্টার জেনারেটর (Pillow)
চালান:  python3 make_posters.py
সব ছবি ../../assets এবং ./ ফোল্ডারে সেভ হবে।
"""
from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "..", "assets", "fonts")
R = os.path.join(FONTS, "HindSiliguri-Regular.ttf")
S = os.path.join(FONTS, "HindSiliguri-SemiBold.ttf")
B = os.path.join(FONTS, "HindSiliguri-Bold.ttf")

DARK = (5, 63, 54)
DARK2 = (11, 93, 82)
TEAL = (18, 144, 127)
AMBER = (232, 161, 28)
AMBER_L = (242, 181, 68)
CREAM = (247, 251, 250)
MINT = (217, 242, 236)
WHITE = (255, 255, 255)


def font(path, size):
    return ImageFont.truetype(path, size)


def vgrad(size, c1, c2, diagonal=True):
    w, h = size
    img = Image.new("RGB", size, c1)
    d = ImageDraw.Draw(img)
    for y in range(h):
        t = y / max(h - 1, 1)
        col = tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
        d.line([(0, y), (w, y)], fill=col)
    if diagonal:
        ov = Image.new("RGBA", size, (0, 0, 0, 0))
        od = ImageDraw.Draw(ov)
        od.polygon([(w, 0), (w, h), (w * .35, h)], fill=(255, 255, 255, 14))
        img = Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")
    return img


def circle(img, box, color, alpha=255):
    ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    d.ellipse(box, fill=color + (alpha,))
    return Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")


def rrect(img, box, color, radius, alpha=255):
    ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    d.rounded_rectangle(box, radius=radius, fill=color + (alpha,))
    return Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")


def text(d, xy, s, f, fill, anchor="la", spacing=0):
    d.multiline_text(xy, s, font=f, fill=fill, anchor=anchor, spacing=spacing, align="right" if anchor.endswith("a") and anchor.startswith("r") else "left")


def header(img, d, tag, W, pad, light=True):
    """top brand bar"""
    brand_col = WHITE if light else DARK
    tag_col = AMBER_L if light else (140, 96, 12)
    d.rounded_rectangle([pad, pad, W - pad, pad + 76], radius=38, fill=None, outline=AMBER, width=3)
    d.text((pad + 28, pad + 38), tag, font=font(S, 27), fill=tag_col, anchor="lm")
    d.text((W - pad - 28, pad + 38), "TAQWA TOUCH FOUNDATION", font=font(S, 22), fill=brand_col, anchor="rm")


def draw_check(d, cx, cy, size, color, width=6):
    """✓ gulo font-e nei — tai hate aka hocche."""
    d.line([(cx - size * .42, cy + size * .04), (cx - size * .1, cy + size * .38)], fill=color, width=width)
    d.line([(cx - size * .1, cy + size * .38), (cx + size * .46, cy - size * .34)], fill=color, width=width)


def footer_bar(img, d, W, H, pad, lines, phone=True):
    y = H - pad - (104 if phone else 40)
    d.rounded_rectangle([pad, y, W - pad, y + 104], radius=26, fill=WHITE)
    d.text((pad + 30, y + 30), lines[0], font=font(S, 27), fill=DARK, anchor="la")
    d.text((pad + 30, y + 66), lines[1], font=font(R, 23), fill=(107, 128, 133), anchor="la")
    d.rounded_rectangle([W - pad - 226, y + 27, W - pad - 26, y + 77], radius=25, fill=TEAL)
    d.text((W - pad - 126, y + 53), "যোগাযোগ করুন", font=font(S, 21), fill=WHITE, anchor="mm")


# ---------------------------------------------------------------- Poster 1: স্বেচ্ছাসেবক আহ্বান
def poster_join(path):
    W, H = 1080, 1350
    pad = 64
    img = vgrad((W, H), DARK, (10, 106, 92))
    img = circle(img, [W - 300, -220, W + 220, 300], AMBER, 235)
    img = circle(img, [-260, H - 620, 300, H - 60], MINT, 26)
    img = circle(img, [-140, H - 300, 160, H + 180], AMBER, 18)
    d = ImageDraw.Draw(img)
    header(img, d, "তাকওয়া টাচ ফাউন্ডেশন", W, pad)
    y = 300
    d.text((pad, y), "আমাদের সাথে", font=font(B, 58), fill=(190, 228, 222))
    d.text((pad, y + 78), "সহযোগী হোন", font=font(B, 92), fill=WHITE)
    d.rounded_rectangle([pad, y + 200, pad + 150, y + 212], radius=6, fill=AMBER)
    d.multiline_text((pad, y + 260),
        "আপনার সময়, শ্রম কিংবা দক্ষতা —\nযেটাই থাকে, সেটাই আমাদের শক্তি।\nএকসাথে কাজ করে বদলে দিই\nএকটি মানুষের জীবন।",
        font=font(R, 40), fill=(214, 240, 236), spacing=16)
    # checklist card
    cy = 840
    img = rrect(img, [pad, cy, W - pad, cy + 300], (255, 255, 255), 28, 240)
    d = ImageDraw.Draw(img)
    items = ["সপ্তাহে ২–৪ ঘণ্টা সময় দিলেই চলবে", "সার্টিফিকেট ও অভিজ্ঞতা পাবেন", "বেতন নেই — ভালোবাসা আছে"]
    for i, it in enumerate(items):
        yy = cy + 56 + i * 72
        d.ellipse([pad + 34, yy - 17, pad + 68, yy + 17], fill=MINT)
        draw_check(d, pad + 51, yy, 30, TEAL, 5)
        d.text((pad + 88, yy), it, font=font(S, 33), fill=DARK, anchor="lm")
    footer_bar(img, d, W, H, pad, ["আমাদের সাথে যুক্ত হোন", "taqwa-touch-foundation.github.io/site"])
    img.save(path, "PNG", optimize=True)

# ---------------------------------------------------------------- Poster 2: ডোনেশন
def poster_donate(path):
    W, H = 1080, 1350
    pad = 64
    img = vgrad((W, H), (3, 46, 40), DARK2)
    img = circle(img, [W - 320, -240, W + 240, 320], AMBER, 240)
    img = circle(img, [-360, H - 560, 260, H + 60], MINT, 20)
    d = ImageDraw.Draw(img)
    header(img, d, "তাকওয়া টাচ ফাউন্ডেশন", W, pad)

    d.text((pad, 300), "আপনার অল্প টাকায়", font=font(B, 52), fill=(190, 228, 222))
    d.text((pad, 372), "এক বেলা খাবার,", font=font(B, 84), fill=WHITE)
    d.text((pad, 466), "একজনের পড়ার সুযোগ", font=font(B, 62), fill=AMBER_L)

    cards = [("১০০৳", "একবেলা খাবার"), ("৫০০৳", "এক পরিবারের রেশন"), ("১০০০৳", "শিক্ষার্থীর শিক্ষা-উপকরণ")]
    cy = 620
    for i, (amt, lbl) in enumerate(cards):
        x0 = pad + i * 318
        img = rrect(img, [x0, cy, x0 + 296, cy + 210], (255, 255, 255), 24, 244)
        d = ImageDraw.Draw(img)
        d.text((x0 + 28, cy + 48), amt, font=font(B, 56), fill=DARK)
        d.rounded_rectangle([x0 + 28, cy + 122, x0 + 80, cy + 130], radius=4, fill=AMBER)
        d.multiline_text((x0 + 28, cy + 148), lbl, font=font(R, 26), fill=(94, 116, 120), spacing=6)

    img = rrect(img, [pad, 890, W - pad, 1120], MINT, 28)
    d = ImageDraw.Draw(img)
    d.text((pad + 36, 924), "সহজে পাঠানোর উপায়", font=font(B, 34), fill=DARK)
    d.text((pad + 36, 986), "বিকাশ / নগদ / রকেট :  ০১৬০৭-২১৫৪২১", font=font(S, 30), fill=DARK)
    d.text((pad + 36, 1036), "ঠিকানা : গোলাপনগর, ভেড়ামারা, কুষ্টিয়া", font=font(R, 27), fill=(52, 88, 84))
    footer_bar(img, d, W, H, pad, ["ডোনেট করুন — হিসাব প্রকাশ্য", "ওয়েবসাইটে প্রতি মাসের রিপোর্ট"])
    img.save(path, "PNG", optimize=True)

# ---------------------------------------------------------------- Poster 3: খাদ্য/শীতবস্ত্র ক্যাম্পেইন
def poster_campaign(path):
    W, H = 1080, 1350
    pad = 64
    img = vgrad((W, H), (253, 242, 216), (247, 251, 250))
    img = circle(img, [W - 340, -260, W + 240, 320], AMBER, 210)
    img = circle(img, [-220, H - 460, 260, H + 60], TEAL, 16)
    d = ImageDraw.Draw(img)
    header(img, d, "চলমান কর্মসূচি", W, pad, light=False)

    d.text((pad, 300), "শীতবস্ত্র ও", font=font(B, 66), fill=DARK)
    d.text((pad, 380), "খাদ্য সহায়তা", font=font(B, 92), fill=TEAL)
    d.rounded_rectangle([pad, 505, pad + 160, 519], radius=7, fill=AMBER)
    d.multiline_text((pad, 560),
        "এই শীতে ৫০০ পরিবারের পাশে\nদাঁড়াতে চাই আমরা।\nআপনার সামর্থ্য অনুযায়ী\nসহযোগিতা করুন।",
        font=font(R, 38), fill=(51, 71, 74), spacing=14)

    # progress
    py = 800
    img = rrect(img, [pad, py, W - pad, py + 200], WHITE, 26)
    d = ImageDraw.Draw(img)
    d.text((pad + 34, py + 34), "লক্ষ্য : ৫০০ কম্বল  •  সংগ্রহ : ১২০ (২৪%)", font=font(S, 30), fill=DARK)
    d.rounded_rectangle([pad + 34, py + 92, W - pad - 34, py + 122], radius=15, fill=(226, 237, 234))
    d.rounded_rectangle([pad + 34, py + 92, pad + 34 + int((W - 2 * pad - 68) * .24), py + 122], radius=15, fill=TEAL)
    d.text((pad + 34, py + 140), "এই মুহূর্তে যা প্রয়োজন: কম্বল, গরম কাপড়, চাল-ডাল-তেল", font=font(R, 26), fill=(94, 116, 120))

    footer_bar(img, d, W, H, pad, ["সহযোগিতা পাঠানোর নম্বর", "বিকাশ / নগদ : ০১৬০৭-২১৫৪২১"])
    img.save(path, "PNG", optimize=True)

# ---------------------------------------------------------------- Profile + cover
def logo_mark(size=512):
    img = vgrad((size, size), TEAL, DARK)
    d = ImageDraw.Draw(img)
    s = size
    d.ellipse([s * .12, s * .12, s * .88, s * .88], outline=WHITE + (110,), width=int(s * .022))
    d.line([s * .5, s * .2, s * .5, s * .62], fill=AMBER, width=int(s * .07))
    d.line([s * .29, s * .41, s * .71, s * .41], fill=AMBER, width=int(s * .07))
    d.arc([s * .28, s * .34, s * .72, s * .72], start=20, end=160, fill=WHITE, width=int(s * .05))
    d.text((s * .5, s * .795), "তাকওয়া টাচ", font=font(S, int(s * .072)), fill=WHITE, anchor="mm")
    return img


def profile_pic(path):
    img = logo_mark(1024).resize((512, 512), Image.LANCZOS)
    img.save(path, "PNG", optimize=True)


def cover(path):
    W, H = 1640, 624
    img = vgrad((W, H), DARK, (12, 116, 100))
    img = circle(img, [W - 380, -240, W + 240, 380], AMBER, 230)
    img = circle(img, [-300, H - 300, 320, H + 280], MINT, 18)
    d = ImageDraw.Draw(img)
    logo = logo_mark(320)
    img.paste(logo, (90, 150))
    d = ImageDraw.Draw(img)
    d.text((470, 210), "তাকওয়া টাচ ফাউন্ডেশন", font=font(B, 86), fill=WHITE, anchor="lm")
    d.text((470, 292), "তাকওয়ার ছোঁয়ায়, বদলে যাক জীবন ও সমাজ", font=font(S, 44), fill=AMBER_L, anchor="lm")
    d.text((470, 356), "শিক্ষা • খাদ্য • চিকিৎসা • রক্তদান • শীতবস্ত্র", font=font(R, 32), fill=(200, 232, 226), anchor="lm")
    d.rounded_rectangle([470, 400, 470 + 400, 400 + 62], radius=31, fill=WHITE)
    d.text((470 + 200, 431), "সদস্য হোন • ডোনেট করুন", font=font(S, 29), fill=DARK, anchor="mm")
    d.text((470, 512), "গোলাপনগর, ভেড়ামারা, কুষ্টিয়া  •  হটলাইন : ০১৬০৭-২১৫৪২১", font=font(R, 28), fill=(214, 240, 236), anchor="lm")
    img.save(path, "PNG", optimize=True)


if __name__ == "__main__":
    out = os.path.join(HERE, "..", "campaign")
    jobs = [
        (poster_join, os.path.join(out, "poster-01-svechchasebok-aahban.png")),
        (poster_donate, os.path.join(out, "poster-02-donate.png")),
        (poster_campaign, os.path.join(out, "poster-03-shitbostro-campaign.png")),
        (profile_pic, os.path.join(out, "facebook-profile-512.png")),
        (cover, os.path.join(out, "facebook-cover-1640x624.png")),
    ]
    for fn, p in jobs:
        fn(p)
        print("✓", os.path.basename(p), os.path.getsize(p) // 1024, "KB")
