import sys, time, json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
o = Options(); o.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
o.add_argument("--window-size=1300,2400"); o.add_argument("--lang=es-AR"); o.add_argument("--disable-blink-features=AutomationControlled")
o.add_experimental_option("excludeSwitches", ["enable-automation"])
d = webdriver.Chrome(options=o)
for tag in sys.argv[1:]:
    d.get("https://www.tiktok.com/tag/" + tag); time.sleep(10)
    for y in (1200, 2400): d.execute_script(f"window.scrollTo(0,{y})"); time.sleep(2)
    out = d.execute_script("return [...document.querySelectorAll('a[href*=\"/video/\"]')].map(a=>({href:a.href,t:(a.parentElement.parentElement.innerText||'').slice(0,200)}))")
    print(tag, len(out), d.find_element("tag name","body").text[:150].replace("\n"," | "))
    json.dump(out, open(f"tt_tag_{tag}.json", "w", encoding="utf-8"), ensure_ascii=False); d.save_screenshot(f"tt_tag_{tag}.png")
d.quit()
