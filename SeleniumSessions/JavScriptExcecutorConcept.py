from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://www.amazon.com')

best_sellers = driver.find_element(By.LINK_TEXT, 'Best Sellers')
# driver.execute_script("arguments[0].click();", best_sellers)
#
# title = driver.execute_script('return document.title')
# print(title)
#
# driver.execute_script('history.go(0)')

# driver.execute_script("alert('hello selenium');")
# time.sleep(3)
# alert = driver.switch_to.alert
# alert.accept()

inner_text = driver.execute_script("return document.documentElement.innerText")
# print(inner_text)

driver.execute_script("arguments[0].style.border = '3px solid red'", best_sellers)

driver.get('https://app.hubspot.com/login')
time.sleep(5)

form = driver.find_element(By.ID, 'hs-login')
driver.execute_script("arguments[0].style.border = '3px solid red'", form)

driver.get('https://amazon.com')
#scroll to bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

driver.get('https://classic.crmpro.com')
forgot_pwd = driver.find_element(By.LINK_TEXT, 'Forgot Password?')
driver.execute_script("arguments[0].scrollIntoView(true);", forgot_pwd)
driver.execute_script("arguments[0].style.border = '3px solid red'", forgot_pwd)

print(driver.execute_script("return navigator.userAgent;"))

time.sleep(3)
driver.close()