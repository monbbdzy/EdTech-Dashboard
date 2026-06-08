#Name : data_processor.py
#Author: Nigina Rashidova
#Description: Script for processing student data
#Date started: 04/06/2026

#__Imports__
import pandas as pd
import numpy as np
from fpdf import FPDF
import matplotlib
matplotlib.use('Agg')  # prevents GUI conflicts with Streamlit
import matplotlib.pyplot as plt
import io


#__Loading the CSV file_
def load_file(file):
    studentData = pd.read_csv(file) 
    return studentData

#__Calculating the Average Grade of the student___ 
def average_grade(studentData):
    df_grades = studentData["Grade"].str.split(',', expand=True).astype(float) #split the grades into seperate columns
    studentData["AverageGrade"] = df_grades.mean(axis=1).round(1) #add a new column = Average Grade 
    return studentData

#__Transforming strings into list of floats in the grade column___
def process_grade_column(studentData):
    # clean and convert the string to a list of float:
    def string_to_float_list(val):
        if isinstance(val, list):
            return val
        if pd.isna(val) or val == "":
            return []
        
        # split string by comma, strip whitespace, convert to float
        return [float(g.strip()) for g in str(val).split(",")]

    # apply to the 'Grade' column
    studentData["Grade"] = studentData["Grade"].apply(string_to_float_list)
    return studentData

#__Calculating the Status of the student___
def status(studentData):
    studentData["Status"] = np.where( #At risk = if student has 5 or more skipped deadlines OR if student's grade is less than 7
    (studentData["Missed_deadlines"] >= 5) | (studentData["AverageGrade"] < 7), "🔴 At Risk", "🟢 On track")
    sorted_data = studentData.sort_values(by="Status", ascending=False) #sorting students based on the risk 
    return sorted_data

#__Calculating the Progress of the student__
def progress(studentData):
    #creating a condition for students who study both English and Math
    is_english_and_math = ((studentData["Course"].str.contains("English", case=False)) & 
                        (studentData["Course"].str.contains("Math", case=False)))

    #calculating the progress of students based on their course
    studentData["Progress"] = np.where(
        is_english_and_math, 
        ((studentData["Progress"].astype(int) / 22)*100).round(1), ((studentData["Progress"].astype(int) / 11)*100).round(1)
    )
    return studentData

#___Identifying the top student___ 
def top_student(studentData):
    # filter students by average grade, skipped deadlines and progress to choose the top performing student
    student= studentData.sort_values(by=["AverageGrade", "Missed_deadlines", 
    "Progress"],ascending=[False, True, False]).iloc[0] # pick the first one
    grades = student["Grade"] #all the grades of the top student
    name = student["Name"] 
    avg_grade = student["AverageGrade"]
# return the name, average grade, and list of grades of TOP student
    return name, avg_grade, grades

#___Calculating total average grade of students____
def total_grade(studentData):
    #check if the DataFrame is empty
    if studentData.empty:
        return 0.0 
    
    if "AverageGrade" not in studentData.columns:
        return 0.0 
    
    #calculate average grade = mean
    avg_grade = studentData["AverageGrade"].mean().round(1)
    
    return avg_grade

#___Calculating the number of students at risk___ 
def risk_students(studentData):
    #check if the DataFrame is empty
    if studentData.empty:
        return 0
    
    if "Status" not in studentData.columns: #status column not found
        return 0 
    count = len(studentData[studentData["Status"] == "🔴 At Risk"])
    grades = studentData[studentData["Status"] =="🔴 At Risk"]["AverageGrade"]
    #return the count of students at risk and the average grades of students at risk
    return count, grades

#___Generating pdf file of the student___
#line chart image creation
def generate_line_chart_image(grades):
    fig, ax = plt.subplots()
    ax.plot(grades, marker="o", color="#1f77b4") #create a plot chart
    ax.set_title("Grades Over Time") #title of the chart
    ax.set_ylabel("Grade") #labels for y and x
    ax.set_xlabel("Unit Number")
    buf = io.BytesIO()
    plt.savefig(buf, format="png") #save the image in png format
    plt.close()
    buf.seek(0)
    return buf

#Donut chart image creation
def generate_donut_chart_image(progress):
    fig, ax = plt.subplots()
    ax.pie(  #create a pie chart
        [progress, 100 - progress], #values = progress of student and whats left 
        labels=[str(progress) + "% Course Completed", str(100 - progress) + "%Course Not Completed"],
        colors=["#1f77b4", "#d3d3d3"],
        wedgeprops=dict(width=0.5) #create a hole to make it a donut chart
    )
    ax.set_title=("Student's course completion")
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    return buf

#Generate the pdf
def generate_pdf(month3_student, month1_student):
    pdf = FPDF() #ust fpdf to generate pdf file
    pdf.add_page()
    
    #setting up the fonts
    pdf.add_font("DejaVu", "", "DejaVuSans.ttf")
    pdf.add_font("DejaVu", "B", "DejaVuSans-Bold.ttf")
    pdf.set_font("DejaVu", "B", 24)
    pdf.cell(0, 10, month3_student["Name"], ln=True)
    
    #title and description
    pdf.set_font("DejaVu", size=14)
    pdf.cell(0, 10, f"Course: {month3_student['Course']}", ln=True)
    pdf.cell(0, 10, f"Status: {month3_student['Status']}", ln=True)
    pdf.cell(0, 10, f"Average Grade: {month3_student['AverageGrade']}", ln=True)
    pdf.cell(0, 10, f"Missed Deadlines: {month3_student['Missed_deadlines']}", ln=True)
    
    #grade growth from 1st month
    growth = round((month3_student["AverageGrade"] / month1_student["AverageGrade"] - 1) * 100, 1)
    pdf.cell(0, 10, f"Grade Growth since 1st Month: {growth}%", ln=True)
    
    # generate and add charts
    line_buf = generate_line_chart_image(month3_student["Grade"])
    donut_buf = generate_donut_chart_image(month3_student["Progress"])
    #add images
    pdf.image(line_buf, x=5, w=100)
    pdf.image(donut_buf, x=5, w=100)
    
    return pdf.output()

