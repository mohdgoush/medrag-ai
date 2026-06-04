import pdfplumber

def extract_text_from_pdf(pdf_path):
    extracted_text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    extracted_text += text + "\n"
        return extracted_text.strip()
    
    except Exception as e:
        raise Exception(
            f"Error Extracting PDF Text: {str(e)}"
        )