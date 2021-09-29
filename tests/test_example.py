import unittest
from example_package.utils import add_one

class TestExamples(unittest.TestCase):

    def test1(self):
        self.assertEqual(add_one(1), 2)

    def test2(self):
        self.assertEqual(add_one(2), 3)
    
    def test3(self):
        self.assertEqual(add_one(3), 4)

if __name__ == '__main__':
    unittest.main()