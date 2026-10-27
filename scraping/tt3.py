import sys, time, json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
o = Options(); o.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
o.add_argument("--window-size=1300,2400"); o.add_argument("--lang=es-AR"); o.add_argument("--disable-blink-features=AutomationControlled")
o.add_experimental_option("excludeSwitches", ["enable-automation"])
d = webdriver.Chrome(options=o); res = {}
for tag in sys.argv[1:]:
    d.get("https://www.tiktok.com/tag/" + tag); time.sleep(9)
    for y in (1500, 3000, 4500): d.execute_script(f"window.scrollTo(0,{y})"); time.sleep(2)
    hdr = d.execute_script("const h=document.querySelector('[data-e2e=\"challenge-vcount\"]');return h?h.innerText:''")
    items = d.execute_script("""return [...document.querySelectorAll('a[href*="/video/"]')].map(a=>{let c=a;for(let i=0;i<5&&c.parentElement;i++){c=c.parentElement;if(c.innerText&&c.innerText.length>40)break}return {href:a.href,t:c.innerText}})""")
    seen = {}
    for x in items: seen.setdefault(x["href"], x["t"])
    res[tag] = {"views": hdr, "items": [{"href": h, "t": t} for h, t in seen.items()]}
    print(tag, "views:", hdr, "items:", len(seen))
json.dump(res, open("tt_tags.json", "w", encoding="utf-8"), ensure_ascii=False); d.quit()
