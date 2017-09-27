import unittest
from anna_work import GetsApple, SumExercise

test_apple = GetsApple()
test_valami = SumExercise()

class GetAppleTest(unittest.TestCase):

    def test_filled(self):
        self.assertEqual(test_apple.get_apple(), "apple")

class SumExerciseTest(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(test_valami.sum_numbers([]), 0)

    def test_with_two_numbers(self):
        self.assertEqual(test_valami.sum_numbers([3, 4]), 7)

    def test_with_two_numbers(self):
        self.assertEqual(test_valami.sum_numbers([0]), 0)


if __name__ == '__main__':
    unittest.main()