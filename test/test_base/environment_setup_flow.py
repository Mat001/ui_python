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


class EnvironmentSetupSmoke(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Setup contains the browser setup attributes."""
        cls.driver = webdriver.Firefox(executable_path='/home/m/applications/geckodriver')
        print('-------------------------------------------------')
        print('Run started at ' + str(datetime.datetime.now()))
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
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
            cls.driver.close()
            cls.driver.quit()
