import pytest
from base.webdriver_factory import WebDriverFactory
import datetime


@pytest.fixture(scope="class")
def driver(request, browser='firefox-local'):        # MANUALLY ADDED BROWSER TYPE HERE - cause addoptions not working
# def driver(request, browser):
    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver_instance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    if driver is not None:
        # driver.quit()
        print('\nRun completed at ' + str(datetime.datetime.now()))


# TODO Fix addoption for browser - not recognized
# def pytest_addoption(parser):
#     parser.addoption("--browser", help="Type of browser")
#
#
# @pytest.fixture(scope="session")
# def browser(request):
#     return request.config.getoption("--browser")
