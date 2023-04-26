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
from LoginToJobbliss import *


def jobblissCompleteCompanySetup():
    logging.basicConfig(filename='Createcompany_log.txt', level=logging.DEBUG, format="%(asctime)s %(message)s",
                        filemode='w')
    # Complete these fields ==================
    CARDNO = '4242424242424242'
    EXPIRY = '0625'
    CVV = '656'
    ZIP = '26333'

    # ==========================================
    fscreenshot = Screenshot.Screenshot()

    TIMEOUT = 10

    options = webdriver.ChromeOptions()
    options.add_argument("--kiosk")
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=3")

    browser = webdriver.Chrome(executable_path=CM().install(), options=options)
    # LoginToCompany
    
    # clickPackage Button

    profilePackage = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/nav/div/div/div/div[3]/div[1]/div[1]')))

    profilePackage.click()
    #pricing Management path

    pricingManagement = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/nav/div/div/div/div[3]/div[2]/div[3]/span')))

    pricingManagement.click()



    clickPackage = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/main/div[2]/div/div[2]/div/div/div/div/div[3]/div/div/div/div[2]/div[2]/div/button')))

    clickPackage.click()
    time.sleep(3)
    
#----------------------------------------------------
#---Comment out this part since the package is card details are already loaded. 

#-- Come back to put logic of when the card details are not there ------

#-- Below code  helps you put your  company address and card details ----

    # Enter Company Email Address
    user_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH,
            '/html/body/div/form/div/div[2]/span[1]/span[2]/div/div[2]/span/input')))

    user_element.send_keys(CARDNO)

    # expiryofCard
    expiryOfCard_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH,
            '/html/body/div/form/div/div[2]/span[2]/span/span/input')))

    expiryOfCard_element.send_keys(EXPIRY)
    time.sleep(1)

    # Enter CVV
    lastname_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH,
            '/html/body/div/form/div/div[2]/span[3]/span/span/input')))

    lastname_element.send_keys(CVV)
    time.sleep(1)

    # ENTER ZIPCODE
    zip_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH,
            '/html/body/div/form/div/div[2]/span[4]/span/span/input')))

    zip_element.send_keys(ZIP)
    time.sleep(1)

    # ------------------
    # Business Info:
    # -----------------
    addCard_button = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div[2]/div/form/div[2]/div/div/button'
        )))
    print("Adding Card Now")

    addCard_button.click()

    time.sleep(3)

    # Take a screenshot of the Page and store it for analysis.
    image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='SuccessFullCreation.png')
    time.sleep(3)
    screenshot = Image.open('SuccessFullCreation.png')
    get_url = browser.current_url
    print("You are now on :"+str(get_url))
    print("You have successfully Created and completed setting up your profile")
    # screenshot.show()


if __name__ == '__main__':
    jobblissLogin()
    jobblissLogin().browser.execute_script('''window.open("https://alpha.jobbliss.com/dashboard","_blank");''')
    jobblissCompleteCompanySetup()
