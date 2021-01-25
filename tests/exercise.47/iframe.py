import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time


class Iframe(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r"../../chromedriver.exe")
        self.driver.maximize_window()

    def test_iframe(self):
        try:
            driver = self.driver
            driver.get('https://www.google.com/')
            btn_menu = self.driver.find_element_by_xpath(
                '//*[@id="gbwa"]/div/a')
            btn_menu.click()
            time.sleep(2)
            driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div[3]/iframe"))
            #or
            #driver.switch_to.frame(0) #just when there is a only iframe
            btn_yt = driver.find_element_by_xpath(
                "/html/body/div/c-wiz/div/div/c-wiz/div/div/ul[1]/li[4]/a")
            btn_yt.click()
            time.sleep(3)
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def tearDow(self):
        """Stop web driver"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2)
