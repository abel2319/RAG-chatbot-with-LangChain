# RAG Chatbot with LangChain + Ollama

This is a Retrieval-Augmented Generation (RAG) chatbot using LangChain and Ollama (llama3.2).

## How to Use

1. Place your medical PDF documents in `data/`.
2. Run `python scripts/index_documents.py` to load, split, and embed them.
3. Launch the chatbot via `interfaces/streamlit_app.py`, `cli.py`, or `api.py`.

## Features
- Uses `llama3.2` model from Ollama.
- Embeds with `mxbai-embed-large`.
- Vector store backed by Chroma.
- Clean interface with Streamlit, CLI, or FastAPI.

---

Let me know if you'd like a Dockerfile or CI/CD pipeline added!