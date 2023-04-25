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
import parameters
import csv
import cv2
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import imutils
from imgcompare import is_equal, image_diff_percent
from PIL import Image


logging.basicConfig(filename='Company_Flow_log.txt', level=logging.DEBUG, format="%(asctime)s %(message)s",
                        filemode='w')
# Complete these variables ==================

USERNAME = 'eunice@velocityinc.tech'
PASSWORD = 'Velocity'
SEARCH = '********'
TIMEOUT = 10

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

time.sleep(2)

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
    time.sleep(7)

    #get the images you want to compare.
    original = cv2.imread("CompanyLoggedInControl.png")
    new = cv2.imread("CompanyLoggedIn.png")
    #resize the images to make them small in size. A bigger size image may take a significant time
    #more computing power and time
    original = imutils.resize(original, height = 600)
    new = imutils.resize(new, height = 600)

    #create a copy of original image so that we can store the
    #difference of 2 images in the same on
    diff = original.copy()
    cv2.absdiff(original, new, diff)

    # converting the difference into grayscale images
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # increasing the size of differences after that we can capture them all
    for i in range(0, 3):
        dilated = cv2.dilate(gray.copy(), None, iterations=i + 1)


    (T, thresh) = cv2.threshold(dilated, 3, 255, cv2.THRESH_BINARY)

    # now we have to find contours in the binarized image
    cnts = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)


    for c in cnts:
        # nicely fiting a bounding box to the contour
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(new, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # remove comments from below 2 lines if you want to
        # for viewing the image press any key to continue
        # simply write the identified changes to the disk
    cv2.imwrite("testchanges.png", new)
    image1 = Image.open("CompanyLoggedInControl.png")
    image2 = Image.open("CompanyLoggedIn.png")
    new_image = image1.resize((1789, 795)).convert('RGB')
    new_image2 = image2.resize((1789, 795)).convert('RGB')


    new_image.save('myimage_1.jpg')
    new_image2.save('myimage_2.png')
    time.sleep(5)


    is_same = is_equal(new_image, new_image2, tolerance=1)
    percentage = image_diff_percent('myimage_1.jpg', 'myimage_2.png')
    print(is_same)
    print(percentage,'% difference')

    #data
    header = ['Test Case' 'State']
    data = ['Company Login' 'Passed']

    with open('AutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)

        time.sleep(3)
    print("Logged In As a Company/Admin Successfully")
except (NoSuchElementException, TimeoutException) as le:
    print(le)
    data = ['Company Login' 'Failed' '{le}']

    with open('AutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(data)

        time.sleep(3)

finally:
    
    print('Login Process Complete..Testing Uploading of Documents a Company Now...')  
