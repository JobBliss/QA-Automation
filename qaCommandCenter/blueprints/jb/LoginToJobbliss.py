from email import header
import os
import time
from typing import final
import requests
from urllib import request
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
import csv



def jobblissLogin():
    logging.basicConfig(filename='LoginToJobbliss_log.txt', level=logging.DEBUG, format="%(asctime)s %(message)s",
                        filemode='w')
   
    USERNAME = 'anesuchiodza@yahoo.com'
    PASSWORD = 'testCase123_'
    SEARCH = '********'
    # ==========================================
    fscreenshot = Screenshot.Screenshot()
    print("Login As a Company/Admin")


    TIMEOUT = 10

    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=3")
    options.add_argument("--headless")
    #options.add_argument("--kiosk")

    browser = webdriver.Chrome(executable_path=CM().install(), options=options)
    #LoginToCompany
    browser.get(
        'https://alpha.jobbliss.com/signin')

    #time.sleep(30)

    #time.sleep(20)
    print("[Info] - Logging in process in progress...")
    # emailAddress
    user_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.NAME, 'email')))

    user_element.send_keys(USERNAME)

    #time.sleep(5)


    # PassWord
    passWed = browser.find_element(By.XPATH, '//input[@id="password"]')
    # pass_element = WebDriverWait(browser, TIMEOUT).until(
    #      EC.invisibility_of_element_located((
    #          By.XPATH, "//input[@id='password']")))
    
   
    #pass_element.send_keys(PASSWORD)
    passWed.send_keys(PASSWORD)

    login_button = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/div/span/form/div[1]/div/button')))

    time.sleep(0.4)

    login_button.click()

    time.sleep(10)

    browser.get('https://alpha.jobbliss.com/dashboard')

    try:
        #check if we have actually got in on the site since you can not access dashboard without logging in. Element to be located is the dashbord text "Dashboard"
        elem = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/main/div[1]/ul/li/span[2]'))
            # Take a screenshot of the Page and store it for analysis.
        
        )
        image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='CompanyLoggedIn.png')
        time.sleep(3)

        header = ['Test Name', 'State']

        #data
        data = ['Company Login' 'Passed']

        with open('AutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(header)

            writer.writerow(data)

            time.sleep(3)
        print("Logged In As a Company/Admin Successfully")
    finally:
        #browser.quit()  
        print('script done running.. on to the next, please check results to understand status of test..')  
   
    

   


if __name__ == '__main__':
    jobblissLogin()
