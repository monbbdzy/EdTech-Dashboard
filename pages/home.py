#Name : app.py 
#Author: Nigina Rashidova
#Description: Script for displaying the data
#Date started: 05/06/2026

#__Imports__ 
import data_processor
import streamlit as st
# from streamlit_echarts import st_echarts

st.set_page_config(page_title="Just SAT", layout="wide")

#____Filters____
st.sidebar.header("Filters")
st.sidebar.slider("Month", 1, 2, 3, key="month")
st.sidebar.selectbox("Course", ["All", "English", "Math", "English & Math"], key="course")

#___Filter configurations____
month_filter = st.session_state.get('month', 1) #Get the month selected by the user 
course_filter = st.session_state.get("course", "All") #Get the course selected by the user


#____Uploading student data____
student_data = data_processor.load_file("month" + str(month_filter) + ".csv") 
student_data = data_processor.average_grade(student_data)
student_data = data_processor.process_grade_column(student_data)
student_data = data_processor.progress(student_data)
student_data = data_processor.status(student_data)

#____Apply the course filter____
if course_filter != "All":
    student_data = student_data[student_data["Course"] == course_filter]

#____Title and description____
st.title(":four_leaf_clover:Just SAT - prepare for SAT the *right* way!")
st.caption("Leading online SAT school in Uzbekistan.")
st.divider()


#____Home page____
st.header("Student Dashboard")
st.caption("Monitor and review student progress across different courses.")

#____Key performance indicators____
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
        chart_type = "line",
        border=True
    )
    #Average grade across all courses
    at_risk_count, at_risk_grades = data_processor.risk_students(student_data) #number of students at risk
    on_track_percent = str(round((((len(student_data) - at_risk_count) / len(student_data))*100),2)) + "%"
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
    at_risk_percent = str(round((at_risk_count / len(student_data))*100, 2)) + "%"
    st.metric(
        label="Students at Risk", 
        value=at_risk_count, 
        delta=at_risk_percent,
        delta_description="Students at Risk",
        delta_color = "inverse", 
        delta_arrow="off",
        chart_data= at_risk_grades,
        chart_type = "line",
        border=True, height=214
    )

#____Overview of student data____
st.header("Overview of students")
st.caption("Filtered by the status of the student.")

# Adding more information about each column
st.dataframe(student_data, column_config={
        "Grade": None,       # Hiding rades -> average grade is only displayed
        "Name" : st.column_config.TextColumn(
           "Name",
           help="Student's full name",
        ),
        "Course" : st.column_config.TextColumn(
           "Course",
           help="The course student is enrolled in",
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

# #____Pie chart for course popularity analysis____
# options = {
#     "tooltip": {"trigger": "item"},
#     "legend": {"top": "5%", "left": "center"},
#     "series": [
#         {
#             "name": "Access From",
#             "type": "pie",
#             "radius": ["40%", "70%"],
#             "avoidLabelOverlap": False,
#             "itemStyle": {
#                 "borderRadius": 10,
#                 "borderColor": "#fff",
#                 "borderWidth": 2,
#             },
#             "label": {"show": False, "position": "center"},
#             "emphasis": {
#                 "label": {"show": True, "fontSize": 40, "fontWeight": "bold"}
#             },
#             "labelLine": {"show": False},
#             "data": [
#                 {"value": 1048, "name": "Search Engine"},
#                 {"value": 735, "name": "Direct"},
#                 {"value": 580, "name": "Email"},
#                 {"value": 484, "name": "Union Ads"},
#                 {"value": 300, "name": "Video Ads"},
#             ],
#         }
#     ],
# }
# st_echarts(options=options, height="500px")

    