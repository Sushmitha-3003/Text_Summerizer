import PyPDF2
import os

def load_text_from_txt(file_path):
    """Reads all text from a text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"An error occurred while reading the TXT file: {e}")
        return None

def load_text_from_pdf(file_path):
    """Extracts text from a PDF file."""
    try:
        with open(file_path, 'rb') as pdf_file_obj:
            pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text

    except Exception as e:
        print(f"An error occurred while reading the PDF file: {e}")
        return None

def load_text_from_file(file_path):
    """Detects file type and loads text accordingly."""
    if not file_path:
        print("Error: No file path provided.")
        return None

    file_extension = file_path.split('.')[-1].lower()

    if file_extension == 'pdf':
        return load_text_from_pdf(file_path)
    elif file_extension == 'txt':
        return load_text_from_txt(file_path)
    else:
        print(f"Error: Unsupported file type '{file_extension}'")
        return None

def save_original_text(text, file_path):
    """Saves a string of text to a file."""
    output_dir = os.path.dirname(file_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Original text saved to {file_path}")
    except Exception as e:
        print(f"An error occurred while saving the original file: {e}")