 🤖 PDF RAG Assistant

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
🛠️ Tech Stack
Python
Streamlit
PyPDF
Sentence Transformers
FAISS
NumPy
Ollama
Llama 3.2
📂 Project Structure
pdf-rag-assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── data/
│   └── sample.pdf
│
├── src/
│   ├── __init__.py
│   ├── loader.py
│   ├── cleaner.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── rag_pipeline.py
│
└── vectorstore/
    └── index.faiss
⚙️ How It Works
1. PDF Loading

The application extracts text from the PDF using pypdf.

2. Text Cleaning

Unnecessary spaces and formatting are cleaned before processing.

3. Chunking

The document is divided into meaningful question-answer chunks.

4. Embeddings

Each chunk is converted into a numerical vector using:

all-MiniLM-L6-v2

The generated embeddings have a dimension of:

384
5. Vector Search

FAISS is used to search for the most relevant document chunks based on semantic similarity.

6. Context Retrieval

The most relevant chunks are selected and provided as context to the language model.

7. Answer Generation

Llama 3.2 generates the final answer using the retrieved PDF context.

💻 Installation

Clone the repository:

git clone https://github.com/Mukesh3597/pdf-rag-assistant.git

Move into the project directory:

cd pdf-rag-assistant

Install dependencies:

pip install -r requirements.txt

Make sure Ollama is installed and the required model is available:

ollama pull llama3.2:3b
▶️ Run the Application

Start the Streamlit application:

streamlit run app.py

The application will open in your browser.

🧪 Example Questions

You can ask questions such as:

What is Machine Learning?

What is Artificial Intelligence?

What is overfitting?

What is supervised learning?

The system retrieves relevant information from the PDF before generating the answer.

🎯 Why RAG?

Instead of relying only on the language model's existing knowledge, this project retrieves relevant information from the provided document and uses it as context.

This helps the application provide answers grounded in the selected PDF.

🔮 Future Improvements
Multiple PDF support
PDF upload directly from the UI
Source citations for every answer
Chat history
Improved retrieval with reranking
Metadata-based document filtering
Automated evaluation of retrieval quality
Deployment as a web application
👨‍💻 Author

Mukesh

GitHub:
https://github.com/Mukesh3597
