import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time


class Assert(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r"../../chromedriver.exe")

    def test_mouse_actions(self):
        try:
            driver = self.driver
            driver.get('https://www.google.com/')
            btn_good_luck = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[2]')
            btn_search = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
            btn_business = self.driver.find_element_by_xpath('//*[@id="fsl"]/a[2]')
            movement = ActionChains(self.driver)
            m1 = movement.move_to_element(btn_good_luck).perform()
            time.sleep(2)
            m2 = movement.move_to_element(btn_search).perform()
            time.sleep(2)
            m3 = movement.move_to_element(btn_business).click().perform()
            time.sleep(2)

            #movement.move_to_element(btn_good_luck).move_to_element(btn_search).move_to_element(btn_business).perform()

        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def tearDow(self):
        """Stop web driver"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2)
