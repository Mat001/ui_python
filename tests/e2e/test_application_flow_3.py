import time
import os

from page_object.locators import Locator
from tests.test_data.data import TestData
from page_object.pages.login import Login
from page_object.pages.home import Home
from page_object.pages.awi_testing_wave_training import AwiTestingWaveTraining
from page_object.pages.foyer import Foyer
from page_object.pages.portal import Portal

from base.webdriver_factory import WebDriverFactory


def test_application_flow_3(driver):

    #################################################################################
    print('\n#   LOGIN PAGE    ####################\n')
    #################################################################################

    username = 'boston5'        # TODO - abstract this so it can be any username, password
    password = os.getenv("BOSTONS_PASSW")


    # Creating an instance of class and passing the current driver instance
    login = Login(driver)
    print('Loading login page...')

    # Verify that we're on login page
    assert driver.title == Locator.login_page_title
    print('Titles match.')

    assert driver.current_url == WebDriverFactory.BASE_URL
    print('URL successfully points to Login page -', driver.current_url)

    # log in
    try:
        login.login_username(username)
        login.login_passw(password)
        login.click_log_in()
        driver.implicitly_wait(5)  # wait until page has loaded
    except Exception as e:
        print(e)

    #################################################################################
    print('\n#   HOME PAGE PAGE    ####################\n')
    #################################################################################
    home = Home(driver)
    try:
        home.click_awi_testing_wave_training_link()
        driver.implicitly_wait(5)
    except Exception as e:
        print(e)

    #################################################################################
    print('\n#   AWI TESTING WAVE PAGE PAGE    ####################\n')
    #################################################################################
    awi_testing_wave_training = AwiTestingWaveTraining(driver)
    try:
        awi_testing_wave_training.click_enter_training_room()
        driver.implicitly_wait(5)
    except Exception as e:
        print(e)

    time.sleep(2)

    #################################################################################
    print('\n#   FOYER PAGE    ####################\n')
    #################################################################################
    foyer = Foyer(driver)
    foyer.click_process_user()

    #################################################################################
    print('\n#   PORTAL PAGE    ####################\n')
    #################################################################################
    portal = Portal(driver)

    # loop here to process multiple particpants
    for participant in range(10):
        driver.implicitly_wait(5)
        time.sleep(3)
        portal.click_grant_access()
        time.sleep(3)
        print('Processed participant: ', participant)

    time.sleep(3)
    foyer.save_screenshot()
    time.sleep(60)
