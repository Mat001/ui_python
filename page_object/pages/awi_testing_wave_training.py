"""home page"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException

from page_object.locators import Locator


class AwiTestingWaveTraining:

    def __init__(self, driver):
        self.driver = driver

        try:
            self.training_room_link = driver.find_element(By.LINK_TEXT, Locator.enter_wave_training)
        except (NoSuchElementException, InvalidSelectorException) as e:
            print(e)

    # methods
    def click_enter_training_room(self):
        self.training_room_link.click()
