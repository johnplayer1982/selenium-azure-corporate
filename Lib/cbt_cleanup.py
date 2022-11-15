def clean_up(driver, test_result, api_session):
    print("Done with session %s" % driver.session_id)
    driver.quit()
    # Here we make the api call to set the test's score.
    # Pass it it passes, fail if an assertion fails, unset if the test didn't finish
    if test_result is not None:
        api_session.put('https://crossbrowsertesting.com/api/v3/selenium/' + driver.session_id,
            data={'action':'set_score', 'score':test_result})
