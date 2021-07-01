"""Locators for each page"""

class Locator:

    # login page
    login_page_title = 'Foundation Virtual Space'
    username = 'user_name'      # name
    password = 'password'       # name
    login_button = 'log_in'     # name

    # home page
    awi_testing_wave_training = 'AWI Testing Wave Training'

    # AWI Testing Wave Training page
    enter_wave_training = '>>> Enter Wave Training <<<'

    # Foyer
    process_user = 'pop-user'
    queue_total = '.queue-total'

    # Portal
    grant_access = 'access-granted'
    picture = 'idpic'

    # home page
    earth_log_out = '/html/body/table/tbody/tr/td[2]/table[2]/tbody/tr/td[4]/a/img'



# class Locator:
#
#     # home
#     home_page_title = 'My Store'
#     logo = '.logo'
#     signIn = '.login'
#     contact_us = '#contact-link > a:nth-child(1)'
#
#     # authentication - choose register or login
#     auth_page_title = 'Login - My Store'
#     auth_txt = '.page-heading'
#     email_create = '#email_create'
#     submit_create = '#SubmitCreate'
#     email_login = '#email'
#     passw_login = '#passwd'
#     submit_login = '#SubmitLogin'
#
#     # registration
#     reg_page_title = 'Login - My Store'
#     reg_txt = 'div.account_creation:nth-child(1) > h3:nth-child(1)'
#     entitlement_male = '#id_gender1'
#     entitlement_female = '#id_gender2'
#     fname = '#customer_firstname'
#     lname = '#customer_lastname'
#     email = '#email'
#     passw_create = '#passwd'
#     day = '#days'
#     month = '#months'
#     year = '#years'
#     fname_address = '#firstname'
#     lname_address = '#lastname'
#     company = '#company'
#     address1 = '#address1'
#     address2 = '#address2'
#     city = '#city'
#     state = '#id_state'  # dropdown - select state
#     zip = '#postcode'
#     country = '#id_country' # dropdown - select united states
#     phone_mobile = '#phone_mobile'
#     address_alias = '#alias'
#     submit_account = '#submitAccount'
#
#     # my account
#     myaccount_text = '.page-heading'
#     page_url = 'http://automationpractice.com/index.php?controller=my-account'
#     women_link_text = 'Women'
#
#     # category
#     product_shirt = '#color_2'    # pick shirt with id color 2
#
#     # product
#     quantity = '#quantity_wanted'
#     size = '#group_1'   # dropdown, select size
#     button_add_to_cart = '#add_to_cart > button'
#
#     # selection pop up
#     popup_prod_confirm = 'layer_cart_product_title'
#     proceed_popup = '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a'
#
#     # order summary
#     unit_price = "// *[contains( @ id, 'product_price_')]/span"
#     quantity_order = '#product_1_4_0_113198 > td.cart_quantity.text-center > ' \
#                      'input.cart_quantity_input.form-control.grey'    # css
#     total_price_products = 'total_product'    # id
#     shipping = 'total_shipping'     # id
#     tax = 'total_tax'   # id
#     total_price = 'total_price'     # id
#     proceed_to_address = '//*[@id="center_column"]/p[2]/a[1]'
#
#     # address
#     delivery_address = '#address_delivery > li.address_address1.address_address2'
#     billing_fullname = '#address_invoice > li.address_firstname.address_lastname'
#     proceed_to_shipping = 'processAddress'  # name
#
#     # shipping
#     tos_checkbox = 'cgv'    # id
#     proceed_to_payment = 'processCarrier'   # name
#
#     # payment
#     bankwire = 'bankwire'   # class
#
#     # pre-confirmation
#     bankwire_text = 'page-subheading'   # class - use to confirm on the page
#     button_confirm_order = '#cart_navigation > button'   # css
#
#     # order confirmation
#     confirmation_text = 'page-heading'    # class - use to assert text is visible:
#     confirmed_total = '//*[@id="center_column"]/div/span/strong'    # compare with stored
#     button_back_to_orders = '#center_column > p > a'  # css
#
#     # order history
#     history_text = '#center_column > h1'
#     presence_of_invoice = '//*[@id="order-list"]/tbody/tr[1]/td[6]/a'
