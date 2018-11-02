"""product page"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, InvalidSelectorException
from selenium.webdriver.support.ui import Select

from test.page_object.locators import Locator


class Product:

    def __init__(self, driver):
        self.driver = driver

        try:
            self.quantity = driver.find_element(By.CSS_SELECTOR, Locator.quantity)
            self.size = driver.find_element(By.CSS_SELECTOR, Locator.size)
            self.button_add_to_cart = driver.find_element(By.CSS_SELECTOR,
                                                          Locator.button_add_to_cart)
        except (NoSuchElementException, InvalidSelectorException) as e:
            print(e)

    # get
    @property
    def get_quantity(self):
        return self.quantity

    @property
    def get_size(self):
        return self.size

    @property
    def get_button_add_to_cart(self):
        return self.button_add_to_cart

    # methods
    def enter_quantity(self, quantity):
        self.quantity.clear()
        self.quantity.send_keys(quantity)

    def select_size(self, size):
        selected_size = Select(self.size).select_by_visible_text(size)
        return selected_size

    def add_to_cart(self, quantity, size):
        self.enter_quantity(quantity)
        self.select_size(size)
        self.button_add_to_cart.click()






