# from importlib.machinery import SourceFileLoader
# iframeswitch = SourceFileLoader('getiframeswitch', '../Lib/iframeswitch.py').load_module()
# iframeswitch.to_iframe(driver)
# iframeswitch.to_parent(driver)

def to_iframe(driver, selector):
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    print(' - Switched to iframe')

def to_parent(driver):
    driver.switch_to.default_content()
    print(' - Switched out of iframe')
