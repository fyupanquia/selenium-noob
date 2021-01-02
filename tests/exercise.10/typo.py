import unittest
from selenium import webdriver


class Typos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'../../chromedriver.exe')
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text("Typos").click()

    def test_find_typo(self):
        driver = self.driver
        attempts = 1
        right_text = "Sometimes you'll see a typo, other times you won't."

        while True:
            text_to_check = driver.find_element_by_css_selector(
                '#content > div > p:nth-child(3)').text
            if text_to_check != right_text:
                attempts += 1
                driver.refresh()
            else:
                break

        print(f'It took {attempts} attempts to find the typo')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
