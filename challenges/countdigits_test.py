import unittest
from countDigits_hard import digits_count

class TestMyCode(unittest.TestCase):
    def test_digits_count(self):
        self.assertEqual(digits_count(23467), 5) 
        self.assertEqual(digits_count(12.122), 5)
        self.assertEqual(digits_count(0), 1)
        self.assertEqual(digits_count(-12.212), 5)
        self.assertEqual(digits_count(1.23), 3)

if __name__ == '__main__':
    unittest.main()
