import xlrd

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/')
time.sleep(2)

url = driver.find_element(By.ID, 'Form_submitForm_subdomain')
first_name = driver.find_element(By.ID, 'Form_submitForm_FirstName')
last_name = driver.find_element(By.ID, 'Form_submitForm_LastName')
email = driver.find_element(By.ID, 'Form_submitForm_Email')
job_title = driver.find_element(By.ID, 'Form_submitForm_JobTitle')
company_name = driver.find_element(By.ID, 'Form_submitForm_CompanyName')
contact = driver.find_element(By.ID, 'Form_submitForm_Contact')
total_emp = driver.find_element(By.ID, 'Form_submitForm_NoOfEmployees')
industry = driver.find_element(By.ID, 'Form_submitForm_Industry')
country = driver.find_element(By.ID, 'Form_submitForm_Country')

workbook = xlrd.open_workbook("DataFileForPython.xlsx")
sheet = workbook.sheet_by_name("Registration")

#get total number of rows
rowCount = sheet.nrows
colCount = sheet.ncols
print(rowCount)
print(colCount)

# for current_row in range(1, rowCount):
#     user_name = sheet.cell_value(current_row, 0)
#     password = sheet.cell_value(current_row, 1)
#
#     print(user_name + "    " + password)

for current_row in range(1, rowCount):
    urlValue = sheet.cell_value(current_row, 0)
    firstName = sheet.cell_value(current_row, 1)
    lastName = sheet.cell_value(current_row, 2)
    emailID = sheet.cell_value(current_row, 3)
    jobTitle = sheet.cell_value(current_row, 4)
    company = sheet.cell_value(current_row, 5)
    phoneNumber = sheet.cell_value(current_row, 6)
    totalEmp = sheet.cell_value(current_row, 7)
    industryName = sheet.cell_value(current_row, 8)
    countryName = sheet.cell_value(current_row, 9)

    print(urlValue + firstName + lastName)

    url.clear()
    url.send_keys(urlValue)
    first_name.clear()
    first_name.send_keys(firstName)
    last_name.clear()
    last_name.send_keys(lastName)
    email.clear()
    email.send_keys(emailID)
    job_title.clear()
    job_title.send_keys(jobTitle)
    company_name.clear()
    company_name.send_keys(company)
    contact.clear()
    contact.send_keys(phoneNumber)
    total_emp.send_keys(totalEmp)
    industry.send_keys(industryName)
    country.send_keys(countryName)

time.sleep(5)
driver.close()
