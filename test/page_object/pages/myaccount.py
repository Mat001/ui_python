"""my account page"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, InvalidSelectorException

from test.page_object.locators import Locator


class MyAccount:

    def __init__(self, driver):
        self.driver = driver

        try:
            self.page_url = driver.current_url
            self.myaccount_text = driver.find_element(By.CSS_SELECTOR, Locator.myaccount_text)
            self.women_link_text = WebDriverWait(driver, 10).until \
                (EC.element_to_be_clickable((By.LINK_TEXT, Locator.women_link_text)))
        except (NoSuchElementException, InvalidSelectorException) as e:
            print(e)

    # get
    @property
    def get_page_url(self):
        return self.page_url

    @property
    def get_myaccount_text(self):
        return self.myaccount_text

    @property
    def get_women_link_text(self):
        return self.women_link_text

    # methods
    def click_women(self):
        self.women_link_text.click()
