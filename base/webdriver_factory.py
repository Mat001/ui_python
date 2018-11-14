from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime


class WebDriverFactory:

    BASE_URL = 'http://automationpractice.com/index.php'

    def __init__(self, browser):
        self.browser = browser

    def get_webdriver_instance(self):

        # select browser
        if self.browser == "firefox-remote":
            driver = self.ff_remote
        elif self.browser == "chrome-remote":
            driver = self.chrome_remote
        elif self.browser == 'firefox-local':
            driver = self.ff
        elif self.browser == 'chrome-local':
            driver = self.chrome
        else:
            driver = self.ff_remote

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

    @property
    def ff_remote(self):
        """ Run remotely (on selenium grid, needs docker compose to run first). Window
        size is increased to accommodate page scrolling on categories page"""
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                  desired_capabilities=DesiredCapabilities.FIREFOX)
        driver.set_window_size(1920, 1080)
        return driver

    @property
    def chrome_remote(self):
        """Remotely"""
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                  desired_capabilities=DesiredCapabilities.CHROME)
        driver.set_window_size(1920, 1080)
        return driver

    @property
    def ff(self):
        """Locally"""
        path_to_geckodriver = '/home/m/applications/geckodriver'
        driver = webdriver.Firefox(executable_path=path_to_geckodriver)
        driver.maximize_window()
        return driver

    @property
    def chrome(self):
        """Locally"""
        path_to_chromedriver = '/home/m/applications/chromedriver'
        driver = webdriver.Chrome(executable_path=path_to_chromedriver)
        driver.maximize_window()
        return driver






