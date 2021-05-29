import example
import unittest

#adding white spaces is the stupidest thing ive ever seen. does not add to functionality.
class TestCase(unittest.TestCase):
    def testAddition(self):
        self.assertEqual(example.addition(3, 5), 8)


if __name__ == '__main__':
    unittest.main()
