from test.page_object.locators import Locator
from test.test_base.environment_setup import EnvironmentSetup
from test.page_object.pages.home import Home
from test.page_object.pages.registration import Registration
import time

import unittest


class MyStoreRegistration(EnvironmentSetup):

    def test_registration(self):
        print('######################################################')
        print('#   REGISTRATION PAGE')
        print('######################################################')
        pass


        # driver = self.driver
        # self.driver.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
        # self.driver.set_page_load_timeout(20)
        #
        # # calling registration page object to proceed with registration flow
        # reg = Registration(driver)
        # # this implies is_displayed()
        # if reg.get_reg_txt() == 'YOUR PERSONAL INFORMATION':
        #     print('Authentication page successfully loaded', reg.get_reg_txt().text)
        # else:
        #     print('Authentication page not loaded')
