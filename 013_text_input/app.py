from numpy import result_type
import streamlit as st

name = st.text_input("Enter your name", "Type here...")

if st.button('Submit'):
    result = name.title()
    st.success(result)