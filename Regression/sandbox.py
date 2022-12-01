from selenium import webdriver
from selenium.webdriver.common.by import By
from importlib.machinery import SourceFileLoader
import time, os, platform

if platform.system() == "Darwin":
    # driver = webdriver.Safari()
    driver = webdriver.Chrome("../Webdrivers/chromedriver")
else:
    browser = "Edge"
    DRIVER_BIN = "..\Webdrivers\msedgedriver.exe"
    driver = webdriver.Edge(executable_path=DRIVER_BIN)

resize = SourceFileLoader('getresize', '../Lib/resize.py').load_module()
stylechecker = SourceFileLoader('getstylechecker', '../Lib/stylechecker.py').load_module()
dismisscookie = SourceFileLoader('getdismisscookiefile', '../Lib/dismisscookie.py').load_module()
clearinput = SourceFileLoader('getclearinputfile', '../Lib/clearinput.py').load_module()

# Selectors
global_selectors = SourceFileLoader('getsselectors', '../Selectors/selectors.py').load_module()
selectors = global_selectors.get_selector()

urls = [
    "https://moneyhelper-tools.netlify.app/en/ltt-calculator",
    # "https://moneyhelper-tools.netlify.app/cy/ltt-calculator",
]

resize.resizeDesktop(driver)

for url in urls:

    driver.get(url)
    print("Visiting {}".format(url))

    # List to hold any style warnings
    style_warnings = []

    # ----------- Start ---------- #

    dismisscookie.dismissCookieBanner(driver)

    # Confirm we have the selectors available
    for id, selector in selectors.items():
        print(id)
        print(selector)

    # ----------- End ---------- #

# Return any style warnings (If strict styles set to false in Helpers/stylechecker.py)
if len(style_warnings):
    print('\nCSS Warnings\n------------')
    for items in style_warnings:
        if not items == None:
            for item in items:
                for entry in item:
                    print('+ {}'.format(entry))

driver.close()
