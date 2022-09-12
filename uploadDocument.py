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



def uploadDoc():
    logging.basicConfig(filename='LoginToJobbliss_log.txt', level=logging.DEBUG, format="%(asctime)s %(message)s",
                        filemode='w')
    # Complete these 2 fields ==================
    #USERNAME = 'anesu+contractor@velocityinc.tech'
    #PASSWORD = 'Greenballs123'
    USERNAME = 'anesuchiodza@yahoo.com'
    PASSWORD = 'testCase123_'
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

    # clickDocuments

    clickdoc_button = WebDriverWait(browser, TIMEOUT).until(
         EC.presence_of_element_located((
             By.XPATH,
             '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/nav/div[6]/div/details/summary/span')))

    time.sleep(0.4)

    clickdoc_button.click()
    
    time.sleep(1)

    docall_button = WebDriverWait(browser, TIMEOUT).until(
         EC.presence_of_element_located((
             By.XPATH,
             '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/nav/div[6]/div/details/div[1]/a/span')))

    time.sleep(0.4)

    docall_button.click()

    upload_button = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH,
            '//*[@id="uploadFile"]')))

    time.sleep(0.4)

    upload_button.click()
    time.sleep(3)

    pyautogui.write('C:\\Users\\anesu_velocityinc\\PycharmProjects\\Automations\\requirements.txt')
    
    time.sleep(3)
    pyautogui.press('enter')
    
    time.sleep(3)
    print('Document Uploaded Successfully!')
    print('Good Bye!')
    time.sleep(3)
    browser.close()
   

    #c.stop()

# Documents xpath
# /html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/nav/div[6]/div/details/summary/span/span[2]
if __name__ == '__main__':
    uploadDoc()
