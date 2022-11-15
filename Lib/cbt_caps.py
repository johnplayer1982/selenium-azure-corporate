# Function to set caps for crossbrowser testing:
# caps = SourceFileLoader('getcaps', 'Helpers/cbt_caps.py').load_module()
# caps = caps.setCaps(
#     platform='Windows', 
#     browser='Chrome', 
#     version='102', 
#     release=release, 
#     build=build
# )

def setCaps(platform, browser, version, release, build):
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