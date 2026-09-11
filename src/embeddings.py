from sentence_transformers import SentenceTransformer
from src.loader import chunks


model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):
    embeddings = model.encode(chunks)

    return embeddings


embeddings = create_embeddings(chunks)

print("Total chunks:", len(chunks))
print("Total embeddings:", len(embeddings))
print("Vector size:", len(embeddings[0]))
# Test
"""texts = [
    "What is Machine Learning?",
    "Machine Learning is a part of Artificial Intelligence."
]

embeddings = create_embeddings(texts)

print("Number of texts:", len(embeddings))
print("Vector size:", len(embeddings[0]))"""

