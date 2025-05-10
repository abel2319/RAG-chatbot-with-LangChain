import streamlit as st
st.set_page_config(page_title="🧠 RAG ML Engineer Chatbot")


from interfaces.streamlit_app import show_ui
import os
from scripts.index_documents import index_documents

def run():
    ready = True
    if ready:
        #if not os.path.isdir("store/rag_chroma"):
        st.warning("Indexing documents, please wait...")
        vector = index_documents()
        st.success("Documents indexed successfully!")
        
        show_ui(vector)
    else:
        st.stop()

run()