from selenium import webdriver

driver = webdriver.Chrome()

class ListOfElements():
    def test(self):

        baseurl = "https://letskodeit.teachable.com/p/practice"
        driver.get(baseurl)

        elementListByClassName = driver.find_elements_by_class_name("inputs")
        length1 = len(elementListByClassName)
        if elementListByClassName is not None:
            print(f'The length of class Name list is {length1}')
        elementListByTagName = driver.find_elements_by_tag_name("td")
        length2 = len(elementListByTagName)
        if elementListByTagName is not None:
            print(f"The length of Tag Name list is {length2}")

ct = ListOfElements()
ct.test()