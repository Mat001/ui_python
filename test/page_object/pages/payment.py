"""payment page"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, \
    InvalidSelectorException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test.page_object.locators import Locator


class Payment:

    def __init__(self, driver):
        self.driver = driver

        try:
            self.bankwire_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, Locator.bankwire)))
        except (NoSuchElementException, InvalidSelectorException, TimeoutException) as e:
            print(e)

    # methods
    def proceed(self):
        self.bankwire_button.click()