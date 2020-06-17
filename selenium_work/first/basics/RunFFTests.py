from selenium import webdriver

class RunFFTests():
    def testMethod(self):
    driver = webdriver.Firefox(executable_path='/Location of the geko driver here')
    driver.get("http://www.letskodeit.com")

ff = RunFFTests()
ff.testMethod()


