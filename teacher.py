import streamlit as st
import pandas as pd 
import functions

def teacher_page(conn, cursor):
    user_menu = ["Add teacher", "View All teachers", "View teacher", "Edit teacher", "Remove teacher"]
    user_choice = st.sidebar.selectbox("Menu", user_menu)

    match user_choice:
        case "Add teacher":
            teacher_ID = st.text_input("teacher ID:") 
            teacher_name = st.text_input("teacher_name:")
            Email  = st.text_input("Email ID")
            Phone = st.text_input('Phone :')
            no_of_courses = st.text_input("Number of courses conducted:")

            if st.button("Add teacher"):
                query = ('INSERT INTO teacher_info (teacher_ID, teacher_name, Email, Phone, no_of_courses) VALUES (%s, %s, %s, %s, %s);')
                values = (teacher_ID, teacher_name, Email, Phone, no_of_courses)
                cursor.execute(query, values)
                conn.commit()
                st.success("Successfully added User: {}".format(teacher_name)) 
            
        case "View All teachers":
            df = functions.view_all_teachers(cursor)
            st.dataframe(df)
        
        case "View teacher":
            teacher_ID = st.text_input("Teacher ID:") 

            if st.button("View teacher"):
           
                cursor.execute("SELECT * FROM teacher_info WHERE teacher_ID = '%s'" %(teacher_ID))
                data = cursor.fetchall()
                df = pd.DataFrame(data, columns=['teacher_ID', 'teacher_name', 'Email', 'Phone', 'no_of_courses'])
                st.dataframe(df)

        case "Edit teacher":
            edit_menu = ['teacher_ID', 'teacher_name', 'Email', 'Phone', 'no_of_courses']
            edit_choice = st.selectbox("Menu", edit_menu)

            if edit_choice == 'teacher_name':
                teacher_ID = st.text_input("teacher_ID:")
                teacher_name = st.text_input("teacher teacher_name:")

                if st.button("Update"):
                    query = ('UPDATE teacher_info SET teacher_name = %s WHERE teacher_ID = %s;')
                    values = (teacher_name, teacher_ID)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated teacher")
            

            if edit_choice == 'Email':
                teacher_ID = st.text_input("teacher_ID:")
                Email = st.text_input("Email :")

                if st.button("Update"):
                    query = ('UPDATE teacher_info SET Email = %s WHERE teacher_ID = %s;')
                    values = (Email, teacher_ID)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated teacher")

            if edit_choice == 'Phone':
                teacher_ID = st.text_input("teacher_ID:")
                Phone = st.text_input("Phone:")

                if st.button("Update"):
                    query = ('UPDATE teacher_info SET Phone = %s WHERE teacher_ID = %s;')
                    values = (Phone, teacher_ID)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated teacher")
            
            if edit_choice == 'no_of_courses':
                teacher_ID = st.text_input("teacher_ID:")
                no_of_courses = st.text_input("Number of Courses:")

                if st.button("Update"):
                    query = ('UPDATE teacher_info SET no_of_courses = %s WHERE teacher_ID = %s;')
                    values = (no_of_courses, teacher_ID)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated teacher")
                
        case "Remove teacher":
            df = functions.view_all_teachers(cursor)
            with st.expander('View all teachers'):
                st.dataframe(df)
            
            list_of_users = [i for i in df.iloc[:, 0]]
            selected_user = st.selectbox("Select teacher ID to Delete", list_of_users)
            if st.button("Delete teacher"):
                cursor.execute('DELETE FROM teacher_info WHERE teacher_ID="{}"'.format(selected_user))
                cursor.execute('ALTER TABLE teacher_info AUTO_INCREMENT=1')
                conn.commit()
                st.success("teacher has been deleted successfully")

