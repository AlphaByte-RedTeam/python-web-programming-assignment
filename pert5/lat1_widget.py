import streamlit as st
import numpy as np
import pandas as pd

st.subheader("4-Widgets:")

st.write("4A: Slider")
x = st.slider("x")  # 👈 this is a widget
st.write(x, "squared is", x * x)


st.write("4B: Text input")
st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name


st.write("4C: Checkbox")
if st.checkbox("Show dataframe"):
    chart_data = pd.DataFrame(np.random.randn(5, 2), columns=["a", "b"])

    chart_data


st.write("4D: Selectbox")
df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})

option = st.selectbox("Which number do you like best?", df["first column"])

"You selected: ", option
