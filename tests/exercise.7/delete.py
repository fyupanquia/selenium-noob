import unittest
from selenium import webdriver
from time import sleep


class AddRemoveElements_Reto(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path=r'../../chromedriver.exe')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver

        n_add = int(input('How many elements would you like to add?: '))

        add_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/button')


        for i in range(n_add):
            add_button.click()

        n_remove = int(input('How many elements would you like to remove?: '))

        while n_add>0 and n_remove>0:
            for i in range(n_remove):
                delete_button = driver.find_element_by_xpath(
                    '//*[@id="elements"]/button[1]')
                delete_button.click()
                n_add -= 1
                break

        sleep(3)
        print(f"There are {n_add} elements on the screen")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)
