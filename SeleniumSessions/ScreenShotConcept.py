from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(10)

options = webdriver.ChromeOptions()
options.headless = True

driver.get('https://www.reddit.com/')

print(driver.title)

# driver.get_screenshot_as_file('reddit.png')

'''full screenshot'''
#make sure that you are running in headless mode

S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
driver.set_window_size(S('Width'),S('Height'))
driver.find_element_by_tag_name('body').screenshot('reddit_full_1.png')

time.sleep(3)
driver.close()
