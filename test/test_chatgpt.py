from openai import OpenAI
from config import OPENAI_API_KEY

# Inicializar con clave API
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_text(prompt):
    response = client.completions.create(
        model="gpt-4o-mini",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def test_generate_text():
    prompt = "Genera una pregunta de opción múltiple sobre derecho."
    result = generate_text(prompt)
    assert result is not None and len(result) > 0
    print("GPT response:", result)

if __name__ == "__main__":
    test_generate_text()
    print("Test passed!")
