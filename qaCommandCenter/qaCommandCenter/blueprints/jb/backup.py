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
from Screenshot import *



def jobblissLogin():
    # Complete these 2 fields ==================
    USERNAME = 'anesu+contractor@velocityinc.tech'
    PASSWORD = 'Greenballs123'
    SEARCH = 'Welcome to email'
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

    print("[Info] - Logging in...")
    # emailAddress
    user_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div/span/form/span[1]/div/div[2]/div/div/input')))

    user_element.send_keys(USERNAME)

    # clickNext Button
    # nextButton = WebDriverWait(browser, TIMEOUT).until(
    #     EC.presence_of_element_located((
    #         By.XPATH, '//*[@id="login-signin"]')))
    #
    # nextButton.click()
    # time.sleep(3)

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
    browser.maximize_window()
    # searchEmail
    search_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="mail-search"]/div/div/div[1]/ul/li/div/div/input[1]')))

    search_element.send_keys(SEARCH)

    search_button = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="mail-search"]/div/button')))

    time.sleep(0.4)

    search_button.click()

    # Read the email
    read_mail = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="mail-app-component"]/div/div/div/div[3]/div/div/div[2]/div/div[1]/ul/li[2]/a')))

    time.sleep(0.4)

    read_mail.click()
    # Take a screenshot of the Page and store it for analysis.
    image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='yahootest.png')
    time.sleep(3)
    screenshot = Image.open('yahootest.png')
    screenshot.show()

    # Condition Logic, If the text searched is there open email and report success. (Optional as one can take a look at the screenshots)
    # Option to log the info in  a seperate file can be explored.


if __name__ == '__main__':
    jobblissLogin()
