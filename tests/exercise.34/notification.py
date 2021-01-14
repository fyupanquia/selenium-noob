import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time


class Notification(unittest.TestCase):
    def setUp(self):
        o = Options()
        # 1 allow, 2 disable
        o.add_experimental_option(
            "prefs", {"profile.default_content_setting_values.notifications": 2})
        self.driver = webdriver.Chrome(
            chrome_options=o, executable_path="../../chromedriver.exe")

    def test_popup(self):
        driver = self.driver
        try:
            driver.get(
                "https://developer.mozilla.org/es/docs/Web/API/notification")
            time.sleep(5)
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def tearDow(self):
        """Stop web driver"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
