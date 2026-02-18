"""
Ejercicio 2
Procesador de Textos Inteligente
Autor: Esteban

Descripción:
Permite elegir una tarea para procesar un texto:
- resumir
- profesionalizar
- simplificar
- ampliar
"""

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# ==========================
# Cargar API KEY
# ==========================
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

# ==========================
# Función principal
# ==========================
def procesar_articulo(texto, tarea):

    configuration = types.GenerateContentConfig(
        system_instruction="""
Eres un Editor Editorial de prestigio.
Tus respuestas deben ser profesionales, claras, estructuradas y bien redactadas.
"""
    )

    if tarea == "resumir":
        instruccion = "Elabora un resumen ejecutivo claro y conciso del siguiente texto."
    elif tarea == "profesionalizar":
        instruccion = "Reescribe el texto con un tono formal, técnico y profesional."
    elif tarea == "simplificar":
        instruccion = "Reescribe el texto en un lenguaje sencillo y fácil de entender."
    elif tarea == "ampliar":
        instruccion = "Amplía el texto agregando más detalles y profundidad conceptual."
    else:
        return "Tarea no válida."

    prompt = f"""
{instruccion}

Texto:
{texto}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=configuration,
        contents=prompt
    )

    return response.text


# ==========================
# Programa principal
# ==========================
if __name__ == "__main__":

    print("=== PROCESADOR DE TEXTOS INTELIGENTE ===\n")

    print("Tareas disponibles:")
    print("1. resumir")
    print("2. profesionalizar")
    print("3. simplificar")
    print("4. ampliar")

    tarea = input("\nEscriba la tarea que desea realizar: ").strip().lower()


    print("\nAhora ingrese el texto:\n")
    texto = input()

    resultado = procesar_articulo(texto, tarea)

    print("\n===== RESULTADO =====\n")
    print(resultado)
