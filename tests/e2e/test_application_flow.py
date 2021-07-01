from selenium import webdriver
import os

import time
from page_object.locators import Locator
from page_object.pages.login import Login
from page_object.pages.home import Home
from page_object.pages.awi_testing_wave_training import AwiTestingWaveTraining
from page_object.pages.foyer import Foyer
from page_object.pages.portal import Portal
from helpers import get_url_parameter, get_participant_sescodes

from base.webdriver_factory import WebDriverFactory
from session_codes import participants_sescodes_dict


# TODO - have 3 AOs in the same codebase (arbitrary number of AOs) - use cli option for username and password?
# TODO - or place all three application flow files into the test/e2e directory and run tests in parallel!!!!!
# TODO -DONE - fix the loop of granting access to stop when noone in the queue (that should fix the stale element exception at the end of the run )
# TODO - script to take users out of the room back into the foyer for another round of testing
# TODO - fix pytest_addoptions (to be able to choose browser & to add username & passw
# TODO - test on diff browsers (Chrome, FF)
# TODO - CONSIDER SCENARIO WHERE THE QUEUE IS TEMPORARILY EMPTY, THEN MORE USERS COME


def test_application_flow(driver):

    #################################################################################
    print('\n#   LOGIN PAGE    ####################\n')
    #################################################################################

    username = 'mp'
    password = os.getenv('MATJAZ_STAGING_PASSWORD')

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

    # add participants to the queue using session codes
    for sescode in participants_sescodes_dict['participants']:
        # options = webdriver.ChromeOptions()
        path_to_geckodriver = '/home/m/applications/geckodriver'
        driver2 = webdriver.Firefox(executable_path=path_to_geckodriver)
        driver2.maximize_window()
        queue_url = f'https://vt.clairvision.org/vsstaging/vsMain?tg=Tg_10950&pk=2166&sescode={sescode}&room_type=1'  # TODO does tg needs to be that? what is tg?
        driver2.get(queue_url)
    time.sleep(3600)
