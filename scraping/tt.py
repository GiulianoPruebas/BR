import sys, time, json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
o = Options(); o.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
o.add_argument("--window-size=1300,2400"); o.add_argument("--lang=es-AR"); o.add_argument("--disable-blink-features=AutomationControlled")
d = webdriver.Chrome(options=o)
for q in sys.argv[1:]:
    d.get("https://www.tiktok.com/search/video?q=" + q.replace(" ", "%20")); time.sleep(10)
    for y in (1500, 3000): d.execute_script(f"window.scrollTo(0,{y})"); time.sleep(2)
    out = d.execute_script("return [...document.querySelectorAll('a[href*=\"/video/\"]')].map(a=>({href:a.href,t:(a.closest('[data-e2e=\"search_video-item\"]')||a.parentElement.parentElement).innerText.slice(0,300)}))")
    print(q, len(out), d.find_element("tag name","body").text[:200].replace("\n"," | "))
    json.dump(out, open("tt_" + q.replace(" ", "_") + ".json", "w", encoding="utf-8"), ensure_ascii=False)
    d.save_screenshot("tt_" + q.replace(" ", "_") + ".png")
d.quit()
