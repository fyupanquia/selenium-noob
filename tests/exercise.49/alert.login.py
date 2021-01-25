import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import keyboard
import time
import pyautogui

class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r"../../chromedriver.exe")
        self.driver.maximize_window()

    def test_login(self):
        try:
            driver = self.driver
            driver.get(
                "http://217.182.87.241/testlink/login.php")
            time.sleep(3)
            keyboard.write("fyupanquia")
            time.sleep(1)
            pyautogui.press("tab")
            keyboard.write("fyupanquia")
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(5)

        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def tearDow(self):
        """Stop web driver"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2)
