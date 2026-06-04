from rag.embeddings import model
import numpy as np

def retrieve(chunks, index, query, top_k=3):
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")
    distances, indices = index.search(query_embedding,top_k)

    retrieved_chunks = []
    for idx in indices[0]:
        if idx != -1:
            retrieved_chunks.append(
                {
                    "text": chunks[idx]
                }
            )
    return retrieved_chunks