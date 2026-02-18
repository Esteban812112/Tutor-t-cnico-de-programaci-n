"""
Ejercicio 1
Conexión básica a Gemini
Explicar qué es la inferencia en IA en menos de 50 palabras.
"""

import os
from dotenv import load_dotenv
from google import genai

# Cargar variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Inicializar cliente
client = genai.Client(api_key=API_KEY)

# Realizar consulta
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explica qué es la inferencia en Inteligencia Artificial en menos de 50 palabras."
)

print("\nRespuesta:\n")
print(response.text)
