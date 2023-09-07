import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col2:
    st.title("Saheed Akinyemi")
    content = """
    Hi, I'm Saheed! I am a Python Programmer, Network Engineer and a Cyber Security Enthusiast. I graduated in 2018 
    and I currently work with NetIT solutions as a Network Engineer. Welcome to my portfolio website.
    """
    st.info(content)