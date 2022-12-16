from importlib.machinery import SourceFileLoader
from selenium.webdriver.common.by import By
import requests

# Lib
resize = SourceFileLoader('getresize', '../Lib/resize.py').load_module()

# Selectors
global_selectors = SourceFileLoader('getsselectors', '../Selectors/selectors.py').load_module()
selectors = global_selectors.get_selector()

# Styles
header_styles = {
    "padding" : "10px",
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
        resize.resizeDesktop(driver)
        headers = driver.find_elements(By.CSS_SELECTOR, selectors['header_selector'])

        if len(headers):
            for header in headers:
                check_styles(driver, selector=selectors['header_selector'], styles=header_styles, description='Header')

                # Logo
                print(' - Checking Logo')
                logo_container = driver.find_element(By.CSS_SELECTOR, selectors['logo_container_selector'])
                logo_links = driver.find_elements(By.CSS_SELECTOR, selectors['logo_link_selector'])
                logo_image = driver.find_element(By.CSS_SELECTOR, selectors['logo_image_selector'])

                assert logo_container and logo_links and logo_image
                print('  + Logo container, link and image elements found')

                logo_link_href = logo_links[1].get_attribute('href')
                logo_link_status = requests.get(logo_link_href).status_code
                if not devmode:
                    assert logo_link_status == 200
                    print(f' - Logo link status OK: {logo_link_status}')

        else:
            error = f"> Error: Header not found: {url}"
            raise AssertionError(error)
