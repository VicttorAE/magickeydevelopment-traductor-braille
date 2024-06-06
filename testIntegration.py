import unittest
from BrailleTranslator import BrailleTranslator
from BrailleImageGenerator import BrailleImageGenerator
import os

class TestIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.translator = BrailleTranslator('brailleDictionary.txt')
        cls.image_generator = BrailleImageGenerator(cls.translator)
    
    def test_generate_braille_image(self):
        text = "Hola Mundo"
        output_file = "test_braille.png"
        self.image_generator.generar_senaletica_braille(text, output_file)
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
