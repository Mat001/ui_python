"""category page"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from page_object.locators import Locator


class Category:

    def __init__(self, driver):
        self.driver = driver

        try:
            self.product_shirt = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                  Locator.product_shirt)))
        except (NoSuchElementException, InvalidSelectorException) as e:
            print(e)

    # get
    @property
    def get_product_shirt(self):
        return self.product_shirt

    # methods
    def select_blue_tshirt(self):
        self.driver.execute_script("window.scrollBy(0, 500);")
        scroll = ActionChains(self.driver).move_to_element(self.product_shirt)
        scroll.perform()

        self.product_shirt.click()



