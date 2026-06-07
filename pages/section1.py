#__Imports__ 
import data_processor
import streamlit as st

st.set_page_config(page_title="Just SAT", layout="wide")


#____Uploading student data____
student_data = data_processor.load_file("students.csv")
student_data = data_processor.average_grade(student_data)
student_data = data_processor.process_grade_column(student_data)
student_data = data_processor.progress(student_data)
student_data = data_processor.status(student_data)

#____English page____
st.title("English")
st.caption("Monitor students' performance across the English course")
st.divider()

#__Grades bar___
st.header("Students of English Module")
st.caption("... and their performance across the units.")

english_grades_df = student_data[student_data["Course"] == "English"]
st.dataframe(english_grades_df, column_config={
    "Course":None, #hiding course column, we alr know its english
    "Name" : st.column_config.TextColumn(
           "Name",
           help="Student's full name",
        ),
        "Grade" : st.column_config.LineChartColumn(
            "Grades",
            help="Student's grades for unit tests"
        ),
        "AverageGrade" : st.column_config.NumberColumn(
           "Average Grade",
           help="Student's average grade across the enrolled course",
        ),
        "Missed_deadlines" : st.column_config.NumberColumn(
           "Missed Deadlines",
           help="The number of deadlines student missed",
        ),
        "Progress": st.column_config.ProgressColumn(
            "Progress",
            help="The student's course completion percentage",
            format="%f%%",
            min_value=0,
            max_value=100,
        ),
        "Status": st.column_config.TextColumn(
            "Status",
            help="Student's current academic standing",
        ),
    },
    hide_index=True)
