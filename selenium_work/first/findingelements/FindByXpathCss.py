from selenium import webdriver

class FindByXpathCss():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        elementByXpath = driver.find_element_by_xpath("//input[@id='name']")

        elementByCss = driver.find_element_by_css_selector("#displayed-text")
        if elementByXpath is not None:
            print("We found an element Xpath")
        if elementByCss is not None:
            print("We found an element by CSS")
ct = FindByXpathCss()
ct.test()