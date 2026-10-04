import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='meta-llama/Llama-3.1-8B-Instruct',task='text-generation'
)

model = ChatHuggingFace(
    llm=llm
)

st.header("NIGGA'S DEN")

user_input = st.text_input("Write your prompt: ")

if st.button('Summarize'):
    res = model.invoke(user_input)
    st.write(res.content)

