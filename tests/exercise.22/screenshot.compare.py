import unittest
from selenium import webdriver
import cv2 #pip3 install opencv-python

class ExplicitWait(unittest.TestCase):
    
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome(executable_path=r'../../chromedriver.exe')
		cls.driver.maximize_window()

	def test_mercado_libre(self):
		name = "q"
		driver = self.driver
		driver.implicitly_wait(5)
		driver.get('https://www.google.com/')
		driver.save_screenshot('_img.png')

	def test_compare(self):
		img = cv2.imread('img.png')
		_img = cv2.imread('_img.png')

		diff = cv2.absdiff(img, _img)
		imggray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
		contours,_ = cv2.findContours(imggray,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

		for c in contours:
			if cv2.contourArea(c) >= 20:
				position_x, position_y, width, high = cv2.boundingRect(c)
				cv2.rectangle(_img, (position_x, position_y), (position_x+width,position_y+high),(0,0,255),2)

		while(1):
			cv2.imshow('img', img)
			cv2.imshow('_img', _img)
			cv2.imshow('Differences: ', diff)
			key = cv2.waitKey(5) & 0xFF
			if key == 27:
				break
		cv2.destroyAllWindows()

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()

if __name__ == "__main__":
  unittest.main(verbosity=2)
