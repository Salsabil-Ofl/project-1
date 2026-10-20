import streamlit as st

st.set_page_config(
    page_title="Sign In",
    page_icon="🔑",
    layout="centered"
)

st.title("🔐 Sign In")

st.write("Please enter your details to continue")

# Inputs
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Button
if st.button("Sign In"):
    if username and password:
        st.success(f"Welcome {username} ")
    else:
        st.error("Please fill all fields")