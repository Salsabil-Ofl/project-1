import streamlit as st


st.set_page_config(
    page_title="TimeCraft | رحلة عبر الزمن", 
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="⏳"
)

home_page = st.Page(
    page='pages/home.py',
    title='الصفحة الرئيسية',
    icon='🏠',
    default=True,
    url_path="home"
)


chatbot2_page = st.Page(
    page='pages/chatbot2.py', 
    title='اسأل الذكاء الاصطناعي', 
    icon='✨',
    url_path="chatbot2"
)
chatbot_page = st.Page(
    page='pages/chatbot.py', 
    title='بوابة العصور التاريخية', 
    icon='🕰️',
    url_path="chatbot"
)

about_page = st.Page(
    page='pages/about.py', 
    title='عن التطبيق', 
    url_path="about"
)

ex_page = st.Page(
    page='pages/ex.py', 
    title='الأحداث التاريخية', 
    url_path="experiments"
)

pro_page = st.Page(
    page='pages/pro.py', 
    title='الموسوعة الشخصية', 
    icon='👤',
    url_path="profile"
)
signin_page = st.Page(
    page='pages/signin.py', 
    title='تسجيل الدخول', 
    icon='🔑',
    url_path="signin"
)

signup_page = st.Page(
    page='pages/signup.py', 
    title='إنشاء حساب', 
    icon='📝',
    url_path="signup"
)

all_pages = st.navigation(
    pages=[
        home_page,
        signin_page,
        signup_page,
        chatbot2_page,
        about_page,
        ex_page,
        pro_page,
        chatbot_page
    ],
    position='top'
)

all_pages.run()

# خلفية جميلة باستخدام Streamlit فقط
