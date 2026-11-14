import streamlit as st

st.set_page_config(page_title="TimeCraft | Sign Up", page_icon="📝", layout="centered")
st.title("📝 Create an account")
st.info("Account creation is a user-interface demo only. Do not enter a real password.")

with st.form("sign_up_form"):
    username = st.text_input("Username")
    email = st.text_input("Email address")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm password", type="password")
    submitted = st.form_submit_button("Preview sign-up")

if submitted:
    if not all((username.strip(), email.strip(), password, confirm_password)):
        st.error("Complete all fields to preview the form.")
    elif password != confirm_password:
        st.error("The passwords do not match.")
    else:
        st.success("The form is valid. This prototype does not create or store accounts.")
