"""history page"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, \
    InvalidSelectorException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_object.locators import Locator


class History:

    def __init__(self, driver):
        self.driver = driver

        try:
            self.history_text = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                  Locator.history_text)))
        except (NoSuchElementException, InvalidSelectorException, TimeoutException) as e:
            print(e)

    # get
    @property
    def get_history_text(self):
        return self.history_text

    # values
    @property
    def get_hist_text_value(self):
        return self.history_text.get_attribute('innerText').strip()
