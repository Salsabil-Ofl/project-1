import streamlit as st

st.title("📝 Sign Up")

if "users" not in st.session_state:
    st.session_state.users = []

# Inputs
col1, col2 = st.columns([1, 2])

with col1:
    username = st.text_input("Username")

with col2:
    email = st.text_input("Email")

password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

# Sign Up button
if st.button("Sign Up" , width=500):
    if username and email and password and confirm_password:

        if password == confirm_password:
            # Save user temporarily
            st.session_state.users.append({
                "username": username,
                "email": email,
                "password": password
            })

            st.success("Account created successfully 🎉")

        else:
            st.error("Passwords do not match")

    else:
        st.error("Please fill all fields")

