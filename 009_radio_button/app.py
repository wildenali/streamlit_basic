import streamlit as st

status = st.radio("Select Gender: ", ('Male', 'Female'))
if status == 'Male':
    st.success("Male")
else:
    st.success("Female")