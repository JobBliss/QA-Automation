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



def jobblissCreateCompany():

    logging.basicConfig(filename='log.txt', level=logging.DEBUG, format="%(asctime)s %(message)s", filemode='w')
    # Complete these fields ==================
    USERNAME = 'anesuchiodza@yahoo.com'
    PASSWORD = 'testCase123_'
    FNAME = 'Moses'
    LNAME= 'Gumbochuma'
    NOEMPLOYEES='4'
    CITY = 'Honolulu'
    BNAME = 'GreenBottle Investments'
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
        'https://alpha.jobbliss.com/signup')

    time.sleep(2)

    print("[Info] - Logging in...")


    #clickCompany Button
    clickCompany = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/button')))

    clickCompany.click()
    time.sleep(3)
    browser.maximize_window()

    #Enter Company Email Address
    user_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH,
            '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/form/div[1]/div/div/span[1]/div/div[2]/div[1]/div/input')))

    user_element.send_keys(USERNAME)

    # Enter First Name
    firstname_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH,
            '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/form/div[1]/div/div/span[2]/div/div[2]/div/div/input')))

    firstname_element.send_keys(FNAME)
    time.sleep(1)

    # Enter Last Name
    lastname_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH,
            '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/form/div[1]/div/div/span[3]/div/div[2]/div[1]/div/input')))

    lastname_element.send_keys(LNAME)
    time.sleep(1)

    # PassWord
    pass_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/form/div[1]/div/div/span[4]/div/div[2]/div[1]/div/input')))

    pass_element.send_keys(PASSWORD)
    time.sleep(1)

    # PassWord
    confirm_pass_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH,
            '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/form/div[1]/div/div/span[5]/div/div[2]/div[1]/div/input')))

    confirm_pass_element.send_keys(PASSWORD)
    time.sleep(1)
    #------------------
    #Business Info:
    #-----------------
    #Business Name
    businessname_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH,
            '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/form/div[1]/div/div/div/span[1]/div/div[2]/div[1]/div/input')))

    businessname_element.send_keys(BNAME)
    time.sleep(1)

    #City
    city_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH,
            '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/form/div[1]/div/div/div/span[2]/div/div[2]/div[1]/div/input')))

    city_element.send_keys(CITY)
    time.sleep(1)

    #Number of Employees

    no_employees_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH,
            '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/form/div[1]/div/div/div/span[3]/div/div[2]/div/div/input')))

    no_employees_element.send_keys(NOEMPLOYEES)

    time.sleep(10)

    signup_button = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/form/div[2]/div[2]/div/button')))
    print("signing up now")

    signup_button.click()

    time.sleep(3)

    # Take a screenshot of the Page and store it for analysis.
    image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='CreateAccCompany.png')
    time.sleep(3)
    screenshot = Image.open('CreateAccCompany.png')
    screenshot.show()



if __name__ == '__main__':
    jobblissCreateCompany()
