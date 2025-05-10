
from langchain_core.runnables import RunnablePassthrough
from langchain_community.llms import Ollama
from .prompt import get_prompt_template

llm = Ollama(model="llama3.2")


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def create_chatbot(retriever):
    prompt = get_prompt_template()
    rag_chain = (
        RunnablePassthrough.assign(
            context=lambda x: format_docs(retriever.get_relevant_documents(x["question"]))
        )
        | prompt
        | llm
    )
    return rag_chain
