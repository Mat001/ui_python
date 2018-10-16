"""Set up set-up and tear-down for unit tests
This setup is designed for testing individual pages
(setUp and tearDown per each test method)"""

import unittest
import datetime
from selenium import webdriver

#


class EnvironmentSetup(unittest.TestCase):

    def setUp(self):
        """Setup contains the browser setup attributes."""
        self.driver = webdriver.Firefox(executable_path='/home/m/applications/geckodriver')
        print('-------------------------------------------------')
        print('Run started at ' + str(datetime.datetime.now()))
        self.driver.implicitly_wait(20)		# not sure why it's needed - to fully load the page?
        self.driver.maximize_window()

    def tearDown(self):
        """Teardown method to close browser and quit."""
        # if driver hasn't closed already, te close it and quit it
        if self.driver is not None:
            print('-------------------------------------------------')
            print('Run completed at ' + str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()