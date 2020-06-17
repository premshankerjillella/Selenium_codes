from selenium import webdriver

driver = webdriver.Chrome()  # To make the browser close instatnly
# don't make the driver class global put it in the test
class FindByClassTag():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver.get(baseUrl)

        elementByClassName = driver.find_element_by_class_name("displayed-class")
        elementByClassName.send_keys("Testing the element")
        if elementByClassName is not None:
            print("We found an element  by Class  Name")

        elementByTagName = driver.find_element_by_tag_name("h1")
        print(elementByTagName.text)
        if elementByTagName is not None:
            print("We found an element  by Tag  Name")

ct = FindByClassTag()
ct.test()