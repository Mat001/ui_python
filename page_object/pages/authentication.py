"""Authentication page"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException

from page_object.locators import Locator


class Authentication:

    def __init__(self, driver):
        self.driver = driver

        try:
            self.auth_text = driver.find_element(By.CSS_SELECTOR, Locator.auth_txt)
            self.email_create = driver.find_element(By.CSS_SELECTOR, Locator.email_create)
            self.submit_create = driver.find_element(By.CSS_SELECTOR, Locator.submit_create)
            self.email_login = driver.find_element(By.CSS_SELECTOR, Locator.email_login)
            self.passw_login = driver.find_element(By.CSS_SELECTOR, Locator.passw_login)
            self.submit_login = driver.find_element(By.CSS_SELECTOR, Locator.submit_login)
        except (NoSuchElementException, InvalidSelectorException) as e:
            print(e)

    # get
    @property
    def get_auth_txt(self):
        return self.auth_text

    @property
    def get_email_create(self):
        return self.email_create

    @property
    def get_submit_create(self):
        return self.submit_create

    @property
    def get_email_login(self):
        return self.email_login

    @property
    def get_passw_login(self):
        return self.passw_login

    # methods
    def create_account(self, email):
        self.email_create.clear()
        self.email_create.send_keys(email)

    def login_email(self, email):
        self.email_login.clear()
        self.email_login.send_keys(email)

    def login_passw(self, passw):
        self.passw_login.clear()
        self.passw_login.send_keys(passw)

    def submit_create_acc(self):
        self.submit_create.click()

    def submit_login_acc(self):
        self.submit_login.click()














