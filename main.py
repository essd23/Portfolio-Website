import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col2:
    st.title("Saheed Akinyemi")
    content = """
  Hi, I'm Saheed! I am a Python Programmer, Network Engineer and a Cyber Security Enthusiast. I graduated in 2018
with a Bachelors Degree from Osun State University. I currently work with NetIT solutions as a Network Engineer. 
 Welcome to my portfolio website.
    """
    st.info(content)

content2 = """
    Below you can find some of the apps I hvave built in Python. Feel free to contact me."""

st.write(content2)