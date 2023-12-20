from tests_.baseTest import BaseTestForCookieClicker
from pages_.cookiesAddingPage import CookiesAddingPage
from time import sleep


class TestForAddingCookiesCountByOne(BaseTestForCookieClicker):
    def test_for_adding_cookies_count_by_one(self):
        cookiesAddingPageObj = CookiesAddingPage(self.driver)
        cookiesAddingPageObj.click_to_cookies_adding_button()
        sleep(5)
        self.assertEqual(cookiesAddingPageObj.get_count_cookies(), 1, "wrong Cookies count adding ")

