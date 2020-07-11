from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://cgi-lib.berkeley.edu/ex/fup.html')
time.sleep(2)
#type='file' should be there to use send keys in seleniukm for upload the file
driver.find_element(By.NAME, 'upfile').send_keys('C:\\Users\pradi\Desktop\hubspot.png')
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# driver.get('http://hubspot.com/')
# print(driver.get_cookies())

time.sleep(3)
driver.close()