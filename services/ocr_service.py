import pytesseract
from PIL import Image
import re

pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract.exe")

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(image)
        return extracted_text.strip()

    except Exception as e:
        raise Exception(f"OCR Error: {str(e)}")


def clean_extracted_text(text):

    text = text.strip()

    # Replace multiple spaces/tabs with single space
    text = re.sub(r'[ \t]+', ' ', text)

    # Replace multiple newlines with single newline
    text = re.sub(r'\n{2,}', '\n', text)

    return text