import anthropic
from config import CLAUDE_API_KEY

# Configura el cliente de Anthropic con la clave API
client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

def generate_claude_text(prompt):
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    # Accede directamente al texto de la respuesta
    return response.content

def test_generate_claude_text():
    prompt = "Genera una pregunta de opción múltiple sobre derecho."
    result = generate_claude_text(prompt)
    assert result is not None and len(result) > 0
    print("Claude response:", result)  # Imprime el texto generado

if __name__ == "__main__":
    test_generate_claude_text()
    print("Test passed!")
