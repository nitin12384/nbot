import unittest

class TestWorking(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(2+2, 4)
        print("Test Passed.")



if __name__ == '__main__':
    unittest.main()