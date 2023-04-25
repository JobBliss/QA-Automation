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

def qaTest():
    # Complete these 3 fields ==================
    USERNAME = 'anesuchiodza@gmail.com'
    PASSWORD = 'zipassW0rd123!'
    SEARCH = 'Verify My Account'
    # ==========================================
    #fscreenshot = Screenshot.Screenshot()


    TIMEOUT = 10

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=3")

    browser = webdriver.Chrome(executable_path=CM().install(), options=options)

    browser.get(
        'https://www.browserstack.com/test-university')

    time.sleep(2)

    print("[Info] - Logging in...")


    # # click SIgn In Button
    signInButton = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="signinFormLink"]')))

    signInButton.click()
    # time.sleep(3)
    #ENter Email

    user_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="user_email_login"]')))

    user_element.send_keys(USERNAME)

    # Enter PassWord
    pass_element = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="user_password"]')))

    pass_element.send_keys(PASSWORD)
    #
    login_button = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.ID, 'user_submit')))

    time.sleep(0.4)
    #
    login_button.click()
    #
    # time.sleep(5)
    # browser.maximize_window()
    # # searchEmail
    # search_element = WebDriverWait(browser, TIMEOUT).until(
    #     EC.presence_of_element_located((
    #         By.XPATH, '//*[@id="mail-search"]/div/div/div[1]/ul/li/div/div/input[1]')))
    #
    # search_element.send_keys(SEARCH)
    #
    # search_button = WebDriverWait(browser, TIMEOUT).until(
    #     EC.presence_of_element_located((
    #         By.XPATH, '//*[@id="mail-search"]/div/button')))
    #
    # time.sleep(0.4)
    #
    # search_button.click()
    #
    # # Read the email // to be changed to pick link (this is specific to path and the test case l have for now, not sustainable)
    # read_mail = WebDriverWait(browser, TIMEOUT).until(
    #     EC.presence_of_element_located((
    #         By.LINK_TEXT("Thank you for registering with JobBliss").click())))
    #
    # time.sleep(3)
    #
    # #read_mail.click()
    # time.sleep(2)
    #
    # click_verify = WebDriverWait(browser, TIMEOUT).until(
    #     EC.presence_of_element_located((
    #         By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[4]/ul/li/div/div[2]/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/table/tbody/tr/td')))
    #
    # time.sleep(0.4)
    #
    # click_verify.click()

    # Take a screenshot of the Page and store it for analysis.
    # image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='emailSending.png')
    time.sleep(20)
    # screenshot = Image.open('emailSending.png')
    # screenshot.show()

    # Condition Logic, If the text searched is there open email and report success. (Optional as one can take a look at the screenshots)
    # Option to log the info in  a seperate file can be explored.


if __name__ == '__main__':
    qaTest()
