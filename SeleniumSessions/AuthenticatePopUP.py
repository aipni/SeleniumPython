from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth/')
time.sleep(2)



time.sleep(3)
driver.close()
