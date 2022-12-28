from importlib.machinery import SourceFileLoader
from selenium.webdriver.common.by import By
import requests

# Selectors
global_selectors = SourceFileLoader('getsselectors', '../Selectors/selectors.py').load_module()
selectors = global_selectors.get_selector()

# Styles
youtube_embed_styles = {
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

    for url in component_urls:
        driver.get(url)
        youtube_embeds = driver.find_elements(By.CSS_SELECTOR, selectors['youtube_embed_selector'])

        if len(youtube_embeds):
            for youtube_embed in youtube_embeds:
                # Comment describing the element
                check_styles(driver, selector=selectors['youtube_embed_selector'], styles=youtube_embed_styles, description='YouTube Embed Container')

                youtube_iframe = youtube_embed.find_element(By.CSS_SELECTOR, selectors['youtube_iframe_selector'])
                print(' - Embed iframe found')
                youtube_iframe_src = youtube_iframe.get_attribute('src')
                youtube_iframe_src_status = requests.get(youtube_iframe_src).status_code
                if youtube_iframe_src_status == 200:
                    print(f' - YouTube Video src status: {youtube_iframe_src_status}')
                else:
                    error = f'> YouTube Video src status incorrect: {youtube_iframe_src_status}'
                    raise AssertionError(error)

                youtube_iframe_width = youtube_iframe.get_attribute('width')
                assert youtube_iframe_width == "100%"
                print(f' - YouTube iframe width correct: {youtube_iframe_width}')

                # transcript_header = youtube_iframe.find_element(By.CSS_SELECTOR, selectors['youtube_accordion_header_selector'])
                # assert transcript_header.get_attribute('aria-expanded') == "false"
                # assert transcript_header.get_attribute('tabindex') == "0"

        else:
            print(' - Component not found')
