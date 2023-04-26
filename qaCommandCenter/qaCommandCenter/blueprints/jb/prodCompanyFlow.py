from asyncore import write
import os
import time
import selenium
import pyautogui
import logging
import infofeedtest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from PIL import Image
from Screenshot import *
import datetime
import csv
import parameters
import paths
import sendEmail
import renderResults



logging.basicConfig(filename='Company_Flow_log.txt', level=logging.DEBUG, format="%(asctime)s %(message)s",
                        filemode='w')
# Complete these variables ==================

USERNAME = 'anesuchiodza@yahoo.com'
PASSWORD = 'testCase123_'
SEARCH = '********'
TIMEOUT = 10

start_time = datetime.datetime.now()
print(start_time)

#LoginSeq.LoginToJobbliss.jobblissLogin()
#LoginSeq.ManagerLogin.jobblissLogin()
#LoginSeq.ContractorLogin.jobblissLogin()


# ==========================================
fscreenshot = Screenshot.Screenshot()
print("Login As a Company/Admin")



search_word_count = 'Passed'

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument("--log-level=3")
#options.add_argument("--headless")
options.add_argument("--kiosk")

browser = webdriver.Chrome(executable_path=CM().install(), options=options)
#LoginToCompany
browser.get(parameters.prodsigninlink)

print("[Info] - Logging in process in progress...")
    # emailAddress
user_element = WebDriverWait(browser, TIMEOUT).until(
    EC.presence_of_element_located((
        By.NAME, 'email')))

user_element.send_keys(parameters.adminUsername)

#time.sleep(5)


# PassWord
passWed = browser.find_element(By.XPATH, '//input[@id="password"]')

#pass_element.send_keys(PASSWORD)
passWed.send_keys(parameters.adminPass)

login_button = WebDriverWait(browser, TIMEOUT).until(
    EC.presence_of_element_located((
        By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/div/span/form/div[1]/div/button')))

time.sleep(0.4)

login_button.click()

time.sleep(10)

browser.get('https://app.jobbliss.com/dashboard')
try:
    #check if we have actually got in on the site since you can not access dashboard without logging in. Element to be located is the dashbord text "Dashboard"
    elem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/main/div[1]/ul/li/span[2]'))
        # Take a screenshot of the Page and store it for analysis.
    
    )
    image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='CompanyLoggedIn.png')
    time.sleep(3)

    #data
    header = ['Test Case','State','Date']
    timenow=datetime.datetime.now()
    data = ['Company Login','Passed',{timenow}]

    with open('prodAutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)

        time.sleep(3)
    print("Logged In As a Company/Admin Successfully")
except (NoSuchElementException, TimeoutException) as le:
    print(le)
    data = ['Company Login','Failed',{datetime.datetime.now()}]

    with open('prodAutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(data)

        time.sleep(3)

finally:
    
    print('Login Process Complete..Testing Uploading of Documents a Company...')  

#Uploading Documents
try:
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
    #data = ['Upload_Document','Passed',{datetime.datetime.now()}]

    with open('prodAutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(data)

        time.sleep(3)
    #Locating uploaded documentC:\Users\anesu_velocityinc\PycharmProjects\Automations\emailLogin.py

except (NoSuchElementException, TimeoutException):
    print('Failed to upload document')
    data = ['Upload_Document','Failed']

    with open('prodAutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(data)

        time.sleep(3)


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
    data = ['Upload_Document','Passed']

    with open('prodAutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)

except (NoSuchElementException, TimeoutException):
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
    data = ['Upload_Document', 'Failed']

    with open('prodAutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)



finally:
    print('Completed uploading of documents process')


#Adding Notes to a Contactractor or resource

# # clickCompanyResources
time.sleep(10)
try:
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

    #searchPerson

    searchPerson = WebDriverWait(browser,TIMEOUT).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/main/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div/input')))
    searchPerson.send_keys('StriveTWO Contractor')
    time.sleep(10)
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
            '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/main/section/div/div/div/div[2]/div[2]/div/nav/a[6]')))

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
    data = ['Write_Notes','Passed']

    with open('prodAutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)

    time.sleep(3)

except (NoSuchElementException, TimeoutException):
    data = ['Write_Notes','Failed']

    with open('prodAutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)

        time.sleep(3)

#Delete note
try:
    DeleteNotes_button = WebDriverWait(browser, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, '//*[@id="6b827f22-65e8-464e-a9a0-9e6c9f6876f3"]/div/div/div/div[3]/div/div/div/div[3]/div[2]/div/a[2]/p')))
    DeleteNotes_button.click()

    image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='addNotes.png')
    time.sleep(3)
    #screenshot = Image.open('addNotes.png')

    #Write the notes.
    confirmDeleteNotes = WebDriverWait(browser, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, '//*[@id="vueConfirm"]/div/div/button[2]')))
    confirmDeleteNotes.click()
        

    time.sleep(4)
    data = ['Delete_Notes','Passed']

    with open('prodAutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        

        writer.writerow(data)

        time.sleep(3)

except (NoSuchElementException, TimeoutException):
    data = ['Delete_Notes','Failed']

    with open('prodAutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(data)

        time.sleep(3)
# clickCompanyResources

# CompanyResources_button = WebDriverWait(browser, TIMEOUT).until(
#     EC.presence_of_element_located((
#         By.XPATH,
#         '//*[@id="app"]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/nav/div[2]/div/details/summary')))

# time.sleep(0.4)

#CompanyResources_button.click()

time.sleep(1)
#CompanyDatabase
try:
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

    #Remove Contractor From Company

    removefromCo_button = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH,
            '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/main/section/div/div/div/div[1]/div/div[2]/div[1]/div/button')))

    time.sleep(0.4)

    removefromCo_button.click()
    time.sleep(3)

    #ConfirmRemove
    confirm_remove_button = WebDriverWait(browser, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[3]/div/div[2]/form/div[1]/div[3]/div[2]/div/button')))
    confirm_remove_button.click()

    image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='removeContractorFromCompany.png')
    time.sleep(3)
    screenshot = Image.open('removeContractorFromCompany.png')
    #Log in CSV
    
    #data
    data = ['Remove_Contractor_From_Company','Passed']

    with open('prodAutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(data)

    time.sleep(3)
    print('Contractor removed Successfully!')

    time.sleep(3)
except (NoSuchElementException, TimeoutException):
    data = ['Remove_Contractor_From_Company','Failed']

    with open('prodAutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(data)

    time.sleep(3)

#Switch Package

browser.get('https://app.jobbliss.com/dashboard')

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


    #data
    data = ['Switch Subscription Package','Passed']

    with open('prodAutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        

        writer.writerow(data)

        time.sleep(3)

except (NoSuchElementException, TimeoutException):
    #data
    data = ['Switch Subscription Package','Failed']

    with open('prodAutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)

        time.sleep(3)

finally:
    print('Done')


# clickManage
try:
    clickManage_button = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH,
            '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/nav/div[4]/div/details/summary/span')))

    time.sleep(0.4)

    clickManage_button.click()

    time.sleep(1)
    #Managers
    manager_button = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH,
            '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/nav/div[4]/div/details/div[1]')))

    time.sleep(0.4)

    manager_button.click()
    searchManager = WebDriverWait(browser,TIMEOUT).until(EC.presence_of_element_located((By.XPATH,paths.searchmanagerfilter)))
    searchManager.send_keys('Tyler Prod Manager')
    time.sleep(5)

    viewprofile_button = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH,
            '//*[@id="app"]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/main/div[2]/div/div[1]/div/div/div[2]/div[1]/div[2]/div/div[2]/a/div/div/button/span')))

    time.sleep(0.4)

    viewprofile_button.click()
    time.sleep(3)

    disableprofile_button = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH,
            '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/main/section/div/div/div/div[1]/div/div[2]/div[1]/div/button')))

    time.sleep(0.4)

    disableprofile_button.click()
    time.sleep(3)
    #ConfirmDisable
    confirm_disable_button = WebDriverWait(browser, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div/button[2]')))
    confirm_disable_button.click()
    time.sleep(5)
    # DeleteManager
    deleteMgr_button = WebDriverWait(browser, TIMEOUT).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/main/section/div/div/div/div[1]/div/div[2]/div[2]/div/button')))
    deleteMgr_button.click()
    time.sleep(5)
    # DeleteManagerConfirm
    deleteMgrConfirm_button = WebDriverWait(browser, TIMEOUT).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div/button[2]')))
    deleteMgrConfirm_button.click()

    data = ['Delete_Manager','Passed']

    with open('prodAutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)

        time.sleep(3)
except(NoSuchElementException, TimeoutException):
    data = ['Delete_Manager','Failed']

    with open('prodAutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)

        time.sleep(3)

#Invite Contractor/Company Database

browser.get(parameters.proddbview)
browser.maximize_window()

try:
    #try this block first
    elemupload = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, paths.uploadContractor))     
    )
    elemupload.click()

    emailCont = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, paths.emailContractor))     
    )
    emailCont.send_keys(parameters.contractorEmail)

    fname = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, paths.fnameContractor))     
    )
    fname.send_keys(parameters.fnameContractor)

    lname = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, paths.lnameContractor))     
    )
    lname.send_keys(parameters.lnameContractor)
    time.sleep(10)
    addContr = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, paths.invitecontractor))     
    )
    addContr.click()


    image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='dataBase.png')
    time.sleep(3)
    #data
    data = ['inviteContractor','Passed']

    with open('prodAutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)

        time.sleep(3)
#catch exception
except:
    #now try this block 
    elemupload = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, paths.uploadContractor))     
    )
    elemupload.click()

    emailCont = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, paths.emailContractor))     
    )
    emailCont.send_keys(parameters.contractorEmail)

    fname = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, paths.fnameContractor))     
    )
    fname.send_keys(parameters.fnameContractor)

    lname = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, paths.lnameContractor))     
    )
    lname.send_keys(parameters.lnameContractor)

    time.sleep(10)

    addContr = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, paths.invitecontractor))     
    )
    addContr.click()


    image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='dataBase.png')
    time.sleep(3)

    #data
    data = ['inviteContractor','Passed']

    with open('prodAutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        time.sleep(3)

else:
    
    data = ['inviteContractor','Failed']
    with open('prodAutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(data)

        time.sleep(3)
    #check if we have actually got in on the site since you can not access dashboard without logging in. Element to be located is the dashbord text "Dashboard"
    
finally:
    #browser.quit()  
    print('script done running.. on to the next, please check results to understand status of test..')  


#Create Group
time.sleep(10)

browser.get(parameters.groupsLink)

try:
    #check if we have actually got in on the site since you can not access dashboard without logging in. Element to be located is the dashbord text "Dashboard"
    elemCreateGroup = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, paths.createGroup))     
    )
    elemCreateGroup.click()

    groupName = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, paths.group_name))     
    )
    groupName.send_keys(parameters.groupName)

    createGroup = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, paths.createButton))     
    )
    createGroup.click()


    image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='CompanyLoggedIn.png')
    time.sleep(3)


    #data
    data = ['GroupCreation','Passed']

    with open('prodAutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(data)

        time.sleep(3)
    print("Group creation Successful")
except:
    elemCreateGroup = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, paths.createGroupA))
        # Take a screenshot of the Page and store it for analysis.
    
    )
    elemCreateGroup.click()

    groupName = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, paths.group_name))     
    )
    groupName.send_keys(parameters.groupName)

    createGroup = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, paths.createButton))     
    )
    createGroup.click()

    image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='CompanyLoggedIn1.png')
    time.sleep(3)


    #data
    data = ['Create_Group','Passed']

    with open('prodAutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(data)

        time.sleep(3)
    print("Logged In As a Company/Admin Successfully")

    print('Failed to Execute')
else:
    
    data = ['Create Group Button Click','Failed']
    with open('prodAutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)


        writer.writerow(data)

        time.sleep(3)
    #check if we have actually got in on the site since you can not access dashboard without logging in. Element to be located is the dashbord text "Dashboard"
    
finally:
    #browser.quit()  
    print('script done running.. on to the next, please check results to understand status of test..')  


time.sleep(3)

# opening text file in read only mode
file = open("./prodAutomationQA_Summary.csv", "r")


# reading data of the file
read_data = file.read()
per_word = read_data.split()

total =len(per_word)
print(total)
print(per_word)

num_rows = 0

for row in open("./prodAutomationQA_Summary.csv"):
    num_rows += 1


# converting data in lower case and the counting the occurrence 
word_count = read_data.count(search_word_count)

reader = csv.reader(file)
linecount= len(list(reader))


# printing word and it's count
print(f"The word '{search_word_count}' appeared {word_count} times.")
linecount=num_rows-1
percentageresult = (word_count/linecount)*100

print(f"'{percentageresult}' %" )

if percentageresult<85:
    print("The test has failed")

else:
    print('We have the Go Ahead with P2 Tests')

end_time = datetime.datetime.now()
print(start_time)
print(end_time)

timediff = end_time - start_time

print(timediff)

print(f"Total time taken to execute the script is {timediff.total_seconds()} seconds")
inMinutes = timediff/60
print(inMinutes)

ms = timediff.total_seconds() * 1000
print(f"Total time taken to execute the script is {inMinutes} minutes")

lines = [f"We have {word_count} test cases that passed.", f" Percentage pass-rate is '{percentageresult}' %" , f"The total time taken to execute the test cases is {inMinutes} seconds"]
with open('emailContent.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

infofeedtest.results()
renderResults.renderresults()
