import unittest
from selenium import webdriver


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()
        print ("in tear down")

    def test_challenge3(self):
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)

        cars = self.driver.find_elements_by_xpath('//*[@id="tabTrending"]/div[1]/div[2]/div/ul/li/a')
        for make in cars:
            print(make.text)
            print(make.get_attribute("href"))



if __name__ == '__main__':
        unittest.main()