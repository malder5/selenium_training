import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
# Helpers
from fixture.session import SessionHelper
from fixture.page import PageHelper
from fixture.geo_zones import GeoZonesHelper

class Application():
    def __init__(self, browser='chrome'):
        # Libs
        self.pytest = pytest
        # Browsers
        if browser == 'chrome':
            options = Options()
            options.add_argument("start-maximized")
            # options.headless = 'headless'
            # options.add_argument('--window-size=1920x1080')
            self.driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\Roman\Downloads\chromedriver.exe')
            self.driver.implicitly_wait(10)
            # print(self.driver.capabilities)
        elif browser == 'ie':
            self.driver = webdriver.Ie(executable_path=r'C:\Users\Roman\Downloads\IEDriverServer.exe')
        elif browser == 'opera':
            self.driver = webdriver.Opera(executable_path=r'C:\Users\Roman\Downloads\operadriver64.exe')
        elif browser == 'firefox':
            self.driver = webdriver.Firefox(executable_path=r'C:\Users\Roman\Downloads\chromedriver.exe')
        else:
            raise ValueError('Неизвестный браузер {}'.format(browser))
        # Helpers
        self.session = SessionHelper(self)
        self.page = PageHelper(self)
        self.geozones = GeoZonesHelper(self)



    def is_valid(self):
        try:
            self.driver.current_url()
            return True
        except:
            return False

    def destroy(self):
        self.driver.quit()