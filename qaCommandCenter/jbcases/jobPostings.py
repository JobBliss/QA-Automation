import os
import time
import pyautogui
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



def uploadDoc():
    logging.basicConfig(filename='JobPosting_log.txt', level=logging.DEBUG, format="%(asctime)s %(message)s",
                        filemode='w')
    # Complete these 2 fields ==================
   
    USERNAME = 'anesuchiodza@yahoo.com'
    PASSWORD = 'testCase123_'
    
    # ==========================================
    fscreenshot = Screenshot.Screenshot()


    TIMEOUT = 10

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=3")

    browser = webdriver.Chrome(executable_path=CM().install(), options=options)
    #LoginToCompany
    browser.get(
        'https://alpha.jobbliss.com/signin')

    time.sleep(2)
    browser.maximize_window()

    print("[Info] - Logging in...")
    # emailAddress
    user_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div/span/form/span[1]/div/div[2]/div/div/input')))

    user_element.send_keys(USERNAME)

    # PassWord
    pass_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div/span/form/span[2]/div/div[2]/div/div/div/input')))

    pass_element.send_keys(PASSWORD)

    login_button = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div/span/form/div[1]/div/button')))

    time.sleep(0.4)

    login_button.click()

    time.sleep(5)

    # click recruiting

    clickrecruiting_button = WebDriverWait(browser, TIMEOUT).until(
         EC.presence_of_element_located((
             By.XPATH,
             '#//*[@id="app"]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/nav/div[5]/div/details/summary')))

    time.sleep(0.4)

    clickrecruiting_button.click()
    
    time.sleep(1)

    jobpost_button = WebDriverWait(browser, TIMEOUT).until(
         EC.presence_of_element_located((
             By.XPATH,
             '//*[@id="app"]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/nav/div[5]/div/details/div/a')))

    time.sleep(0.4)

    jobpost_button.click()

    time.sleep(5)

   
    try:

        #Creat Posting Button
        createposting = WebDriverWait(browser, TIMEOUT).until(
            EC.presence_of_element_located((
                By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/main/section/div/div[1]/div/div/div[1]/div/div/div/button')))

        createposting.click()

        #Fill in the Form

        jobtitle = WebDriverWait(browser, TIMEOUT).until(
            EC.presence_of_element_located((
                By.NAME,
                'job_title')))

        time.sleep(0.4)

        jobtitle.send_keys('Name of Job')

        #Country
        country = WebDriverWait(browser, TIMEOUT).until(
            EC.presence_of_element_located((
                By.XPATH,
                '//*[@id="app"]/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[3]/div/div[2]/form/span/div/div[1]/div[2]/div[2]/div/div/div/div/div[2]/input')))
        time.sleep(0.4)
        country.send_keys('Albania')

        region = WebDriverWait(browser, TIMEOUT).until(
            EC.presence_of_element_located((
                By.XPATH,
                '//*[@id="e156c8ab-a5d5-4b8a-a42f-308749ad8621"]')))
        time.sleep(0.4)
        region.send_keys('Uptown')

        #city

        cityField = WebDriverWait(browser, TIMEOUT).until(
            EC.presence_of_element_located((
                By.XPATH,
                '//*[@id="37921b3d-dcfc-40f2-8d89-06c429041b0a"]')))
        time.sleep(0.4)
        cityField.send_keys('BigCup')
        
        image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='UploadedDocument.png')
        time.sleep(3)


        print('...............')

        print('....... Document Found ......')
        time.sleep(0.4)
        header = ['Test Name', 'State']

        #data
        data = ['Job Posting Failed' 'Passed']

        with open('AutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)

    except:
        search_element = WebDriverWait(browser, TIMEOUT).until(
            EC.presence_of_element_located((
                By.NAME, 'input_filter')))

        search_element.send_keys('emailLogin.py')

        #click on search

        search_button = WebDriverWait(browser, TIMEOUT).until(
            EC.presence_of_element_located((
                By.XPATH,
                '//*[@id="app"]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/main/div[2]/div/div[1]/div/div[1]/form/div[2]/div/button')))

        time.sleep(0.4)

        search_button.click()
        time.sleep(6)
        image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='UploadedDocumentFail.png')
        time.sleep(3)


        print('...............')

        print('....... Document Not Found ......')
        time.sleep(0.4)
        header = ['Test Name', 'State']

        #data
        data = ['Job Posting', 'Failed']

        with open('AutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)



    finally:
        
        browser.quit()

    print('Thank you. Good Bye!')
    

if __name__ == '__main__':
    uploadDoc()
