import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
import os

class Download(unittest.TestCase):

    def setUp(self):
        cOptions = Options()
        print(os.path.abspath(""))
        cOptions.add_experimental_option(
            "prefs", {"download.default_directory": os.path.abspath("")})
        self.driver = webdriver.Chrome(
            executable_path=r"../../chromedriver.exe", chrome_options=cOptions)
        self.driver.maximize_window()

    def test_download(self):
        try:
            driver = self.driver
            driver.get(
                "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download")
            driver.switch_to.frame(0)
            time.sleep(3)
            driver.find_element_by_xpath("/html/body/p[2]/a").click()
            time.sleep(5)

        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def tearDow(self):
        """Stop web driver"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2)
