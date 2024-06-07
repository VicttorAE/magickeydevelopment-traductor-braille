# test_braille_translator.py

import unittest
from BrailleTranslator import BrailleTranslator

class TestBrailleTranslator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.translator = BrailleTranslator('brailleDictionary.txt')

    def test_number_prefix_single_digit(self):
        self.assertEqual(self.translator.texto_a_braille('1'), '⠼⠂')

    def test_number_prefix_multiple_digits(self):
        self.assertEqual(self.translator.texto_a_braille('123'), '⠼⠂⠆⠒')

    def test_number_prefix_with_text(self):
        self.assertEqual(self.translator.texto_a_braille('a1b2c3'), '⠁⠼⠂⠃⠼⠆⠉⠼⠒')

    def test_number_prefix_separated_digits(self):
        self.assertEqual(self.translator.texto_a_braille('1 2 3'), '⠼⠂ ⠼⠆ ⠼⠒')

    def test_number_prefix_single_and_multiple_digits(self):
        self.assertEqual(self.translator.texto_a_braille('a1 23b'), '⠁⠼⠂ ⠼⠆⠒⠃')

if __name__ == '__main__':
    unittest.main()
