from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://classic.crmpro.com/')
time.sleep(3)

username_ele = driver.find_element(By.NAME, 'username')
password_ele = driver.find_element(By.NAME, 'password')

login_button = driver.find_element(By.XPATH, "//input[@type='submit']")

act_chains = ActionChains(driver)
act_chains.send_keys_to_element(username_ele, 'batchautomation')
act_chains.send_keys_to_element(password_ele, 'Test@12345')
act_chains.click(login_button).perform()
# act_chains.perform()https://classic.crmpro.com/


time.sleep(3)
driver.close()