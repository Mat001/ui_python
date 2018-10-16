from test.test_base.environment_setup import EnvironmentSetup
from test.page_object.pages.home import Home
from test.page_object.pages.authentication import Authentication
from test.page_object.pages.registration import Registration


class MyStoreAuthentication(EnvironmentSetup):

    def test_authentication(self):
        print('######################################################')
        print('#   AUTHENTICATION PAGE')
        print('######################################################')

        # SHOULD CONTINUE FROM THE FIRST PAGE !!!!! SHOULD WAIT FOR IT TO LOAD.
        # SHOULD NOT NEED TO LOAD AUTH PAGE SEPARATELY
        driver = self.driver
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.set_page_load_timeout(20)

        # calling home page object to click on Register Link - DON'T I DO THAT ON PREVIOUS PAGE ???????? MAYBE IT'S BETTER on this page?
        home = Home(driver)
        print('Loading home page...')
        if home.get_signIn.is_displayed():
            print('Authentication Link displaying', '(' + home.get_signIn.text + ')')
            home.get_signIn.click()
            driver.implicitly_wait(5)   # wait until page has loaded

        # calling registration page object to proceed with registration flow
        auth = Authentication(driver)
        print('Loading authentication page...')
        driver.implicitly_wait(5)

        # this implies is_displayed()
        if auth.get_auth_txt.text == 'AUTHENTICATION':
            print('Authentication page loaded.', '(page heading:', auth.get_auth_txt.text + ')')
        else:
            print('Authentication page not loaded')
        try:
            auth.create_account('mtest@mtest.com')
            auth.submit_create_acc()
        except Exception as e:
            print("Exception occurred ", e)

        # verify that next page loads
        # calling registration page object to proceed with registration flow
        reg = Registration(driver)
        driver.implicitly_wait(5)
        print('Loading registration page...')

        # this implies is_displayed()
        if reg.get_reg_txt.text == 'YOUR PERSONAL INFORMATION':
            print('Registration page loaded.', '(page heading: ', reg.get_reg_txt.text + ')')
        else:
            print('Registration page not loaded')
