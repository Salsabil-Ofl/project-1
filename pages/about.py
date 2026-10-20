
import streamlit as st
import time
import numpy as np
from streamlit_folium import st_folium
import folium



st.set_page_config(page_title="مشروع حضارة", layout="wide")


st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        text-align: center;
        margin-bottom: 20px;
    }
    .card:hover {
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }
    .container {
        padding: 2px 16px;
    }
    .title-text {
        color: #2c3e50;
        font-family: 'Arial';
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    
    st.sidebar.title("التنقل")
    page = st.sidebar.radio("انتقل إلى:", ["عن المشروع والفريق", "اتصل بنا"])

    if page == "عن المشروع والفريق":
        show_about_page()
    elif page == "اتصل بنا":
        show_contact_page()

def show_about_page():
    st.markdown("<h1 style='text-align: center;'>عن المشروع والفريق</h1>", unsafe_allow_html=True)
    st.write("---")
    
    st.subheader("💡 فكرة المشروع")
    st.info("هذا المشروع يهدف إلى تسليط الضوء على الحضارة العريقة باستخدام التقنيات الحديثة، وربط الماضي بالحاضر من خلال أدوات التكنولوجيا المتقدمة.")

    st.write("---")
    
   
    st.subheader("👥 أعضاء الفريق")
    
    
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div class="card" style="background-color: #e2d1ad; padding: 15px; border-radius: 10px; border: 2px solid #8e735b; text-align: center;">
                <h3 style="color: #000000; margin-bottom: 0; font-weight: bold;">Sama Saeed</h3>
                <p style="color: #1a1a1a; font-style: italic;">Contact Us Page Admin</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="card" style="background-color: #e2d1ad; padding: 15px; border-radius: 10px; border: 2px solid #8e735b; text-align: center;">
                <h3 style="color: #000000; margin-bottom: 0; font-weight: bold;">Rewan Mohamed</h3>
                <p style="color: #1a1a1a; font-style: italic;">Historical Events Page Official</p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="card" style="background-color: #e2d1ad; padding: 15px; border-radius: 10px; border: 2px solid #8e735b; text-align: center;">
                <h3 style="color: #000000; margin-bottom: 0; font-weight: bold;">Mariem Montasser</h3>
                <p style="color: #1a1a1a; font-style: italic;">Character Encyclopedia Page Administrator</p>
            </div>
        """, unsafe_allow_html=True)
    
    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown("""
            <div class="card" style="background-color: #e2d1ad; padding: 15px; border-radius: 10px; border: 1px solid #8e735b;">
                <h3 style="color: #000000; margin-bottom: 0; font-weight: bold;">Salsabil Ebrahime</h3>
                <p style="color: #1a1a1a; font-style: italic;">Chatbot Page Administrator</p>
            </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
            <div class="card" style="background-color: #e2d1ad; padding: 15px; border-radius: 10px; border: 1px solid #8e735b;">
                <h3 style="color: #000000; margin-bottom: 0; font-weight: bold;">Buthaina Waleed</h3>
                <p style="color: #1a1a1a; font-style: italic;">History Page Administrator</p>
            </div>
        """, unsafe_allow_html=True)

    with col6:
        st.markdown("""
            <div class="card" style="background-color: #e2d1ad; padding: 15px; border-radius: 10px; border: 1px solid #8e735b;">
                <h3 style="color: #000000; margin-bottom: 0; font-weight: bold;">Esraa Badawy</h3>
                <p style="color: #1a1a1a; font-style: italic;">Home Screen Administrator</p>
            </div>
        """, unsafe_allow_html=True)
def show_contact_page():
    st.markdown("<h1 style='text-align: center;'>اتصل بنا - Contact Us</h1>", unsafe_allow_html=True)
    st.write("يسعدنا استقبال استفساراتكم واقتراحاتكم.")
    
   
    with st.form(key='contact_form'):
        name = st.text_input("الأسم الكامل")
        email = st.text_input("البريد الإلكتروني")
        subject = st.selectbox("سبب التواصل", ["استفسار عام", "اقتراح للمشروع", "مشكلة تقنية"])
        message = st.text_area("رسالتك")
        
        submit_button = st.form_submit_button(label='إرسال الرسالة')
        
        if submit_button:
            if name and email and message:
                st.success(f"شكراً يا {name}، تم استلام رسالتك!")
            else:
                st.warning("يرجى ملء كافة الخانات المطلوبة.")


if __name__ == "__main__":
    main()