import unittest
import test_class2


class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a,"a is not True")
        #Only shows when test fails
        b = False
        self.assertFalse(b,"b is not False")
        #     if assertion fails at any line, it does not go to the next lint
        #    of the same method, it goes to next methpd


    def test_assertEqual(self):
        a="Test"
        b="Test"
        self.assertEqual(a,b,msg="a is not equal to b")


if  __name__ == '__main__':
    unittest.main(verbosity=2)