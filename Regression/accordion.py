from importlib.machinery import SourceFileLoader
from selenium.webdriver.common.by import By
import requests, time

resize = SourceFileLoader('getresize', '../Lib/resize.py').load_module()

# Selectors
global_selectors = SourceFileLoader('getsselectors', '../Selectors/selectors.py').load_module()
selectors = global_selectors.get_selector()

# Styles
accordion_styles = {
    "padding-top" : "16px",
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
        resize.resizeDesktop(driver)
        driver.get(url)
        time.sleep(1)
        accordions = driver.find_elements(By.CSS_SELECTOR, selectors['accordion_selector'])

        if len(accordions):
            for accordion in accordions:
                check_styles(driver, selector=selectors['accordion_selector'], styles=accordion_styles, description='Accordion')

                # Confirm accordion has closed class on load
                accordion_classes = accordion.get_attribute('class')
                if 'open' in accordion_classes:
                    error = '> Accordion open on load'
                    raise AssertionError(error)
                else:
                    print(' - Accordion closed on load')
                
                # Open accordion
                accordion.click()
                time.sleep(1)
                print(' - Accordion clicked')
                accordion_classes = accordion.get_attribute('class')
                if 'open' in accordion_classes:
                    print(' - Accordion open')
                else:
                    error = '> Accordion not open after click'
                    raise AssertionError(error)
                
                second_level_items = accordion.find_elements(By.CSS_SELECTOR, selectors['accordion_sub_item'])
                second_level_items_len = len(second_level_items)
                print(f' - {second_level_items_len} second level items found')
                for item in second_level_items:

                    second_level_content = item.find_element(By.CSS_SELECTOR, selectors['accordion_sub_item_content'])
                    second_level_content_classes = second_level_content.get_attribute('class')
                    if 'closed' in second_level_content_classes:
                        assert not second_level_content.is_displayed()
                        print(' - Second level content hidden on load')
                    else:
                        error = '> Second level content displayed on load, should be hidden and contain the class "closed"'
                        raise AssertionError(error)

                    item.click()
                    print(' - Second level item clicked')

                    item_classes = item.get_attribute('class')
                    if 'open' in item_classes:
                        assert item.is_displayed()
                        print(' - Sub accordion title contains "open" class')
                    else:
                        error = '> Sub accordion title does not contain "open" class'
                        raise AssertionError(error)

                    second_level_content_classes = second_level_content.get_attribute('class')
                    if 'open' in second_level_content_classes:
                        assert second_level_content.is_displayed()
                        print(' - Second level content displayed')
                    else:
                        error = '> Second level content not displayed in accordion'
                        raise AssertionError(error)
                    
                    item.click()
                    print(' - Second level item clicked again to close')

                    second_level_content_classes = second_level_content.get_attribute('class')
                    if 'closed' in second_level_content_classes:
                        assert not second_level_content.is_displayed()
                        print(' - Second level content closed')
                    else:
                        error = '> Second level content displayed in accordion after clicking to close'
                        raise AssertionError(error)

                accordion.click()
                time.sleep(1)
                print(' - Clicked top level accordion to close')
                accordion_classes = accordion.get_attribute('class')
                if 'closed' in accordion_classes:
                    print(' - Accordion closed')
                else:
                    error = '> Accordion not closed after click'
                    raise AssertionError(error)

        else:
            error = f"> Error: Accordion not found: {url}"
            raise AssertionError(error)
