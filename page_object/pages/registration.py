"""Registration page"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException
from page_object.locators import Locator


class Registration:

    def __init__(self, driver):
        self.driver = driver

        try:
            self.reg_txt = driver.find_element(By.CSS_SELECTOR, Locator.reg_txt)
            self.entitlement_male = driver.find_element(By.CSS_SELECTOR, Locator.entitlement_male)
            self.entitlement_female = driver.find_element(By.CSS_SELECTOR, Locator.entitlement_female)
            self.fname = driver.find_element(By.CSS_SELECTOR, Locator.fname)
            self.lname = driver.find_element(By.CSS_SELECTOR, Locator.lname)
            self.email = driver.find_element(By.CSS_SELECTOR, Locator.email)
            self.passw_create = driver.find_element(By.CSS_SELECTOR, Locator.passw_create)
            self.day = driver.find_element(By.CSS_SELECTOR, Locator.day)
            self.month = driver.find_element(By.CSS_SELECTOR, Locator.month)
            self.year = driver.find_element(By.CSS_SELECTOR, Locator.year)
            self.fname_address = driver.find_element(By.CSS_SELECTOR, Locator.fname_address)
            self.lname_address = driver.find_element(By.CSS_SELECTOR, Locator.lname_address)
            self.company = driver.find_element(By.CSS_SELECTOR, Locator.company)
            self.address1 = driver.find_element(By.CSS_SELECTOR, Locator.address1)
            self.address2 = driver.find_element(By.CSS_SELECTOR, Locator.address2)
            self.city = driver.find_element(By.CSS_SELECTOR, Locator.city)
            self.state = driver.find_element(By.CSS_SELECTOR, Locator.state)
            self.zip = driver.find_element(By.CSS_SELECTOR, Locator.zip)
            self.country = driver.find_element(By.CSS_SELECTOR, Locator.country)
            self.phone_mobile = driver.find_element(By.CSS_SELECTOR, Locator.phone_mobile)
            self.address_alias = driver.find_element(By.CSS_SELECTOR, Locator.address_alias)
            self.submit_account = driver.find_element(By.CSS_SELECTOR, Locator.submit_account)
        except (NoSuchElementException, InvalidSelectorException) as e:
            print('Exception ', e)

    # get
    @property
    def get_reg_txt(self):
        return self.reg_txt

    @property
    def get_entitlement_male(self):
        return self.entitlement_male

    @property
    def get_entitlement_female(self):
        return self.entitlement_female

    @property
    def get_fname(self):
        return self.fname

    @property
    def get_lname(self):
        return self.lname

    @property
    def get_passw_create(self):
        return self.passw_create

    @property
    def get_day(self):
        return self.day

    @property
    def get_month(self):
        return self.month

    @property
    def get_year(self):
        return self.year

    @property
    def get_fname_address(self):
        return self.fname_address

    @property
    def get_lname_address(self):
        return self.lname_address

    @property
    def get_company(self):
        return self.company

    @property
    def get_address1(self):
        return self.address1

    @property
    def get_address2(self):
        return self.address2

    @property
    def get_city(self):
        return self.city

    @property
    def get_state(self):
        return self.state

    @property
    def get_zip(self):
        return self.zip

    @property
    def get_country(self):
        return self.country

    @property
    def get_phone_mobile(self):
        return self.phone_mobile

    @property
    def get_address_alias(self):
        return self.address_alias

    # methods
    def verify_email_prepopulated(self, chosen_at_acc_creation):
        currently_displayed = self.email.get_attribute('value')
        assert currently_displayed == chosen_at_acc_creation

    def choose_entitlement(self, gender):
        if gender == 'male':
            return self.entitlement_male
        elif gender == 'female':
            return self.entitlement_female
        else:
            return None

    def select_day(self, day):
        selected_day = Select(self.day).select_by_value(day)
        return selected_day

    def select_month(self, month):
        selected_month = Select(self.month).select_by_value(month)
        return selected_month

    def select_year(self, year):
        selected_year = Select(self.year).select_by_value(year)
        return selected_year

    def select_state(self, state):
        selected_state = Select(self.state).select_by_visible_text(state)
        return selected_state

    def select_country(self, country):
        selected_country = Select(self.country).select_by_visible_text(country)
        return selected_country

    def fill_reg_form(self, entitlement_param, fname_param, lname_param, passw_param, day, month, year,
                      fname_address_param, lname_address_param, company, address1_param, address2_param,
                      city_param, state_param, zip_param, country_param, phone_mobile_param, alias_param):
        self.choose_entitlement(entitlement_param)
        self.fname.clear()
        self.fname.send_keys(fname_param)
        self.lname.clear()
        self.lname.send_keys(lname_param)
        self.passw_create.clear()
        self.passw_create.send_keys(passw_param)
        self.lname.click()  # click out of passw box because small window covers date dropdowns
        self.select_day(day)
        self.select_month(month)
        self.select_year(year)
        self.fname_address.clear()
        self.fname_address.send_keys(fname_address_param)
        self.lname_address.clear()
        self.lname_address.send_keys(lname_address_param)
        self.company.clear()
        self.company.send_keys(company)
        self.address1.clear()
        self.address1.send_keys(address1_param)
        self.address2.clear()
        self.address2.send_keys(address2_param)
        self.city.clear()
        self.city.send_keys(city_param)
        self.select_state(state_param)
        self.zip.clear()
        self.zip.send_keys(zip_param)
        self.select_country(country_param)
        self.phone_mobile.clear()
        self.phone_mobile.send_keys(phone_mobile_param)
        self.address_alias.clear()
        self.address_alias.send_keys(alias_param)

    def submit_reg(self):
        self.submit_account.click()








































