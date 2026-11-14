import streamlit as st

st.set_page_config(
    page_title="TimeCraft | Historical Explorer",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="⏳",
)

home_page = st.Page(
    page="pages/home.py",
    title="Home",
    icon="🏠",
    default=True,
    url_path="home",
)

simulation_page = st.Page(
    page="pages/chatbot.py",
    title="What If? Scenarios",
    icon="🕰️",
    url_path="scenarios",
)

assistant_page = st.Page(
    page="pages/chatbot2.py",
    title="AI Assistant",
    icon="✨",
    url_path="assistant",
)

world_updates_page = st.Page(
    page="pages/world_updates.py",
    title="World Updates",
    icon="🌐",
    url_path="world-updates",
)

history_page = st.Page(
    page="pages/ex.py",
    title="Historical Events",
    icon="📜",
    url_path="events",
)

figures_page = st.Page(
    page="pages/pro.py",
    title="Historical Figures",
    icon="👤",
    url_path="figures",
)

about_page = st.Page(
    page="pages/about.py",
    title="About",
    icon="ℹ️",
    url_path="about",
)

sign_in_page = st.Page(
    page="pages/signin.py",
    title="Sign In",
    icon="🔑",
    url_path="signin",
)

sign_up_page = st.Page(
    page="pages/signup.py",
    title="Sign Up",
    icon="📝",
    url_path="signup",
)

navigation = st.navigation(
    [
        home_page,
        history_page,
        figures_page,
        simulation_page,
        world_updates_page,
        assistant_page,
        about_page,
        sign_in_page,
        sign_up_page,
    ],
    position="top",
)
navigation.run()
