import sys, time, json
from selenium import webdriver
from selenium.webdriver.edge.options import Options
o = Options(); o.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
d = webdriver.Edge(options=o)
d.execute_script("[...document.querySelectorAll('div[role=button],button')].filter(b=>b.innerText.trim()=='Ahora no').forEach(b=>b.click())"); time.sleep(2)
res = {}
for tag in sys.argv[1:]:
    d.get(f"https://www.instagram.com/explore/tags/{tag}/"); time.sleep(8)
    for y in (1200, 2600): d.execute_script(f"window.scrollTo(0,{y})"); time.sleep(3)
    items = d.execute_script("""return [...document.querySelectorAll('a[href*="/p/"],a[href*="/reel/"]')].map(a=>{const i=a.querySelector('img');return {href:a.href,alt:i?i.alt:''}})""")
    seen = {}; [seen.setdefault(x["href"], x["alt"]) for x in items]
    res[tag] = [{"href": h, "alt": a} for h, a in seen.items()]
    print(tag, len(seen), "|", d.title, "|", d.current_url)
    d.save_screenshot(f"ig_{tag}.png"); time.sleep(4)
json.dump(res, open("ig_tags.json", "w", encoding="utf-8"), ensure_ascii=False)
