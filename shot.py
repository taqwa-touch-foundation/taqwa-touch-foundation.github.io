from playwright.sync_api import sync_playwright
import pathlib, time
url = "http://127.0.0.1:8899/index.html"
out = pathlib.Path("/workspace/site/preview")
with sync_playwright() as p:
    b = p.chromium.launch(args=["--force-color-profile=srgb","--font-render-hinting=none"])
    def shot(name, w, h, full=True, scale=2):
        pg = b.new_page(viewport={"width":w,"height":h}, device_scale_factor=scale)
        pg.goto(url, wait_until="load")
        pg.add_style_tag(content=".reveal{opacity:1!important;transform:none!important}*{transition:none!important;animation:none!important}")
        pg.wait_for_timeout(1500)
        pg.screenshot(path=str(out/name), full_page=full)
        # console errors
        pg.close()
    shot("desktop-full.png", 1440, 900, True, 1)
    shot("mobile-full.png", 414, 900, True, 2)
    pg = b.new_page(viewport={"width":1440,"height":900}, device_scale_factor=2)
    errors=[]
    pg.on("console", lambda m: errors.append(m.type+": "+m.text) if m.type=="error" else None)
    pg.on("pageerror", lambda e: errors.append("pageerror: "+str(e)))
    pg.goto(url, wait_until="load"); pg.wait_for_timeout(2000)
    pg.screenshot(path=str(out/"hero.png"), clip={"x":0,"y":0,"width":1440,"height":900})
    print("CONSOLE:", errors if errors else "no errors")
    b.close()
