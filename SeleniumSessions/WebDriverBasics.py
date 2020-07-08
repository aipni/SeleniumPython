import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.google.com/")
print(driver.title)

driver.find_element(By.NAME, 'q').send_keys("naveen automationlabs")
time.sleep(5)
optionList = driver.find_elements(By.CSS_SELECTOR,'ul.erkvQe li span')
print(len(optionList))

for ele in optionList:
    print(ele.text)
    if ele.text=='naveen automationlabs youtube':
        ele.click()
        break


time.sleep(5)

driver.quit()

