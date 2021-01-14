import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

class Confirm(unittest.TestCase):
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
                'file:///G:/prjs/python/selenium-noob/tests/exercise.32/confirm.alert.html')
            time.sleep(3)
            btn = driver.find_element_by_id('btn')
            btn.click()
            time.sleep(3)
            alert = driver.switch_to_alert()
            alert_text = alert.text
            ifconfirm = input(alert_text+ " (Y/N): ")
            if ifconfirm=='Y':
                print("accepted...")
                alert.accept()
            else:
                print("dismissed...")
                alert.dismiss()
            time.sleep(3)
            

        except NoSuchElementException as ex:
            self.fail(ex.msg)


if __name__ == "__main__":
    unittest.main(verbosity=2)
