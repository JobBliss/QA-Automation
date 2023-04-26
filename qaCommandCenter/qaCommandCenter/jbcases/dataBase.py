from email import header
import os
import time
from tokenize import group
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
import paths

import parameters



def dataBaseview():
    logging.basicConfig(filename='dataBaseView.txt', level=logging.DEBUG, format="%(asctime)s %(message)s",
                        filemode='w')
   
   
    # ==========================================
    fscreenshot = Screenshot.Screenshot()
    print("Login As a Company/Admin")


    TIMEOUT = 10

    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=3")
    #options.add_argument("--headless")
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

    user_element.send_keys(parameters.USERNAME)

    #time.sleep(5)


    # PassWord
    passWed = browser.find_element(By.XPATH, '//input[@id="password"]')
  
   
    #pass_element.send_keys(PASSWORD)
    passWed.send_keys(parameters.PASSWORD)

    login_button = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, paths.loginButton)))

    time.sleep(0.4)

    login_button.click()

    time.sleep(10)
    #dbview
    browser.get(parameters.dbview)
    browser.maximize_window()

    try:
        #try this block first
        elemupload = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, paths.uploadContractor))     
        )
        elemupload.click()

        

        emailCont = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, paths.emailContractor))     
        )
        emailCont.send_keys(parameters.contractorEmail)

        fname = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, paths.fnameContractor))     
        )
        fname.send_keys(parameters.fnameContractor)

        lname = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, paths.lnameContractor))     
        )
        lname.send_keys(parameters.lnameContractor)
        time.sleep(10)
        addContr = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, paths.invitecontractor))     
        )
        addContr.click()


        image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='dataBase.png')
        time.sleep(3)

        header = ['Test Name', 'State']

        #data
        data = ['inviteContractor' 'Passed']

        with open('AutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(header)

            writer.writerow(data)

            time.sleep(3)
    #catch exception
    except:
        #try this block first
        elemupload = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, paths.uploadContractor))     
        )
        elemupload.click()

        

        emailCont = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, paths.emailContractor))     
        )
        emailCont.send_keys(parameters.contractorEmail)

        fname = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, paths.fnameContractor))     
        )
        fname.send_keys(parameters.fnameContractor)

        lname = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, paths.lnameContractor))     
        )
        lname.send_keys(parameters.lnameContractor)

        time.sleep(10)

        addContr = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, paths.invitecontractor))     
        )
        addContr.click()


        image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='dataBase.png')
        time.sleep(3)

        header = ['Test Name', 'State']

        #data
        data = ['inviteContractor' 'Passed']

        with open('AutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(header)

            writer.writerow(data)

            time.sleep(3)

    else:
        header = ['Test Name', 'State']
        data = ['inviteContractor' 'Failed']
        with open('AutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(header)

            writer.writerow(data)

            time.sleep(3)
        #check if we have actually got in on the site since you can not access dashboard without logging in. Element to be located is the dashbord text "Dashboard"
        
    finally:
        #browser.quit()  
        print('script done running.. on to the next, please check results to understand status of test..')  
   

if __name__ == '__main__':
    dataBaseview()
