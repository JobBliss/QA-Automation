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



def emailLogin():
    # Complete these fields ==================
    USERNAME = 'anesuchiodza'
    PASSWORD = 'zipassW0rd123!'
    SUBJECT = 'P1 Automation Results'
    EMAIL_TO = 'anesu@velocityinc.tech'
    MessageBody = ''
    # ==========================================
    fscreenshot = Screenshot.Screenshot()


    TIMEOUT = 10

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=3")

    browser = webdriver.Chrome(executable_path=CM().install(), options=options)

    browser.get(
        'https://login.yahoo.com/?.src=ym&pspid=2023538075&activity=ybar-mail&.lang=en-US&.intl=us&.done=https%3A%2F%2Fmail.yahoo.com%2Fd%2F%3Fpspid%3D2023538075%26activity%3Dybar-mail')

    time.sleep(2)
    browser.maximize_window()

    print("[Info] - Logging in...")
    # emailAddress
    user_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="login-username"]')))

    user_element.send_keys(USERNAME)

    # clickNext Button
    nextButton = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="login-signin"]')))

    nextButton.click()
    time.sleep(3)

    # PassWord
    pass_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="login-passwd"]')))

    pass_element.send_keys(PASSWORD)

    login_button = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="login-signin"]')))

    time.sleep(0.4)

    login_button.click()

    time.sleep(5)
    browser.maximize_window()
    # searchEmail
    compose_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="app"]/div[2]/div/div[1]/nav/div/div[1]/a')))

    compose_element.click()

    emailTo = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="message-to-field"]')))

    time.sleep(0.4)

    emailTo.send_keys(EMAIL_TO)


    subjectElement = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="mail-app-component"]/div/div/div/div[1]/div[3]/div/div/input')))

    time.sleep(0.4)

    subjectElement.send_keys(SUBJECT)

    #
    setting_data = open('emailContent.txt', 'r')
    lining = setting_data.readlines()
    limited_n_ints = ''
    for i in lining:
        limited_n_ints = limited_n_ints + i
        
    MessageBody = limited_n_ints

    messageComposer = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH , '//*[@id="editor-container"]/div[1]')))

    messageComposer.send_keys(MessageBody)

    time.sleep(3)

    #//*[@id="mail-app-component"]/div/div/div/div[2]/div[2]/div/button

    sendMsg = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH , '//*[@id="mail-app-component"]/div/div/div/div[2]/div[2]/div/button')))

    sendMsg.click()

    time.sleep(5)

    print('Email sent')

    

    # Take a screenshot of the Page and store it for analysis.
   

if __name__ == '__main__':
    emailLogin()
