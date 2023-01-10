from importlib.machinery import SourceFileLoader
from selenium.webdriver.common.by import By
import requests

resize = SourceFileLoader('getresize', '../Lib/resize.py').load_module()

# Selectors
global_selectors = SourceFileLoader('getsselectors', '../Selectors/selectors.py').load_module()
selectors = global_selectors.get_selector()

# Styles
image_styles = {
    "padding" : "10px",
}

image_inner_styles = {
    "margin-top" : "35px",
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
    print('\nTesting image component')

    for url in component_urls:
        driver.get(url)
        image_components = driver.find_elements(By.CSS_SELECTOR, selectors['image_container_selector'])
        image_components_len = len(image_components)
        print(f' - {image_components_len} image components found')

        if len(image_components):
            for image_component in image_components:
                # Comment describing the element
                check_styles(driver, selector=selectors['image_container_selector'], styles=image_styles, description='Image')
                check_styles(driver, selector=selectors['image_innaer_container_selector'], styles=image_inner_styles, description='Image Inner Container')

                # Figure out if this image has a link
                try:
                    # If this component contains an image with the 'a.cmp-image__link' selector
                    image_with_link = image_component.find_element(By.CSS_SELECTOR, selectors['image_with_link_selector'])
                    image_with_link_href = image_with_link.get_attribute('href')
                    image_has_link = True
                except:
                    image_has_link = False

                if image_has_link:
                    print(' - Image has link')
                    image_with_link_href_status = requests.get(image_with_link_href).status_code
                    if not devmode:
                        if image_with_link_href_status == 200:
                            print(' - Image link status ok')
                        else:
                            error = f'> Image link status not ok: {image_with_link_href_status}'
                            raise AssertionError(error)
                    else:
                        print(f' - Tests in devmode, status acceptable: {image_with_link_href_status}')
                else:
                    print(' - Image does not include a link')

        else:
            print(' - Image component not found')
