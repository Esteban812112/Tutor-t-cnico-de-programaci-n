"""
Ejercicio 3
Chat de soporte con historial (few-shot)
"""

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Cargar variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

# Configuración con rol
configuration = types.GenerateContentConfig(
    system_instruction="""
Eres un vendedor amable de una tienda de tecnología.
Responde con especificaciones claras y tono amigable.
"""
)

# Historial few-shot
history = [
    {
        "role": "user",
        "parts": [{"text": "¿Qué características tiene el iPhone 15?"}]
    },
    {
        "role": "model",
        "parts": [{"text": "El iPhone 15 cuenta con chip A16 Bionic, cámara de 48MP y pantalla OLED de 6.1 pulgadas."}]
    },
    {
        "role": "user",
        "parts": [{"text": "¿Qué memoria trae el portátil Lenovo IdeaPad?"}]
    },
    {
        "role": "model",
        "parts": [{"text": "El Lenovo IdeaPad incluye 16GB de RAM, 512GB SSD y procesador Intel Core i7."}]
    }
]

chat = client.chats.create(
    model="gemini-2.5-flash",
    config=configuration,
    history=history
)

print("\n--- Chat Tienda Tecnología ---")
print("(Escribe 'finalizar' para salir)\n")

while True:
    user_input = input("Cliente: ")

    if user_input.lower() == "finalizar":
        print("Vendedor: ¡Gracias por visitarnos! 😊")
        break

    try:
        response = chat.send_message(user_input)
        print(f"\nVendedor: {response.text}\n")
    except Exception as e:
        print(f"Error: {e}")
