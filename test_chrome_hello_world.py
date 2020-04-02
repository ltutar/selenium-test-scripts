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
# the value is provided by XL Release
driver.get("${RANCHER_WEB_APPLICATION_URL}")
print(driver.title)
assert "Rancher" in driver.title

assert "Hello world!" in driver.page_source

print("Headless Chrome Initialized on Linux OS")

driver.quit()
