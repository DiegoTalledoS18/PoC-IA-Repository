import google.generativeai as genai
import os
from config import GOOGLE_API_KEY

# Configura el cliente de Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Inicializa el modelo
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_text(prompt):
    response = model.generate_content(prompt)
    return response.text.strip()

def test_generate_text():
    prompt = "Genera una pregunta de opción múltiple sobre derecho."
    result = generate_text(prompt)
    assert result is not None and len(result) > 0
    print("Gemini response:", result)

if __name__ == "__main__":
    test_generate_text()
    print("Test passed!")