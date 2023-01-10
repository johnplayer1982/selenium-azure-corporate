from selenium import webdriver
from importlib.machinery import SourceFileLoader
import platform

import header
import bio_profile
import embed_youtube
import hero
import accordion
import image

baseUrl = "http://maps-test-aem-author.uksouth.cloudapp.azure.com"
devmode = True

# Certain things wont work if we need to auth to see the site, these will be warnings rather than failues:
# Set to false when testing on a dispatcher URL
requires_auth = True

if platform.system() == "Darwin":
    # browser = "Safari"
    # driver = webdriver.Safari()
    browser = "Chrome"
    driver = webdriver.Chrome("../Webdrivers/chromedriver")
else:
    browser = "Edge"
    DRIVER_BIN = "..\Webdrivers\msedgedriver.exe"
    driver = webdriver.Edge(executable_path=DRIVER_BIN)
    print("Testing on PC")

# Specify tests
tests = {
    "Header" : header,
    "Bio Profile" : bio_profile,
    "YouTube Embed" : embed_youtube,
    "Hero Image" : hero,
    "Accordion" : accordion,
    "Image" : image,
}

if requires_auth:
    authtest = SourceFileLoader('getauthtest', '../Lib/testauth.py').load_module()
    driver.get(baseUrl)
    authtest.authuser(driver)

# Run
for key, value in tests.items():
    print('> Testing {}\n'.format(key))
    value.runTest(baseUrl, driver, browser, devmode)
    print('\n> End of {} test\n'.format(key))

driver.close()
