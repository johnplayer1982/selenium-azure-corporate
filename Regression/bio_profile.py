from importlib.machinery import SourceFileLoader
from selenium.webdriver.common.by import By

style_warnings = []

# Selectors
global_selectors = SourceFileLoader('getsselectors', '../Selectors/selectors.py').load_module()
selectors = global_selectors.get_selectors()

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

def runTest(baseUrl, driver, browser):

    # Component URLs - Where to find the component
    component_urls = [
        f"{baseUrl}/mps/en/jp-test/ticket-specific/7510---bio-profile-link-configuration-doesn-t-work.html"
    ]

    for url in component_urls:
        driver.get(url)
        bio_profiles = driver.find_elements(By.CSS_SELECTOR, selectors['bio_profile_selector'])
        if len(bio_profiles):
            for bio_profile in bio_profiles:
                # Comment describing the element
                check_styles(driver, selector=selectors['bio_profile_selector'], styles=bio_profile_styles, description='Bio Profile Component')
        else:
            print(' - Component not found')

    # Return any style warnings
    if len(style_warnings):
        return style_warnings
