from smtpd import Options

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options

import time
#
# options = Options()
# options.add_argument('--allow-running-insecure-content')
# options.add_argument('--ignore-certificate-errors')

# desired_capabilities = DesiredCapabilities().CHROME.copy()
# desired_capabilities['acceptInsecureCerts'] = True

options = Options()
options.set_capability('acceptInsecureCerts', True)


# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=desired_capabilities)

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.implicitly_wait(10)

driver.get('https://expired.badssl.com/')

print(driver.find_element(By.TAG_NAME, 'h1').text)



time.sleep(3)
driver.close()