from importlib.machinery import SourceFileLoader
from selenium.webdriver.common.by import By
import requests, time

resize = SourceFileLoader('getresize', '../Lib/resize.py').load_module()

# Selectors
global_selectors = SourceFileLoader('getsselectors', '../Selectors/selectors.py').load_module()
selectors = global_selectors.get_selector()

# Styles
bio_profile_styles = {
    "padding" : "20px",
}

bio_profile_title_styles = {
    "color" : "20, 57, 96",
    "font-size" : "20px",
    "line-height" : "36px",
    "margin" : "0px",
    "padding" : "0px"
}

bio_profile_role_link_styles = {
    "color" : "81, 81, 81",
    "font-size" : "16px",
    "line-height" : "22px",
    "text-decoration-line" : "underline"
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
        bio_profiles = driver.find_elements(By.CSS_SELECTOR, selectors['bio_profile_selector'])
        if len(bio_profiles):
            for bio_profile in bio_profiles:

                # Check component styles
                check_styles(driver, selector=selectors['bio_profile_selector'], styles=bio_profile_styles, description='Bio Profile Component')

                # Image
                image_container = bio_profile.find_element(By.CSS_SELECTOR, selectors['bio_profile_image_container_selector'])
                image = image_container.find_element(By.CSS_SELECTOR, selectors['bio_profile_image_selector'])
                print(' - Image found')

                if image.is_displayed():
                    print(' - Bio image visible')
                else:
                    error = "> Bio image not visible: {url}"
                    raise AssertionError(error)
                
                image_src = image.get_attribute('src')
                image_src_status = requests.get(image_src).status_code

                # Title / Name
                role_title = bio_profile.find_element(By.CSS_SELECTOR, selectors['bio_profile_title_selector'])
                if role_title.is_displayed():
                    print(' - Title / Name found')
                else:
                    error = f'> Bio profile name / title not found: {url}'
                check_styles(driver, selector=selectors['bio_profile_title_selector'], styles=bio_profile_title_styles, description='Bio Profile Title / Name')

                # Role
                role_title_link = bio_profile.find_element(By.CSS_SELECTOR, selectors['bio_profile_role_link_selector'])
                check_styles(driver, selector=selectors['bio_profile_role_link_selector'], styles=bio_profile_role_link_styles, description='Bio Profile Role Link')

                title_link_a = role_title_link.get_attribute('href')
                title_link_status = requests.get(title_link_a).status_code
                print(' - Role title link found')

                # Email - Optional field
                try:
                    email_address = bio_profile.find_element(By.CSS_SELECTOR, selectors['bio_profile_email_selector'])
                    print(' - Email address found')
                except:
                    print(' - Email address not found, optional field')

                # Check status codes of image and link href, on dispatcher only
                if not devmode:

                    # Check status code of title link
                    if title_link_status == 200:
                        print(' - Title link status OK: 200')
                    elif title_link_status >= 400 and title_link_status < 500 :
                        error = f'> {url} Bio profile title link not found: {title_link_status}'
                        raise AssertionError(error)
                    else:
                        error = f'> {url} Bio profile title link error: {title_link_status}'
                        raise AssertionError(error)

                    # Check status code of image
                    if image_src_status == 200:
                        print(' - Bio image src status OK: 200')
                    elif image_src_status >= 400 and image_src_status < 500 :
                        error = f'> {url} Bio image src not found: {image_src_status}'
                        raise AssertionError(error)
                    else:
                        error = f'> {url} Bio image src error: {title_link_status}'
                        raise AssertionError(error)

                # Bio profile content, expandable when content added
                try:
                    bio_profile_content = bio_profile.find_element(By.CSS_SELECTOR, selectors['bio_profile_content_container_selector'])
                    bio_profile_present = True
                    print(' - Bio profile content container found')
                except:
                    bio_profile_present = False
                    print(' - Bio profile content not added to page (optional elements)')

                if bio_profile_present:
                    bio_profile_content_intro = bio_profile.find_element(By.CSS_SELECTOR, selectors['bio_profile_detail_intro_selector'])
                    print(' - Bio profile content text found')

                    bio_profile_more_content = bio_profile.find_element(By.CSS_SELECTOR, selectors['bio_profile_detail_more_content_selector'])
                    bio_profile_more_content_style = bio_profile_more_content.get_attribute('style')
                    if bio_profile_more_content_style == "display: none;":
                        print(' - Bio profile more content hidden by default')
                    else:
                        error = '> Bio profile more content NOT hidden by default'
                        raise AssertionError(error)

                    bio_profile_more_content_trigger = bio_profile.find_element(By.CSS_SELECTOR, selectors['bio_profile_detail_showhide_selector'])
                    print(' - Read more link found')

                    bio_profile_more_content_trigger.click()
                    print(' - Read more link clicked')
                    time.sleep(1)
                    print(' - Allowing 1 seconds for the content to display')
                    bio_profile_more_content_style = bio_profile_more_content.get_attribute('style')
                    if bio_profile_more_content_style:
                        error = f'> Bio profile more content text has unexpected inline style: {bio_profile_more_content_style}'
                        raise AssertionError(error)
                    else:
                        print(' - More content container has no styles, expected as displayed')
                    
                    bio_profile_more_content_trigger.click()
                    print(' - Read more link clicked again')
                    time.sleep(1)
                    bio_profile_more_content_style = bio_profile_more_content.get_attribute('style')
                    if bio_profile_more_content_style == "display: none;":
                        print(' - Bio profile more content hidden')
                    else:
                        error = '> Bio profile more content NOT hidden'
                        raise AssertionError(error)

        else:
            error = f'> Bio profile component expected on {url} but not found'
            raise AssertionError(error)
            print(' - Component not found')
