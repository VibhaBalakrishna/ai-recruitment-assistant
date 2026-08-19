import streamlit as st
from recruitment_assistent import extract

st.title("AI Recruitment Assistant")
st.write("Describe your experience, skills, or background below:")

user_input = st.text_input("Your input:")

if user_input:
    result = extract(user_input)
    st.subheader("Extracted Information")
    st.json(result)