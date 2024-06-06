import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont

# Diccionario Braille
braille_dict = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋',
    'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇',
    'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠟', 'r': '⠗',
    's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭',
    'y': '⠽', 'z': '⠵',
    'á': '⠷', 'é': '⠮', 'í': '⠌', 'ó': '⠨', 'ú': '⠾',
    '0': '⠴', '1': '⠂', '2': '⠆', '3': '⠒', '4': '⠲', '5': '⠢',
    '6': '⠖', '7': '⠶', '8': '⠦', '9': '⠔',
    '.': '⠲', ',': '⠂', ';': '⠆', ':': '⠒', '!': '⠖', '?': '⠦',
    ' ': ' '
}

# Funciones de Conversión
def texto_a_braille(texto):
    """
    Generate a Braille representation of the given text by looking up each character in the braille_dict.

    Parameters:
        texto (str): The text to convert to Braille.

    Returns:
        str: The Braille representation of the input text.
    """
    return ''.join(braille_dict.get(char, '') for char in texto.lower())

def braille_a_texto(braille):
    """
    Generate text of the given braille text string by looking up each character in a reverse braille_dict.

    Parameters:
        braille (str): The Braille text to be converted to text.

    Returns:
        str: The corresponding text string.
    """
    reverse_braille_dict = {v: k for k, v in braille_dict.items()}
    return ''.join(reverse_braille_dict.get(char, '') for char in braille)

# Función para Generar Señalética Braille
def generar_senaletica_braille(texto, nombre_archivo):
    """
    Generates an image with Braille text and saves it to a file.

    This function converts a given text to its Braille equivalent, creates an image with the Braille text,
    and saves it to a specified file.

    Parameters:
        texto (str): The text to be converted to Braille.
        nombre_archivo (str): The name of the file to save the Braille signage image.

    Returns:
        None
    """
    braille_text = texto_a_braille(texto)
    img = Image.new('RGB', (len(braille_text) * 20, 30), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    d.text((10, 10), braille_text, font=font, fill=(0, 0, 0))
    img.save(nombre_archivo)

# Función para Imprimir en Espejo
def imprimir_en_espejo_braille(texto):
    """
    Generate a Braille representation of the given text by looking up each character in the braille_dict and returns
    it in reverse order.

    Parameters:
        texto (str): The text to be converted to Braille.

    Returns:
        str: The Braille representation of the input text in reverse order.
    """
    braille_text = texto_a_braille(texto)
    return braille_text[::-1]

# Interfaz Gráfica con Tkinter
class BrailleApp:
    """
    A class to create a GUI application for translating text between Spanish and Braille, generating Braille signage,
    and printing Braille text in mirror mode.

    Attributes:
    root : Tk
        The root window of the Tkinter application.
    label_esp : Label
        Label for the Spanish text input field.
    text_esp : Text
        Text widget for inputting Spanish text.
    label_brl : Label
        Label for the Braille text input field.
    text_brl : Text
        Text widget for inputting Braille text.
    btn_esp_to_brl : Button
        Button to convert Spanish text to Braille.
    btn_brl_to_esp : Button
        Button to convert Braille text to Spanish.
    btn_generar_senaletica : Button
        Button to generate Braille signage from Spanish text.
    btn_imprimir_espejo : Button
        Button to print Braille text in mirror mode.

    Methods:
    convertir_esp_a_brl():
        Converts Spanish text from the input field to Braille and displays it in the Braille text field.
    convertir_brl_a_esp():
        Converts Braille text from the input field to Spanish and displays it in the Spanish text field.
    generar_senaletica():
        Generates a Braille signage image from the Spanish text input and saves it as 'senaletica.png'.
    imprimir_espejo():
        Converts Spanish text to mirrored Braille text and displays it in the Braille text field.
    """
    def __init__(self, root):
        """
        Initialize the GUI for the Transcriptor Braille application.
        Sets up the text labels and input fields for Alphabetic text and Braille text,
        as well as the buttons for converting text between languages, generating Braille signage,
        and printing in mirror mode.
        """
        self.root = root
        self.root.title("Transcriptor Braille")
        
        # Entradas y etiquetas
        self.label_esp = tk.Label(root, text="Texto en Español:")
        self.label_esp.grid(row=0, column=0)
        
        self.text_esp = tk.Text(root, height=10, width=50)
        self.text_esp.grid(row=1, column=0)
        
        self.label_brl = tk.Label(root, text="Texto en Braille:")
        self.label_brl.grid(row=0, column=1)
        
        self.text_brl = tk.Text(root, height=10, width=50)
        self.text_brl.grid(row=1, column=1)
        
        # Botones
        self.btn_esp_to_brl = tk.Button(root, text="Español a Braille", command=self.convertir_esp_a_brl)
        self.btn_esp_to_brl.grid(row=2, column=0)
        
        self.btn_brl_to_esp = tk.Button(root, text="Braille a Español", command=self.convertir_brl_a_esp)
        self.btn_brl_to_esp.grid(row=2, column=1)

        self.btn_generar_senaletica = tk.Button(root, text="Generar Señalética Braille", command=self.generar_senaletica)
        self.btn_generar_senaletica.grid(row=3, column=0)

        self.btn_imprimir_espejo = tk.Button(root, text="Imprimir en Espejo", command=self.imprimir_espejo)
        self.btn_imprimir_espejo.grid(row=3, column=1)
        
    def convertir_esp_a_brl(self):
        """
        Convert Spanish text from the input field to Braille and display it in the Braille text field.
        """
        texto_esp = self.text_esp.get("1.0", tk.END).strip()
        texto_brl = texto_a_braille(texto_esp)
        self.text_brl.delete("1.0", tk.END)
        self.text_brl.insert(tk.END, texto_brl)
        
    def convertir_brl_a_esp(self):
        """
        Convert Braille text from the input field to Spanish and display it in the Spanish text field.
        """
        texto_brl = self.text_brl.get("1.0", tk.END).strip()
        texto_esp = braille_a_texto(texto_brl)
        self.text_esp.delete("1.0", tk.END)
        self.text_esp.insert(tk.END, texto_esp)

    def generar_senaletica(self):
        """
        Generate a Braille signage image from the Spanish text input and save it as 'senaletica.png'.
        Display a message box confirming the save location.
        """
        texto_esp = self.text_esp.get("1.0", tk.END).strip()
        nombre_archivo = "senaletica.png"
        generar_senaletica_braille(texto_esp, nombre_archivo)
        messagebox.showinfo("Generación de Señalética", f"Señalética Braille guardada como {nombre_archivo}")

    def imprimir_espejo(self):
        """
        Convert Spanish text to mirrored Braille text and display it in the Braille text field.
        """
        texto_esp = self.text_esp.get("1.0", tk.END).strip()
        texto_brl_espejo = imprimir_en_espejo_braille(texto_esp)
        self.text_brl.delete("1.0", tk.END)
        self.text_brl.insert(tk.END, texto_brl_espejo)

if __name__ == "__main__":
    root = tk.Tk()
    app = BrailleApp(root)
    root.mainloop()
