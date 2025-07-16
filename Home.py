import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images\\pp.jpg")

with col2:
    st.title("Yiğit Ali Çiftçi")
    content = """
    Hi, I'm Yiğit, a computer engineering student based in Turkey. 
    I'm passionate about Python development and data science, with a current focus on software development and machine learning.
    I'm actively working on personal projects involving data analysis and building web applications using Python. 
    My goal is to become a skilled data scientist and make meaningful contributions to real-world problems through data-driven solutions.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""

st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[::2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images\\" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[1::2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images\\" + row["image"])
        st.write(f"[Source Code]({row['url']})")