from typing_extensions import assert_type
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import altair as alt
import graphviz as graphviz

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

df= pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y'])

st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

df= pd.DataFrame(
    np.random.randn(500, 3),
    columns=['x', 'y', 'z'])
c = alt.Chart(df).mark_circle().encode(
    x='x' , y='y' , size='z', color='z', tooltip=['x', 'y', 'z'])
st.altair_chart(c, use_container_width=True)

st.graphviz_chart('''
    digraph {
        Big_shark -> Tuna
        Tuna -> Mackerel
        Mackerel -> Small_fishes
        Small_fishes -> Shrimp
    }
''')