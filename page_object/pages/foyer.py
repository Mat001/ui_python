"""home page"""

import datetime

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException

from page_object.locators import Locator


class Foyer:

    def __init__(self, driver):
        self.driver = driver

        try:
            self.process_user_button = driver.find_element(By.ID, Locator.process_user)
            self.queue_total = driver.find_element(By.CSS_SELECTOR, Locator.queue_total)
        except (NoSuchElementException, InvalidSelectorException) as e:
            print(e)

    @property
    def in_queue(self):
        return int(self.queue_total.text)

    # methods
    def click_process_user(self):
        self.process_user_button.click()

    def save_screenshot(self):
        self.driver.save_screenshot('screenshots/foyer_screenshot_' + str(datetime.datetime.now()) + '.png')
