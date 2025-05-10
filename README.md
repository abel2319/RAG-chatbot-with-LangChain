# RAG Chatbot with LangChain + Ollama

This is a Retrieval-Augmented Generation (RAG) chatbot using LangChain and Ollama (llama3.2).

## How to Use

1. Place your medical PDF documents in `data/`.
2. Run `streamlit run main.py` to load, split, embed them and launch the chatbot.

## Features
- Uses `llama3.2` model from Ollama.
- Embeds with `mxbai-embed-large`.
- Vector store backed by Chroma.

---

Let me know if you'd like a Dockerfile or CI/CD pipeline added!