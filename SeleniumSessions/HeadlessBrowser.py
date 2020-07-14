from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from webdriver_manager.firefox import GeckoDriverManager

import time

options = webdriver.ChromeOptions()
# options.headless = False
options.add_argument('--headless')
# options.add_argument('--incognito')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


# options = webdriver.FirefoxOptions()
# options.headless = True
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

driver.implicitly_wait(10)

driver.get('https://www.reddit.com/')
time.sleep(3)

print(driver.title)

time.sleep(3)
driver.close()