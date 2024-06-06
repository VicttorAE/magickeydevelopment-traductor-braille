# BrailleApp.py

import tkinter as tk
from tkinter import messagebox
from BrailleTranslator import BrailleTranslator
from BrailleImageGenerator import BrailleImageGenerator

class BrailleApp:
    def __init__(self, root, translator, image_generator):
        self.root = root
        self.translator = translator
        self.image_generator = image_generator
        self.root.title("Transcriptor Braille")
        
        fuente_grande = ('Helvetica', 14)
        
        # Entradas y etiquetas
        self.label_esp = tk.Label(root, text="Texto en Español:", font=fuente_grande)
        self.label_esp.grid(row=0, column=0)
        
        self.text_esp = tk.Text(root, height=10, width=50, font=fuente_grande)
        self.text_esp.grid(row=1, column=0)
        
        self.label_brl = tk.Label(root, text="Texto en Braille:",font=fuente_grande)
        self.label_brl.grid(row=0, column=1)
        
        self.text_brl = tk.Text(root, height=10, width=50, font=fuente_grande)
        self.text_brl.grid(row=1, column=1)
        
        # Botones
        self.btn_esp_to_brl = tk.Button(root, text="Español a Braille", command=self.convertir_esp_a_brl, font=fuente_grande)
        self.btn_esp_to_brl.grid(row=2, column=0)
        
        self.btn_brl_to_esp = tk.Button(root, text="Braille a Español", command=self.convertir_brl_a_esp, font=fuente_grande)
        self.btn_brl_to_esp.grid(row=2, column=1)

        self.btn_generar_senaletica = tk.Button(root, text="Generar Señalética Braille", command=self.generar_senaletica, font=fuente_grande)
        self.btn_generar_senaletica.grid(row=3, column=0)

        self.btn_imprimir_espejo = tk.Button(root, text="Imprimir en Espejo", command=self.imprimir_espejo, font=fuente_grande)
        self.btn_imprimir_espejo.grid(row=3, column=1)
        
        # Configurar el ajuste de columnas y filas
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)


    def convertir_esp_a_brl(self):
        texto_esp = self.text_esp.get("1.0", tk.END).strip()
        texto_brl = self.translator.texto_a_braille(texto_esp)
        self.text_brl.delete("1.0", tk.END)
        self.text_brl.insert(tk.END, texto_brl)
        
    def convertir_brl_a_esp(self):
        texto_brl = self.text_brl.get("1.0", tk.END).strip()
        texto_esp = self.translator.braille_a_texto(texto_brl)
        self.text_esp.delete("1.0", tk.END)
        self.text_esp.insert(tk.END, texto_esp)

    def generar_senaletica(self):
        texto_esp = self.text_esp.get("1.0", tk.END).strip()
        nombre_archivo = "senaletica.png"
        self.image_generator.generar_senaletica_braille(texto_esp, nombre_archivo)
        messagebox.showinfo("Generación de Señalética", f"Señalética Braille guardada como {nombre_archivo}")

    def imprimir_espejo(self):
        texto_esp = self.text_esp.get("1.0", tk.END).strip()
        texto_brl_espejo = self.image_generator.imprimir_en_espejo_braille(texto_esp)
        self.text_brl.delete("1.0", tk.END)
        self.text_brl.insert(tk.END, texto_brl_espejo)
        
         # Configurar el tamaño y la posición de la ventana
        window_width = 800  # Ancho de la ventana
        window_height = 600  # Alto de la ventana
        position_x = int(self.root.winfo_screenwidth() / 2 - window_width / 2)
        position_y = int(self.root.winfo_screenheight() / 2 - window_height / 2)
        self.root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        # Configurar el ajuste de columnas y filas
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Mostrar la ventana
        self.root.mainloop()

