import streamlit as st
import requests

st.title("Lambda Runner 🐳⚙️")

code = st.text_area("Enter your Python code below:")

if st.button("Run"):
    if code.strip():
        with st.spinner("Running your code..."):
            response = requests.post("http://localhost:8000/run", json={"code": code})
            if response.ok:
                st.success("Output:")
                st.code(response.json().get("output"))
            else:
                st.error("Something went wrong.")
    else:
        st.warning("Please enter some code to run.")

