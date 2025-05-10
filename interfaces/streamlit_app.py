import streamlit as st
import pickle
from app.chatbot import create_chatbot

def show_ui(vector):
    st.title("🧠 RAG ML Engineer Chatbot")

    #with open("vectorstore.pkl", "rb") as f:
    #    vectorstore = pickle.load(f)
    vectorstore = vector
    
    chatbot = create_chatbot(vectorstore.as_retriever())

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "Hello, I am Kabel your assistant, How can I help you?"}]

    with st.sidebar:
        if st.button("Clear chat history"):
            st.session_state["messages"] = [{"role": "assistant", "content": "Hello, I am Kabel your assistant, How can I help you?"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Your message"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = chatbot.invoke({"question": prompt})
                st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})