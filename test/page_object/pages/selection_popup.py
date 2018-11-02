"""selection pop up page"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, \
    InvalidSelectorException, ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test.page_object.locators import Locator


class SelectionPopUp:

    def __init__(self, driver):
        self.driver = driver

        try:
            # wait for ajax popup to fully load and element is visible
            self.popup_prod_confirm = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, Locator.popup_prod_confirm)))
            # wait for ajax popup to fully load and element is visible
            self.proceed_popup = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Locator.proceed_popup)))
        except (NoSuchElementException, InvalidSelectorException, TimeoutException,
                ElementNotInteractableException) as e:
            print(e)

    # get
    @property
    def get_prod_confirm(self):
        return self.popup_prod_confirm

    @property
    def get_proceed_button(self):
        return self.proceed_popup

    # methods
    def proceed(self):
        self.get_proceed_button.click()

