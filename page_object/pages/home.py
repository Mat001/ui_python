"""home page"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException

from page_object.locators import Locator


class Home:

    def __init__(self, driver):
        self.driver = driver

        try:
            self.awi_testing_wave_training_link = driver.find_element(By.LINK_TEXT, Locator.awi_testing_wave_training)
        except (NoSuchElementException, InvalidSelectorException) as e:
            print(e)


    # methods
    def click_awi_testing_wave_training_link(self):
        self.awi_testing_wave_training_link.click()
