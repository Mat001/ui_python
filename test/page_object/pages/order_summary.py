"""order summary page"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, \
    InvalidSelectorException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test.page_object.locators import Locator


class OrderSummary:

    def __init__(self, driver):
        self.driver = driver

        try:
            self.unit_price = driver.find_element(By.XPATH, Locator.unit_price)
            # use EC only on this element, other will be visible as well
            self.total_price_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, Locator.total_price_products)))
            self.shipping = driver.find_element(By.ID, Locator.shipping)
            self.tax = driver.find_element(By.ID, Locator.tax)
            self.total_price = driver.find_element(By.ID, Locator.total_price)
            self.proceed_to_address = driver.find_element(By.XPATH,
                                                          Locator.proceed_to_address)
        except (NoSuchElementException, InvalidSelectorException) as e:
            print(e)

    # get
    @property
    def get_unit_price(self):
        return self.unit_price

    @property
    # def get_quantity_order(self):
    #     return self.quantity_order

    @property
    def get_total_price_products(self):
        return self.total_price_products

    @property
    def get_shipping(self):
        return self.shipping

    @property
    def get_tax(self):
        return self.tax

    @property
    def get_total_price(self):
        return self.total_price

    # values
    @property
    def get_unit_price_value(self):
        return self.unit_price.get_attribute('innerText').strip()

    # @property
    # def get_quantity_order_value(self):
    #     return self.quantity_order.get_attribute('value')

    @property
    def get_total_price_products_value(self):
        return self.total_price_products.get_attribute('innerText')

    @property
    def get_shipping_value(self):
        return self.shipping.get_attribute('innerText')

    @property
    def get_tax_value(self):
        return self.tax.get_attribute('innerText')

    @property
    def get_total_price_value(self):
        return self.total_price.get_attribute('innerText')

    # methods
    def proceed(self):
        self.proceed_to_address.click()

    def calculate_total_price(self, quantity):
        unit_price = float(self.get_unit_price_value[1:])
        tax = float(self.get_tax_value[1:])
        shipping = float(self.get_shipping_value[1:])

        return (unit_price * quantity) + tax + shipping

    def total_price_value(self):
        return float(self.get_total_price_value[1:])











































