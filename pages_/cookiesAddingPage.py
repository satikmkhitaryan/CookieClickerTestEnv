from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage
from time import sleep

class CookiesAddingPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.__cookiesAddingButtonLocator = By.ID, "bigCookie"
        self.__cookiesCountLocator = By.ID, "cookies"

    def click_to_cookies_adding_button(self):
        cookiesAddingButtonElement = self._find_element(self.__cookiesAddingButtonLocator)
        self._click_to_element(cookiesAddingButtonElement)

    def click_to_cookies_adding_10_time_button(self):
        cookiesAddingButtonElement = self._find_element(self.__cookiesAddingButtonLocator)
        i = 10
        while i > 0:
            self._click_to_element(cookiesAddingButtonElement)
            sleep(1)
            i -= 1

    def get_count_cookies(self):
        cookiesCountElement = self._find_element(self.__cookiesCountLocator)
        cookiesElementAllText = self._get_element_text(cookiesCountElement)
        cookiesCountElementText = cookiesElementAllText.split()[0]
        return int(cookiesCountElementText)

