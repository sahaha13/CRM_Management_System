import streamlit as st
import pandas as pd
import functions

def course(conn, cursor):
        user_menu = ["Add course", "View All courses", "View course", "Edit course", "Remove course"]
        user_choice = st.sidebar.selectbox("Menu", user_menu)

        match user_choice:
            case "Add course":
                Course_ID = st.text_input("Course ID:")
                Course_Name = st.text_input("Course Name:")
                No_of_pax = st.text_input("No of pax:")
                Venue = st.text_input("Venue:")
                Teacher_ID = st.text_input("Teacher ID:")
                Volunteer_ID = st.text_input("Volunteer ID:")
                Course_Start_Date = st.date_input("Course Start Date:")
                Course_End_Date = st.date_input("Course End Date:")

                if st.button("Add course"):
                    query = ('INSERT INTO course_details (Course_ID, Course_Name, No_of_pax, Venue, Teacher_ID, Volunteer_ID, Course_Start_Date, Course_End_Date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);')
                    values = (Course_ID, Course_Name, No_of_pax, Venue, Teacher_ID, Volunteer_ID, Course_Start_Date, Course_End_Date)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully added Course: {}".format(Course_Name))

            case "View All courses":
                df = functions.view_all_courses(cursor)
                st.dataframe(df)

            case "View course":
                Course_ID = st.text_input("Course ID:")

                if st.button("View Course"):
                    cursor.execute("SELECT * FROM course_details WHERE Course_ID = '%s'" %(Course_ID))
                    data = cursor.fetchall()
                    df = pd.DataFrame(data, columns=['Course_ID', 'Course_Name', 'No_of_pax', 'Venue', 'Teacher_ID', 'Volunteer_ID', 'Course_Start_Date', 'Course_End_Date'])
                    st.dataframe(df)
            
            case "Edit course":
                edit_menu = ['Course_Name', 'No_of_pax', 'Venue', 'Teacher_ID', 'Volunteer_ID', 'Course_Start_Date', 'Course_End_Date']
                edit_choice = st.selectbox("Menu", edit_menu)

                if edit_choice == 'Course_Name':
                    Course_ID = st.text_input("Course_ID:")
                    Course_Name = st.text_input("Course_Name:")

                    if st.button("Update"):
                        query = ('UPDATE course_details SET Course_Name = %s WHERE Course_ID = %s;')
                        values = (Course_Name, Course_ID)
                        cursor.execute(query, values)
                        conn.commit()
                        st.success("Successfully Updated Course")

                if edit_choice == 'No_of_pax':
                    Course_ID = st.text_input("Course_ID:")
                    No_of_pax = st.text_input("No_of_pax:")

                    if st.button("Update"):
                        query = ('UPDATE course_details SET No_of_pax = %s WHERE Course_ID = %s;')
                        values = (No_of_pax, Course_ID)
                        cursor.execute(query, values)
                        conn.commit()
                        st.success("Successfully Updated Course")
                
                if edit_choice == 'Venue':
                    Course_ID = st.text_input("Course_ID:")
                    Venue = st.text_input("Venue:")

                    if st.button("Update"):
                        query = ('UPDATE course_details SET Venue = %s WHERE Course_ID = %s;')
                        values = (Venue, Course_ID)
                        cursor.execute(query, values)
                        conn.commit()
                        st.success("Successfully Updated Course")
                
                if edit_choice == 'Teacher_ID':
                    Course_ID = st.text_input("Course_ID:")
                    Teacher_ID = st.text_input("Teacher_ID:")

                    if st.button("Update"):
                        query = ('UPDATE course_details SET Teacher_ID = %s WHERE Course_ID = %s;')
                        values = (Teacher_ID, Course_ID)
                        cursor.execute(query, values)
                        conn.commit()
                        st.success("Successfully Updated Course")
                
                if edit_choice == 'Volunteer_ID':
                    Course_ID = st.text_input("Course_ID:")
                    Volunteer_ID = st.text_input("Volunteer_ID:")

                    if st.button("Update"):
                        query = ('UPDATE course_details SET Volunteer_ID = %s WHERE Course_ID = %s;')
                        values = (Volunteer_ID, Course_ID)
                        cursor.execute(query, values)
                        conn.commit()
                        st.success("Successfully Updated Course")
                
                if edit_choice == 'Course_Start_Date':
                    Course_ID = st.text_input("Course_ID:")
                    Course_Start_Date = st.date_input("Course_Start_Date:")

                    if st.button("Update"):
                        query = ('UPDATE course_details SET Course_Start_Date = %s WHERE Course_ID = %s;')
                        values = (Course_Start_Date, Course_ID)
                        cursor.execute(query, values)
                        conn.commit()
                        st.success("Successfully Updated Course")
                
                if edit_choice == 'Course_End_Date':
                    Course_ID = st.text_input("Course_ID:")
                    Course_End_Date = st.date_input("Course_End_Date:")

                    if st.button("Update"):
                        query = ('UPDATE course_details SET Course_End_Date = %s WHERE Course_ID = %s;')
                        values = (Course_End_Date, Course_ID)
                        cursor.execute(query, values)
                        conn.commit()
                        st.success("Successfully Updated Course")
            
            case "Remove course":
                df = functions.view_all_courses(cursor)
                with st.expander('View all Courses'):
                    st.dataframe(df)
            
                list_of_users = [i for i in df.iloc[:, 0]]
                selected_user = st.selectbox("Select Course_ID to Delete", list_of_users)
                if st.button("Delete Course"):
                    cursor.execute('DELETE FROM course_details WHERE Course_ID="{}"'.format(selected_user))
                    cursor.execute('ALTER TABLE course_details AUTO_INCREMENT=1')
                    conn.commit()
                    st.success("Participant has been deleted successfully")



