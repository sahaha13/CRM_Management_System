import streamlit as st
from participant import participant
from teacher import teacher_page
from volunteer import volunteer
from course import course
from advance import advance

import mariadb

conn =  mariadb.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="workshop_management"
) 

cursor = conn.cursor()




def main():
    st.sidebar.image("aolf_logo_1.png")
   
    st.title("Art Of Living CRM")

    table_menu = ["Participant Information", "Teacher Information", "Volunteer Information", "Course Information", "Advanced Program eligibility information"]
    table_choice = st.sidebar.selectbox("Table", table_menu)

    match table_choice:
        case "Participant Information":
            participant(conn, cursor)
    
        case "Teacher Information":
            teacher_page(conn, cursor)
    
        case "Volunteer Information":
            volunteer(conn, cursor)
    
        case "Course Information":
            course(conn, cursor)
    
        case "Advanced Program eligibility information":
            advance(conn, cursor)
        
       

    conn.close()
  
if __name__ == '__main__':
    main()