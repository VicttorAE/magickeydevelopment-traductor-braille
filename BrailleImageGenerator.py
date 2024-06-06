from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog, messagebox

class BrailleImageGenerator:
    def __init__(self, translator):
        self.translator = translator
    
    def generar_senaletica_braille(self, texto, nombre_archivo):
        braille_text = self.translator.texto_a_braille(texto)
        nombre_archivo = filedialog.asksaveasfilename(
            defaultextension = ".*", title = "Save File", filetypes = (("PNG Files", "*.png"), ("All Files", "*.*"), ))
        img = Image.new('RGB', (len(braille_text) * 30, 50), color=(255, 255, 255))
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype('Font/ONCE_CBE_6.ttf', 30)
        d.text((10, 10), braille_text, font=font, fill=(0, 0, 0))
        img.save(nombre_archivo)

    def imprimir_en_espejo_braille(self, texto):
        braille_text = self.translator.texto_a_braille(texto)
        return braille_text[::-1]
