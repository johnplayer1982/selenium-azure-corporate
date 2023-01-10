from importlib.machinery import SourceFileLoader
from selenium.webdriver.common.by import By
import requests

# Selectors
global_selectors = SourceFileLoader('getsselectors', '../Selectors/selectors.py').load_module()
selectors = global_selectors.get_selector()

# Styles

button_container_styles = {
    'padding' : '10px',
}

button_inner_container_styles = {
    'margin-top' : '20px',
}

primary_button_styles = {
    "display" : "block",
    "margin" : "0px",
    "padding" : "0px",
}

secondary_button_styles = {
    "display" : "block",
    "margin" : "0px",
    "padding" : "0px",
}

def check_styles(driver, selector, styles, description):
    stylechecker = SourceFileLoader('getstylechecker', '../Lib/stylechecker.py').load_module()
    element = driver.find_element(By.CSS_SELECTOR, selector)
    styles = stylechecker.checkstyle(
        element,
        styles,
        description
    )

def runTest(baseUrl, driver, browser, devmode):

    # Component URLs - Where to find the component
    component_urls = [
        f"{baseUrl}/content/maps/mps/en/jp-test/mps-double-column.html?wcmmode=disabled"
    ]

    for url in component_urls:
        driver.get(url)

        buttons = driver.find_elements(By.CSS_SELECTOR, selectors['button_container_selector'])
        buttons_len = len(buttons)
        print(f' - {buttons_len} buttons found')
        
        primary_buttons = driver.find_elements(By.CSS_SELECTOR, selectors['primary_button_selector'])
        primary_buttons_len = len(primary_buttons)
        print(f' - {primary_buttons_len} are primary buttons')

        secondary_buttons = driver.find_elements(By.CSS_SELECTOR, selectors['secondary_button_selector'])
        secondary_buttons_len = len(secondary_buttons)
        print(f' - {secondary_buttons_len} are secondary buttons')

        if len(buttons):
            for button in buttons:
                check_styles(driver, selector=selectors['button_container_selector'], styles=button_container_styles, description='Button Container')
                check_styles(driver, selector=selectors['button_inner_container_selector'], styles=button_inner_container_styles, description='Button Inner Container')

        if len(primary_buttons):
            for primary_button in primary_buttons:
        
                # Comment describing the element
                check_styles(driver, selector=selectors['primary_button_selector'], styles=primary_button_styles, description='Primary Button')

                primary_button_span = primary_button.find_element(By.CSS_SELECTOR, 'span')
                
                assert primary_button_span.value_of_css_property('border-radius') == "25px"
                assert "29, 82, 138" in primary_button_span.value_of_css_property('background-color')
                assert "255, 255, 255" in primary_button_span.value_of_css_property('color')
                assert primary_button_span.value_of_css_property('font-size') == "19px"
                print(' - Primary button styles ok')

                primary_button_href = primary_button.get_attribute('href')
                if not devmode:
                    primary_button_href_status = requests.get(primary_button_href).status_code
                    if not primary_button_href_status == 200:
                        error = "> Primary button on page does not resolve 200"
                        raise AssertionError(error)
            
        if len(secondary_buttons):
            for secondary_button in secondary_buttons:
                # Comment describing the element
                check_styles(driver, selector=selectors['secondary_button_selector'], styles=secondary_button_styles, description='Secondary Button')

                secondary_button_span = secondary_button.find_element(By.CSS_SELECTOR, 'span')
                
                assert secondary_button_span.value_of_css_property('border-radius') == "25px"
                assert "0, 0, 0" in secondary_button_span.value_of_css_property('background-color')
                assert "29, 82, 138" in secondary_button_span.value_of_css_property('color')
                assert secondary_button_span.value_of_css_property('font-size') == "19px"
                print(' - Secondary button styles ok')

                secondary_button_href = secondary_button.get_attribute('href')
                if not devmode:
                    secondary_button_href_status = requests.get(secondary_button_href).status_code
                    if not secondary_button_href_status == 200:
                        error = "> Secondary button on page does not resolve 200"
                        raise AssertionError(error)

        else:
            print(' - Component not found')
