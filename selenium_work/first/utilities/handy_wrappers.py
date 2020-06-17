from selenium.webdriver.common.by import By


class HandyWrappers():

    def __init__(self, driver):
        self.driver = driver

    def getByTpe(self, locatorType):
        locatorType = locatorType.lower()

        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        else:
            print("Not supported Locator Type")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByTpe(locatorType)
            element = self.driver.find_element(byType, locator)
        except:
            print("Element not found")
        return element

    def isElementPresent(self,locator, byType):
        element = None
        try:
            element = self.driver.find_element(byType, locator)
            if element is not None:
                return True
            else : return  False
        except:
            print("Element not found")
            return False
    def elementPresenceCheck(self,locator, byType):
        try:
            element = self.driver.find_elements(byType,locator)
            if len(element) > 0:
                return True
            else: return False
        except:
            print("Element not found")
            return False