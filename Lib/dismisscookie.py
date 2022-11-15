import time
from selenium.webdriver.common.by import By

def dismissCookieBanner(driver):
    time.sleep(1)
    
    try:
        cookie_modal = driver.find_element(By.CSS_SELECTOR, 'div.t-cookie-consent-modal')
        cookie_modal_btns = cookie_modal.find_elements(By.CSS_SELECTOR, "button.t-button")
        cookie_modal_btns[2].click()
        print(' - Cookie modal dismissed')
    except:
        print(' - Cookie banner not found, either previously dismissed or testing on test environment')
        pass
