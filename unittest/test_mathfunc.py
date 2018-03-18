import unittest
from mathfunc import *

class TestMathFunc(unittest.TestCase):

    def test_add(self):
        self.assertEquals(3,add(1,2))
        self.assertNotEquals(4,add(2,2))
    def test_minus(self):
        self.assertEquals(1,minus(3,2))
        self.assertNotEquals(2,minus(3,2))
    def test_multi(self):
        self.assertEquals(4,multi(2,2))
        self.assertNotEquals(5,multi(2,2))
    def test_divide(self):
        self.assertEquals(2,divide(4,2))
        self.assertNotEquals(3,divide(4,2))

if "__name__" == "__main__":
    unittest.main()
