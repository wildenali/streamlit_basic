import streamlit as st
from PIL import Image

img = Image.open("../sinchan.jpg")
st.image(img, width=200)
st.image(img, width=500)
st.image(img, width=1000)