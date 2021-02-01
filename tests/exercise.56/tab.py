import time
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest


class ETAB(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r"../../chromedriver.exe")
        self.driver.maximize_window()

    def test_etab(self):
        try:
            driver = self.driver
            driver.get("https://www.w3schools.com/howto/howto_css_login_form.asp")
            time.sleep(3)
            btn_popup = driver.find_element_by_xpath('//*[@id="main"]/button')
            btn_popup.click();
            iusername = driver.find_element_by_xpath('//*[@id="id01"]/div/div[2]/div/input[1]')
            iusername.send_keys('fyupanquia')
            iusername.send_keys(Keys.TAB)
            time.sleep(2)
            ipassword = driver.find_element_by_xpath('//*[@id="id01"]/div/div[2]/div/input[2]')
            ipassword.send_keys(Keys.TAB)
            time.sleep(2)
        except WebDriverException as ex:
            print('Handled error:', ex.msg)
            self.fail(ex.msg)

    def tearDow(self):
        """Stop web driver"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2)
