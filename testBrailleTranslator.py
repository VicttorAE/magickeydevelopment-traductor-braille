import unittest
from BrailleTranslator import BrailleTranslator

class TestBrailleTranslator(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.translator = BrailleTranslator('brailleDictionary.txt')
    
    def test_vocales_acentuadas(self):
        self.assertEqual(self.translator.texto_a_braille('áéíóú'), '⠷⠮⠌⠨⠾')
    
    def test_abecedario(self):
        self.assertEqual(self.translator.texto_a_braille('abcdefghijklmnopqrstuvwxyz'), '⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵')
    
    def test_numeros(self):
        self.assertEqual(self.translator.texto_a_braille('0123456789'), '⠴⠂⠆⠒⠲⠢⠖⠶⠦⠔')
    
    def test_caracteres_especiales(self):
        self.assertEqual(self.translator.texto_a_braille('.,;:!?@%&*+=-¡¿'), '⠲⠂⠆⠒⠖⠦⠈⠌⠯⠇⠶⠬⠤⠮⠢')
    
    def test_ñ_Ü(self):
        self.assertEqual(self.translator.texto_a_braille('ñÜ'), '⠻⠳')
    
    def test_mayusculas(self):
        # Definir el comportamiento esperado para las mayúsculas
        expected_output = '⠠⠁⠠⠃⠠⠉⠠⠙⠠⠑⠠⠋⠠⠛⠠⠓⠠⠊⠠⠚⠠⠅⠠⠇⠠⠍⠠⠝⠠⠕⠠⠏⠠⠟⠠⠗⠠⠎⠠⠞⠠⠥⠠⠧⠠⠺⠠⠭⠠⠽⠠⠵'
        self.assertEqual(self.translator.texto_a_braille('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), expected_output)

if __name__ == '__main__':
    unittest.main()
