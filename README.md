# Prueba Unitaria del Traductor Braille

Esta prueba unitaria evalúa el reconocimiento de caracteres para la traducción a Braille utilizando la clase BrailleTranslator.

## Objetivo de la Prueba

El objetivo de esta prueba es verificar que el método `texto_a_braille()` de la clase BrailleTranslator pueda reconocer correctamente varios tipos de caracteres y traducirlos a su equivalente en Braille.

## Descripción de los casos de prueba

1. **setUpClass**: Este método inicializa un objeto BrailleTranslator con el archivo 'brailleDictionary.txt' para preparar la prueba.

2. **test_vocales_acentuadas**: Este test verifica la traducción correcta de vocales acentuadas ('áéíóú') a su representación en Braille.

3. **test_abecedario**: Se evalúa si el abecedario completo ('abcdefghijklmnopqrstuvwxyz') se traduce correctamente a Braille.

4. **test_numeros**: Se comprueba la traducción adecuada de números ('0123456789') a su equivalente Braille.

5. **test_caracteres_especiales**: Este test verifica la traducción de caracteres especiales (',.;:!?@%&*+=-¡¿') a su representación en Braille.

6. **test_ñ_Ü**: Se evalúa si los caracteres especiales ('ñ' y 'Ü') se traducen correctamente a Braille.

## Cómo Ejecutar la Prueba

Para ejecutar esta prueba unitaria, ejecute el modulo `testBrailleTranslator` utilizando un marco de pruebas como `unittest`. Asegúrese de que las dependencias y los archivos necesarios, incluido 'brailleDictionary.txt', estén disponibles en el entorno de prueba.

Puede hacer uso de:

```terminal
python -m unittest testBrailleTranslator.py
```


## Resultado de la Prueba

Al ejecutar el test se obtuvo el resultado:

![Characters unit test](testResult/unitTestResult.png)

El resultado de la prueba muestra que hubo 3 fallos en la traducción de los caracteres especiales, las mayúsculas y los caracteres especiales ('.,;:!?@%&*+=-¡¿'). 

Los caracteres especiales ('ñ' y 'Ü') también fallaron en la traducción a Braille.


# Prueba Unitaria del Reconocimiento de Números en Braille

Esta prueba unitaria se enfoca en evaluar el reconocimiento de números para la traducción a Braille utilizando la clase BrailleTranslator.

## Objetivo de la Prueba

El objetivo de esta prueba es verificar que el método `texto_a_braille()` de la clase BrailleTranslator pueda reconocer correctamente números y traducirlos a su equivalente en Braille.

## Descripción del Caso de Prueba

### Test de Reconocimiento de Números

1. **test_number_prefix_single_digit**: Verifica si un número de un solo dígito ('1') se traduce correctamente a su representación en Braille.

2. **test_number_prefix_multiple_digits**: Evalúa si un número de varios dígitos ('123') se traduce correctamente a Braille.

3. **test_number_prefix_with_text**: Comprueba la traducción adecuada de un texto que contiene números ('a1b2c3') a su equivalente Braille.

4. **test_number_prefix_separated_digits**: Verifica la traducción de números separados ('1 2 3') a su representación en Braille.

5. **test_number_prefix_single_and_multiple_digits**: Evalúa si un texto que contiene tanto un número de un solo dígito como números de varios dígitos combinados ('a1 23b') se traduce correctamente a Braille.

## Cómo Ejecutar la Prueba

Para ejecutar esta prueba unitaria, ejecute el módulo `testBrailleNumber.py` utilizando un marco de pruebas como `unittest`. Asegúrese de que las dependencias y los archivos necesarios, incluido 'brailleDictionary.txt', estén disponibles en el entorno de prueba.

Puede hacer uso de:

```terminal
python -m unittest testBrailleNumber.py
```