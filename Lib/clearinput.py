# from importlib.machinery import SourceFileLoader
# clearinput = SourceFileLoader('getclearinputfile', '../Lib/clearinput.py').load_module()
# clearinput.clear_input_field(driver, selector='input#selector')

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def clear_input_field(driver, selector):
    input_field = driver.find_element(By.CSS_SELECTOR, selector)
    input_field_len = len(input_field.get_attribute('value'))
    counter = 0
    while counter < input_field_len:
        input_field.send_keys(Keys.BACKSPACE)
        counter += 1
    print(' - Input field input cleared')
