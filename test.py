import example
import unittest

class TestCase(unittest.TestCase):
    def testAddition(self):
        self.assertEqual(example.addition(3,5), 8)


if __name__ == '__main__':
    unittest.main()