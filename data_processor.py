#Name : data_processor.py
#Author: Nigina Rashidova
#Description: Script for processing student data
#Date started: 04/06/2026

import pandas as pd
import numpy as np

#Loading the CSV file
def load_file(file):
    studentData = pd.read_csv(file) 
    return studentData

#Calculating the Average Grade of the student 
def average_grade(studentData):
    df_grades = studentData["Grade"].str.split(',', expand=True).astype(float) #Split the grades into seperate columns
    studentData["AverageGrade"] = df_grades.mean(axis=1).round(1) #Add a new column Average Grade 
    return studentData

#Transforming strings into list of floats
def process_grade_column(studentData):
    # clean and convert the string to a list of float:
    def string_to_float_list(val):
        if isinstance(val, list):
            return val
        if pd.isna(val) or val == "":
            return []
        
        # Split string by comma, strip whitespace, convert to int
        return [float(g.strip()) for g in str(val).split(",")]

    # Apply the conversion to the 'Grade' column
    studentData["Grade"] = studentData["Grade"].apply(string_to_float_list)
    return studentData

#Calculating the Status of the student
def status(studentData):
    studentData["Status"] = np.where( #At risk = if student has 3 or more skipped deadlines OR if student's grade is less than 7
    (studentData["Missed_deadlines"] >= 5) | (studentData["AverageGrade"] < 7), "🔴 At Risk", "🟢 On track")
    sorted_data = studentData.sort_values(by="Status", ascending=False) #Sorting students based on the risk 
    return sorted_data

#Calculating the Progress of the student
def progress(studentData):
    #Creating a condition for students who study both English and Math
    is_english_and_math = ((studentData["Course"].str.contains("English", case=False)) & 
                        (studentData["Course"].str.contains("Math", case=False)))

    #Calculating the progress of students based on their course
    studentData["Progress"] = np.where(
        is_english_and_math, 
        ((studentData["Progress"].astype(int) / 22)*100).round(1), ((studentData["Progress"].astype(int) / 11)*100).round(1)
    )
    return studentData

#Identifying the top student 
def top_student(studentData):
    # Filter students by average grade, skipped deadlines and progress to choose the top performing student
    student= studentData.sort_values(by=["AverageGrade", "Missed_deadlines", 
    "Progress"],ascending=[False, True, False]).iloc[0] # Pick the first one
    grades = student["Grade"] #All the grades of the top student
    name = student["Name"] 
    avg_grade = student["AverageGrade"]

    return name, avg_grade, grades

#Calculating total average grade of students
def total_grade(studentData):
    #check if the DataFrame is empty
    if studentData.empty:
        return 0.0 
    
    if "AverageGrade" not in studentData.columns:
        return 0.0 
    
    #Calculate average grade
    avg_grade = studentData["AverageGrade"].mean().round(1)
    
    return avg_grade

#Calculating the number of students at risk 
def risk_students(studentData):
    #check if the DataFrame is empty
    if studentData.empty:
        return 0
    
    if "Status" not in studentData.columns:
        return 0 
    count = len(studentData[studentData["Status"] == "🔴 At Risk"])
    grades = studentData[studentData["Status"] =="🔴 At Risk"]["AverageGrade"]
    
    return count, grades

