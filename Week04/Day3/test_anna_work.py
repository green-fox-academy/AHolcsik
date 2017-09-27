import unittest
from anna_work import GetsApple, SumExercise, Anagramm, CountLetters

test_apple = GetsApple()
test_valami = SumExercise()
test_anagramm = Anagramm()
test_word = CountLetters()

class GetAppleTest(unittest.TestCase):

    # def test_empty(self):
    #     self.assertEqual(test_apple.get_apple(), )

    def test_filled(self):
        self.assertEqual(test_apple.get_apple(), 'apple')

class SumExerciseTest(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(test_valami.sum_numbers([]), 0)

    def test_with_two_numbers(self):
        self.assertEqual(test_valami.sum_numbers([3, 4]), 7)

    def test_with_zero(self):
        self.assertEqual(test_valami.sum_numbers([0]), 0)

class AnagrammTest(unittest.TestCase):

    def test_if_anagramm(self):
        self.assertTrue(test_anagramm.is_anagramm('dog','god'))

    def test_if_letter_number_is_equal(self):
        self.assertFalse(test_anagramm.is_anagramm('purple','mapple'))

    def test_if_letter_number_is_different(self):
        self.assertFalse(test_anagramm.is_anagramm('hello','helloworld'))

    def test_if_strings_are_same(self):
        self.assertTrue(test_anagramm.is_anagramm('doggo','doggo'))

class CountLettersTest(unittest.TestCase):

    def test_for_empty(self):
        self.assertEqual(test_word.number_of_letters(''), {})

    def test_for_empty(self):
        self.assertEqual(test_word.number_of_letters('a'), {'a' : 1})

    def test_for_empty(self):
        self.assertEqual(test_word.number_of_letters('ab'), {'a' : 1, 'b' : 1})

    def test_for_empty(self):
        self.assertEqual(test_word.number_of_letters('aa'), {'a' : 2})

        
          

if __name__ == '__main__':
    unittest.main()