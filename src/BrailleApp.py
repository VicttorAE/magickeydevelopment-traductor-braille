# BrailleApp.py

import tkinter as tk
from tkinter import messagebox
from BrailleTranslator import BrailleTranslator
from BrailleImageGenerator import BrailleImageGenerator

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
    def __init__(self, root, translator, image_generator):
        """
        Initialize the GUI for the Transcriptor Braille application.

        Sets up the text labels and input fields for Alphabetic text and Braille text, as well as the buttons 
        for converting text between languages, generating Braille signage, and printing in mirror mode.

        Parameters:
            root (Tk): The root window of the Tkinter application.
            translator (Translator): An instance of the Translator class for text translation.
            image_generator (ImageGenerator): An instance of the ImageGenerator class for generating Braille signage images.
        
        Returns:
            None
        """
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
        """
        Converts the text in the Spanish text field to Braille and displays the result in the Braille text field.

        This function retrieves the text from the Spanish text field, calls the `texto_a_braille` method of the `translator` 
        object to convert the text to Braille, and then updates the Braille text field with the converted text.

        Parameters:
            self (BrailleApp): The current instance of the BrailleApp class.

        Returns:
            None
        """

        texto_esp = self.text_esp.get("1.0", tk.END).strip()
        texto_brl = self.translator.texto_a_braille(texto_esp)
        self.text_brl.delete("1.0", tk.END)
        self.text_brl.insert(tk.END, texto_brl)
        
    def convertir_brl_a_esp(self):
        """
        Converts the text in the Braille text field to Spanish and displays the result in the Spanish text field.

        This function retrieves the text from the Braille text field, calls the `braille_a_texto` method of the `translator` 
        object to convert the text to Spanish, and then updates the Spanish text field with the converted text.

        Parameters:
            self (BrailleApp): The current instance of the BrailleApp class.

        Returns:
            None
        """
        texto_brl = self.text_brl.get("1.0", tk.END).strip()
        texto_esp = self.translator.braille_a_texto(texto_brl)
        self.text_esp.delete("1.0", tk.END)
        self.text_esp.insert(tk.END, texto_esp)

    def generar_senaletica(self):
        """
        Generates a Braille signage image based on the text in the Spanish text field.

        This function retrieves the text from the Spanish text field, generates a Braille signage image using the
        `generar_senaletica_braille` method of the `image_generator` object, and displays a message box with the
        information that the Braille signage image has been saved.

        Parameters:
            self (BrailleApp): The current instance of the BrailleApp class.

        Returns:
            None
        """
        texto_esp = self.text_esp.get("1.0", tk.END).strip()
        nombre_archivo = "senaletica.png"
        self.image_generator.generar_senaletica_braille(texto_esp, nombre_archivo)
        messagebox.showinfo("Generación de Señalética", f"Señalética Braille guardada como {nombre_archivo}")

    def imprimir_espejo(self):
        """
        Prints the mirrored Braille text in the Braille text field and configures the size and position of the window.
        
        This function retrieves the Spanish text from the text field, generates the mirrored Braille text using the 
        `imprimir_en_espejo_braille` method of the `image_generator` object, and displays the mirrored Braille text in 
        the Braille text field. The size and position of the window are configured to ensure that it is centered on 
        the screen. The window is displayed using the `mainloop` method of the Tkinter root window.
        
        Parameters:
            self (BrailleApp): The current instance of the BrailleApp class.
        
        Returns:
            None
        """
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

