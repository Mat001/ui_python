"""home page"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException

from page_object.locators import Locator


class Home:

    def __init__(self, driver):
        self.driver = driver

        try:
            self.logo = driver.find_element(By.CSS_SELECTOR, Locator.logo)
            self.signIn = driver.find_element(By.CSS_SELECTOR, Locator.signIn)
            self.contact_us = driver.find_element(By.CSS_SELECTOR, Locator.contact_us)
        except (NoSuchElementException, InvalidSelectorException) as e:
            print(e)

    # get
    @property
    def get_logo(self):
        return self.logo

    @property
    def get_signIn(self):
        return self.signIn

    @property
    def get_contact_us(self):
        return self.contact_us

    # methods
    def click_signIn(self):
        self.signIn.click()
