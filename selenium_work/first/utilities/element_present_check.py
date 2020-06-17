from selenium import webdriver
from selenium.webdriver.common.by import  By
from utilities.handy_wrappers import HandyWrappers
import time

class ElementPresentCheck():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)
        hw = HandyWrappers(driver)

        elementResult = hw.isElementPresent("name",By.ID)
        print(elementResult)

        elementResult2 = hw.elementPresenceCheck("//input[@id='name']",By.XPATH)
        print(elementResult2)

ct = ElementPresentCheck()
ct.test()