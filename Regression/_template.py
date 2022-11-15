from selenium.webdriver.common.by import By
from importlib.machinery import SourceFileLoader

# Import lib scripts
resize = SourceFileLoader('getresize', '../Lib/resize.py').load_module()
dismisscookie = SourceFileLoader('getdismisscookiefile', '../Lib/dismisscookie.py').load_module()
stylechecker = SourceFileLoader('getstylechecker', '../Lib/stylechecker.py').load_module()

locales = {
    "en",
    "cy"
}

# Style warnings
style_warnings = []

def runTest(baseUrl, driver, browser):

    for locale in locales:
        tool_url = f'{baseUrl}/{locale}'
        driver.get(tool_url)
        dismisscookie.dismissCookieBanner(driver)

        # ---------- Add tests here ---------- #

        url = f'{baseUrl}/{locale}'
        driver.get(url)

        # ---------- End tests here ---------- #

    # Return any style warnings (If strict styles set to false in Helpers/stylechecker.py)
    if len(style_warnings):
        print('\nCSS Warnings\n------------')
        for items in style_warnings:
            if not items == None:
                for item in items:
                    if len(item):
                        print(f'+ {item}')
