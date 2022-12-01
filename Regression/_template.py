# Usage
# -----
# 1) Import the SourceFileLoader lib
# from importlib.machinery import SourceFileLoader
# -----
# 2) Import this script
# componentchecker = SourceFileLoader('getcomponentfile', '../Components/_components_template.py').load_module()
# -----
# 3) Run the check function, store result in a variable
# component_styles = componentchecker.check_componentName(driver)
# -----
# 4) If any style warning are returned, append them to the style_warnings list
# if component_styles:
#   style_warnings.append(component_styles)
# -----

from importlib.machinery import SourceFileLoader
from selenium.webdriver.common.by import By

style_warnings = []

# Selectors
global_selectors = SourceFileLoader('getsselectors', '../Selectors/selectors.py').load_module()
selectors = global_selectors.get_selectors()

# Styles
component_styles = {
    "" : "",
    "" : "",
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
        f"{baseUrl}/path/to/page"
    ]

    for url in component_urls:
        driver.get(url)
        components = driver.find_elements(By.CSS_SELECTOR, selectors['dummy_selector'])

        if len(components):
            for component in components:
                # Comment describing the element
                check_styles(driver, selector=selectors['dummy_selector'], styles=component_styles, description='Element description')

                # Run tests
        else:
            print(' - Component not found')

    # Return any style warnings
    if len(style_warnings):
        return style_warnings
