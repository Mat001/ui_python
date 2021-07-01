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


def test_application_flow_2(driver):

    #################################################################################
    print('\n#   LOGIN PAGE    ####################\n')
    #################################################################################

    username = 'boston3'        # TODO - abstract this so it can be any username, password
    password = os.getenv('BOSTONS_PASSW')
    print('PASSW ', password)
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

    # from xxx import participants_sescodes_dict
    # print('HERE ', participants_sescodes_dict)
    #
    # ao1_sescode = participants_sescodes_dict['ao'][0]
    # print('AOOOO ', ao1_sescode, type(ao1_sescode))
    # queue_url = f'https://vt.clairvision.org/vsstaging/vsMain?tg=Tg_10950&pk=2166&sescode={ao1_sescode}&room_type=1'

    # ao1_sescode = 'J7D5ASdSKEFZEkqZ4E'
    # queue_url = f'https://vt.clairvision.org/vsstaging/vsMain?tg=Tg_10950&pk=2166&sescode={ao1_sescode}&room_type=1'
    # driver.get(queue_url)

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

    # #################################################################################
    # print('\n#   FOYER PAGE    ####################\n')
    # #################################################################################
    foyer = Foyer(driver)

    # #################################################################################
    # print('\n#   PORTAL PAGE    ####################\n')
    # #################################################################################
    # only look for portal access button if someone is in the queue
    if foyer.in_queue > 0:
        print('FOYER QUEUE TOTAL: ', str(foyer.in_queue), type(foyer.in_queue))
        foyer.click_process_user()
        portal = Portal(driver)
        # else wait until someone is in the que - add polling here because people may come in queue sporadically and there will be phases when quue number will be zero
        # but for now it's ok to just assume there will always be someone in the queue

        # loop here to process multiple particpants
        for participant in range(10):
            print('TRUE/FALSE: ', portal.is_pic_displayed())
            if portal.is_pic_displayed():  # photo in portal is not undefined:
                print('=== INSIDE LOOP ====')
                time.sleep(3)
                portal.click_grant_access()
                time.sleep(3)
                print('--- participant ---: ', participant)
            else:
                print('QUEUE EMPTY.')
                break

        print('EXITED FOR LOOP')
    print('BACK TO THE MAIN FLOW')
    time.sleep(3)
    foyer.save_screenshot()
    time.sleep(60)

    foyer = Foyer(driver)

    #################################################################################
    print('\n#   PORTAL PAGE    ####################\n')
    #################################################################################
    # only look for portal access button if someone is in the queue
    if foyer.in_queue > 0:
        print('FOYER QUEUE TOTAL: ', str(foyer.in_queue), type(foyer.in_queue))
        foyer.click_process_user()
        portal = Portal(driver)
        # else wait until someone is in the que - add polling here because people may come in queue sporadically and there will be phases when quue number will be zero
        # but for now it's ok to just assume there will always be someone in the queue

        # loop here to process multiple particpants
        for participant in range(10):
            print('TRUE/FALSE: ', portal.is_pic_displayed())
            if portal.is_pic_displayed():  # photo in portal is not undefined:
                print('=== INSIDE LOOP ====')
                time.sleep(3)
                portal.click_grant_access()
                time.sleep(3)
                print('--- participant ---: ', participant)
            else:
                print('QUEUE EMPTY.')
                break

        print('EXITED FOR LOOP')
    print('BACK TO THE MAIN FLOW')
    time.sleep(3)
    foyer.save_screenshot()
    time.sleep(60)