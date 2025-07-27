import streamlit as st
from PIL import Image

# Page setup
st.set_page_config(page_title="TrueFace: Detect the Fake", layout="centered")

# Load and display the correct logo
image = Image.open("SVSTO.png")
st.image(image, width=250)

# Title and slogan
st.markdown("<h1 style='color:#4B2E83; font-family:Arial;'>TrueFace</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:#FF4500; font-family:Arial;'>DETECT THE FAKE. PROTECT THE TRUTH.</h3>", unsafe_allow_html=True)

# Optional introduction text
st.write("Welcome to TrueFace — an interactive cybersecurity awareness tool that helps you detect fake media and stay digitally safe. Start the quiz to test your skills!")
