from langchain_community import embeddings 
from langchain_chroma import Chroma 
import os

def test(documents):
    print("Number of documents:", len(documents))
    print("Sample document:", documents[0].page_content)

    # Test embedding
    embedding = embeddings.OllamaEmbeddings(model="mxbai-embed-large")
    sample_embedding = embedding.embed_query(documents[0].page_content)
    print("Embedding length:", len(sample_embedding))

def create_vectorstore(documents):
    embedding = embeddings.OllamaEmbeddings(model="mxbai-embed-large")
    vectorstore = Chroma(
        collection_name='rag_chroma',
        embedding_function=embedding,
        persist_directory=os.path.join("store/", 'rag_chroma')
    )

    vectorstore.add_documents(documents)
    #vectorstore.persist()

    return vectorstore