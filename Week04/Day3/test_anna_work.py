import unittest
from anna_work import GetsApple, SumExercise, Anagramm

test_apple = GetsApple()
test_valami = SumExercise()
test_anagramm = Anagramm()

class GetAppleTest(unittest.TestCase):

    def test_filled(self):
        self.assertEqual(test_apple.get_apple(), "apple")

class SumExerciseTest(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(test_valami.sum_numbers([]), 0)

    def test_with_two_numbers(self):
        self.assertEqual(test_valami.sum_numbers([3, 4]), 7)

    def test_with_zero(self):
        self.assertEqual(test_valami.sum_numbers([0]), 0)

class AnagrammTest(unittest.TestCase):

    def test_is_working(self):
        self.assertTrue(test_anagramm.is_anagramm('dog','god'))

    def test_is_working(self):
        self.assertFalse(test_anagramm.is_anagramm('purple','mapple'))

    def test_is_working(self):
        self.assertFalse(test_anagramm.is_anagramm('hello','helloworld'))

    def test_is_working(self):
        self.assertTrue(test_anagramm.is_anagramm('doggo','doggo'))

if __name__ == '__main__':
    unittest.main()