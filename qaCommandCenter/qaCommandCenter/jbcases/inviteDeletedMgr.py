import os
import time
import selenium
from LoginToJobbliss import *
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
from uploadDocument import *


USERNAME = 'anesuchiodza@yahoo.com'
PASSWORD = 'testCase123_'

TIMEOUT=10
# Complete these fields ==================
CARDNO = '4242424242424242'
EXPIRY = '0625'
CVV = '656'
ZIP = '26333'

# ==========================================
fscreenshot = Screenshot.Screenshot()

logging.basicConfig(filename='LoginSeq_Log.txt', level=logging.DEBUG,
                    format="%(asctime)s %(message)s", filemode='w')
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument("--log-level=3")
#options.add_argument("--headless")
options.add_argument("--kiosk")

browser = webdriver.Chrome(executable_path=CM().install(), options=options)
#LoginToCompany
browser.get(
    'https://alpha.jobbliss.com/signin')



#time.sleep(20)
print("[Info] - Logging in process in progress...")
# emailAddress
user_element = WebDriverWait(browser, TIMEOUT).until(
    EC.presence_of_element_located((
        By.NAME, 'email')))

user_element.send_keys(USERNAME)

#time.sleep(5)


# PassWord
passWed = browser.find_element(By.XPATH, '//input[@id="password"]')

#pass_element.send_keys(PASSWORD)
passWed.send_keys(PASSWORD)

login_button = WebDriverWait(browser, TIMEOUT).until(
    EC.presence_of_element_located((
        By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/div/span/form/div[1]/div/button')))

time.sleep(0.4)

login_button.click()

time.sleep(10)

browser.get('https://alpha.jobbliss.com/dashboard')

try:
    #check if we have actually got in on the site since you can not access dashboard without logging in. Element to be located is the dashbord text "Dashboard"
    elem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/main/div[1]/ul/li/span[2]'))
        # Take a screenshot of the Page and store it for analysis.
    
    )
    inviteButton = WebDriverWait(browser, TIMEOUT).until(
    EC.presence_of_element_located((
        By.ID, 'inviteNewManager')))

    inviteButton.click()


    #emailField
    emailField = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.NAME, 'email0')))

    emailField.send_keys('achiodza74@gmail.com')

    nameField = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.NAME, 'csv_item_given_name')))

    nameField.send_keys('QAT')

    nameField = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.NAME, 'csv_item_family_name')))

    nameField.send_keys('Person')
    time.sleep(10)
    inviteMgr = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.ID, 'inviteManager')))

    inviteMgr.click()

    


    
    

   
   


    # Take a screenshot of the Page and store it for analysis.
    image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='SuccessInvitation.png')
    time.sleep(3)
   
   

    header = ['Test Name', 'State']

    #data
    data = ['Invite Deleted Manager' 'Passed']

    with open('AutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        #writer.writerow(header)

        writer.writerow(data)

        time.sleep(3)
    print("Invite Sent Successfully To a Previously Deleted Manager")

finally:
    #browser.quit()  
    print('Script done running.. on to the next, please check results to understand status of test..')  





