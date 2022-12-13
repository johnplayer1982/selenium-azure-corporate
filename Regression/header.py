from importlib.machinery import SourceFileLoader
from selenium.webdriver.common.by import By

style_warnings = []

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
    style_warnings.append(styles)

def runTest(baseUrl, driver, browser, requires_auth):

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

                # Run tests

        else:
            error = f"> Error: Header not found: {url}"
            raise AssertionError(error)

    # Return any style warnings
    if len(style_warnings):
        return style_warnings
