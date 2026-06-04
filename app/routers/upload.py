from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os

from services.ocr_service import extract_text_from_image, clean_extracted_text
from services.pdf_service import extract_text_from_pdf

from rag.chunking import create_chunks
from rag.embeddings import create_embeddings
from rag.vector_store import create_faiss_index, save_index, save_metadata

router = APIRouter()

UPLOAD_DIR = "uploads"
VECTOR_DIR = "vector_stores"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(VECTOR_DIR, exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_path = os.path.join( UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file,buffer)

        # IMAGE
        if file.content_type.startswith("image/"):
            extracted_text = extract_text_from_image(file_path)
            text = clean_extracted_text (extracted_text)

        # PDF
        elif file.content_type == "application/pdf":
            text = extract_text_from_pdf(file_path)

        else:

            raise HTTPException(
                status_code=400,
                detail="Unsupported file type"
            )

        # Chunking
        chunks = create_chunks(text)

        # Embeddings
        embeddings = create_embeddings(chunks)

        # FAISS
        index = create_faiss_index(embeddings)

        # Save
        save_index(index,"vector_stores/medical_index.faiss")
        save_metadata(chunks,"vector_stores/metadata.pkl")

        return {
            "message": "Medical report processed successfully",
            "chunks_created": len(chunks)
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )