#Name : app.py 
#Author: Nigina Rashidova
#Description: Main application script
#Date started: 05/06/2026

#__Imports__ 
import data_processor
import streamlit as st

st.set_page_config(page_title="Just SAT", layout="wide")

#____Navigation____
pg = st.navigation(
    [
        #pages at the sidebar
        st.Page("pages/home.py", title="Home", icon=":material/home:", default=True), #home page
        st.Page("pages/section1.py", title="Student Profile", icon=":material/person_search:"), #student profile page
        st.Page("pages/section2.py", title="About Us", icon=":material/school:") #about us page
    ]
)

pg.run()


