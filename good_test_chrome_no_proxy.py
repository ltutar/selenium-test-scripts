import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
#https://peter.sh/experiments/chromium-command-line-switches/
chrome_options.add_argument('--no-sandbox') # Bypass OS security model
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--headless") # Runs Chrome in headless mode.

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

print("Levent's password:")
print(@@password@@)

time.sleep(4)

print(driver.page_source.encode("utf-8"))

assert "No results found." not in driver.page_source

print("Headless Chrome Initialized on Linux OS")

driver.close()
