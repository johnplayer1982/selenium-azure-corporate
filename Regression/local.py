from selenium import webdriver
from selenium.webdriver.common.by import By
import os, platform, time

import _template

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
    "Example Test" : _template,
}

# Run
for key, value in tests.items():
    print('> Testing {}\n'.format(key))
    value.runTest(baseUrl, driver)
    print('\n> End of {} test\n'.format(key))

driver.close()
