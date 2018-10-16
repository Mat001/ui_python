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
    # email field should be prepopulated (can test this with assertion)
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



