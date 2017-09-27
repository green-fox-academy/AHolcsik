import unittest
from apples import GetsApple

test_apple = GetsApple()

class GetAppleTest(unittest.TestCase):

    def test_filled(self):
        self.assertEqual(test_apple.get_apple(), "apple")


if __name__ == '__main__':
    unittest.main()