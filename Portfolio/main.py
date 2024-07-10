import streamlit as st

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
