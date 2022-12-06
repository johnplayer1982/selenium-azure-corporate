from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, os
from dotenv import load_dotenv
load_dotenv()

def authuser(driver):

    # Fetch username and password from .env
    username = os.getenv('TEST_USERNAME')
    password = os.getenv('TEST_PASSWORD')

    time.sleep(2)
    print(' - Pausing for a moment to allow the test login form to load')

    try:
        driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys(username)
        driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys(password)
        driver.find_element(By.CSS_SELECTOR, 'button#submit-button').click()
        print(' - Authenticated on the test environment')
    except:
        print(' - Something went wrong logging in to test')
    return
