import streamlit as st

# 1. إعدادات الصفحة والـ Theme التاريخي
st.set_page_config(page_title="TimeCraft | بوابة العصور", layout="wide")

st.markdown("""
    <style>
    import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap');

    /* الخلفية العامة */
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/dark-leather.png");
        background-color: #1a120b;
        color: #e2d1ad;
        font-family: 'Amiri', serif;
    }

    /* العناوين الذهبية */
    h1, h2, h3 {
        color: #d4af37 !important;
        text-align: center;
        text-shadow: 2px 2px 4px #000;
    }


    /* تصميم الأزرار */
    div.stButton > button {
        background-color: #3d2b1f;
        color: #d4af37;
        border: 1px solid #d4af37;
        width: 100%;
        font-size: 1.2rem;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #d4af37;
        color: #1a120b;
    }

    /* تعديل شكل الـ Metrics */
    [data-testid="stMetricValue"] {
        color: #d4af37 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- محتوى الصفحة ---
st.markdown('<h1>🕰️ بوابة العصور: اختر نقطة التحول التاريخية</h1>', unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div class="control-panel">', unsafe_allow_html=True)
    st.subheader("🎮 لوحة التحكم")
    
    era = st.selectbox(
        "اختر الحقبة الزمنية التي تريد استكشافها:",
        ["....اختر",
         "الثورة الفرنسية (1789)",
         "الحرب العالمية الثانية (1939)",
         "اكتشاف أمريكا (1492)",
         "الثورة الصناعية (1760)",
         "العصر الذهبي الإسلامي"]
    )
    
    detail_level = st.select_slider(
        "مستوى دقة المحاكاة التاريخية:",
        options=["أساسي", "متوسط", "متقدم", "شامل"]
    )
    
    start_sim = st.button("🚀 بدء المحاكاة الزمنية")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if start_sim and era != "....اختر":
        st.success(f"✨ تم تفعيل بوابة الزمن! نحن الآن في {era}")
        
        # --- قسم الثورة الفرنسية ---
        if era == "الثورة الفرنسية (1789)":
            st.header("🇫🇷 الثورة الفرنسية")
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Jacques_Bertaux_-_Prise_du_palais_des_Tuileries_-_1793.jpg/250px-Jacques_Bertaux_-_Prise_du_palais_des_Tuileries_-_1793.jpg", 
                     caption="اقتحام سجن الباستيل", use_container_width=True)
            
            st.info("📜 نبذة تاريخية: سقوط الملكية وظهور مفاهيم حقوق الإنسان.")
            
            # عرض المقاييس بشكل أنيق
            m1, m2 = st.columns(2)
            m1.metric("السنة", "1789", "بداية الثورة")
            m2.metric("المكان", "باريس، فرنسا")
            
            st.warning("🤔 ماذا لو لم يقتحم الشعب سجن الباستيل؟ هل كان نابليون سيظهر؟")

        # --- قسم الحرب العالمية الثانية ---
        elif era == "الحرب العالمية الثانية (1939)":
            st.header("🌍 الحرب العالمية الثانية")
            st.image("https://fmcdn.alqaheranews.net/2c2f7460-684e-11ef-83b0-ef159e6c0f8c-file-1725187042980-577631689?&w=700&compress=80&gravity=face", 
                     use_container_width=True)
            
            m1, m2 = st.columns(2)
            m1.metric("بداية الحرب", "1939")
            m2.metric("المشاركون", "+50 دولة")
            
            st.error("💭 السيناريو البديل: ماذا لو انتصرت دول المحور؟")

        # --- قسم اكتشاف أمريكا ---
        elif era == "اكتشاف أمريكا (1492)":
            st.header("⛵ اكتشاف أمريكا")
            st.image("https://img.youm7.com/large/20171012033500350.jpg", 
                     use_container_width=True)
            
            m1, m2 = st.columns(2)
            m1.metric("السنة", "1492")
            m2.metric("القائد", "كولومبوس")
            
            st.success("🌟 ماذا لو لم تصل السفن؟ هل كانت الحضارات الأصلية ستزدهر؟")

        # --- قسم الثورة الصناعية ---
        elif era == "الثورة الصناعية (1760)":
            st.header("⚙️ الثورة الصناعية")
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Powerloom_weaving_in_1835.jpg/800px-Powerloom_weaving_in_1835.jpg", 
                     use_container_width=True)
            
            m1, m2 = st.columns(2)
            m1.metric("البداية", "1760")
            m2.metric("المصدر", "بريطانيا")

        # --- العصر الذهبي الإسلامي ---
        elif era == "العصر الذهبي الإسلامي":
            st.header("🕌 العصر الذهبي الإسلامي")
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Aristotle_Rossello_Ardit.jpg/800px-Aristotle_Rossello_Ardit.jpg", 
                     use_container_width=True)
            
            m1, m2 = st.columns(2)
            m1.metric("الفترة", "750-1258 م")
            m2.metric("المركز", "بغداد")
            
            st.success("🌙 ماذا لو استمر العصر الذهبي؟ كيف كانت مكانتنا العلمية اليوم؟")

        st.write("---")
        st.success(f"✅ تم تحميل المسارات البديلة للحقبة بنجاح!")
        
    elif start_sim and era == "....اختر":
        st.warning("⚠️ من فضلك اختر حقبة تاريخية أولاً لبدء المحاكاة!")