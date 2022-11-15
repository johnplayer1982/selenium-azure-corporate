# scroll = SourceFileLoader('getscroll', '../Lib/scroll.py').load_module()
# scroll.to(driver, pixels=400)

def to(driver, pixels):
    driver.execute_script(f"window.scrollTo(0, {pixels})")
    print(f' - Scrolled down {pixels}px')
