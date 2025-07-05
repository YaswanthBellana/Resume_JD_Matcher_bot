import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()

def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()
