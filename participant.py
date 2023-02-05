import streamlit as st
import pandas as pd 
import functions

def participant(conn, cursor):
    user_menu = ["Add Participant", "View All Participants", "View Participant", "Edit Participant", "Remove Participant"]
    user_choice = st.sidebar.selectbox("Menu", user_menu)

    match user_choice:
        case "Add Participant":
            name = st.text_input("Name:") 
            email = st.text_input("Email ID:")
            Registration_ID = st.text_input("Registration ID")
            Amount = st.selectbox("Amount",["1000", "1200", "1500"])
            source = st.text_input("Source:")
            Registration_type = st.selectbox('Registration type',["Online", "Offline"])
            District = st.text_input('District:')
            Phone = st.text_input('Phone :')
            Course_ID = st.text_input('Course ID:')


            if st.button("Add participant"):
                query = ('INSERT INTO participant_info (name, email, Registration_ID, Amount, source, Registration_type, District, Phone, Course_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);')
                values = (name, email, Registration_ID, Amount, source, Registration_type, District, Phone, Course_ID)
                cursor.execute(query, values)
                conn.commit()
                st.success("Successfully added User: {}".format(name))

        case "View All Participants":
            df = functions.view_all_participants(cursor)
            st.dataframe(df)

        case "View Participant":
            name = st.text_input("Name:") 

            if st.button("View Participant"):
                
                cursor.execute("SELECT * FROM participant_info WHERE name = '%s'" %(name))
                data = cursor.fetchall()
                df = pd.DataFrame(data, columns=['name', 'email', 'Registration_ID', 'Amount', 'source', 'Registration_type', 'District', 'Phone', 'Course_ID'])
                st.dataframe(df)

        case "Edit Participant":
            edit_menu = ['name', 'email', 'Amount', 'source', 'Registration_type', 'District', 'Phone', 'Course_ID']
            edit_choice = st.selectbox("Menu", edit_menu)

            if edit_choice == 'name':
                Registration_ID = st.text_input("Registration_ID:")
                name = st.text_input("name:")

                if st.button("Update"):
                    query = ('UPDATE participant_info SET name = %s WHERE Registration_ID = %s;')
                    values = (name, Registration_ID)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Participant")
            
            

            if edit_choice == 'email':
                Registration_id = st.text_input("Registration_ID:")
                email = st.text_input("Email:")

                if st.button("Update"):
                    query = ('UPDATE participant_info SET email = %s WHERE Registration_ID = %s;')
                    values = (email, Registration_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Participant")

            if edit_choice == 'Amount':
                user_id = st.text_input("Registration ID:")
                amount = st.text_input("Amount:")

                if st.button("Update"):
                    query = ('UPDATE participant_info SET Amount = %s WHERE Registration_ID = %s;')
                    values = (amount , user_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Participant")
            
            if edit_choice == 'source':
                user_id = st.text_input("Participant ID:")
                source = st.date_input("source:")

                if st.button("Update"):
                    query = ('UPDATE participant_info SET source = %s WHERE Registration_ID = %s;')
                    values = (source, user_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Participant")

            if edit_choice == 'Registration_type':
                user_id = st.text_input("Registration ID:")
                type = st.text_input("Registration type:")

                if st.button("Update"):
                    query = ('UPDATE participant_info SET Registration_type = %s WHERE Registration_ID = %s;')
                    values = (type, user_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated User")
            
            if edit_choice == 'District':
                user_id = st.text_input("Registration ID:")
                District = st.text_input("District:")

                if st.button("Update"):
                    query = ('UPDATE participant_info SET District = %s WHERE Registration_ID = %s;')
                    values = (District, user_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated User")
            
            if edit_choice == 'Phone':
                user_id = st.text_input("Participant ID:")
                Phone = st.text_input("Phone number:")

                if st.button("Update"):
                    query = ('UPDATE participant_info SET Phone = %s WHERE Registration_ID = %s;')
                    values = (Phone, user_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated User")
            
            if edit_choice == 'Course_ID':
                user_id = st.text_input("Participant ID:")
                Phone = st.text_input("Course_ID:")

                if st.button("Update"):
                    query = ('UPDATE participant_info SET Course_ID = %s WHERE Registration_ID = %s;')
                    values = (Phone, user_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated User")
        
        case "Remove Participant":
            df = functions.view_all_participants(cursor)
            with st.expander('View all Participants'):
                st.dataframe(df)
            
            list_of_users = [i for i in df.iloc[:, 2]]
            selected_user = st.selectbox("Select Registration ID to Delete", list_of_users)
            if st.button("Delete User"):
                cursor.execute('DELETE FROM participant_info WHERE Registration_ID="{}";'.format(selected_user))
                cursor.execute('ALTER TABLE participant_info AUTO_INCREMENT=1')
                conn.commit()
                st.success("Participant has been deleted successfully")