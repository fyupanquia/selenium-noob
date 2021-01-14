import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

class Prompt(unittest.TestCase):
    def setUp(self):
        """Start web driver"""
        self.driver = webdriver.Chrome(
            executable_path=r'../../chromedriver.exe')

    def tearDow(self):
        """Stop web driver"""
        self.driver.quit()

    def test_popup(self):
        driver = self.driver
        try:
            driver.get(
                'file:///G:/prjs/python/selenium-noob/tests/exercise.33/page.html')
            btn = driver.find_element_by_id('btn')
            btn.click()
            alert = driver.switch_to_alert()
            ifconfirm = input("Do you want to accept the prompt (Y/N): ")
            if ifconfirm=='Y':
                alert_text = alert.text
                name = input(alert_text + ": ")
                alert.send_keys(name)
                time.sleep(2)
                print("accepted...")
                alert.accept()
            else:
                print("dismissed...")
                alert.dismiss()
            time.sleep(2)
        except NoSuchElementException as ex:
            self.fail(ex.msg)


if __name__ == "__main__":
    unittest.main(verbosity=2)
