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





def jobblissCreateCompany():

    logging.basicConfig(filename='Createcompany_log.txt', level=logging.DEBUG, format="%(asctime)s %(message)s", filemode='w')
    # Complete these fields ==================
    USERNAME = 'achiodza@gmail.com'
    PASSWORD = 'testCase123_'
    FNAME = 'Rodney'
    LNAME= 'Cleanshizoo'
    NOEMPLOYEES='3'
    CITY = 'Honolulu'
    BNAME = 'JB Inc'
    # ==========================================
    fscreenshot = Screenshot.Screenshot()

    TIMEOUT = 5

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=3")
    #options.add_argument("--incognito")
    #options.add_argument("--kiosk")

    browser = webdriver.Chrome(executable_path=CM().install(), options=options)
    
    #LoginToCompany
        
    browser.get(
        'https://alpha.jobbliss.com/signup')

    browser.maximize_window()


    print("[Info] - Signing up in progress...")


    #clickCompany Button
    clickCompany = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/button')))

    clickCompany.click()
        

    #Enter Company Email Address
    user_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.TAG_NAME , "input")))

    user_element.send_keys(USERNAME)

    # Enter First Name
    firstname_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.NAME,
            'givenName')))

    firstname_element.send_keys(FNAME)
    

    # Enter Last Name
    lastname_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.NAME,
            'familyName')))

    lastname_element.send_keys(LNAME)
    

    # PassWord
    pass_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.NAME, 'password')))

    pass_element.send_keys(PASSWORD)
    

    # PassWord
    confirm_pass_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.NAME,
            'confirm')))

    confirm_pass_element.send_keys(PASSWORD)
    
    #------------------
    #Business Info:
    #-----------------
    #Business Name
    businessname_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.NAME,
            'business_name')))

    businessname_element.send_keys(BNAME)
    

    #City
    city_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.NAME,
            'business_city')))

    city_element.send_keys(CITY)
    

    #Number of Employees

    no_employees_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.NAME,
            'Employees')))

    no_employees_element.send_keys(NOEMPLOYEES)

   

    signup_button = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.ID, 'signup'
            )))
    print("Signing up now")

    signup_button.click()

    time.sleep(7)

    # Take a screenshot of the Page and store it for analysis.
    image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='CreateCompanyAcc.png')
    time.sleep(10)
    print("You have successfully signed up.")
    screenshot = Image.open('CreateCompanyAcc.png')
    #screenshot.show()

    time.sleep(3)
    print("Closing browser now...")
    browser.quit()


    

if __name__ == '__main__':
    jobblissCreateCompany()
    #emailLogin()
