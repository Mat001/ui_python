"""Locators for each page"""


class Locator:

    # home
    home_page_title = 'My Store'
    logo = '.logo'
    signIn = '.login'
    contact_us = '#contact-link > a:nth-child(1)'

    # authentication - choose register or login
    auth_page_title = 'Login - My Store'
    auth_txt = '.page-heading'
    email_create = '#email_create'
    submit_create = '#SubmitCreate'
    email_login = '#email'
    passw_login = '#passwd'
    submit_login = '#SubmitLogin'

    # registration
    reg_page_title = 'Login - My Store'
    reg_txt = 'div.account_creation:nth-child(1) > h3:nth-child(1)'
    entitlement_male = '#id_gender1'
    entitlement_female = '#id_gender2'
    fname = '#customer_firstname'
    lname = '#customer_lastname'
    email = '#email'
    passw_create = '#passwd'
    day = '#days'
    month = '#months'
    year = '#years'
    fname_address = '#firstname'
    lname_address = '#lastname'
    company = '#company'
    address1 = '#address1'
    address2 = '#address2'
    city = '#city'
    state = '#id_state'  # dropdown - select state
    zip = '#postcode'
    country = '#id_country' # dropdown - select united states
    phone_mobile = '#phone_mobile'
    address_alias = '#alias'
    submit_account = '#submitAccount'

    # my account
    myaccount_text = '.page-heading'
    page_url = 'http://automationpractice.com/index.php?controller=my-account'
    women_link_text = 'Women'

    # category
    product_shirt = '#color_2'    # pick shirt with id color 2

    # product
    quantity = '#quantity_wanted'
    size = '#group_1'   # dropdown, select size
    button_add_to_cart = '#add_to_cart > button'

    # selection pop up
    popup_prod_confirm = 'layer_cart_product_title'
    proceed_popup = '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a'

    # order summary
    unit_price = 'price'    # class
    quantity_order = '//*[@id="product_1_4_0_113190"]/td[5]/input[2]'   # xpath
    # quantity_order = 'cart_quantity_input form-control grey'    # class
    total_price_products = 'total_product_price_1_4_113190'    # id
    shipping = 'total_shipping'     # id
    tax = 'total_tax'   # id
    total_price = 'total_price'     # id
    proceed_to_address = '//*[@id="center_column"]/p[2]/a[1]'

    # order summary - address
    delivery_address = 'address_address1 address_address2'  # class - use to verify
    biling_fullname = 'address_firstname address_lastname'  # class - use to verify
    proceed_to_shipping = 'processAddress'  # name

    # order summary - shipping
    carrier_title = 'carrier_title' # class - get text to match 'Choose a shipping option for this address: Jeany'
    tos_checkbox = 'cgv'    # id
    proceed_to_payment = 'processCarrier'   # name

    # order summary - payment
    bankwire = 'bankwire'   # class


    # oredr summary - pre-confirming payment
    bankwire_text = 'page-subheading'   # class - use to confirm on the page
    button_confirm_order = 'button btn btn-default button-medium'   # class

    # order confirmation
    order_confirmation_text = 'page-heading'    # class - use to assert text is visible:
    #  ORDER CONFIRMATION
    confirmed_total = '//*[@id="center_column"]/div/span/strong'    # compare with
    # stored total_price
    bankwire_account_holder = '//*[@id="center_column"]/div/strong[1]'  # should match Pradeep Macharla
    button_back_to_orders = 'button-exclusive btn btn-default'  # class

    # order history
    history_text = '//*[@id="center_column"]/p' # confirm on history page by matching text

























