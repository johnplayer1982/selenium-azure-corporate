from importlib.machinery import SourceFileLoader
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import requests, time

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

def logo(driver, devmode):

    # Logo
    print(' - Checking Logo')
    logo_container = driver.find_element(By.CSS_SELECTOR, selectors['logo_container_selector'])
    logo_links = driver.find_elements(By.CSS_SELECTOR, selectors['logo_link_selector'])
    logo_image = driver.find_element(By.CSS_SELECTOR, selectors['logo_image_selector'])

    assert logo_container and logo_links and logo_image
    print('  + Logo container, link and image elements found')

    logo_link_href = logo_links[1].get_attribute('href')
    logo_link_status = requests.get(logo_link_href).status_code
    print(f' - Logo link status {logo_link_status}')
    if not devmode:
        assert logo_link_status == 200
        print(f' - Logo link status OK: {logo_link_status}')

def desktop_navigation(driver, devmode):

    # Desktop
    resize.resizeDesktop(driver)
    nav = driver.find_element(By.CSS_SELECTOR, selectors['menu_container_selector'])
    # Lists
    desktop_nav_list = nav.find_element(By.CSS_SELECTOR, selectors['menu_desktop_selector'])

    # List items
    top_level_desktop_nav_list_items = driver.find_elements(By.CSS_SELECTOR, selectors['menu_desktop_top_level_with_submenu'])
    top_level_desktop_nav_list_items_len = len(top_level_desktop_nav_list_items)
    print(f' - {top_level_desktop_nav_list_items_len} Navigation links found in sub menus')

    # Sub menus
    sub_menus = driver.find_elements(By.CSS_SELECTOR, selectors['submenu_selector'])
    sub_menus_len = len(sub_menus)
    print(f' - {sub_menus_len} sub-menus found')
    # Confirm all submenus are hidden
    for item in sub_menus:
        visibility = item.value_of_css_property('visibility')
        if visibility == 'hidden':
            print(' - Sub menu not visible')
        else:
            error = '> Submenu visible on load'
            raise AssertionError(error)
    
    # Hover over menu items, confirm submenus display
    for menu_item in top_level_desktop_nav_list_items:

        menu_item_text = menu_item.find_element(By.CSS_SELECTOR, 'a > span')
        print(f' - Checking menu item: {menu_item_text.text}')
        a = ActionChains(driver)
        m = menu_item
        a.move_to_element(m).perform()
        time.sleep(1)

        m_submenu = menu_item.find_element(By.CSS_SELECTOR, selectors['submenu_selector'])
        m_submenu_visibility = m_submenu.value_of_css_property('visibility')
        if m_submenu_visibility == 'visible':
            print(' - Submenu visible')
        else:
            error = f'> Submenu not visible after top level menu item hover on {menu_item_text}'
            raise AssertionError(error)

        # Check link status of submenu items
        print('\nChecking submenu links')
        m_submenu_links = m_submenu.find_elements(By.CSS_SELECTOR, selectors['menu_list_item_link_selector'])
        if devmode:
            expected_m_submenu_link_status = 401
        else:
            expected_m_submenu_link_status = 200

        for link in m_submenu_links:

            link_text = link.text
            print(f' - Checking link {link_text}')
            link_href = link.get_attribute('href')
            if not link_href == None:
                print(f' - Checking link href {link_href}')
                link_status = requests.get(link_href).status_code
                if link_status == expected_m_submenu_link_status:
                    print(f' - Link desintation status OK: {link_status}')
                else:
                    error = f' - Link desintation status NOT OK: {link_status}, should be {expected_m_submenu_link_status}'
                    raise AssertionError(error)
            else:
                print(' - Link href none, assumed submenu trigger')

        # Move mouse away
        a.move_by_offset(300, 300).perform()
        print(' - Mouse moved by offset to close submenu')

def mobile_navigation(driver):

    print('\nChecking mobile navigation')
    resize.resizeMobile(driver)
    driver.get(driver.current_url)
    # Mobile menu button
    mobile_menu_btn = driver.find_element(By.CSS_SELECTOR, selectors['menu_mobile_toggle_selector'])
    if mobile_menu_btn.value_of_css_property('display') == 'block':
        print('- Mobile menu button visible')
    else:
        error = '> Mobile menu not button visible'
        raise AssertionError(error)

    # Mobile menu
    mobile_menu = driver.find_element(By.CSS_SELECTOR, selectors['menu_container_selector'])
    mobile_menu_display = mobile_menu.get_attribute('style')
    print(f' - Menu inline style: {mobile_menu_display}')

    mobile_menu_button = driver.find_element(By.CSS_SELECTOR, selectors['menu_mobile_toggle_selector'])
    mobile_menu_button.click()
    print(' - Clicked mobile menu button')
    time.sleep(1)
    print(' - Allowing a second for the menu to open')

    menu_toggle_classes = mobile_menu_button.get_attribute('class')
    if 'is-active' in menu_toggle_classes:
        print(' - Menu toggle button has expected "is-active" class')
    else:
        error = '> Menu toggle button is missing "is-active" class'
        raise AssertionError(error)

    mobile_menu_display = mobile_menu.get_attribute('style')
    if mobile_menu_display == 'display: block;':
        print(f' - Mobile menu visible')
    else:
        error = '> Mobile menu not visible after menu button click'
        raise AssertionError(error)
    
    mobile_menu = driver.find_element(By.CSS_SELECTOR, selectors['menu_mobile_selector'])
    mobile_menu_items = mobile_menu.find_elements(By.CSS_SELECTOR, selectors['menu_mobile_items_selector'])
    
    for item in mobile_menu_items:

        item_link = item.find_element(By.CSS_SELECTOR, 'a')
        item_link.click()
        print(' - Opening submenu')

        item_link.click()
        print(' - Closing submenu')
        time.sleep(1)

def runTest(baseUrl, driver, browser, devmode):

    # Component URLs - Where to find the component
    component_urls = [
        f"{baseUrl}/content/maps/mps/en/jp-test/mps-double-column.html?wcmmode=disabled"
    ]

    for url in component_urls:
        driver.get(url)
        resize.resizeDesktop(driver)
        time.sleep(1)
        headers = driver.find_elements(By.CSS_SELECTOR, selectors['header_selector'])

        if len(headers):
            for header in headers:
                check_styles(driver, selector=selectors['header_selector'], styles=header_styles, description='Header')

                logo(driver, devmode)
                desktop_navigation(driver, devmode)
                mobile_navigation(driver)

        else:
            error = f"> Error: Header not found: {url}"
            raise AssertionError(error)
