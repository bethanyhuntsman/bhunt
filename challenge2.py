import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        self.driver.get("https://www.copart.com")

        self.driver.find_element_by_id("input-search").click()
        self.driver.find_element_by_id("input-search").send_keys("exotics")
        self.driver.find_element_by_id("input-search").send_keys(Keys.ENTER)
        time.sleep(6)
        self.assertIn("PORSCHE", self.driver.find_element_by_id("serverSideDataTable").text)


if __name__ == '__main__':
        unittest.main()