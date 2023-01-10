from importlib.machinery import SourceFileLoader
from selenium.webdriver.common.by import By

resize = SourceFileLoader('getresize', '../Lib/resize.py').load_module()

# Selectors
global_selectors = SourceFileLoader('getsselectors', '../Selectors/selectors.py').load_module()
selectors = global_selectors.get_selector()

# Styles
link_list_container_styles = {
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

    resize.resizeDesktop(driver)

    for url in component_urls:
        driver.get(url)
        link_lists = driver.find_elements(By.CSS_SELECTOR, selectors['link_list_container_selector'])

        if len(link_lists):
            for link_list in link_lists:
                # Comment describing the element
                check_styles(driver, selector=selectors['link_list_container_selector'], styles=link_list_container_styles, description='Link List Container')

                link_list_content_container = link_list.find_element(By.CSS_SELECTOR, selectors['link_list_content_container_selector'])
                assert link_list_content_container.value_of_css_property('padding') == "0px 15px"
                print(' - Link list content container styles OK')

                link_list_heading = link_list_content_container.find_element(By.CSS_SELECTOR, selectors['link_list_heading_selector'])
                assert link_list_heading.value_of_css_property('padding') == "0px"
                assert link_list_heading.value_of_css_property('margin') == "36px 0px 30px"
                assert link_list_heading.value_of_css_property('font-size') == "26px"
                assert link_list_heading.value_of_css_property('font-weight') == "900"
                assert link_list_heading.value_of_css_property('font-family') == "Roboto"
                print(' - Link list title <h2> styles OK')

                link_list_list = link_list_content_container.find_element(By.CSS_SELECTOR, selectors['link_list_list_selector'])
                assert link_list_list.value_of_css_property('margin') == "-4px 0px 20px 20px"
                assert link_list_list.value_of_css_property('padding') == "0px"
                assert link_list_list.value_of_css_property('font-size') == "16px"
                assert link_list_list.value_of_css_property('font-weight') == "400"
                assert link_list_list.value_of_css_property('list-style-type') == "disc"
                print(' - Link list <ul> styles OK')

                link_list_list_items = link_list_list.find_elements(By.CSS_SELECTOR, selectors['link_list_list_item_selector'])
                for item in link_list_list_items:
                    assert item.value_of_css_property('font-size') == "16px"
                    assert item.value_of_css_property('font-weight') == "600"
                    assert "11, 12, 12" in item.value_of_css_property('color')
                    assert item.value_of_css_property('line-height') == "24px"
                print(' - List item <li> styles OK')

                link_list_list_item_links = link_list_list.find_elements(By.CSS_SELECTOR, selectors['link_list_list_item_link_selector'])
                for link in link_list_list_item_links:
                    assert link.value_of_css_property('text-decoration') == "underline solid rgb(29, 82, 138)"
                print(' - List item link <a> styles OK')

        else:
            print(' - Link list component not found')
