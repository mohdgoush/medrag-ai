from sentence_transformers import SentenceTransformer
import numpy as np

model = None


def get_model():
    global model
    if model is None:
        model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    return model

def create_embeddings(chunks):
    try:

        model = get_model()

        embeddings = (
            model.encode(
                chunks,
                convert_to_numpy=True
            )
            .astype(np.float32)
        )

        return embeddings

    except Exception as e:
        raise Exception(
            f"Embedding Error: {str(e)}"
        )