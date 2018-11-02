"""category page"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, InvalidSelectorException

from test.page_object.locators import Locator


class Category:

    def __init__(self, driver):
        self.driver = driver

        try:
            self.product_shirt = driver.find_element(By.CSS_SELECTOR,
                                                    Locator.product_shirt)
        except (NoSuchElementException, InvalidSelectorException) as e:
            print(e)

    # get
    @property
    def get_product_shirt(self):
        return self.product_shirt

    # methods
    def select_blue_tshirt(self):
        self.product_shirt.click()



