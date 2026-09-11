# 🤖 PDF RAG Assistant

A document-based Question Answering system built using **Retrieval-Augmented Generation (RAG)**.

The application allows users to ask questions about information contained in a PDF and generates answers using relevant retrieved content from the document.

## 🚀 Features

- 📄 PDF text extraction
- 🧹 Text cleaning and preprocessing
- ✂️ Structure-aware document chunking
- 🧠 Semantic embeddings using Sentence Transformers
- 🔎 Similarity search using FAISS
- 🤖 Local LLM using Ollama and Llama 3.2
- 💬 Interactive Streamlit chat interface
- 🎯 Context-based answer generation
- 🔒 Local AI processing without requiring an external LLM API

## 🏗️ Architecture

```text
PDF Document
     ↓
Text Extraction
     ↓
Text Cleaning
     ↓
Document Chunking
     ↓
Sentence Transformer
     ↓
384-D Embeddings
     ↓
FAISS Vector Index
     ↓
User Question
     ↓
Query Embedding
     ↓
Similarity Search
     ↓
Relevant Context
     ↓
Llama 3.2
     ↓
Generated Answer
     ↓
Streamlit UI
