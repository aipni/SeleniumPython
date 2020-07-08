from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://www.spicejet.com/')
time.sleep(3)

'''move to element '''
login_ele = driver.find_element(By.ID, 'ctl00_HyperLinkLogin')
act_chains = ActionChains(driver)
act_chains.move_to_element(login_ele).perform()

clubMember_ele = driver.find_element(By.LINK_TEXT, 'SpiceClub Members')
act_chains.move_to_element(clubMember_ele).perform()

memberLogin_ele = driver.find_element(By.LINK_TEXT, 'Member Login')
memberLogin_ele.click()


time.sleep(3)
driver.close()
