from test.test_base.environment_setup import EnvironmentSetupSmoke
from test.page_object.locators import Locator
from test.test_data.data import TestData
from test.page_object.pages.home import Home
from test.page_object.pages.authentication import Authentication
from test.page_object.pages.registration import Registration
from test.page_object.pages.myaccount import MyAccount
from test.page_object.pages.category import Category
from test.page_object.pages.product import Product
from test.page_object.pages.selection_popup import SelectionPopUp
from test.page_object.pages.order_summary import OrderSummary
from test.page_object.pages.address import Address
from test.page_object.pages.shipping import Shipping
from test.page_object.pages.payment import Payment
from test.page_object.pages.pre_confirmation import PreConfirmation
from test.page_object.pages.confirmation import Confirmation
from test.page_object.pages.history import History
import unittest


class Smoke(EnvironmentSetupSmoke):

    def test_application_flow(self):

        # Using the driver instance created in EnvironmentSetupSmoke
        driver = self.driver
        url = self.url
        td = TestData()

        # randomize email
        import time
        email = 'mtest' + str(int(time.time())) + '@mtest.com'
        print('Email: ', email)

        #################################################################################
        print('\n#   HOME PAGE    ####################\n')
        #################################################################################
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

        self.assertTrue(home.get_contact_us.is_displayed(),
                        msg='ContactUs link NOT displayed.')
        print('Found Contact Us link - ', home.get_contact_us.get_attribute('href'))

        self.assertEqual(url, driver.current_url)
        print('URL successfully points to Home page -', driver.current_url)

        #################################################################################
        print('\n#   AUTHENTICATION PAGE    ####################\n')
        #################################################################################
        self.assertTrue(home.get_signIn.is_displayed())
        print('Authentication Link displaying', '(' + home.get_signIn.text + ')')
        home.click_signIn()
        driver.implicitly_wait(5)  # wait until page has loaded

        # calling authentication page object to proceed with creating account flow
        auth = Authentication(driver)
        print('Loading authentication page...')
        driver.implicitly_wait(5)

        self.assertEquals(auth.get_auth_txt.text, 'AUTHENTICATION',
                          msg='AUTHENTICATION text not found or displayed.')
        print('Authentication page loaded.', '(page heading:', auth.get_auth_txt.text + ')')
        try:
            auth.create_account(email)
            auth.submit_create_acc()
        except Exception as e:
            print(e)

        #################################################################################
        print('\n#   REGISTRATION PAGE    ####################\n')
        #################################################################################
        # calling registration page object to proceed with registration flow
        reg = Registration(driver)
        driver.implicitly_wait(10)
        print('Loading registration page...')

        self.assertTrue(reg.get_reg_txt.text == 'YOUR PERSONAL INFORMATION',
                        msg='YOUR PERSONAL INFORMATION text not found.')
        print('Registration page loaded.', '(page heading: ', reg.get_reg_txt.text + ')')
        reg.verify_email_prepopulated(email)

        try:
            reg.fill_reg_form(entitlement_param=td.entitlement_param,
                              fname_param=td.fname_param,
                              lname_param=td.lname_param, passw_param=td.passw_param,
                              day=td.day, month=td.month, year=td.year,
                              fname_address_param=td.fname_address_param,
                              lname_address_param=td.lname_address_param,
                              company=td.company,
                              address1_param=td.address1_param,
                              address2_param=td.address2_param,
                              city_param=td.city_param, state_param=td.state_param,
                              zip_param=td.zip_param, country_param=td.country_param,
                              phone_mobile_param=td.phone_mobile_param,
                              alias_param=td.alias_param)

            reg.submit_reg()
        except Exception as e:
            print(e)

        #################################################################################
        print('\n#   MY ACCOUNT PAGE    ####################\n')
        #################################################################################
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

        #################################################################################
        print('\n#   CATEGORIES PAGE    ####################\n')
        #################################################################################
        cat = Category(driver)
        driver.implicitly_wait(10)
        print('Loaded category page.')

        # on Women page click blue color on product Faded Short Sleeve T-shirts to
        cat.select_blue_tshirt()

        #################################################################################
        print('\n#   PRODUCT PAGE    ####################\n')
        #################################################################################
        product = Product(driver)
        driver.implicitly_wait(10)
        product.add_to_cart(quantity=td.quantity, size=td.size)
        print('Selected quantity and size.')

        #################################################################################
        print('\n#   SELECTION POP-UP PAGE    ####################\n')
        #################################################################################
        popup = SelectionPopUp(driver)
        # wait for ajax pop-up window to appear - done in page object with EC wait
        self.assertTrue(popup.get_prod_confirm.is_displayed())
        self.assertEqual(popup.get_prod_confirm.get_attribute(
            'innerText'), 'Faded Short Sleeve T-shirts')
        self.assertTrue(popup.get_proceed_button.is_displayed())
        print('Presence of selected product confirmed.')
        popup.proceed()

        #################################################################################
        print('\n#   ORDER SUMMARY PAGE    ####################\n')
        #################################################################################
        order_sum = OrderSummary(driver)
        driver.implicitly_wait(10)
        print('Unit price', order_sum.get_unit_price_value)
        print('Quantity order', td.quantity)  # actual user selection
        print('Shipping', order_sum.get_shipping_value)
        print('Total price products', order_sum.get_total_price_products_value)
        print('Tax', order_sum.get_tax_value)
        print('Total_price_value', order_sum.get_total_price_value)
        self.assertEqual(order_sum.calculate_total_price(td.quantity),
                         order_sum.total_price_value())
        print('Calculated total price validated.')
        total_price = order_sum.total_price_value()
        order_sum.proceed()

        #################################################################################
        print('\n#   ADDRESS    ####################\n')
        #################################################################################
        order_addr = Address(driver)
        self.assertEqual(order_addr.get_delivery_address_text,
                         td.address1_param + ' ' + td.address2_param)

        self.assertEqual(order_addr.get_billing_full_name_text,
                         td.fname_address_param + ' ' + td.lname_address_param)
        print('Delivery address validated.')
        print('Billing name validated.')
        order_addr.proceed()

        #################################################################################
        print('\n#   SHIPPING    ####################\n')
        #################################################################################
        shipping = Shipping(driver)
        shipping.check_tos()
        print('Terms of service accepted.')
        shipping.proceed()
        print('Proceed...')

        #################################################################################
        print('\n#   PAYMENT    ####################\n')
        #################################################################################
        payment = Payment(driver)
        payment.proceed()
        print('Proceed...')

        #################################################################################
        print('\n#   PRE-CONFIRMATION    ####################\n')
        #################################################################################
        preconf = PreConfirmation(driver)
        print('Proceed...')
        preconf.proceed()

        #################################################################################
        print('\n#   CONFIRMATION    ####################\n')
        #################################################################################
        conf = Confirmation(driver)
        self.assertEqual(conf.get_conf_text_value, 'ORDER CONFIRMATION')
        self.assertEqual(conf.get_confirmed_total_value, total_price)
        print('Total price confirmed.')
        conf.back_to_orders()
        print('Proceed...')

        #################################################################################
        print('\n#   ORDER HISTORY    ####################\n')
        #################################################################################
        history = History(driver)
        self.assertEqual(history.get_hist_text_value, 'ORDER HISTORY')
        print('Order history page validated.')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
