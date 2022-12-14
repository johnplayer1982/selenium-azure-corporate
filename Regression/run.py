from selenium import webdriver
from importlib.machinery import SourceFileLoader
import os, requests

username = os.getenv("CBT_USERNAME")
authkey = os.getenv("CBT_AUTHKEY")
environment = os.getenv("ENVIRONMENT")
build = os.getenv("BUILD")
baseUrl = os.getenv("BASEURL")

api_session = requests.Session()
api_session.auth = (username, authkey)
test_result = None
build = build
release = "Money Helper Corporate - {}".format(build)
requires_auth = True
devmode = True

def setCaps(platform, browser, version):
    caps = {
        'name': '{}'.format(release),
        'build': '{}'.format(build),
        'platform': platform,
        'browserName': browser,
        'version' : version,
        'screenResolution' : '1920x1080',
        'record_video' : 'true',
        'max_duration' : '3600'
    }
    return caps

def get_driver():
    driver = webdriver.Remote(
        command_executor="http://%s:%s@hub.crossbrowsertesting.com/wd/hub"%(username, authkey),
        desired_capabilities=caps)
    return driver

def run_tests(tests, browser):
    try:
        for key, value in tests.items():
            print('Testing {}'.format(key))
            value.runTest(baseUrl, driver, browser, devmode)
            print('End of {} test\n'.format(key))
        test_result = 'pass'
    except AssertionError as e:
        test_result = 'fail'
        raise
    return test_result

def clean_up(driver, test_result):
    print("Done with session %s" % driver.session_id)
    driver.quit()
    # Here we make the api call to set the test's score.
    # Pass it it passes, fail if an assertion fails, unset if the test didn't finish
    if test_result is not None:
        api_session.put('https://crossbrowsertesting.com/api/v3/selenium/' + driver.session_id,
            data={'action':'set_score', 'score':test_result})

# ---------- Tools ---------- #

# Import the tools
import header
import bio_profile
import embed_youtube
import hero
import accordion
import image
import buttons
import link_list

# Set the caps
caps = setCaps(
    platform='MacOS 11.0',
    browser='Safari', 
    version='14'
)

# Get the driver
driver = get_driver()

# Specify the tests
tests = {
    "Header" : header,
    "Bio Profile" : bio_profile,
    "YouTube Embed" : embed_youtube,
    "Hero Image" : hero,
    "Accordion" : accordion,
    "Image" : image,
    "Buttons" : buttons,
    "Link List" : link_list,
}

if requires_auth:
    authtest = SourceFileLoader('getauthtest', '../Lib/testauth.py').load_module()
    driver.get(baseUrl)
    authtest.authuser(driver)

# Run the tests
test_result = run_tests(tests, browser=caps.get("browserName"))

# Cleanup
clean_up(
    driver,
    test_result
)
