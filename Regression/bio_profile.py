from importlib.machinery import SourceFileLoader
from selenium.webdriver.common.by import By
import requests

style_warnings = []

# Selectors
global_selectors = SourceFileLoader('getsselectors', '../Selectors/selectors.py').load_module()
selectors = global_selectors.get_selector()

# Styles
bio_profile_styles = {
    "padding" : "20px",
}

def check_styles(driver, selector, styles, description):
    stylechecker = SourceFileLoader('getstylechecker', '../Lib/stylechecker.py').load_module()
    element = driver.find_element(By.CSS_SELECTOR, selector)
    styles = stylechecker.checkstyle(
        element,
        styles,
        description
    )
    style_warnings.append(styles)

def runTest(baseUrl, driver, browser, requires_auth):

    # Component URLs - Where to find the component
    component_urls = [
        f"{baseUrl}/content/maps/mps/en/jp-test/mps-double-column.html?wcmmode=disabled"
    ]

    for url in component_urls:
        driver.get(url)
        bio_profiles = driver.find_elements(By.CSS_SELECTOR, selectors['bio_profile_selector'])
        if len(bio_profiles):
            for bio_profile in bio_profiles:

                # Check component styles
                check_styles(driver, selector=selectors['bio_profile_selector'], styles=bio_profile_styles, description='Bio Profile Component')

                # Check component functionality
                if not requires_auth:
                    title_link = bio_profile.find_element(By.CSS_SELECTOR, selectors['bio_profile_role_link_selector'])
                    title_link_a = title_link.get_attribute('href')
                    title_link_status = requests.get(title_link_a).status_code
                    if title_link_status == 200:
                        print(' - Title link status OK: 200')
                    elif title_link_status >= 400 and title_link_status < 500 :
                        error = f'> {url} Bio profile title link not found: {title_link_status}'
                        raise AssertionError(error)
                    else:
                        error = f'> {url} Bio profile title link error: {title_link_status}'
                        raise AssertionError(error)

        else:
            print(' - Component not found')

    # Return any style warnings
    if len(style_warnings):
        return style_warnings
