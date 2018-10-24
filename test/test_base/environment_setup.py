# For the flow use setUpClass
# Place url and driver creation into setUp.
# I'd also like to create page instances at the top of smoke test file - right now this doesn't work

"""Set up set-up and tear-down for smoke test application flow
This setup is designed for testing the whole application flow
(one setUp and one tearDown method for the class).
Setu and teardown only happen once, at the beginning of the flow
and at the end (and not for each test method)"""

import unittest
import datetime
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os


class EnvironmentSetupSmoke(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Setup contains the browser setup attributes."""
        #######################################
        # remotely
        #######################################
        # remotely (on selenium grid, needs docker compose to run first)
        if os.getenv('BROWSER') == 'firefox':
            cls.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                          desired_capabilities=DesiredCapabilities.FIREFOX)
        elif os.getenv('BROWSER') == 'chrome':
            cls.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                          desired_capabilities=DesiredCapabilities.CHROME)
        else:
            raise Exception('unknown browser {}'.format(os.environ['BROWSER']))

        #######################################
        # locally
        #######################################
        # firefox
        # path_to_geckodriver = '/home/m/applications/geckodriver'
        # cls.driver = webdriver.Firefox(executable_path=path_to_geckodriver)
        # cls.driver.maximize_window()

        # chrome
        # path_to_chromedriver = '/home/m/applications/chromedriver'
        # cls.driver = webdriver.Chrome(executable_path=path_to_chromedriver)
        # cls.driver.maximize_window()

        print('-------------------------------------------------')
        print('Run started at ' + str(datetime.datetime.now()))
        browser_name = cls.driver.capabilities['browserName']
        if browser_name == 'chrome':
            print('Browser: ', browser_name, cls.driver.capabilities['version'])
        else:
            print('Browser: ', browser_name, cls.driver.capabilities['browserVersion'])

        cls.driver.implicitly_wait(20)
        cls.url = 'http://automationpractice.com/index.php'
        cls.driver.get(cls.url)
        cls.driver.set_page_load_timeout(20)

    @classmethod
    def tearDownClass(cls):
        """Teardown method to close browser and quit."""
        # if driver hasn't closed already, te close it and quit it
        if cls.driver is not None:
            print('-------------------------------------------------')
            print('Run completed at ' + str(datetime.datetime.now()))
            cls.driver.quit()
