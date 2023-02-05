import streamlit as st
import pandas as pd
import functions

def advance(conn, cursor):
    user_menu = ["Add participant", "View all participants", "View participant", "Edit participant", "Remove participant"]  
    user_choice = st.sidebar.selectbox("Menu", user_menu)

    match user_choice:
        case "Add participant":
            Registration_ID = st.text_input("Registration ID:")
            Name = st.text_input("Name:")
            Email_ID = st.text_input("Email_ID:")
            Phone = st.text_input("Phone:")
            Number_of_courses = st.text_input("Number of courses:")
            Course_ID = st.text_input("Course_ID:")

            if st.button("Add participant"):
                query = ('INSERT INTO advance_program_details (Registration_ID, Name, Email, Phone, Number_of_Courses, Course_ID) VALUES (%s, %s, %s, %s, %s, %s);')
                values = (Registration_ID, Name, Email_ID, Phone, Number_of_courses, Course_ID)
                cursor.execute(query, values)
                conn.commit()
                st.success("Successfully added participant")  

        case "View all participants":
            df = functions.view_all_advance(cursor)
            st.dataframe(df)

        case "View participant":
            Registration_ID = st.text_input("Registration ID:")

            if st.button("View participant"):
                cursor.execute("SELECT * FROM advance_program_details WHERE Registration_ID = '%s'" %(Registration_ID))
                data = cursor.fetchall()
                df = pd.DataFrame(data, columns=['Registration_ID', 'Name', 'Email_ID', 'Phone', 'Number_of_courses', 'Course_ID'])
                st.dataframe(df)
        
        case "Edit participant":
            edit_menu = ['Name', 'Email_ID', 'Phone', 'Number_of_courses', 'Course_ID']
            edit_choice = st.selectbox("Menu", edit_menu)

            if edit_choice == 'Name':
                Registration_ID = st.text_input("Registration ID:")
                name = st.text_input("Name:")

                if st.button("Update"):
                    query = ('UPDATE advance_program_details SET Name = %s WHERE Registration_ID = %s;')
                    values = (name, Registration_ID)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated participant")

            if edit_choice == 'Email_ID':
                Registration_ID = st.text_input("Registration ID:")
                Email_ID = st.text_input("Email_ID:")

                if st.button("Update"):
                    query = ('UPDATE advance_program_details SET Email = %s WHERE Registration_ID = %s;')
                    values = (Email_ID, Registration_ID)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated participant")

            if edit_choice == 'Phone':
                Registration_ID = st.text_input("Registration ID:")
                Phone = st.text_input("Phone:")

                if st.button("Update"):
                    query = ('UPDATE advance_program_details SET Phone = %s WHERE Registration_ID = %s;')
                    values = (Phone, Registration_ID)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated participant")

            if edit_choice == 'Number_of_courses':
                Registration_ID = st.text_input("Registration ID:")
                Number_of_courses = st.text_input("Number of courses:")

                if st.button("Update"):
                    query = ('UPDATE advance_program_details SET Number_of_Courses = %s WHERE Registration_ID = %s;')
                    values = (Number_of_courses, Registration_ID)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated participant")

            if edit_choice == 'Course_ID':
                Registration_ID = st.text_input("Registration ID:")
                Course_ID = st.text_input("Course_ID:")

                if st.button("Update"):
                    query = ('UPDATE advance_program_details SET Course_ID = %s WHERE Registration_ID = %s;')
                    values = (Course_ID, Registration_ID)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated participant")
            
        case "Remove participant":
                df = functions.view_all_advance(cursor)
                with st.expander('View all participants'):
                    st.dataframe(df)
            
                list_of_users = [i for i in df.iloc[:, 0]]
                selected_user = st.selectbox("Select Registration_ID to Delete", list_of_users)
                if st.button("Delete participant"):
                    cursor.execute('DELETE FROM advance_program_details WHERE Registration_ID="{}"'.format(selected_user))
                    cursor.execute('ALTER TABLE advance_program_details AUTO_INCREMENT=1')
                    conn.commit()
                    st.success("Participant has been deleted successfully")