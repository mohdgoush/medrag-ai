from fastapi import APIRouter, HTTPException
from app.schemas.models import QueryRequest
from rag.retriever import retrieve
from rag.vector_store import load_index, load_metadata
from services.groq_service import generate_response

router = APIRouter()

chat_history = []

@router.post("/explain")
async def explain_report(request: QueryRequest):
    try:
        index = load_index("vector_stores/medical_index.faiss")
        chunks = load_metadata("vector_stores/metadata.pkl")

        retrieved_chunks = retrieve(
            chunks=chunks,
            index=index,
            query=request.question,
            top_k=3
        )

        answer = generate_response(
            query=request.question,
            retrieved_chunks=retrieved_chunks,
            chat_history=chat_history
        )

        chat_history.append({
            "role": "user",
            "content": request.question
        })

        chat_history.append({
            "role": "assistant",
            "content": answer
        })

        return {
            "question":
            request.question,

            "answer":
            answer
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )