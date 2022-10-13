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




logging.basicConfig(filename='Company_Flow_log.txt', level=logging.DEBUG, format="%(asctime)s %(message)s",
                        filemode='w')
# Complete these variables ==================
#USERNAME = 'anesu+contractor@velocityinc.tech'
#PASSWORD = 'Greenballs123'
USERNAME = 'anesuchiodza@yahoo.com'
PASSWORD = 'testCase123_'
SEARCH = '********'
TIMEOUT = 10


# ==========================================
fscreenshot = Screenshot.Screenshot()
print("Login As a Company/Admin")




options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument("--log-level=3")
#options.add_argument("--headless")
options.add_argument("--kiosk")

browser = webdriver.Chrome(executable_path=CM().install(), options=options)
#LoginToCompany
browser.get(
    'https://alpha.jobbliss.com/signin')

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
    image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='CompanyLoggedIn.png')
    time.sleep(3)

    header = ['Test Name', 'State']

    #data
    data = ['Company Login' 'Passed']

    with open('AutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(header)

        writer.writerow(data)

        time.sleep(3)
    print("Logged In As a Company/Admin Successfully")
finally:
    
    print('Login Complete..Testing Uploading of Documents a Company...')  

#Uploading Documents

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

pyautogui.write('C:\\Users\\anesu_velocityinc\\PycharmProjects\\Automations\\emailLogin.py')

time.sleep(3)
pyautogui.press('enter')

time.sleep(5)
print('Document Uploaded Successfully!')
time.sleep(3)
print('Searching for uploaded document .........................')
#Locating uploaded document
#
try:
    search_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.NAME, 'input_filter')))

    search_element.send_keys('emailLogin.py')

    #click on search

    search_button = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH,
            '//*[@id="app"]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/main/div[2]/div/div[1]/div/div[1]/form/div[2]/div/button')))

    time.sleep(0.4)

    search_button.click()
    time.sleep(6)
    image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='UploadedDocument.png')
    time.sleep(3)


    print('...............')

    print('....... Document Found ......')
    time.sleep(0.4)
    

    #data
    data = ['Upload Document' 'Passed']

    with open('AutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)

except:
    search_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.NAME, 'input_filter')))

    search_element.send_keys('emailLogin.py')

    #click on search

    search_button = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH,
            '//*[@id="app"]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/main/div[2]/div/div[1]/div/div[1]/form/div[2]/div/button')))

    time.sleep(0.4)

    search_button.click()
    time.sleep(6)
    image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='UploadedDocumentFail.png')
    time.sleep(3)


    print('...............')

    print('....... Document Not Found ......')
    time.sleep(0.4)
    

    #data
    data = ['Upload Document', 'Failed']

    with open('AutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)



finally:
    print('Completed uploading of documents')


#Adding Notes to a Contactractor or resource

# # clickCompanyResources
time.sleep(10)
CompanyResources_button = WebDriverWait(browser, TIMEOUT).until(
    EC.presence_of_element_located((
        By.XPATH,
        '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/nav/div[2]/div/details/summary/span')))

time.sleep(0.4)

CompanyResources_button.click()

time.sleep(1)
#CompanyDatabase
companyDb_button = WebDriverWait(browser, TIMEOUT).until(
    EC.presence_of_element_located((
        By.XPATH,
        '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/nav/div[2]/div/details/div[1]/a/span')))

time.sleep(0.4)

companyDb_button.click()

#viewProfile
viewprofile_button = WebDriverWait(browser, TIMEOUT).until(
    EC.presence_of_element_located((
        By.XPATH,
        '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/main/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div/button')))

time.sleep(0.4)

viewprofile_button.click()
time.sleep(3)

#

notesTab = WebDriverWait(browser, TIMEOUT).until(
    EC.presence_of_element_located((
        By.XPATH,
        '//*[@id="6b827f22-65e8-464e-a9a0-9e6c9f6876f3"]/div/div/div/div[2]/div[2]/div/nav/a[6]')))

time.sleep(0.4)

notesTab.click()
time.sleep(3)

#AddNotes Button Click
addNotes_button = WebDriverWait(browser, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, '//*[@id="6b827f22-65e8-464e-a9a0-9e6c9f6876f3"]/div/div/div/div[3]/div/div/div/div[1]/div/div/button')))
addNotes_button.click()

image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='addNotes.png')
time.sleep(3)
#screenshot = Image.open('addNotes.png')

#Write the notes.
NotesWrite = WebDriverWait(browser, TIMEOUT).until(EC.presence_of_element_located((By.ID, 'newNote')))

NotesWrite.send_keys('Imweo Information Here!')

addNote_button = WebDriverWait(browser, TIMEOUT).until(EC.presence_of_element_located((By.ID, 'addNote')))
addNote_button.click()

time.sleep(3)
print('notes Written Successfully!')
time.sleep(3)

browser.get(
    'https://alpha.jobbliss.com/dashboard')

# clickCompanyResources

CompanyResources_button = WebDriverWait(browser, TIMEOUT).until(
    EC.presence_of_element_located((
        By.XPATH,
        '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/nav/div[2]/div/details/summary/span')))

time.sleep(0.4)

CompanyResources_button.click()

time.sleep(1)
#CompanyDatabase
companyDb_button = WebDriverWait(browser, TIMEOUT).until(
    EC.presence_of_element_located((
        By.XPATH,
        '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/nav/div[2]/div/details/div[1]/a/span')))

time.sleep(0.4)

companyDb_button.click()

viewprofile_button = WebDriverWait(browser, TIMEOUT).until(
    EC.presence_of_element_located((
        By.XPATH,
        '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/main/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div/button')))

time.sleep(0.4)

viewprofile_button.click()
time.sleep(3)

removefromCo_button = WebDriverWait(browser, TIMEOUT).until(
    EC.presence_of_element_located((
        By.XPATH,
        '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/main/section/div/div/div/div[1]/div/div[2]/div[1]/div/button')))

time.sleep(0.4)

removefromCo_button.click()
time.sleep(3)

#ConfirmRemove
confirm_remove_button = WebDriverWait(browser, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[3]/div/div[2]/form/div[1]/div[3]/div[2]/div/button')))
confirm_remove_button.click()

image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='removeContractorFromCompany.png')
time.sleep(3)
screenshot = Image.open('removeContractorFromCompany.png')
#Log in CSV
eader = ['Test Name', 'State']

#data
data = ['Remove Contractor From Company' 'Passed']

with open('AutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    #writer.writerow(header)

    writer.writerow(data)

time.sleep(3)
print('Contractor removed Successfully!')

time.sleep(3)

#Switch Package

browser.get('https://alpha.jobbliss.com/dashboard')

try:
    #check if we have actually got in on the site since you can not access dashboard without logging in. Element to be located is the dashbord text "Dashboard"
    elem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/main/div[1]/ul/li/span[2]'))
        # Take a screenshot of the Page and store it for analysis.
    
    )
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

    clickYes = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[3]/div/div[2]/div[3]/form/div[2]/div[1]/div/button')))

    clickYes.click()


    # Take a screenshot of the Page and store it for analysis.
    image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='SuccessFullCreation.png')
    time.sleep(3)
    screenshot = Image.open('SuccessFullCreation.png')
    get_url = browser.current_url
    print("You are now on :"+str(get_url))
    print("You have successfully Created and completed setting up your profile")
    # screenshot.show()
    image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='CompanyLoggedIn.png')
    time.sleep(3)

    header = ['Test Name', 'State']

    #data
    data = ['Switch Subscription Package' 'Passed']

    with open('AutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        #writer.writerow(header)

        writer.writerow(data)

        time.sleep(3)
finally:
    print('Done')





