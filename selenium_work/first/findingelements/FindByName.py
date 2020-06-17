from selenium import webdriver

class FindByName():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        elementById = driver.find_element_by_id("name")

        if elementById is not None:
            print("We found an element")
        # elementByName = driver.find_element_by_name("")

ct = FindByName()
ct.test()