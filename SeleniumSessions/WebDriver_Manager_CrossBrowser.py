from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import time

browserName = "chrome"

if browserName== "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName=="firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    print('please pass the valid browser name :'+browserName)
    raise Exception("driver is not found")

# driver.implicitly_wait(5)
driver.get("http://app.hubspot.com/")
time.sleep(5)
driver.find_element(By.ID, 'username').send_keys("addypradip@gmail.com")
driver.find_element(By.ID, 'password').send_keys("SeleniumPractice2020")
driver.find_element(By.ID, 'loginBtn').click()
print(driver.title)

time.sleep(5)
driver.quit()