import faiss
import numpy as np
import ollama

from src.embeddings import model
from src.loader import chunks

# Load FAISS vector store
index = faiss.read_index("vectorstore/index.faiss")


# Search relevant PDF chunks
def search(query, top_k=3):

    query_embedding = model.encode([query])

    query_embedding = np.array(query_embedding).astype("float32")

    faiss.normalize_L2(query_embedding)

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for i, score in zip(indices[0], distances[0]):

        results.append({"chunk": chunks[i], "score": float(score)})

    # Remove weak matches
    results = [result for result in results if result["score"] >= 0.45]

    return results


# Create context from PDF chunks
def create_context(results):

    context = ""

    for result in results:

        context += result["chunk"] + "\n\n"

    return context


# Generate answer using Ollama
def generate_answer(query, context):

    prompt = f"""
Answer the question using only the context given below.

If the answer is not present in the context, say:

"I could not find the answer in the PDF."

Context:
{context}

Question:
{query}

Answer:
"""

    response = ollama.chat(
        model="llama3.2:3b", messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]
