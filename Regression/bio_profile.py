from importlib.machinery import SourceFileLoader
from selenium.webdriver.common.by import By

style_warnings = []

# Selectors
bio_profile_selector = 'div.bio-profile'
bio_profile_image_container_selector = 'div.bio-profile-image'
bio_profile_image_selector = 'img.profile_image'
bio_profile_content_container_selector = 'div.bio-profile-content'
bio_profile_text_container_selector = 'div.profile-text'
bio_profile_title_selector = 'div.profile-text > h2'
bio_profile_role_selector = 'div.profile-text > h3'
bio_profile_role_link_selector = 'div.profile-text > h3 a'
bio_profile_email_selector = 'div.profile-text > h4'
bio_profile_email_link_selector = 'div.profile-text > h4 a'
bio_profile_detail_selector = 'div.bio-content'
bio_profile_detail_intro_selector = 'div.bio-content p.content'
bio_profile_detail_showhide_selector = 'div.bio-content a.show_hide'
bio_profile_detail_more_content_selector = 'div.bio-content p.more_content'

# Styles
bio_profile_styles = {
    "padding" : "20px",
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
        f"{baseUrl}/mps/en/jp-test/ticket-specific/7510---bio-profile-link-configuration-doesn-t-work.html"
    ]

    for url in component_urls:
        driver.get(url)
        bio_profiles = driver.find_elements(By.CSS_SELECTOR, bio_profile_selector)
        if len(bio_profiles):
            for bio_profile in bio_profiles:
                # Comment describing the element
                check_styles(driver, selector=bio_profile_selector, styles=bio_profile_styles, description='Bio Profile Component')
        else:
            print(' - Component not found')

    # Return any style warnings
    if len(style_warnings):
        return style_warnings
