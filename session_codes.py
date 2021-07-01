from selenium import webdriver
from selenium.webdriver.common.by import By

from helpers import get_participant_sescodes, get_url_parameter

options = webdriver.ChromeOptions()
path_to_chromedriver = "/home/m/applications/chromedriver"
driver = webdriver.Chrome(executable_path=path_to_chromedriver)

driver.get('https://vt.clairvision.org/vsstaging/vsMain')
username = driver.find_element(By.NAME, 'user_name')
username.send_keys('mp')
password = driver.find_element(By.NAME, 'password')
password.send_keys('matjazrocks')
submit = driver.find_element(By.NAME, 'log_in')
submit.click()

# get session code for me
login_url = driver.current_url
print('LOGIN URL ', login_url)
login_sescode = get_url_parameter(login_url, 'sescode')[0]
print('LOGIN SESCODE ', login_sescode)

# get participants' session codes
tg = 'Tg_12000'
room_pk = 2166
number_of_participants = 30

codes = get_participant_sescodes(
    url='https://vt.clairvision.org/vsstaging/vsMain',
    params={'tg': tg, 'room_pk': room_pk, 'num': number_of_participants, 'sescode': login_sescode}
)

participants_sescodes_dict = codes
print(participants_sescodes_dict)

driver.close()
driver.quit()
