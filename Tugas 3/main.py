import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image

st.set_page_config(
	page_title="Python Web Assignment",
	page_icon="🐍",
	layout="wide",
	initial_sidebar_state="expanded",
	menu_items={
		'Get Help': 'https://www.extremelycoolapp.com/help',
		'Report a bug': "https://www.extremelycoolapp.com/bug",
		'About': "# This is a header. This is an *extremely* cool app!"
	}
)

# 1. Write and Magic
st.title("1. Write and Magic")
st.write("Hello world!")
df = pd.DataFrame({
	'first column': [1, 2, 3, 4],
	'second column': [10, 20, 30, 40],
})
df # streamlit magic

st.write(df)

# 2. Text Element
st.title("2. Text Element")
st.title("Streamlit app example")
st.code("let streamlit = 'Streamlit is awesome!'")

# 3. Data Display Elements
st.title("3. Data Display Elements")
st.json({
	'foo': 'bar',
	'baz': 'boz',
	'stuff': [
		'stuff 1',
		'stuff 2',
		'stuff 3',
		'stuff 5',
	],
})

# 4. Chart Elements
st.title("4. Chart Elements")
chart_data = pd.DataFrame(
	np.random.randn(20, 3),
	columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# 5. Input Widget
st.title("5. Input Widget")
agree = st.checkbox('Checked me if you are an awesome programmer!')

if agree:
	st.write('Great!')

# 6. Media Elements
st.title("6. Media Elements")
img = Image.open("./coolcat.jpg")
st.image(img, caption="cool cat with sunglasses")

# 7. Layouts and Containers
st.title("7. Layouts and Containers")
with st.sidebar:
	with st.echo():
		st.write("This code will be printed to the sidebar.")

	with st.spinner("Loading..."):
		time.sleep(5)
	st.success("Done!")

# 8. Status Element
st.title("8. Status Element")
st.error('[ERROR]: Bug will always haunt you', icon="🪲")

# 9. Control Flow
st.title("9. Control Flow")
with st.form("my_form"):
	st.write("Inside the form")
	slider_val = st.slider("Form slider")
	checkbox_val = st.checkbox("Form checkbox")

	# Every form must have a submit button.
	submitted = st.form_submit_button("Submit")
	if submitted:
		st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

# 10. Utilities
st.title("10. Utilities")
st.help(pd.DataFrame)
