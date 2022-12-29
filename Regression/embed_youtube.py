from importlib.machinery import SourceFileLoader
from selenium.webdriver.common.by import By
import requests, time

# Selectors
global_selectors = SourceFileLoader('getsselectors', '../Selectors/selectors.py').load_module()
selectors = global_selectors.get_selector()

# Styles
youtube_embed_styles = {
    "padding" : "10px",
}

transcript_content_text_styles = {
    "font-family" : "Roboto",
}

def check_styles(driver, selector, styles, description):
    stylechecker = SourceFileLoader('getstylechecker', '../Lib/stylechecker.py').load_module()
    element = driver.find_element(By.CSS_SELECTOR, selector)
    styles = stylechecker.checkstyle(
        element,
        styles,
        description
    )

def check_video(driver, youtube_embed):

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

def check_transcript(driver, youtube_embed):

    youtube_footer = youtube_embed.find_element(By.CSS_SELECTOR, selectors['youtube_bottom_section_selector'])
    transcript_header = youtube_footer.find_element(By.CSS_SELECTOR, selectors['youtube_accordion_header_selector'])
    assert transcript_header.get_attribute('aria-expanded') == "false"
    print(' - Aria expanded is false')
    assert transcript_header.get_attribute('tabindex') == "0"
    print(' - Accordion header has tabindex and is keyboard accessible')
    transcript_header.click()
    print(' - Accordion header clicked')
    time.sleep(1)

    transcript_content = youtube_footer.find_element(By.CSS_SELECTOR, selectors['youtube_accordion_content_selector'])
    assert transcript_content.value_of_css_property('display') == "block"
    print(' - Transcript content visible (display: block)')

    transcript_content_text = transcript_content.find_element(By.CSS_SELECTOR, 'p')
    check_styles(driver, selector=selectors['youtube_accordion_content_text_selector'], styles=transcript_content_text_styles, description='YouTube embed transcript text')

    transcript_header.click()
    print(' - Accordion header clicked')
    time.sleep(1)

    transcript_content = youtube_footer.find_element(By.CSS_SELECTOR, selectors['youtube_accordion_content_selector'])
    assert transcript_content.value_of_css_property('display') == "none"
    print(' - Transcript content hidden (display: none)')

def check_transcript_download(driver, devmode):

    download_container = driver.find_element(By.CSS_SELECTOR, selectors['youtube_download_container_selector'])
    download_link = download_container.find_element(By.CSS_SELECTOR, selectors['youtube_download_link_selector'])
    print(' - Download link found')
    download_link_href = download_link.get_attribute('href')
    print(f' - Download href {download_link_href}')

    if devmode:
        expected_transcript_file_link_status = 401
    else:
        expected_transcript_file_link_status = 200
        
    download_link_href_status = requests.get(download_link_href).status_code
    if download_link_href_status == expected_transcript_file_link_status:
        print(f' - Download link status OK {download_link_href_status}')
    else:
        error = f'> Download link status NOT OK {download_link_href_status}'
        raise AssertionError(error)

    download_link_text = download_container.find_element(By.CSS_SELECTOR, selectors['youtube_download_link_text_selector'])
    download_icon = download_container.find_element(By.CSS_SELECTOR, selectors['youtube_download_icon_selector'])

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
                check_styles(driver, selector=selectors['youtube_embed_selector'], styles=youtube_embed_styles, description='YouTube Embed Container')
                check_video(driver, youtube_embed)
                check_transcript(driver, youtube_embed)
                check_transcript_download(driver, devmode)

        else:
            print(' - Component not found')
