"""home page"""
import datetime

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException, \
    StaleElementReferenceException

from page_object.locators import Locator


class Portal:

    def __init__(self, driver):
        self.driver = driver

        try:
            self.grant_access = driver.find_element(By.ID, Locator.grant_access)
            self.portal_picture = driver.find_element(By.CLASS_NAME, Locator.picture)
        except (NoSuchElementException, InvalidSelectorException, StaleElementReferenceException) as e:
            print(e)

    def get_pic_title(self):
        try:
            return self.portal_picture.get_attribute('title')
        except StaleElementReferenceException:
            self.portal_picture = self.driver.find_element(By.CLASS_NAME, Locator.picture)
            return self.portal_picture.get_attribute('title')

    # methods
    def click_grant_access(self):
        '''try catch is needed to avoid stale element exception on grant access page'''
        try:
            self.grant_access.click()
        except StaleElementReferenceException:
            self.grant_access = self.driver.find_element(By.ID, Locator.grant_access)
            self.grant_access.click()

    def is_pic_displayed(self):
        try:
            return self.portal_picture.is_displayed()
        except StaleElementReferenceException:
            self.portal_picture = self.driver.find_element(By.CLASS_NAME, Locator.picture)
            return self.portal_picture.is_displayed()

