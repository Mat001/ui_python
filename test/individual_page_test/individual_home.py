from test.page_object.locators import Locator
from test.test_base.environment_setup import EnvironmentSetup
from test.page_object.pages.home import Home
import unittest


class MyStoreHomePage(EnvironmentSetup):

    def test_home(self):
        print('######################################################')
        print('#   HOME PAGE')
        print('######################################################')

        # Using the driver instances created in EnvironmentSetup
        driver = self.driver
        url = 'http://automationpractice.com/index.php'
        self.driver.get(url)
        self.driver.set_page_load_timeout(20)   # webdriver built-in method
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
        # Creating an instance of class and passing the current driver instance
        m = Home(driver)

        self.assertTrue(m.get_logo.is_displayed(), msg='Logo NOT displayed.')
        print('Logo successfully displayed.')

        # Verifying other elements in the home page
        self.assertTrue(m.get_signIn.is_displayed(), msg='signIn link NOT displayed.')
        print('Found SignIn link - ', m.get_signIn.get_attribute('href'))

        self.assertTrue(m.get_contact_us.is_displayed(), msg='ContactUs link NOT displayed.')
        print('Found Contact Us link - ', m.get_contact_us.get_attribute('href'))

        self.assertEqual(url, driver.current_url)
        print('URL successfully points to Home page -', driver.current_url)


if __name__ == '__main__':
    unittest.main()
