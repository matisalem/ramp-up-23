import unittest
from discount_easy import dis

class TestMyCode(unittest.TestCase):

    def test_dis(self):
        self.assertEqual(dis(100, 20), 80)
        self.assertEqual(dis(200, 50), 100)
        self.assertEqual(dis(0, 50), 0)

if __name__ == '__main__':
    unittest.main()
