import unittest


#  we need to find ways to find setup and tear donce
#  once for all the test cases
# that is setup then all test cases then tearDown
class TestClass1(unittest.TestCase):

    @classmethod #This is a decorator in python
    def setUpClass(cls):
        print("*#"*30)
        print("This code will run once, before all test")
        print("*#" * 30)

    def setUp(self):
        print("This code will run once, before every test")
        #This is execute once before each test

    def test_class1_methodA(self):
        print("Running class1- method A")

    def test_class1_methodB(self):
        print("Running class1 - method B")

    def tearDown(self):
        print("I will run after every test")

    @classmethod
    def tearDownClass(cls):
        print("*#" * 30)
        print("This code will run once,after all test")
        print("*#" * 30)

if __name__ == '__main__':
    unittest.main(verbosity=2)