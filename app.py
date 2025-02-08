import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "Please consult doctor for accurate advise"
    elif "appointment" in user_input:
        return "Wouuld you like to scheldule an appointement with the Doctor?"
    elif "medication" in user_input:
        return "It is important to take a precribed medicined regularly. If you have any concerns please consult the Doctor"
    else:
        response = chatbot(user_input, max_length = 500, num_return_sequences = 1)
        return response[0]['generated_text']

def main():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I assist you today?")
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            with st.spinner("Please wait..."):
                response = healthcare_chatbot(user_input)
                st.write("Healtcare Assistant: ", response)
            # print(response)
        else:
            st.write("Please enter to get a message to get a response")

main()