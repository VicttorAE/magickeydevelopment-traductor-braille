# BrailleTranslator.py

class BrailleTranslator:
    def __init__(self, dict_file):
        self.braille_dict = self.load_dict(dict_file)

    def load_dict(self, dict_file):
        braille_dict = {}
        with open(dict_file, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(':', 1)  # Only split at the first ':'
                if len(parts) == 2:
                    char, braille = parts
                    braille_dict[char] = braille
                else:
                    print(f"Skipping invalid line: {line.strip()}")
        return braille_dict

    def texto_a_braille(self, texto):
        return ''.join(self.braille_dict.get(char, '') for char in texto.lower())

    def braille_a_texto(self, braille):
        reverse_braille_dict = {v: k for k, v in self.braille_dict.items()}
        return ''.join(reverse_braille_dict.get(char, '') for char in braille)
