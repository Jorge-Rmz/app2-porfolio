import streamlit as st
import pandas
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("My name is Jorge Alberto")
    content = """ I am a computer systems engineer,
        I know how to code in different programming languages, among them are
        PHP, Java, Python, and C#. I like learning more about the different
        programming languages.
    """
    st.info(content)


st.write("Below you can find some of the apps. I have built in Python. Feel free to contact me! ")

col3, empty_colum, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.info(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code:]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.info(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")


