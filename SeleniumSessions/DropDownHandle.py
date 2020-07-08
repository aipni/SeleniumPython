from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/')

def select_values(element, value):
    select = Select(element)
    select.select_by_visible_text(value)

def select_values_from_dropdown(dropdownOptionsList, value):
    print(len(dropdownOptionsList))
    for ele in dropdownOptionsList:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break

industry_options = driver.find_elements(By.XPATH, '//*[@id="Form_submitForm_Industry"]/option')
select_values_from_dropdown(industry_options,'Education')
select_values_from_dropdown(industry_options,'Travel')

ele_Industry = driver.find_element(By.ID, 'Form_submitForm_Industry')
ele_Country = driver.find_element(By.ID, 'Form_submitForm_Country')

select_values(ele_Industry,'Education')
select_values(ele_Country,'Nepal')

# select = Select(ele_Industry)

# select.select_by_visible_text('Education')
# select.select_by_index(7)
# select.select_by_value('health')

# print(select.is_multiple)

#print all the value from dropdrown

# select = Select(ele_Industry)
# industry_list = select.options
#
# for ele in industry_list:
#     print(ele.text)
#     if(ele.text=='Automotive'):
#         ele.click()
#         break

# industry_options = driver.find_elements(By.XPATH, '//*[@id="Form_submitForm_Industry"]/option')
# print(len(industry_options))
# for ele in industry_options:
#     print(ele.text)
#     if ele.text=='Travel':
#         ele.click()
#         break

time.sleep(5)
driver.close()