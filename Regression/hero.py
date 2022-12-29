from importlib.machinery import SourceFileLoader
from selenium.webdriver.common.by import By

# Selectors
global_selectors = SourceFileLoader('getsselectors', '../Selectors/selectors.py').load_module()
selectors = global_selectors.get_selector()

# Styles
hero_styles = {
    "padding" : "10px",
}

hero_title_styles = {
    "font-family" : "Roboto"
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
        heros = driver.find_elements(By.CSS_SELECTOR, selectors['hero_selector'])

        if len(heros):
            for hero in heros:
                # Comment describing the element
                check_styles(driver, selector=selectors['hero_selector'], styles=hero_styles, description='Hero Image')

                hero_title = hero.find_element(By.CSS_SELECTOR, selectors['hero_title_text_selector'])
                check_styles(driver, selector=selectors['hero_title_text_selector'], styles=hero_title_styles, description='Hero Title Text')

        else:
            print(' - Component not found')
