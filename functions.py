import streamlit as st
import pandas as pd

def view_all_participants(cursor):
    cursor.execute('SELECT * FROM participant_info')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['name', 'email', 'Registration_ID', 'Amount', 'source', 'Registration_type', 'District', 'Phone', 'Course_ID'])
    return df

def view_all_teachers(cursor):
    cursor.execute('SELECT * FROM teacher_info')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['teacher_ID', 'teacher_name', 'Email', 'Phone', 'no_of_courses'])
    return df
    

def view_all_volunteers(cursor):
    cursor.execute('SELECT * FROM volunteer_info')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Volunteer_ID', 'Name', 'Email_ID', 'Phone', 'Courses_assisted'])
    return df

def view_all_courses(cursor):
    cursor.execute('SELECT * FROM course_details')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Course_ID', 'Course_Name', 'No_of_pax', 'Venue', 'Teacher_ID', 'Volunteer_ID', 'Course_Start_Date', 'Course_End_Date'])
    return df

def view_all_advance(cursor):
    cursor.execute('SELECT * FROM advance_program_details')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["Registration ID", "Name", "Email", "Phone", "Number of courses", "Course_ID"])
    return df