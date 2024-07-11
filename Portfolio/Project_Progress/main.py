import pandas
import streamlit as st

st.set_page_config(layout = "wide")

col1, col2 = st.columns(2)

with col1:
    st.image("/Users/airelking/Desktop/NewRising/Projects/Portfolio/me.jpeg")

with col2:
    st.title("Airel King")
    content = ("Hi I am Airel King! I am a soon to be upgraded Data Analyst. "
               "Keep your eyes out for more projects. This isnt all we are capable of. "
               "Watch out world! We upgraded from Hello world!!!!!")
    st.write(content)


content2 = """
Below you can find some of the apps I have built in Python. 
Feel free to contact me!"""

st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("/Users/airelking/Desktop/NewRising/Projects/Portfolio/portfolio_list_data.csv", sep = ";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("py_portfolio_images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("py_portfolio_images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")



