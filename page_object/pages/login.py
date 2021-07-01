"""home page"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException

from page_object.locators import Locator


class Login:

    def __init__(self, driver):
        self.driver = driver

        try:
            self.username = driver.find_element(By.NAME, Locator.username)      # TODO - fix - not finding this locator
            self.password = driver.find_element(By.NAME, Locator.password)
            self.login_button = driver.find_element(By.NAME, Locator.login_button)
        except (NoSuchElementException, InvalidSelectorException) as e:
            print(e)

    @property
    def get_username(self):
        return self.username

    @property
    def get_password(self):
        return self.password

    # methods
    def login_username(self, user):
        self.username.clear()
        self.username.send_keys(user)

    def login_passw(self, passw):
        self.password.clear()
        self.password.send_keys(passw)

    def click_log_in(self):
        self.login_button.click()
