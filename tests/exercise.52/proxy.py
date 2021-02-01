import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


class Proxy(unittest.TestCase):

    def setUp(self):
        PROXY = "<159.89.121.225:8080>"
        webdriver.DesiredCapabilities.CHROME['proxy'] = {
            "httProxy": PROXY,
            "ftpProxy": PROXY,
            "sslProxy": PROXY,
            "proxyType": "MANUAL",
        }
        self.driver = webdriver.Chrome(
            executable_path=r"../../chromedriver.exe")
        self.driver.maximize_window()
        
    def test_proxy(self):
        try:
            driver = self.driver
            driver.get("https://google.com")
            time.sleep(5)

        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def tearDow(self):
        """Stop web driver"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2)
