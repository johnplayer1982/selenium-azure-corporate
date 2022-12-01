from selenium import webdriver
import platform

import header
import bio_profile
import embed_youtube
import hero

baseUrl = "https://www.moneyhelper.org.uk"

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
    "Hero Image" : hero
}

# Run
for key, value in tests.items():
    print('> Testing {}\n'.format(key))
    value.runTest(baseUrl, driver, browser)
    print('\n> End of {} test\n'.format(key))

driver.close()
