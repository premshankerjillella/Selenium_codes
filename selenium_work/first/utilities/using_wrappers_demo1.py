from selenium import webdriver
from selenium.webdriver.common.by import  By
from utilities.handy_wrappers import HandyWrappers
import time


class UsingWrapppers():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        hw = HandyWrappers(driver)

        textField1 = hw.getElement("name")
        textField1.send_keys("Test")
        time.sleep(2)
        textField2 = hw.getElement("//input[@id='name']",locatorType="xpath")
        textField2.clear()
ct = UsingWrapppers()
ct.test()

