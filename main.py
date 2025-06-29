import streamlit as st

st.title("Project 1")

# Show text
st.header("This is a header")
st.subheader("This is a subheader")
st.text("Normal text")
st.caption("This is AI Viet Nam")

# Phân tách 
st.divider()

# Markdown (có thêm định dạng )
st.markdown("# Heading 1")
st.markdown("## Heading 2")
st.markdown("[AI VN] (https://www.ai.vn)")
st.markdown("""
1. machine learning
2. deep learning
""")
st.markdown(r"$\sqrt{2x+2}$")
st.latex(r"\sqrt{2x+2}")

# Code
st.code(
"""
import numpy as np 
arr = np.array([1, 2, 3, 4, 5])
"""
, language="python")

st.divider()

st.write("Hello World")
st.write("## Heading 2")
st.write(r"$\sqrt{2x+2}$")

print("hello print") # in ra trong terminal, không in trên web