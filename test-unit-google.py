import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

class GoogleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setup the webdriver only once for all tests
        service = Service('D:\\chromedriver.exe')
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.set_window_size(1072, 816)

    @classmethod
    def tearDownClass(cls):
        # Quit the webdriver after all tests
        cls.driver.quit()

    def perform_google_search(self, query):
        self.driver.get("https://www.google.com/")
        time.sleep(1)  # Allow time for the page to load completely
        self.driver.find_element(By.ID, "APjFqb").send_keys(query)
        self.driver.find_element(By.CSS_SELECTOR, "center:nth-child(1) > .gNO89b").click()
        time.sleep(3)  # Allow time for results to load

    def test_addition(self):
        self.perform_google_search("5+5")
        result = self.driver.find_element(By.ID, "cwos").text
        self.assertEqual(result, "10", "Addition result is incorrect.")
        self.assertIn("5+5 -", self.driver.title)

    def test_multiplication(self):
        self.perform_google_search("5*5")
        result = self.driver.find_element(By.ID, "cwos").text
        self.assertEqual(result, "25", "Multiplication result is incorrect.")
        self.assertIn("5*5 -", self.driver.title)

if __name__ == '__main__':
    unittest.main()
