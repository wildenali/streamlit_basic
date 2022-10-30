import streamlit as st

# # Hidden hamburger and footer
# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

hobby = st.selectbox("Hobbies: ",
                    ['Dancing', 'Reading', ' Sports']
                    )

st.write("Your hobby is: ", hobby)