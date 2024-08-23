import fitz  # PyMuPDF
from test_chatgpt import generate_text


def pdf_to_text(pdf_path):
    pdf_document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    pdf_document.close()
    return text


def test_generate_text(pdf_path):
    # Extrae el texto del PDF
    pdf_text = pdf_to_text(pdf_path)

    # Define el prompt utilizando el texto del PDF
    prompt = f"Utilizando Formato JSON Genera 10 pregunta de opción múltiple sobre derecho basada en el siguiente texto:\n\n{pdf_text}"

    # Llama a la función generate_text
    result = generate_text(prompt)

    # Verifica el resultado
    assert result is not None and len(result) > 0
    print("GPT response:", result)


if __name__ == "__main__":
    pdf_path = "C:/Users/DIEGO/Desktop/poc_chatgpt/pdf_files/DERECHO_PENAL.pdf"
    test_generate_text(pdf_path)
    print("Test passed!")
