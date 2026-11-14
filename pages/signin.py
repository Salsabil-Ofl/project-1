import streamlit as st

st.set_page_config(page_title="TimeCraft | Sign In", page_icon="🔑", layout="centered")
st.title("🔐 Sign in")
st.info("Sign-in is a user-interface demo only. No account authentication is implemented.")

with st.form("sign_in_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Continue")

if submitted:
    if username.strip() and password:
        st.warning("This prototype does not verify credentials or create a signed-in session.")
    else:
        st.error("Enter both a username and a password to preview the form.")
