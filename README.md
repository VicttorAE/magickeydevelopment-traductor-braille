# Calidad de Software

## GR2SW

## MagicKey Development

### Integrantes

- Victor Rodriguez
- Karina Arichavala
- Dayana Lema
- Matias Villareal
- Gilson Cango

## 1. Análisis

Historias de Usuario

| Historia de Usuario |                |
|----------------------|-----------------|
| Número:              | 1               |
| Usuario:             | Usuario        |
| Nombre historia:     | Transcripción de textos del español a braille |
| Prioridad en negocio: | Alta          |Riesgo en desarrollo: | Baja |
| Puntos estimados:    | 2              | Iteración asignada: | 1    |
| Descripción:         | Como usuario, quiero poder transcribir textos del español al sistema de escritura braille, incluyendo números, abecedario, vocales acentuadas y signos básicos, para que pueda generar contenido accesible para personas con discapacidad visual. |

| Criterios de aceptación |                |
|----------------------|-----------------|
| Número de HU:              | 1               |
| Descripción:               |                 | 

| Historia de Usuario |                |
|----------------------|-----------------|
| Número:              | 2               |
| Usuario:             | Usuario        |
| Nombre historia:     | Transcripción de textos de braille a español |
| Prioridad en negocio: | Alta          | Riesgo en desarrollo: | Baja |
| Puntos estimados:    | 2              | Iteración asignada: | 1    |
| Descripción:         | Como usuario, quiero poder transcribir textos escritos en braille al español, para poder entender el contenido escrito en braille. |

| Criterios de aceptación |                |
|----------------------|-----------------|
| Número de HU:              | 2               |
| Descripción:               |                 | 

| Historia de Usuario |                |
|----------------------|-----------------|
| Número:              | 3               |
| Usuario:             | Usuario        |
| Nombre historia:     | Generación de señaléticas en braille |
| Prioridad en negocio: | Alta          | Riesgo en desarrollo: | Baja |
| Puntos estimados:    | 2              | Iteración asignada: | 1    |
| Descripción:         | Como usuario, quiero poder generar señalética en braille a partir de textos en español, para mejorar la accesibilidad de edificios, aparatos, juegos de mesa, prendas de vestir, medicamentos, alimentos empacados, etc. |

| Criterios de aceptación |                |
|----------------------|-----------------|
| Número de HU:              | 3               |
| Descripción:               |                 | 

| Historia de Usuario |                |
|----------------------|-----------------|
| Número:              | 4               |
| Usuario:             | Usuario        |
| Nombre historia:     | Generación de impresiones en espejo |
| Prioridad en negocio: | Alta          | Riesgo en desarrollo: | Baja |
| Puntos estimados:    | 2              | Iteración asignada: | 1    |
| Descripción:         | Como usuario, quiero poder generar impresiones en espejo de textos braille, para poder escribir manualmente en braille utilizando un punzón y una regleta. |

| Criterios de aceptación |                |
|----------------------|-----------------|
| Número de HU:              | 4               |
| Descripción:               |                 | 

| Historia de Usuario |                |
|----------------------|-----------------|
| Número:              | 5               |
| Usuario:             | Usuario        |
| Nombre historia:     | Traducción y generación de impresiones guía |
| Prioridad en negocio: | Alta          | Riesgo en desarrollo: | Baja |
| Puntos estimados:    | 2              | Iteración asignada: | 1    |
| Descripción:         | Como usuario, quiero que el sistema se limite a la traducción entre español y braille, y a la generación de impresiones guía, sin incluir funcionalidades adicionales como idiomas adicionales, impresión braille 3D o enseñanza de braille. |

| Criterios de aceptación |                |
|----------------------|-----------------|
| Número de HU:              | 5               |
| Descripción:               |                 | 



# Construcción y evolución de Software
## Flujo de Trabajo Feature Branch Workflow
### Descripción del Flujo de Trabajo

Nuestro equipo utiliza un flujo de trabajo estructurado en Git para separar claramente las fases de desarrollo y testing en ramas dedicadas. Este flujo de trabajo asegura la estabilidad y calidad del código antes de que llegue a producción.

#### Ramas

- **`main`**: Esta rama se mantiene siempre estable y contiene la documentación.
- **`develop`**: Esta rama es donde se realiza el desarrollo activo de nuevas características y funcionalidades. Todos los desarrolladores colaboran en esta rama.
- **`testing`**: Ramas dedicadas para pruebas.
  - **`testing/image-generation`**: En esta rama se prueba la funcionalidad en general.
  - **`testing/character-recognition`**: En esta rama se hacen pruebas unitarias.
- **`preliminar-docs`**: contiene la documentación preliminar antes de enviarla al `main`.
#### Pasos del Flujo de Trabajo

1. **Desarrollo**:
   - Los desarrolladores trabajan en la rama `develop`.
   - Cada nueva característica o cambio se implementa en esta rama.
   - Cuando se completa una característica, se realiza una revisión de código (code review) a través de un pull request.

2. **Testing**:
   - Desde `develop`, se fusiona en las ramas de testing específicas:
     - **`testing/image-generation`**
     - **`testing/character-recognition`**
   - El tester realiza pruebas en estas ramas.
   - Si se encuentran errores, se corrigen en la rama de desarrollo `develop` y luego se vuelven a fusionar en las ramas de testing para retesting.

3. **Documentación Preliminar**:
   - La documentación preliminar se realiza en la rama `preliminar-docs`.
   - Una vez que la documentación está completa y revisada, se fusiona en `main`.

4. **Producción**:
   - Una vez que el código en la rama `testing` ha pasado todas las pruebas, se fusiona en la rama `main`.
   - La rama `main` contiene el código listo para ser desplegado en producción.

![alt text](<Flujo de trabajo.jpg>)

## Documentación del ambiente de desarrollo

### Lenguaje de Programación

- **Python**: Utilizamos la versión 3.12.3, la cual se puede descargar desde [python.org](https://www.python.org/downloads/release/python-3123/).

### Editor de Código

- **Visual Studio Code**: Se utilizó VS Code como editor de código, se puede descargar desde [code.visualstudio.com](https://code.visualstudio.com/).

## Instalación del Ambiente de Desarrollo

### Instalación de Python

1. Descargar el instalador de Python 3.12.3 en el enlace que se indicó con anterioridad.
2. Ejecutar el instalador y seguir las instrucciones para completar la instalación.

### Instalación de Visual Studio Code

1. Descargar el instalador de VS Code en el enlace que se indicó con anterioridad.
2. Ejecutar el instalador y seguir las instrucciones para completar la instalación.

### Configuración del Ambiente de Desarrollo

1. **Instalar extensiones recomendadas en VS Code**:
    - Python: Esta extensión proporciona soporte para Python en VS Code.

2. **Configurar el intérprete de Python**:
    - Abrir VS Code y seleccionar el intérprete de Python 3.12.3:
        - Presionar `Ctrl+Shift+P` para abrir la paleta de comandos.
        - Escribir `Python: Select Interpreter` y seleccionar la versión 3.12.3.

