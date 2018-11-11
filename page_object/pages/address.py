"""address page"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, \
    InvalidSelectorException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_object.locators import Locator


class Address:

    def __init__(self, driver):
        self.driver = driver

        try:
            self.delivery_address = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, Locator.delivery_address)))
            self.billing_full_name = driver.find_element(By.CSS_SELECTOR,
                                                         Locator.billing_fullname)
            self.proceed_to_shipping = driver.find_element(By.NAME,
                                                           Locator.proceed_to_shipping)
        except (NoSuchElementException, InvalidSelectorException) as e:
            print(e)

    # get
    @property
    def get_delivery_address(self):
        return self.delivery_address

    @property
    def get_billing_full_name(self):
        return self.billing_full_name

    @property
    def get_delivery_address_text(self):
        return self.delivery_address.get_attribute('innerText').strip()

    @property
    def get_billing_full_name_text(self):
        return self.billing_full_name.get_attribute('innerText').strip()

    # methods
    def proceed(self):
        self.proceed_to_shipping.click()












































