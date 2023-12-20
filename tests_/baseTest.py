import unittest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener
from testData_.testData import urlForCookieClicker
from pages_.languageSettingsPage import LanguageSettingsPage
from time import sleep


class BaseTestForCookieClicker(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(urlForCookieClicker)
        languageSettingsPageObj = LanguageSettingsPage(self.driver)
        sleep(5)
        languageSettingsPageObj.click_to_english_language_button()
        # sleep(5)

    def tearDown(self):
        self.driver.close()
