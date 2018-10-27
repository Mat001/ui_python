"""category page"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, InvalidSelectorException

from test.page_object.locators import Locator


class Category:

    def __init__(self, driver):
        self.driver = driver

        try:
            pass
        except (NoSuchElementException, InvalidSelectorException) as e:
            print(e)

    # get

    # methods

