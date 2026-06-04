# MedRAG AI

Medical Report Explainer using RAG (Retrieval-Augmented Generation).

## Features

- PDF/Image Medical Report Upload
- OCR using Tesseract
- PDF Text Extraction
- Semantic Chunking
- Sentence Transformer Embeddings
- FAISS Vector Search
- Groq LLM Integration
- FastAPI Backend
- Streamlit Frontend

## Tech Stack

- Python
- FastAPI
- Streamlit
- FAISS
- Sentence Transformers
- Groq
- Tesseract OCR
- PDFPlumber

## Run Backend

```bash
uvicorn main:app --reload