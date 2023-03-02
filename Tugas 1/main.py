import pandas as pd
import numpy as np
import streamlit as st

st.title("First Assignment - Line Chart Using Manual Data Frame")

st.header("Table")
# df = pd.DataFrame({"Col 1": [2, 5, 8, 9], "Col 2": [1, 4, 9, 2]})
df = pd.DataFrame(np.random.randn(20, 3))
st.write(df)

st.header("Line Chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(chart_data)
