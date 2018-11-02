from test.test_base.environment_setup import EnvironmentSetupSmoke
from test.page_object.locators import Locator
from test.page_object.pages.home import Home
from test.page_object.pages.authentication import Authentication
from test.page_object.pages.registration import Registration
from test.page_object.pages.myaccount import MyAccount
from test.page_object.pages.category import Category
from test.page_object.pages.product import Product
from test.page_object.pages.selection_popup import SelectionPopUp
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

        self.assertEquals(auth.get_auth_txt.text, 'AUTHENTICATION', msg='AUTHENTICATION text not found or displayed.')
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
            reg.fill_reg_form(entitlement_param='2', fname_param='Jeanfirst',
                              lname_param='Testlast', passw_param='12345', day='25',
                              month='6', year='2018', fname_address_param='Jeanfirst',
                              lname_address_param='Testlast', company='Fashion Inc.',
                              address1_param='1 Market St.', address2_param='Suite 5',
                              city_param='Denver', state_param='Colorado',
                              zip_param='33333', country_param='United States',
                              phone_mobile_param='5556667777', alias_param='Jeany')

            reg.submit_reg()
        except Exception as e:
            print(e)

        print('\n#   MY ACCOUNT PAGE    ####################\n')

        myacc = MyAccount(driver)
        driver.implicitly_wait(10)
        print('Loading my account page...')

        # verify we're on my account page
        self.assertEquals(driver.current_url, Locator.page_url,
                          msg='Current page URL incorrect.')
        self.assertEquals(myacc.get_myaccount_text.text, 'MY ACCOUNT',
                          msg='MY ACCOUNT text not seen on this page.')
        print('My Account page confirmed.')
        myacc.click_women()

        print('\n#   CATEGORIES PAGE    ####################\n')

        cat = Category(driver)
        driver.implicitly_wait(10)
        print('Loading category page...')

        # on Women page click blue color on product Faded Short Sleeve T-shirts to
        cat.select_blue_tshirt()

        print('\n#   PRODUCT PAGE    ####################\n')
        product = Product(driver)
        driver.implicitly_wait(10)
        product.add_to_cart(quantity=2, size='M')

        print('\n#   SELECTION POP-UP PAGE    ####################\n')
        popup = SelectionPopUp(driver)
        # wait for ajax pop-up window to appear - done in page object with EC wait
        self.assertTrue(popup.get_prod_confirm.is_displayed())
        self.assertEqual(popup.get_prod_confirm.get_attribute(
            'innerText'), 'Faded Short Sleeve T-shirts')
        self.assertTrue(popup.get_proceed_button.is_displayed())
        popup.proceed()

        print('\n#   ORDER SUMMARY PAGE    ####################\n')
        driver.implicitly_wait(10)
        # store price, quantity and total


        # click proceed to checkout

        # wait for address page to load (sign-in page is skipped because already signed
        #  in)
        # click proceed to checkout

        # wait for order-shipping page to load
        # check checkbox Terms of service

        # wait for order-payment page to load
        # assert unit price x quantity matches the total - again
        # click on Pay by bank wire
        # same page-payment, click Confirm my order
        # same page-payment assert confirmation info says Your order on My Store is
        # complete.
        # assert total is unit price + quantity + tax

        # click on Back to Orders
        # assert text Here are the orders you've placed since your account was created.







if __name__ == '__main__':
    unittest.main(warnings='ignore')
