# Taller Gemini - Roles y Procesamiento Inteligente

Autor: Juan Esteban Pinzon Preciado y Jose Felipe Sanabria Lombana

Este repositorio contiene el desarrollo del taller práctico utilizando la API de Google Gemini y el manejo de roles mediante system_instruction.


Ejercicio 1

Se realiza la conexión con la API de Gemini utilizando una API Key almacenada en un archivo `.env`.

El modelo genera una explicación sobre qué es la inferencia en Inteligencia Artificial.

Ejercicio 2

Se implementa la función:

```python
procesar_articulo(texto, tarea)
```

Permite realizar las siguientes tareas:

- resumir -> genera un resumen ejecutivo
- profesionalizar -> convierte el texto a tono formal y técnico
- simplificar -> lenguaje sencillo
- ampliar -> agrega profundidad conceptual

Se utiliza `system_instruction` definiendo el rol como:

"Editor Editorial de prestigio"

Ejercicio 3

Se crea un chat multi-turno utilizando:

- system_instruction
- history (few-shot prompting)
- Rol de vendedor tecnológico

Permite mantener conversación hasta que el usuario escriba "finalizar".

Tecnologías Utilizadas

- Python 3
- google-genai
- python-dotenv

Ejecución

1. Crear archivo `.env` con:

```
GEMINI_API_KEY=TU_API_KEY
```

2. Instalar dependencias:

```
pip install -r requirements.txt
```

3. Ejecutar:

```
python ejercicio1.py
python ejercicio2.py
python ejercicio3.py
```

---

Evidencias de funcionamiento

Ejercicio 1 en ejecución:

<img width="1911" height="1029" alt="image" src="https://github.com/user-attachments/assets/0b15c1ab-2f3f-494a-8063-bd1ddcda31fd" />


Ejercicio 2 en ejecución:
<img width="1919" height="993" alt="image" src="https://github.com/user-attachments/assets/c228aa4f-7395-4a35-96da-15eec9db91f8" />


Ejercicio 3 en ejecución:

<img width="1919" height="1037" alt="image" src="https://github.com/user-attachments/assets/ccb87c6e-6faf-47f0-a79c-1652b241251c" />



---

##  Conclusión

El taller demuestra el uso de roles, configuración mediante system_instruction, procesamiento dinámico de texto y chat multi-turno utilizando la API de Google Gemini.
