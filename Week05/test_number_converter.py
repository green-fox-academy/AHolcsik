import unittest
import number_converter


class Test_number_converter(unittest.TestCase):

    def test_number_converter_with_string_added(self):
        self.assertEqual(number_converter.number_converter_to_float(750), str(750.00) + 'dollars')        

    def test_number_converter_float_and_letters(self):
        self.assertEqual(number_converter.number_converter_to_float(5), str(5.00) + 'dollars\n five dollars')


if __name__ == '__main__':
    unittest.main()