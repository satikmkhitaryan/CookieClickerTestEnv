from tests_.baseTest import BaseTestForCookieClicker
from pages_.cookiesAddingPage import CookiesAddingPage


class TestForAddingCookiesCountBy10000(BaseTestForCookieClicker):
    def test_for_adding_cookies_count_by_10000(self):
        cookiesAddingPageObj = CookiesAddingPage(self.driver)
        cookiesAddingPageObj.click_to_cookies_adding_10_time_button()
        self.assertEqual(cookiesAddingPageObj.get_count_cookies(), 10, "wrong Cookies count adding ")
