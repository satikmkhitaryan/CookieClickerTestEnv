from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage
from common_.utilities_.customLogger import *


class LanguageSettingsPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.__englishLanguageButtonLocator = By.ID, "langSelect-EN"

    def click_to_english_language_button(self):
        languageButtonElement = self._find_element(self.__englishLanguageButtonLocator)
        self._click_to_element(languageButtonElement)

