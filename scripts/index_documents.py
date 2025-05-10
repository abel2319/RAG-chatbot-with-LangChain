from app.ingestion import load_and_split_docs
from app.embedding import create_vectorstore
import pickle

def index_documents():
    docs = load_and_split_docs("data")
    vs = create_vectorstore(docs)
    return vs
