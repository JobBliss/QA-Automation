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
    # Complete these fields ==================
   
    
    # ==========================================
    fscreenshot = Screenshot.Screenshot()

    TIMEOUT = 5

    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=3")
    #options.add_argument("--incognito")
    options.add_argument("--kiosk")

    browser = webdriver.Chrome(executable_path=CM().install(), options=options)
    
    #LoginToCompany
        
    browser.get(parameters.signuplink)

    browser.maximize_window()


    print("[Info] - Signing up in progress...")


    #clickContractor Button
    clickContractor = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/button')))

    clickContractor.click()
        

    #Enter Company Email Address
    user_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.TAG_NAME , "input")))

    user_element.send_keys(parameters.username)

    # Enter First Name
    firstname_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.NAME,
            'givenName')))

    firstname_element.send_keys(parameters.firstName)
    

    # Enter Last Name
    lastname_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.NAME,
            'familyName')))

    lastname_element.send_keys(parameters.LastName)
    

    # PassWord
    pass_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.NAME, 'password')))

    pass_element.send_keys(parameters.contrPass)
    

    # PassWord
    confirm_pass_element = WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((
            By.NAME,
            'confirm')))

    confirm_pass_element.send_keys(parameters.contrPass)
    

    signup_button = WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((
            By.ID, 'signup'
            )))
    print("Signing up now")

    signup_button.click()

    time.sleep(3)

    # Take a screenshot of the Page and store it for analysis.
    image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='CreateContractor.png')
    time.sleep(10)
    print("You have successfully signed up.")
    screenshot = Image.open('CreateContractor.png')
    #screenshot.show()

    
    print("Closing browser now...")
    time.sleep(10)
    browser.quit()


    

if __name__ == '__main__':
    jobblissCreateContractor()
    
