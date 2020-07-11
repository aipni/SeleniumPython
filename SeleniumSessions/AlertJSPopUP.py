from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
time.sleep(2)

driver.find_element(By.NAME, 'proceed').click()

alert_popup = driver.switch_to.alert

print(alert_popup.text)
alert_popup.accept() #click accept or ok in alert warning

#alert_popup.dismiss() #cancel the popup
#alert_popup.send_keys("")

driver.switch_to.default_content()
driver.find_element(By.ID, 'login1').send_keys('automationhub@noemail.com')
driver.find_element(By.ID, 'password').send_keys('automationhub')


time.sleep(3)
driver.close()
