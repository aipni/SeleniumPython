from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://www.reddit.com/')
time.sleep(2)

cookies = driver.get_cookies()

for cook in cookies:
    print(cook)
    print(len(cook))

driver.add_cookie({"name":"python", "domain":"reddit.com","value":"python"})

print(driver.get_cookies())

for cook in cookies:
    print(cook)
    print(len(cook))

time.sleep(3)
driver.close()