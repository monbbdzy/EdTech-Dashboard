#Name : app.py 
#Author: Nigina Rashidova
#Description: Script for displaying the data
#Date started: 05/06/2026

#__Imports__ 
import data_processor
import streamlit as st

st.set_page_config(page_title="Just SAT", layout="wide")

#____Navigation____
pg = st.navigation(
    [
        st.Page("pages/home.py", title="Home", icon=":material/home:", default=True),
        st.Page("pages/section1.py", title="Student Profile", icon=":material/person_search:"),
        st.Page("pages/section2.py", title="About Us", icon=":material/school:")
    ]
)

pg.run()


