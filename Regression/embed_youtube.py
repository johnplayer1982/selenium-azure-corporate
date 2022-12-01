from importlib.machinery import SourceFileLoader
from selenium.webdriver.common.by import By

style_warnings = []

# Selectors
youtube_embed_selector = 'div.embed-youtube'
youtube_iframe_selector = 'div.embed-youtube iframe'
youtube_bottom_section_selector = 'div.cmp-youtube__footer'
youtube_accordion_selector = ''
youtube_accordion_header_selector = ''
youtube_accordion_content_selector = ''
youtube_download_container_selector = 'div.cmp-youtube__download'
youtube_download_link_selector = 'a.cmp-youtube__download-transcript'
youtube_download_link_text_selector = 'span.cmp-youtube__download-transcript-text'
youtube_download_icon_selector = 'span.cmp-youtube__download-transcript-icon'

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
    style_warnings.append(styles)

def runTest(baseUrl, driver, browser):

    # Component URLs - Where to find the component
    component_urls = [
        f"{baseUrl}/path/to/page"
    ]

    for url in component_urls:
        driver.get(url)
        components = driver.find_elements(By.CSS_SELECTOR, youtube_embed_selector)

        if len(components):
            for component in components:
                # Comment describing the element
                check_styles(driver, selector=youtube_embed_selector, styles=youtube_embed_styles, description='YouTube Embed Container')

                # Run tests
        else:
            print(' - Component not found')

    # Return any style warnings
    if len(style_warnings):
        return style_warnings
