import LoginToJobbliss
import os
import time
import selenium
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM
from PIL import Image
from Screenshot import *

LoginToJobbliss.jobblissLogin()

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument("--log-level=3")
browser = webdriver.Chrome(executable_path=CM().install(), options=options)
browser.execute_script('''window.open("https://alpha.jobbliss.com/signin","_blank");''')
print('Logged in as Company')

# clickCompanyResources
TIMEOUT=10

CompanyResources_button = WebDriverWait(browser, TIMEOUT).until(
    EC.presence_of_element_located((
        By.XPATH,
        '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/nav/div[2]/div/details/summary/span')))

time.sleep(0.4)

CompanyResources_button.click()

time.sleep(1)
#CompanyDatabase
companyDb_button = WebDriverWait(browser, TIMEOUT).until(
    EC.presence_of_element_located((
        By.XPATH,
        '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/nav/div[2]/div/details/div[1]/a/span')))

time.sleep(0.4)

companyDb_button.click()

viewprofile_button = WebDriverWait(browser, TIMEOUT).until(
    EC.presence_of_element_located((
        By.XPATH,
        '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/main/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div/button')))

time.sleep(0.4)

viewprofile_button.click()
time.sleep(3)

removefromCo_button = WebDriverWait(browser, TIMEOUT).until(
    EC.presence_of_element_located((
        By.XPATH,
        '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/main/section/div/div/div/div[1]/div/div[2]/div[1]/div/button')))

time.sleep(0.4)

removefromCo_button.click()
time.sleep(3)

#ConfirmRemove
confirm_remove_button = WebDriverWait(browser, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[3]/div/div[2]/form/div[1]/div[3]/div[2]/div/button')))
confirm_remove_button.click()

image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='removeContractorFromCompany.png')
time.sleep(3)
screenshot = Image.open('removeContractorFromCompany.png')

time.sleep(3)
print('Contractor removed Successfully!')
print('Good Bye!')
time.sleep(3)
browser.close()