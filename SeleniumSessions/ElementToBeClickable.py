from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://app.hubspot.com/login')

wait = WebDriverWait(driver, 10)
signup_link = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Sign up')))

print(signup_link.text)
signup_link.click()

first_name = wait.until(ec.visibility_of_element_located((By.ID, 'uid-firstName-5')))
first_name.send_keys('pradeep')


time.sleep(3)
driver.close()