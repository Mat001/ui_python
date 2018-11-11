"""shipping page"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, \
    InvalidSelectorException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_object.locators import Locator


class Shipping:

    def __init__(self, driver):
        self.driver = driver

        try:
            self.tos_checkbox = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, Locator.tos_checkbox)))
            self.proceed_to_payment = driver.find_element(By.NAME,
                                                          Locator.proceed_to_payment)
        except (NoSuchElementException, InvalidSelectorException) as e:
            print(e)

    # get
    @property
    def get_tos_checkbox(self):
        return self.tos_checkbox

    # methods
    def check_tos(self):
        self.tos_checkbox.click()

    def proceed(self):
        self.proceed_to_payment.click()












































