# Checks the styles of an element
# Requires 2 arguments:
# element = The object to run the tests against. eg element = driver.find_element(By.CSS_SELECTOR, 'h1')
# dict = The list of styles to check, eg:
# dict = {
#  "margin-top" : "10px",
#  "font-size" : "38px"
# }
# ---------------------------------------------
# To use in a shared component, see Components/teaser.py for example:
#
# from importlib.machinery import SourceFileLoader
# stylechecker = SourceFileLoader('getstylechecker', '../Lib/stylechecker.py').load_module()
# style_warnings = []
#
# styles = stylechecker.checkstyle(
#     element, 
#     dict,
#     description="Thing you are testing"
# )
# style_warnings.append(styles)
#
# At the end of the script, return the style warnings:
# if len(style_warnings):
#     return style_warnings
#
# ---------------------------------------------
# To call from a tool script:
# from importlib.machinery import SourceFileLoader
# # Import the component script
# tooltitlechecker = SourceFileLoader('gettooltitlechecker', '../Components/tool_title.py').load_module()
# # Run as variable so we can store what is returned
# title_styles = tooltitlechecker.check_tool_title(driver)

def checkstyle(element, dict, description):

    for attribute, style in dict.items():
        print(' - Checking style {attribute} for {description}'.format(attribute=attribute, description=description))
        expected_style = style
        actual_style = element.value_of_css_property(attribute)
        print('   + Expected: {}'.format(expected_style))
        print('   + Actual: {}'.format(actual_style))
        if expected_style in actual_style:
            print('   > {} OK'.format(attribute))
        else:
            error_string = "{description}: {attribute} incorrect - Actual: {actual}, Expected to contain: {expected}".format(description=description, attribute=attribute, expected=expected_style, actual=actual_style)
            print('   X {} NOT OK'.format(attribute))
            raise AssertionError(error_string)
