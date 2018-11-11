"""confirmation page"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, \
    InvalidSelectorException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_object.locators import Locator


class Confirmation:

    def __init__(self, driver):
        self.driver = driver

        try:
            self.confirmation_text = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME,
                                                  Locator.confirmation_text)))
            self.confirmed_total = driver.find_element(By.XPATH,
                                                       Locator.confirmed_total)
            self.back = driver.find_element(By.CSS_SELECTOR,
                                            Locator.button_back_to_orders)
        except (NoSuchElementException, InvalidSelectorException, TimeoutException) as e:
            print(e)

    # get
    @property
    def get_conf_text(self):
        return self.confirmation_text

    @property
    def get_confirmed_total(self):
        return self.confirmed_total

    # values
    @property
    def get_conf_text_value(self):
        return self.confirmation_text.get_attribute('innerText').strip()

    @property
    def get_confirmed_total_value(self):
        return float(self.confirmed_total.get_attribute('innerText')[1:])

    # methods
    def back_to_orders(self):
        self.back.click()
