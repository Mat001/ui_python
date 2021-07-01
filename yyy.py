from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from helpers import get_participant_sescodes, get_url_parameter

options = webdriver.ChromeOptions()
path_to_chromedriver = "/home/m/applications/chromedriver"
driver = webdriver.Chrome(executable_path=path_to_chromedriver)

driver.get('https://vt.clairvision.org/vsstaging/vsMain')
# username = driver.find_element(By.NAME, 'user_name')
# username.send_keys('mp')
# password = driver.find_element(By.NAME, 'password')
# password.send_keys('matjazrocks')
# submit = driver.find_element(By.NAME, 'log_in')
# submit.click()

# # get session code for me
# login_url = driver.current_url
# print('LOGIN URL ', login_url)
# login_sescode = get_url_parameter(login_url, 'sescode')[0]
# print('LOGIN SESCODE ', login_sescode)

# # get participants' session codes
# participants_sescodes_dict = get_participant_sescodes(
#     url='https://vt.clairvision.org/vsstaging/vsMain',
#     params={'tg': 'Tg_12000', 'room_pk': 2166, 'num': 10, 'sescode': login_sescode}
# )

# participants_sescodes = participants_sescodes_dict['participants']  # list
# print('PARTICIPANTS SESCODES', participants_sescodes)

# Log in 100 participants
# add 100 participants to the queue

from session_codes import get_sesscodes

for sescode in get_sesscodes():
    options = webdriver.ChromeOptions()
    path_to_chromedriver = "/home/m/applications/chromedriver"
    driver = webdriver.Chrome(executable_path=path_to_chromedriver)
    # driver.get('https://vt.clairvision.org/vsstaging/vsMain')
    queue_url = f'https://vt.clairvision.org/vsstaging/vsMain?tg=Tg_10950&pk=2166&sescode={sescode}&room_type=1'  # TODO does tg needs to be that? what is tg?
    driver.get(queue_url)
    time.sleep(1)