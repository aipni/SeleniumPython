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

# wait.until(ec.title_is('HubSpot Login'))
wait.until(ec.title_contains('HubSpot'))
print(driver.title)

email_id = wait.until(ec.presence_of_element_located((By.ID, 'username')))
email_id.send_keys("bemsid@noemail.com")

driver.find_element(By.ID, 'password').send_keys("BemsID@123")

time.sleep(3)
driver.close()
