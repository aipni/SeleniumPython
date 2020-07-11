from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('http://www.londonfreelance.org/courses/frames/')
time.sleep(2)

#driver.switch_to.frame('2')
#driver.switch_to.frame('main')
frame_element = driver.find_element(By.NAME, 'main')
driver.switch_to.frame(frame_element)

header_value = driver.find_element(By.CSS_SELECTOR, 'body > h2').text
print(header_value)

driver.switch_to.default_content()
driver.switch_to.parent_frame()



time.sleep(3)
driver.close()
