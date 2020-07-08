from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://app.hubspot.com/')

print(driver.title)

# driver.find_element(By.CSS_SELECTOR, '#username').send_keys('automationhub@noemail.com')

# driver.find_element(By.CLASS_NAME, 'login-email').send_keys('automationhub@noemail.com')
# driver.find_element(By.CLASS_NAME, 'login-password').send_keys('automation@123')
# driver.find_element(By.CLASS_NAME, 'login-submit').click()

# driver.find_element(By.CSS_SELECTOR, 'input.form-control.private-form__control.login-email').send_keys('automationhub@noemail.com')

# driver.find_element(By.XPATH, '//input[@class="form-control private-form__control login-email"]').send_keys('automationhub@noemail.com')

#three class name doest not work
# driver.find_element(By.CLASS_NAME, 'form-control private-form__control login-email').send_keys('automationhub@noemail')

# driver.find_element(By.LINK_TEXT, 'Sign up').click()

# partial link text not recommended tho
driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign').click()

time.sleep(3)

driver.close()