from test.test_base.environment_setup import EnvironmentSetupSmoke
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

        # randomize email
        import time
        email = 'mtest' + str(int(time.time())) + '@mtest.com'
        print('Email: ', email)

        print('\n#   HOME PAGE    ####################\n')

        # Creating an instance of class and passing the current driver instance
        home = Home(driver)
        print('Loading home page...')

        # Verify that we're on home page by comparing page title
        self.assertEqual(driver.title, Locator.home_page_title)
        print('Titles match.')

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

        print('\n#   AUTHENTICATION PAGE    ####################\n')

        self.assertTrue(home.get_signIn.is_displayed())
        print('Authentication Link displaying', '(' + home.get_signIn.text + ')')
        home.click_signIn()
        driver.implicitly_wait(5)  # wait until page has loaded

        # calling authentication page object to proceed with creating account flow
        auth = Authentication(driver)
        print('Loading authentication page...')
        driver.implicitly_wait(5)

        self.assertTrue(auth.get_auth_txt.text == 'AUTHENTICATION', msg='AUTHENTICATION text not found or displayed.')
        print('Authentication page loaded.', '(page heading:', auth.get_auth_txt.text + ')')
        try:
            auth.create_account(email)
            auth.submit_create_acc()
        except Exception as e:
            print(e)

        print('\n#   REGISTRATION PAGE    ####################\n')

        # calling registration page object to proceed with registration flow
        reg = Registration(driver)
        driver.implicitly_wait(10)
        print('Loading registration page...')

        self.assertTrue(reg.get_reg_txt.text == 'YOUR PERSONAL INFORMATION',
                        msg='YOUR PERSONAL INFORMATION text not found.')
        print('Registration page loaded.', '(page heading: ', reg.get_reg_txt.text + ')')
        reg.verify_email_prepopulated(email)

        try:
            reg.fill_reg_form('2', 'Jeanfirst', 'Testlast', '12345', '25', '6', '2018',
                              'Jeanfirst', 'Testlast', 'Fashion Inc.', '1 Market St.', 'Suite 5',
                              'Denver', 'Colorado', '33333', 'United States', '5556667777', 'Jeany')

            reg.submit_reg()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
