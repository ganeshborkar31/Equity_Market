import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
import hashlib

# Load user credentials from CSV file
def load_user_data():
    df = pd.read_csv('users.csv')
    return df

# Hash a password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Prepare credentials for authenticator
df = load_user_data()
credentials = {
    'usernames': {
        row['username']: {
            'name': row['name'],
            'password': row['password']
        }
        for _, row in df.iterrows()
    }
}

# Create the authenticator
authenticator = stauth.Authenticate(
    credentials=credentials,
    cookie_name='your_app_cookie',
    cookie_key='your_secret_cookie_key',  # Secure, unique key
    cookie_expiry_days=30
)

# Streamlit app
st.title("Streamlit User Authentication")

# Login method with location parameter
name, authentication_status, username = authenticator.login('Login', location='main')

if authentication_status:
    st.write(f"Welcome, {name}!")
    # Add your app content here for authenticated users

elif authentication_status is False:
    st.error('Username or password is incorrect')

elif authentication_status is None:
    st.info('Please enter your username and password')

# Register a new user (for admin or initial setup)
def register_user(username, password, name):
    df = load_user_data()
    if username not in df['username'].values:
        new_data = pd.DataFrame({
            'username': [username],
            'password': [hash_password(password)],
            'name': [name]
        })
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv('users.csv', index=False)
        st.success("User registered successfully!")
    else:
        st.warning("Username already exists")

# Registration form
reg_username = st.text_input('New username')
reg_password = st.text_input('New password', type='password')
reg_name = st.text_input('Name')

if st.button('Register'):
    if reg_username and reg_password and reg_name:
        register_user(reg_username, reg_password, reg_name)
