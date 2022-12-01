from importlib.machinery import SourceFileLoader
from selenium.webdriver.common.by import By

style_warnings = []

# Selectors
hero_selector = 'div.heroImage'
hero_image_container_selector = 'div.header-img'
hero_image_selector = 'div.header-img > img'
hero_title_container_selector = 'div.page-category'
hero_title_text_selector = 'div.page-category > h1#page-title'

# Styles
hero_styles = {
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

def runTest(baseUrl, driver, browser):

    # Component URLs - Where to find the component
    component_urls = [
        f"{baseUrl}/path/to/page"
    ]

    for url in component_urls:
        driver.get(url)
        components = driver.find_elements(By.CSS_SELECTOR, hero_selector)

        if len(components):
            for component in components:
                # Comment describing the element
                check_styles(driver, selector=hero_selector, styles=hero_styles, description='Hero Image')

                # Run tests
        else:
            print(' - Component not found')

    # Return any style warnings
    if len(style_warnings):
        return style_warnings
