import os
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM
from PIL import Image
import logging
from Screenshot import *



def jobblissLogin():

    logging.basicConfig(filename='ContractorLogin_log.txt', level=logging.DEBUG, format="%(asctime)s %(message)s", filemode='w')
    # Complete these 2 fields ==================
    USERNAME = 'anesu+contractor@velocityinc.tech'
    PASSWORD = 'Greenballs123'
    SEARCH = '********'
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


    # Take a screenshot of the Page and store it for analysis.
    image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='Contractor.png')
    time.sleep(3)
    screenshot = Image.open('Contractor.png')
    screenshot.show()

    # Condition Logic, If the text searched is there open email and report success. (Optional as one can take a look at the screenshots)
    # Option to log the info in  a seperate file can be explored.


if __name__ == '__main__':
    jobblissLogin()
