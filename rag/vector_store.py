import faiss
import pickle
import numpy as np


def create_faiss_index(embeddings):
    try:
        embeddings = np.array(embeddings).astype("float32")
        dimension = embeddings.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(embeddings)
        return index

    except Exception as e:
        raise Exception(f"Error Creating Index: {str(e)}")

def save_index(index, path):
    faiss.write_index(index, path)

def load_index(path):
    return faiss.read_index(path)

def save_metadata(chunks, path):
    with open(path, "wb") as f:
        pickle.dump(chunks, f)

def load_metadata(path):
    with open(path, "rb") as f:
        return pickle.load(f)