import unittest
from selenium import webdriver
from openpyxl import load_workbook
from PIL import Image
from io import BytesIO
from selenium.common.exceptions import WebDriverException
import time


class CropIMG(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r"../../chromedriver.exe")
        self.driver.maximize_window()

    def test_crop_img(self):
        try:
            driver = self.driver
            driver.get(
                "https://www.google.com")
            time.sleep(3)
            img_element = driver.find_element_by_id("hplogo")
            size = img_element.size
            ilocation = img_element.location
            screen_shot = driver.get_screenshot_as_png()
            img_binary = Image.open(BytesIO(screen_shot))
            print(size)
            print(ilocation)
            x = ilocation['x'] + 100
            y = ilocation['y'] + 100
            #right = ilocation['x'] + size['width']
            width = ilocation['x'] + size['width']
            #bottom = ilocation['y'] + size['height']
            height = ilocation['y'] + size['height']
            img2 = img_binary.crop((x, y, width, height))
            img2.save('default.png')

        except WebDriverException as ex:
            print('Handled error:', ex.msg)
            self.fail(ex.msg)

    def tearDow(self):
        """Stop web driver"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2)
