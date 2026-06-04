from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(chunks):
    try:
        embeddings = model.encode(chunks,convert_to_numpy=True).astype(np.float32)
        return embeddings

    except Exception as e:
        raise Exception(
            f"Embedding Error: {str(e)}"
        )