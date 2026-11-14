import streamlit as st

st.set_page_config(page_title="TimeCraft | About", layout="wide")

section = st.sidebar.radio("About TimeCraft", ["Project and team", "Contact"])

if section == "Project and team":
    st.title("About the project")
    st.info(
        "TimeCraft is an educational prototype that brings selected historical topics together "
        "in a Streamlit application. It is designed to encourage exploration and discussion."
    )
    st.subheader("Project team")
    team = [
        ("Sama Saeed", "Contact page"),
        ("Rewan Mohamed", "Historical events"),
        ("Mariem Montasser", "Historical figures encyclopedia"),
        ("Salsabil Ebrahime", "Scenario and chatbot pages"),
        ("Buthaina Waleed", "History content"),
        ("Esraa Badawy", "Home page"),
    ]
    columns = st.columns(3)
    for index, (name, role) in enumerate(team):
        with columns[index % 3], st.container(border=True):
            st.subheader(name)
            st.caption(role)

else:
    st.title("Contact the team")
    st.write("Use this sample form to draft a comment or project suggestion.")
    with st.form("contact_form"):
        name = st.text_input("Full name")
        email = st.text_input("Email address")
        subject = st.selectbox("Topic", ["General question", "Project suggestion", "Technical issue"])
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")

    if submitted:
        if name.strip() and email.strip() and message.strip():
            st.success("Thanks. This demo does not send or store messages.")
        else:
            st.warning("Please complete the name, email, and message fields.")
