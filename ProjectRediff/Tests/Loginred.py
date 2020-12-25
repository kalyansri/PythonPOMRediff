from selenium import webdriver
import time
import unittest
import sys
from selenium import webdriver
sys.path.append('C:/Users/ADMIN/PycharmProjects/SeleniumProjects')

from ProjectRediff.TestPages.Loginrediff import Loginrediff
from ProjectRediff.TestPages.Homerediff import Homerediff



class LoginTest(unittest.TestCase):
# def is a function #def setUpClass(cls): cls is variable class

    @classmethod
    def setUpClass(Test):
        Test.driver=webdriver.Chrome(executable_path="D:\ecl sel\chromedriver\chromedriver.exe");
        Test.driver.implicitly_wait(60)
        Test.driver.maximize_window()

#driver is variable, why is self is important
    def test_login_valid(self):
        driver=self.driver
        driver.get("https://www.rediff.com/")
        login = Loginrediff(driver)

        Horediff = Homerediff(driver)
        Homerediff.click_News(self)

        Horediff = Homerediff(driver)
        Homerediff.click_BUSINESS(self)

        Horediff = Homerediff(driver)
        Homerediff.click_MOVIES(self)

        Horediff = Homerediff(driver)
        Homerediff.click_CRICKET(self)

        Horediff = Homerediff(driver)
        Homerediff.click_SPORTS(self)

        Horediff = Homerediff(driver)
        Homerediff.click_GETAHEAD(self)

        Horediff = Homerediff(driver)
        Homerediff.click_REALTIMENEWS(self)

        #Horediff = Homerediff(driver)
        #Homerediff.click_FARMERSSTIR(self)

        @classmethod
        def tearDownClass(Test):
            #Test.driver.close()
            #Test.driver.quit()
            print("Test Passed")