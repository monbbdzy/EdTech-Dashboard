#Name : section1.py 
#Author: Nigina Rashidova
#Description: Student Profile page
#Date started: 07/06/2026

#__Imports__ 
import data_processor
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from fpdf import FPDF
import io

st.set_page_config(page_title="Student Profile", layout="wide")

#____Uploading student data____
#_Month 3_
student_data = data_processor.load_file("month3.csv")
student_data = data_processor.average_grade(student_data)
student_data = data_processor.process_grade_column(student_data)
student_data = data_processor.progress(student_data)
student_data = data_processor.status(student_data)

#_Month 1_ (for further progress analysis)
month1 = data_processor.load_file("month1.csv")
month1 = data_processor.average_grade(month1)

#____Title and descriptions____
st.title("👩‍🎓Student Details")
st.caption("View and monitor student's progress and performance.")
st.divider()

#____Search for the needed student____
st.header("Search for the student's profile")
search_input = st.text_input("Search the student you need:", placeholder="🔎 Full name of student")

#____Student Profile Details____
if search_input: #if there is input in the search bar
    filtered_data = student_data[student_data['Name'].str.contains(search_input, case=False)] #find student data
    filtered_data_month1 = month1[month1['Name'].str.contains(search_input, case=False)]#find student data from month1
    
    if not filtered_data.empty:   
        # get the student row only
        student = filtered_data.iloc[0]
        student_month1 = filtered_data_month1.iloc[0]
        
        # display student profile
        st.title(student["Name"]) 
        col1, col2 = st.columns([0.7, 0.3]) #create two columns 
        with col1: #Key info of student
            st.markdown(f"**📑 Course:** {student['Course']}") #use markdown for prettier design
            st.markdown(f"**📊 Grades for unit tests:** {", ".join(map(str, student['Grade']))}")
            st.markdown(f"**❕ Status:** {student['Status']}")
            st.markdown(f"**⏰ Skipped Deadlines:** {student['Missed_deadlines']}")
        with col2: #highlight student's average grade and growht
            #Calculate the grade growth percentage month1 ->month3
            growth = (student["AverageGrade"]/student_month1["AverageGrade"]-1)
            
            st.metric(
                label="Student's Grade:", 
                value=student["AverageGrade"]/10,  #format=percent was affecting this value, thats why i divided it by 10
                delta_description=" Progress from first month",
                delta=growth, 
                format="percent",
                border=True
            )

        #Student details visualised
        col1, col2 = st.columns(2) #create two columns 
        with col1:#Display student's progress = grades
            st.header("Student's progress over months")
            st.divider()
            fig = px.line(y=student["Grade"], #use line graph for grades
                          labels={"y": "Grades",  "x": "Unit number" })
            st.plotly_chart(fig)  # display in app
            
        
        with col2:#Display student's course completion
            st.header(" Student's course completion")
            # Build the donut chart
            fig = go.Figure(data=[go.Pie(
                labels=['Course completed', 'Not completed'], 
                values=[student["Progress"], 100-student["Progress"]], 
                hole=.3,
                marker=dict(colors=['#1f77b4', '#d3d3d3'])
            )])
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
            

        #Download button
        @st.fragment #using fragment to prevent the user from reclicking the button
        def download_pdf():
            pdf_bytes = bytes(data_processor.generate_pdf(student, student_month1))
            st.download_button(
                label="Download PDF Report",
                data=pdf_bytes,
                file_name=student["Name"] + ".pdf",
                mime="application/pdf",
                icon=":material/download:",
            )

        download_pdf()
    
    else: #student not found
        st.warning("No student found with that name.")
    



