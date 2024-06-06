# Proyecto de Calidad de Software

## GR2SW

## MagicKey Development

### Integrantes

- Victor Rodriguez
- Gabriela Arichavala
- Dayana Lema
- Matias Villareal
- Gilson Cango

## Análisis

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




# Flujo de Trabajo Feature Branch Workflow
## Descripción del Flujo de Trabajo

Nuestro equipo utiliza un flujo de trabajo estructurado en Git para separar claramente las fases de desarrollo y testing en ramas dedicadas. Este flujo de trabajo asegura la estabilidad y calidad del código antes de que llegue a producción.

## Ramas

- **`main`**: Esta rama se mantiene siempre estable y contiene la documentación.
- **`develop`**: Esta rama es donde se realiza el desarrollo activo de nuevas características y funcionalidades. Todos los desarrolladores colaboran en esta rama.
- **`testing`**: Una vez que se completa una característica en `develop`, se fusiona en `testing` para pruebas. Esta rama es manejada por el tester.

## Pasos del Flujo de Trabajo

1. **Desarrollo**:
   - Los desarrolladores trabajan en la rama `develop`.
   - Cada nueva característica o cambio se implementa en esta rama.
   - Cuando se completa una característica, se realiza una revisión de código (code review) a través de un pull request.

2. **Testing**:
   - Después de aprobarse una característica en la revisión de código, se fusiona la rama `develop` en la rama `testing`.
   - El equipo de testing realiza pruebas exhaustivas en esta rama.
   - Si se encuentran errores, se corrigen en la rama `develop` y luego se vuelven a fusionar en `testing` para retesting.

3. **Producción**:
   - Una vez que el código en la rama `testing` ha pasado todas las pruebas, se fusiona en la rama `main`.
   - La rama `main` contiene el código listo para ser desplegado en producción.

