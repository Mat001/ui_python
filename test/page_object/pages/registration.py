"""registration page"""

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common.exceptions import TimeoutException, NoSuchElementException, InvalidSelectorException
from test.page_object.locators import Locator


class Registration:

    def __init__(self, driver):
        self.driver = driver

        try:
            self.reg_txt = driver.find_element(By.CSS_SELECTOR, Locator.reg_txt)
            self.entitlement_male = driver.find_element(By.CSS_SELECTOR, Locator.entitlement_male)
            self.entitlement_female = driver.find_element(By.CSS_SELECTOR, Locator.entitlement_female)
            self.fname = driver.find_element(By.CSS_SELECTOR, Locator.fname)
            self.lname = driver.find_element(By.CSS_SELECTOR, Locator.lname)
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
    def fill_reg_form(self, fname_param, lname_param):
        self.entitlement_female.click()
        self.fname.clear()
        self.fname.send_keys(fname_param)
        self.lname.clear()
        self.lname.send_keys(lname_param)
        self.passw_create.clear()


    def submit_reg(self):
        self.submit_account.click()








































