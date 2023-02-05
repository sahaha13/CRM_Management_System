import streamlit as st
import pandas as pd 
import functions

def volunteer(conn, cursor):
    user_menu = ["Add volunteer", "View All volunteers", "View volunteer", "Edit volunteer", "Remove volunteer"]
    user_choice = st.sidebar.selectbox("Menu", user_menu)

    match user_choice:
        case "Add volunteer":
            Volunteer_ID = st.text_input("volunteer ID:") 
            Name = st.text_input("Name:")
            Email_ID  = st.text_input("Email_ID ID")
            Phone = st.text_input('Phone :')
            Courses_assisted = st.text_input("Number of courses conducted:")

            if st.button("Add volunteer"):
                query = ('INSERT INTO volunteer_info (Volunteer_ID, Name, Email_ID, Phone, Courses_assisted) VALUES (%s, %s, %s, %s, %s);')
                values = (Volunteer_ID, Name, Email_ID, Phone, Courses_assisted)
                cursor.execute(query, values)
                conn.commit()
                st.success("Successfully added User: {}".format(Name)) 
            
        case "View All volunteers":
            df = functions.view_all_volunteers(cursor)
            st.dataframe(df)
        
        case "View volunteer":
            Volunteer_ID = st.text_input("Volunteer ID:") 

            if st.button("View volunteer"):
                
                cursor.execute("SELECT * FROM volunteer_info WHERE Volunteer_ID = '%s'" %(Volunteer_ID))
                data = cursor.fetchall()
                df = pd.DataFrame(data, columns=['Volunteer_ID', 'Name', 'Email_ID', 'Phone', 'Courses_assisted'])
                st.dataframe(df)

        case "Edit volunteer":
            edit_menu = ['Volunteer_ID', 'Name', 'Email_ID', 'Phone', 'Courses_assisted']
            edit_choice = st.selectbox("Menu", edit_menu)

            if edit_choice == 'Name':
                Volunteer_ID = st.text_input("Volunteer_ID:")
                name = st.text_input("volunteer name:")

                if st.button("Update"):
                    query = ('UPDATE volunteer_info SET Name = %s WHERE Volunteer_ID = %s;')
                    values = (name, Volunteer_ID)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated volunteer")
            

            if edit_choice == 'Email_ID':
                Volunteer_ID = st.text_input("Volunteer_ID:")
                Email_ID = st.text_input("Email_ID :")

                if st.button("Update"):
                    query = ('UPDATE volunteer_info SET Email_ID = %s WHERE Volunteer_ID = %s;')
                    values = (Email_ID, Volunteer_ID)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated volunteer")

            if edit_choice == 'Phone':
                Volunteer_ID = st.text_input("Volunteer_ID:")
                Phone = st.text_input("Phone:")

                if st.button("Update"):
                    query = ('UPDATE volunteer_info SET Phone = %s WHERE Volunteer_ID = %s;')
                    values = (Phone, Volunteer_ID)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated volunteer")
            
            if edit_choice == 'Courses_assisted':
                Volunteer_ID = st.text_input("Volunteer_ID:")
                Courses_assisted = st.text_input("Number of Courses:")

                if st.button("Update"):
                    query = ('UPDATE volunteer_info SET Courses_assisted = %s WHERE Volunteer_ID = %s;')
                    values = (Courses_assisted, Volunteer_ID)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated volunteer")
                
        case "Remove volunteer":
            df = functions.view_all_volunteers(cursor)
            with st.expander('View all volunteers'):
                st.dataframe(df)
            
            list_of_users = [i for i in df.iloc[:, 0]]
            selected_user = st.selectbox("Select volunteer ID to Delete", list_of_users)
            if st.button("Delete volunteer"):
                cursor.execute('DELETE FROM volunteer_info WHERE Volunteer_ID="{}";'.format(selected_user))
                cursor.execute('ALTER TABLE volunteer_info AUTO_INCREMENT=1')
                conn.commit()
                st.success("volunteer has been deleted successfully")

