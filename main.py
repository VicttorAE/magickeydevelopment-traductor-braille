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
    return ''.join(braille_dict.get(char, '') for char in texto.lower())

def braille_a_texto(braille):
    reverse_braille_dict = {v: k for k, v in braille_dict.items()}
    return ''.join(reverse_braille_dict.get(char, '') for char in braille)

# Función para Generar Señalética Braille
def generar_senaletica_braille(texto, nombre_archivo):
    braille_text = texto_a_braille(texto)
    img = Image.new('RGB', (len(braille_text) * 20, 30), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    d.text((10, 10), braille_text, font=font, fill=(0, 0, 0))
    img.save(nombre_archivo)

# Función para Imprimir en Espejo
def imprimir_en_espejo_braille(texto):
    braille_text = texto_a_braille(texto)
    return braille_text[::-1]

# Interfaz Gráfica con Tkinter
class BrailleApp:
    def __init__(self, root):
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
        texto_esp = self.text_esp.get("1.0", tk.END).strip()
        texto_brl = texto_a_braille(texto_esp)
        self.text_brl.delete("1.0", tk.END)
        self.text_brl.insert(tk.END, texto_brl)
        
    def convertir_brl_a_esp(self):
        texto_brl = self.text_brl.get("1.0", tk.END).strip()
        texto_esp = braille_a_texto(texto_brl)
        self.text_esp.delete("1.0", tk.END)
        self.text_esp.insert(tk.END, texto_esp)

    def generar_senaletica(self):
        texto_esp = self.text_esp.get("1.0", tk.END).strip()
        nombre_archivo = "senaletica.png"
        generar_senaletica_braille(texto_esp, nombre_archivo)
        messagebox.showinfo("Generación de Señalética", f"Señalética Braille guardada como {nombre_archivo}")

    def imprimir_espejo(self):
        texto_esp = self.text_esp.get("1.0", tk.END).strip()
        texto_brl_espejo = imprimir_en_espejo_braille(texto_esp)
        self.text_brl.delete("1.0", tk.END)
        self.text_brl.insert(tk.END, texto_brl_espejo)

if __name__ == "__main__":
    root = tk.Tk()
    app = BrailleApp(root)
    root.mainloop()
