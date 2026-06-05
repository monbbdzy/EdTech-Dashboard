#Name : data_processor.py
#Author: Nigina Rashidova
#Description: Script for processing student data
#Date started: 04/06/2026

import pandas as pd
import numpy as np

#Loading the CSV file
studentData = pd.read_csv("students.csv") 

#Calculating the Average Grade of the student 
df_grades = studentData["Grade"].str.split(',', expand=True).astype(float) #Split the grades into seperate columns
studentData["AverageGrade"] = df_grades.mean(axis=1).round(1) #Add a new column Average Grade 

#Calculating the Status of the student
studentData["Status"] = np.where( #At risk = if student has 3 or more skipped deadlines OR if student's grade is less than 7
    (studentData["Missed_deadlines"] >= 3) | (studentData["AverageGrade"] < 7), "At Risk", "On track")

#Calculating the Progress of the student
#Creating a condition for students who study both English and Math
is_english_and_math = ((studentData["Course"].str.contains("English", case=False)) & 
                      (studentData["Course"].str.contains("Math", case=False)))

#Calculating the progress of students based on their course
studentData["Progress"] = np.where(
    is_english_and_math, 
    ((studentData["Progress"].astype(int) / 8)*100).round(1), ((studentData["Progress"].astype(int) / 4)*100).round(1)
)



