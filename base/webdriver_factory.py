from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime


class WebDriverFactory:

    BASE_URL = 'http://automationpractice.com/index.php'

    # def __init__(self, browser):
    #     self.browser = browser

    def get_webdriver_instance(self):

        #######################################
        # remotely
        #######################################
        # remotely (on selenium grid, needs docker compose to run first)
        # window size is increased to accommodate page scrolling on categories page

        # remote firefox
        driver = self.ff_remote()

        # remote chrome
        # driver = self.chrome_remote()


        #######################################
        # locally
        #######################################
        # local firefox
        # driver = self.ff()

        # local chrome
        # driver = self.chrome()

        print('-------------------------------------------------')
        print('Run started at ' + str(datetime.datetime.now()))
        browser_name = driver.capabilities['browserName']
        if browser_name == 'chrome':
            print('Browser: ', browser_name, driver.capabilities['version'])
        else:
            print('Browser: ', browser_name, driver.capabilities['browserVersion'])

        driver.implicitly_wait(20)

        driver.get(self.BASE_URL)
        driver.set_page_load_timeout(20)

        return driver

    def ff_remote(self):
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                  desired_capabilities=DesiredCapabilities.FIREFOX)
        driver.set_window_size(1920, 1080)
        return driver

    def chrome_remote(self):
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                  desired_capabilities=DesiredCapabilities.CHROME)
        driver.set_window_size(1920, 1080)
        return driver

    def ff(self):
        path_to_geckodriver = '/home/m/applications/geckodriver'
        driver = webdriver.Firefox(executable_path=path_to_geckodriver)
        driver.maximize_window()
        return driver

    def chrome(self):
        path_to_chromedriver = '/home/m/applications/chromedriver'
        driver = webdriver.Chrome(executable_path=path_to_chromedriver)
        driver.maximize_window()
        return driver






