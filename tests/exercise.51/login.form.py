import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


class LoginForm(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        self.driver = webdriver.Chrome(
            executable_path=r"../../chromedriver.exe", options=chrome_options)
        self.driver.maximize_window()

    def test_login_form(self):
        try:
            driver = self.driver
            driver.get(
                "https://www.w3schools.com/howto/howto_css_login_form.asp")
            btn_popup = driver.find_element_by_xpath('//*[@id="main"]/button')
            btn_login = driver.find_element_by_xpath(
                '//*[@id="id01"]/div/div[2]/div/button')
            iuser = driver.find_element_by_xpath(
                '//*[@id="id01"]/div/div[2]/div/input[1]')
            ipassword = driver.find_element_by_xpath(
                        '//*[@id="id01"]/div/div[2]/div/input[2]')
            with open('data.csv') as file:
                for i, line in enumerate(file):
                    btn_popup.click()                    
                    _ = (line)
                    parts = _.split(",")
                    #try:
                        #gotdata = parts[1]
                    user = parts[0]
                    password = parts[1]
                    #except IndexError:
                    #    gotdata = ''

                    print(user,' , ',password)
                    time.sleep(1)
                    iuser.send_keys(user)
                    time.sleep(1)
                    ipassword.send_keys(password)
                    time.sleep(1)
                    iuser.clear()
                    ipassword.clear()
                    btn_login.click()
                file.close()

        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def tearDow(self):
        """Stop web driver"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2)
