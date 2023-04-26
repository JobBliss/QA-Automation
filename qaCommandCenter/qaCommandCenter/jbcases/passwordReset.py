import os
import time
import selenium
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM
from PIL import Image
from Screenshot import *
from emailLogin import *
import parameters


def jobblissCreateContractor():

    logging.basicConfig(filename='CreateContractor_log.txt', level=logging.DEBUG, format="%(asctime)s %(message)s", filemode='w')
    
    fscreenshot = Screenshot.Screenshot()

    TIMEOUT = 10

    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=3")
    #options.add_argument("--incognito")
    options.add_argument("--kiosk")

    browser = webdriver.Chrome(executable_path=CM().install(), options=options)
    
        
    browser.get(parameters.forgotPwd)

    browser.maximize_window()

    print("[Info] - Reset Password Process . . .")

    #emailField 
    emailField = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.ID, 'email')))

    emailField.send_keys(parameters.contractorEmail)
    time.sleep(10)

    #submitDetails Button.cls

    submitDetails = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/div/span/form/div[1]/div/button')))

    submitDetails.click()
    time.sleep(5)   
        

    
    browser.quit()


    

if __name__ == '__main__':
    jobblissCreateContractor()
    
