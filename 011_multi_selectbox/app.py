import streamlit as st

hobbies = st.multiselect("Hobbies: ",
                        ['Dancing', 'Reading', 'Sports']
                        )

st.write("You selected", len(hobbies), 'hobbies')