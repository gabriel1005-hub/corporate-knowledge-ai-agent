# 🧠 NovaCore Knowledge AI

> Enterprise Knowledge Assistant powered by Local AI (Ollama + ChromaDB)

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.46-red)
![LangChain](https://img.shields.io/badge/LangChain-1.x-green)
![Ollama](https://img.shields.io/badge/Ollama-Local-black)
![License](https://img.shields.io/badge/License-MIT-purple)

---

## 📖 Overview

NovaCore Knowledge AI is a Retrieval-Augmented Generation (RAG) application designed to answer questions using internal corporate documentation.

Instead of relying on external knowledge, the assistant searches a private knowledge base stored in ChromaDB and generates grounded answers using a local Large Language Model running on Ollama.

The project demonstrates how to build a private enterprise AI assistant without depending on cloud-hosted LLMs.

---

## ✨ Features

- 📄 PDF document ingestion
- 📚 Automatic document chunking
- 🧠 Local embeddings with Ollama
- 🔎 Semantic search using ChromaDB
- 🤖 Local LLM inference (Qwen)
- 💬 Chat interface with Streamlit
- 📊 Dynamic system metrics
- 📚 Source attribution
- 🔒 100% Local AI (No OpenAI API required)

---

# 🏗 Architecture
Corporate Documents
│
▼
PDF Loader
│
▼
Document Processor
│
▼
Chunking
│
▼
Embeddings (nomic-embed-text)
│
▼
ChromaDB
│
▼
Retriever
│
▼
Qwen 2.5 (Ollama)
│
▼
Streamlit UI

---

# 📂 Project Structure
corporate-knowledge-ai/
│
├── app/
│ ├── config/
│ ├── loaders/
│ ├── models/
│ ├── processors/
│ ├── rag/
│ ├── services/
│ ├── ui/
│ └── vectorstore/
│
├── data/
│ ├── raw/
│ └── vector_db/
│
├── docs/
├── tests/
│
├── streamlit_app.py
├── main.py
├── requirements.txt
└── README.md

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/gabriel1005-hub/corporate-knowledge-ai-agent.git

Enter the project

cd corporate-knowledge-ai-agent

Create virtual environment

python -m venv .venv

Activate

Windows

.venv\Scripts\activate

Linux / Mac

source .venv/bin/activate

Install dependencies

pip install -r requirements.txt

🦙 Install Ollama

Download Ollama

https://ollama.com/download

Install the models

ollama pull nomic-embed-text
ollama pull qwen2.5:3b

🚀 Run

Index documents

python main.py

Launch Streamlit

streamlit run streamlit_app.py

🧠 Tech Stack
Python 3.12
Streamlit
LangChain
Ollama
ChromaDB
PyPDF
Pandas

📸 Screenshots

🔒 Privacy

This application runs completely locally.

No corporate documentation is sent to third-party LLM providers.

🚀 Future Improvements
Docker deployment
Oracle Cloud deployment
User authentication
Conversation memory
Document upload from UI
Multi-user support

👩‍💻 Author

Gabriel Garcia

Data Analyst | AI & Analytics

GitHub:

https://github.com/gabriel1005-hub

📄 License

No License