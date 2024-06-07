# BrailleTranslator.py

class BrailleTranslator:
    def __init__(self, dict_file):
        """
        Initializes a new instance of the class.

        Parameters:
            dict_file (str): The path to the file containing the dictionary.

        Returns:
            None
        """
        self.braille_dict = self.load_dict(dict_file)

    def load_dict(self, dict_file):
        """
        Load a dictionary from a file.

        This function reads a file specified by the `dict_file` parameter and loads its contents into a dictionary.
        Each line in the file is split at the first ':' character, and if the resulting parts have exactly two elements,
        the character and its corresponding braille representation are added to the `braille_dict` dictionary.
        If a line does not have exactly two parts, it is skipped and a message is printed to the console.

        Parameters:
            dict_file (str): The path to the file containing the dictionary.

        Returns:
            dict: The loaded dictionary containing the character-braille mappings.
        """
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
        """
        Generate a Braille representation of the given text by looking up each character in the braille_dict.

        Parameters:
            texto (str): The text to convert to Braille.

        Returns:
            str: The Braille representation of the input text.
        """
        return ''.join(self.braille_dict.get(char, '') for char in texto.lower())

    def braille_a_texto(self, braille):
        """
        Generate text of the given braille text string by looking up each character in a reverse braille_dict.

        Parameters:
            braille (str): The Braille text to be converted to text.
            
        Returns:
            str: The corresponding text string.
        """
        reverse_braille_dict = {v: k for k, v in self.braille_dict.items()}
        return ''.join(reverse_braille_dict.get(char, '') for char in braille)
