import streamlit as st
import PyPDF2
from pdf2image import convert_from_bytes
import pytesseract
from PIL import Image
from io import BytesIO

def extract_pdf_text(pdf_file):
    """
    Attempts to extract text from a PDF using PyPDF2. If no text
    is extracted (i.e. scanned image PDF), converts pages to images and uses OCR.
    """
    text = ""
    try:
        pdf_bytes = pdf_file.read()
        pdf_file.seek(0)
        reader = PyPDF2.PdfReader(BytesIO(pdf_bytes))
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        if text.strip() == "":
            images = convert_from_bytes(pdf_bytes)
            for image in images:
                page_text = pytesseract.image_to_string(image, lang="ara+eng")
                text += page_text + "\n"
        return text
    except Exception as e:
        st.error(f"Error processing PDF: {e}")
        return ""

def process_uploaded_file(uploaded_file):
    """
    Supports file uploads of types:
      - PDF: extracts text (or uses OCR if scanned)
      - TXT: reads the text directly
      - Images (JPG, JPEG, PNG): extracts text using OCR
    """
    content = ""
    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            content = extract_pdf_text(uploaded_file)
        elif uploaded_file.type in ["image/jpeg", "image/jpg", "image/png"]:
            image = Image.open(uploaded_file)
            content = pytesseract.image_to_string(image, lang="ara+eng")
        elif uploaded_file.type in ["text/plain"]:
            content = uploaded_file.read().decode("utf-8")
        else:
            try:
                content = uploaded_file.read().decode("utf-8")
            except Exception as e:
                st.error(f"Error reading file: {e}")
    return content
