# Set remote driver
def get_driver(webdriver, username, authkey, caps):
    driver = webdriver.Remote(
        command_executor="http://%s:%s@hub.crossbrowsertesting.com/wd/hub"%(username, authkey),
        desired_capabilities=caps)
    return driver
