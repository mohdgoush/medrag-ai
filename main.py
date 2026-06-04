from fastapi import FastAPI
from app.routers.upload import router as upload_router
from app.routers.explain import router as explain_router

app = FastAPI( title="MedRAG AI")

app.include_router(upload_router)
app.include_router(explain_router)

@app.get("/")
def home():
    return {
        "message":
        "MedRAG AI is running"
    }