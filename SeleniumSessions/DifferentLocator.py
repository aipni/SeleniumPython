from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/')

print(driver.title)

username_url = driver.find_element(By.ID, 'Form_submitForm_subdomain')
first_name = driver.find_element(By.ID, 'Form_submitForm_FirstName')
last_name = driver.find_element(By.ID, 'Form_submitForm_LastName')
email = driver.find_element(By.ID,'Form_submitForm_Email')
feature = driver.find_element(By.LINK_TEXT,'Features')

username_url.send_keys('AutomationHub')
first_name.send_keys('Automation')
last_name.send_keys('Hub')
email.send_keys('automationhub@noemail.com')
feature.click()

time.sleep(3)

driver.close()