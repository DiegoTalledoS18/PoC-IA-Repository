from openai import OpenAI
from config import OPENAI_API_KEY

# Configurar el cliente OpenAI con la clave API importada
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_text(prompt):
    # Crear una solicitud de completado
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un experto en generar contenido educativo. Ayúdame creando una pregunta de opción múltiple sobre derecho."},  # Mensaje del sistema en español
            {"role": "user", "content": prompt}
        ]
    )

    # Retornar la respuesta del asistente
    return completion.choices[0].message.content

def test_generate_text():
    prompt = "Genera una pregunta de opción múltiple sobre derecho."
    result = generate_text(prompt)
    assert result is not None and len(result) > 0
    print("GPT response:", result)

if __name__ == "__main__":
    test_generate_text()
    print("Test passed!")