from langchain.prompts import PromptTemplate

def get_prompt_template():
    return PromptTemplate(
        input_variables=["context", "question"],
        template="""
        You are a helpful assistant. Use the following context to answer the question. \
        Use the following pieces of retrieved context to answer the question. \
        If you don't know the answer, just say that you don't know, do not invent, or ask the user to \
        reformulate his question. \

        Context:
        {context}

        Question:
        {question}

        Helpful Answer:
        """
    )
