import streamlit as st

if st.checkbox("Show/Hide"):
    st.text("Showing the widget")
    print("Masuk")
else:
    print("Keluar")