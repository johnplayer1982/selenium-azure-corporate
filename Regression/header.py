from importlib.machinery import SourceFileLoader
from selenium.webdriver.common.by import By

style_warnings = []

# Selectors

# Header
header_selector = 'div.header'
header_left_container_selector = 'div.left.header_side'

# Logo
logo_container_selector = 'div.logo_container'
logo_link_selector = 'div.logo_container a'
logo_image_selector = 'img.default_logo'

# Navigation
menu_container_selector = 'nav.main_menu_container'
menu_desktop_selector = 'ul.menu.desktop-ul'
submenu_selector = 'ul.sub-menu'
menu_list_item_selector = 'li.menu-item'
menu_language_item_selector = 'li.lang-item'
menu_mobile_selector = 'ul.menu.mobile-ul'
menu_mobile_toggle_selector = 'div.mobile-navigation-toggle'

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

def runTest(baseUrl, driver, browser):

    # Component URLs - Where to find the component
    component_urls = [
        f"{baseUrl}/path/to/page"
    ]

    for url in component_urls:
        driver.get(url)
        components = driver.find_elements(By.CSS_SELECTOR, header_selector)

        if len(components):
            for component in components:
                # Comment describing the element
                check_styles(driver, selector=header_selector, styles=header_styles, description='Header')

                # Run tests
        else:
            print(' - Component not found')

    # Return any style warnings
    if len(style_warnings):
        return style_warnings
