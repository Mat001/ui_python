from test.test_base.environment_setup_flow import EnvironmentSetupSmoke
from test.page_object.locators import Locator
from test.page_object.pages.home import Home
from test.page_object.pages.authentication import Authentication
from test.page_object.pages.registration import Registration
import unittest


class Smoke(EnvironmentSetupSmoke):

    def test_application_flow(self):

        # Using the driver instance created in EnvironmentSetupSmoke
        driver = self.driver
        url = self.url

        print('\n######################################################')
        print('#   HOME PAGE')
        print('######################################################\n')

        # Creating an instance of class and passing the current driver instance
        home = Home(driver)
        print('Loading home page...')

        # Verify that we're on home page by comparing page title
        actual_title = driver.title
        expected_title = Locator.home_page_title
        try:
            self.assertEqual(actual_title, expected_title)
            print('Titles match.')
        except Exception as e:
            print(e, 'Titles don\'t match. Did page load?')

        # Verify if the logo present or not in homepage
        self.assertTrue(home.get_logo.is_displayed(), msg='Logo NOT displayed.')
        print('Logo successfully displayed.')

        # Verifying other elements in the home page
        self.assertTrue(home.get_signIn.is_displayed(), msg='signIn link NOT displayed.')
        print('Found SignIn link - ', home.get_signIn.get_attribute('href'))

        self.assertTrue(home.get_contact_us.is_displayed(), msg='ContactUs link NOT displayed.')
        print('Found Contact Us link - ', home.get_contact_us.get_attribute('href'))

        self.assertEqual(url, driver.current_url)
        print('URL successfully points to Home page -', driver.current_url)

        print('\n######################################################')
        print('#   AUTHENTICATION PAGE')
        print('#######################################################\n')

        if home.get_signIn.is_displayed():
            print('Authentication Link displaying', '(' + home.get_signIn.text + ')')
            home.get_signIn.click()
            driver.implicitly_wait(5)   # wait until page has loaded

        # calling authentication page object to proceed with creating account flow
        auth = Authentication(driver)
        print('Loading authentication page...')
        driver.implicitly_wait(5)

        if auth.get_auth_txt.text == 'AUTHENTICATION':
            print('Authentication page loaded.', '(page heading:', auth.get_auth_txt.text + ')')
        else:
            print('Authentication page not loaded')
        try:
            auth.create_account('mtest@mtest.com')
            auth.submit_create_acc()
        except Exception as e:
            print("Exception occurred ", e)

        print('\n######################################################')
        print('#   REGISTRATION PAGE')
        print('#######################################################\n')

        # calling registration page object to proceed with registration flow
        reg = Registration(driver)
        driver.implicitly_wait(10)
        print('Loading registration page...')

        # this implies is_displayed()
        if reg.get_reg_txt.text == 'YOUR PERSONAL INFORMATION':
            print('Registration page loaded.', '(page heading: ', reg.get_reg_txt.text + ')')
        else:
            print('Registration page not loaded')

        reg.fill_reg_form('TESTFIRST', 'TESTLAST')
        import time
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()