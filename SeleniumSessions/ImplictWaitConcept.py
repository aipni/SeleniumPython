from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)

#time_out = 10
#dynamic_wait
#imp wait will be applied for all the web elements
#global wait
#find_elements
#only for web elements
#not for non web elements: titile, url, alerts

driver.get('https://app.hubspot.com/login')

print(driver.title)

user_name = driver.find_element(By.ID, 'username')
user_name.send_keys("bemsid@noemail.com")

user_password = driver.find_element(By.ID, 'password')
user_password.send_keys("BemsID@123")

#ele3
#ele4
#ele5


time.sleep(3)
driver.close()