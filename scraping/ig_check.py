from selenium import webdriver
from selenium.webdriver.edge.options import Options
o = Options(); o.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
d = webdriver.Edge(options=o)
print([ (h, d.switch_to.window(h) or d.current_url) for h in d.window_handles])
for h in d.window_handles:
    d.switch_to.window(h)
    if "instagram" in d.current_url:
        print(d.current_url, "|", d.title); print(d.find_element("tag name","body").text[:300].replace("\n"," | ")); d.save_screenshot("ig_state.png")
