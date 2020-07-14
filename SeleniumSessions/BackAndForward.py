from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://amazon.com')
driver.find_element(By.LINK_TEXT, 'Best Sellers')
time.sleep(2)

driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.back()

driver.refresh()

time.sleep(3)
driver.close()