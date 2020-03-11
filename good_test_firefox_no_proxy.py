import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.set_headless()

driver = webdriver.Firefox(options=opts)
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

time.sleep(4)

print(driver.page_source.encode("utf-8"))

assert "No results found." not in driver.page_source

print ("Headless Firefox Initialized on Linux OS")

driver.close()

