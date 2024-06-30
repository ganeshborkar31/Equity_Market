import streamlit as st
import pandas as pd
import os


# File path for the CSV 'database'
db_file = 'users_db.csv'

# Load users database from CSV or create empty DataFrame if not exists
if os.path.exists(db_file):
    users_db = pd.read_csv(db_file, index_col='username')
else:
    users_db = pd.DataFrame(columns=['username', 'password']).set_index('username')

def signup_user(username, password):
    global users_db
    if username in users_db.index:
        return False
    else:
        # Add user to DataFrame and save
        users_db.loc[username] = [password]  # Note: In a real application, hash the password!
        users_db.to_csv(db_file)
        return True

def login_user(username, password):
    global users_db
    if username in users_db.index and users_db.loc[username, 'password'] == password:
        return True
    else:
        return False

def acc():
    st.title("Login & Signup ")

    menu = [ "Login", "Signup"]
    choice = st.selectbox("Menu", menu)

    # if choice == "Home":
    #     st.subheader("Home")
    #     st.write("Welcome to the home page!")

    if choice == "Login":
        st.subheader("Login")

        with st.form(key='login_form'):
            username = st.text_input("Username")
            password = st.text_input("Password", type='password')
            submit_button = st.form_submit_button(label='Login')

        if submit_button:
            if login_user(username, password):
                st.success(f"Welcome {username}!")
            else:
                st.warning("Incorrect Username/Password")

    elif choice == "Signup":
        st.subheader("Create New Account")

        with st.form(key='signup_form'):
            new_username = st.text_input("Username")
            new_password = st.text_input("Password", type='password')
            submit_button = st.form_submit_button(label='Signup')

        if submit_button:
            if signup_user(new_username, new_password):
                st.success("You have successfully created a valid account!")
                st.info("Go to the Login Menu to login")
            else:
                st.warning("Username already exists")



