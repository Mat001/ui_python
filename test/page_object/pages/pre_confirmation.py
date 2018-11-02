"""pre-confirmation page"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, \
    InvalidSelectorException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test.page_object.locators import Locator


class PreConfirmation:

    def __init__(self, driver):
        self.driver = driver

        try:
            self.confirm_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                  Locator.button_confirm_order)))
        except (NoSuchElementException, InvalidSelectorException) as e:
            print(e)

    # methods
    def proceed(self):
        self.confirm_button.click()