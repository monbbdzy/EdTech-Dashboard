#Name : app.py
#Author: Nigina Rashidova
#Description: Script for displaying the data
#Date started: 05/06/2026

#__Imports__ 
import data_processor
import streamlit as st

st.set_page_config(page_title="Just SAT", layout="wide")


#____Uploading student data____
student_data = data_processor.load_file("students.csv")
student_data = data_processor.average_grade(student_data)
student_data = data_processor.progress(student_data)
student_data = data_processor.status(student_data)


#____Title and description____
st.image("logo.png", width=78) # Adjust width to your preference
st.title("Just SAT - prepare for SAT the *right* way!")
st.caption("Leading online SAT school in Uzbekistan.")
st.divider()

#____Home page____
st.header("Student Dashboard")
st.caption("Monitor and review student progress across different courses.")

# Key performance indicators
row = st.container(horizontal=True) #Create a row container
with row:
    #Top student
    #Get the name, average grade and all grades of top student
    student_name, student_grade, grades = data_processor.top_student(student_data)
    st.metric(
        label="Top Student", 
        value=student_name, 
        delta_description=" average grade",
        delta=student_grade, 
        delta_arrow ="off",
        chart_data=grades,
        chart_type = "bar",
        border=True
    )
    #Average grade across all courses
    at_risk_count, at_risk_grades = data_processor.risk_students(student_data) #number of students at risk
    on_track_percent = str(((len(student_data) - at_risk_count) / len(student_data))*100) + "%"
    st.metric(
        label="Average Grade of students", 
        value=data_processor.total_grade(student_data), 
        delta=on_track_percent,
        delta_description="Students on Track", 
        delta_arrow="off",
        chart_data=student_data["AverageGrade"], 
        chart_type="area", border=True
    )
    #Number of students at risk
    at_risk_percent = str((at_risk_count / len(student_data))*100) + "%"
    st.metric(
        label="Students at Risk", 
        value=at_risk_count, 
        delta=at_risk_percent,
        delta_description="Students at Risk",
        delta_color = "inverse", 
        delta_arrow="off",
        chart_data= at_risk_grades,
        chart_type = "bar",
        border=True, height=214
    )

#Overview of student data
st.header("Overview of students")
st.caption("Filtered by the status of the student.")

# Adding more information about each column
st.dataframe(student_data, column_config={
        "Grade": None,       # Hiding the column -> average grade is only displayed
        "Name" : st.column_config.TextColumn(
           "Name",
           help="Student's full name",
        ),
        "Course" : st.column_config.TextColumn(
           "Course",
           help="The course student is enrolled in",
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


    