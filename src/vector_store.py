import faiss
import numpy as np

from embeddings import embeddings


def create_vector_store(embeddings):
    embeddings = np.array(embeddings).astype("float32")

    # Vectors ko normalize karo
    faiss.normalize_L2(embeddings)

    dimension = embeddings.shape[1]

    # Inner Product + normalized vectors = cosine similarity
    index = faiss.IndexFlatIP(dimension)

    index.add(embeddings)

    return index


index = create_vector_store(embeddings)

faiss.write_index(index, "vectorstore/index.faiss")

print("Total vectors:", index.ntotal)
print("Vector dimension:", index.d)
print("Vector store saved successfully!")