import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="TimeCraft | الأحداث التاريخية", layout="wide", page_icon="📜")

# 2. تحسين المظهر باستخدام CSS (التصميم التاريخي الفاخر)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap');

    /* الخلفية العامة */
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/dark-leather.png");
        background-color: #1a120b;
        color: #e2d1ad;
        font-family: 'Amiri', serif;
    }

    /* العناوين */
    h1, h2, h3 {
        color: #d4af37 !important;
        text-shadow: 2px 2px 4px #000;
        direction: rtl;
    }

    /* تنسيق القائمة الجانبية */
    section[data-testid="stSidebar"] {
        background-color: #261a0d !important;
        border-right: 2px solid #d4af37;
    }

    /* بطاقة المحتوى */
    .content-card {
        background: rgba(38, 26, 13, 0.7);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #8e735b;
        margin-top: 20px;
        line-height: 1.8;
        direction: rtl;
        text-align: right;
    }

    /* تحسين الصور */
    img {
        border-radius: 15px;
        border: 2px solid #d4af37;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    
    /* تنسيق الـ Radio Buttons */
    div[data-testid="stSidebarUserContent"] {
        color: #d4af37 !important;
        direction: rtl;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. القائمة الجانبية (Sidebar)
st.sidebar.markdown("<h2 style='text-align: center;'>📌 التنقل</h2>", unsafe_allow_html=True)
selection = st.sidebar.radio("اختار الحقبة الزمنية:", ["الرئيسية", "المعارك الإسلامية", "الحرب العالمية الأولى"])

# 4. العنوان الرئيسي
st.markdown("<h1 style='text-align: center; font-size: 50px;'>📜 أرشيف العصور </h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 22px; color: #e2d1ad;'>استكشف أهم المعارك واللحظات التي شكلت وجه التاريخ</p>", unsafe_allow_html=True)

# 5. محتوى الصفحات
if selection == "الرئيسية":
    st.markdown("""
        <div style='text-align: center;'>
            <p style='font-size: 20px;'>لقد تم تفعيل بوابة الزمن. اختر قسماً من القائمة الجانبية لتبدأ رحلتك الاستكشافية في أعماق الماضي.</p>
        </div>
    """, unsafe_allow_html=True)

elif selection == "المعارك الإسلامية":
    st.markdown("<h2 style='text-align: right; color: #d4af37;'>⚔️ من عبق البطولات الإسلامية</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # تأكدي من مسار الصورة الصحيح أو استخدام رابط مباشر
        st.image('images/m.jpg', caption="تصور لفتح مكة المكرمة") 
    
    with col2:
        st.markdown(f"""
            <div class="content-card">
                <h3 style="color: #d4af37;">الفتح الأعظم: فتح مكة (8 هـ)</h3>
                <p>
                يعد <b>فتح مكة</b> حدثاً مفصلياً في التاريخ الإسلامي، وقع في 20 رمضان عام 8 هـ. 
                كانت ذروة الحدث عندما دخل النبي ﷺ المسجد الحرام، وحطم الأصنام وهو يتلو: 
                <i>"وَقُلْ جَاءَ الْحَقُّ وَزَهَقَ الْبَاطِلُ إِنَّ الْبَاطِلَ كَانَ زَهُوقًا"</i>.
                </p>
                <hr style="border-color: #8e735b;">
                <p>
                <b>قمة التسامح:</b> حين قال ﷺ لأهل مكة: "ما تظنون أني فاعل بكم؟" قالوا: "خيراً، أخ كريم وابن أخ كريم"، 
                فقال: <b>"اذهبوا فأنتم الطلقاء"</b>. وبذلك انتهى الوثن وأصبحت مكة دار إسلام وأمان.
                </p>
            </div>
        """, unsafe_allow_html=True)

elif selection == "الحرب العالمية الأولى":
    st.markdown("<h2 style='text-align: right; color: #d4af37;'>🌍 جبهات الحرب العالمية الأولى</h2>", unsafe_allow_html=True)
    col3, col4 = st.columns([1, 2])
    
    with col3:
        st.image('images/m1.jpg', caption="سيارات الأجرة التي نقلت الجنود للجبهة")
    
    with col4:
        st.markdown(f"""
            <div class="content-card">
                <h3 style="color: #d4af37;">معركة المارن الأولى (1914): "معجزة المارن"</h3>
                <p>
                تعتبر واحدة من أهم المعارك الإستراتيجية، حيث أوقفت الزحف الألماني نحو باريس وغيرت مسار الحرب 
                إلى <b>حرب الخنادق</b> الطويلة.
                </p>
                <p><b>أبرز ملامح المعركة:</b></p>
                <ul>
                    <li>استخدام 600 سيارة أجرة باريسية لنقل الجنود بسرعة إلى الجبهة.</li>
                    <li>فشل "خطة شليفن" الألمانية وتحول الحرب إلى استنزاف.</li>
                    <li>منع سقوط العاصمة الفرنسية وحماية توازن القوى العالمي حينذاك.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

# 6. التذييل (Sidebar info)
st.sidebar.divider()
st.sidebar.markdown("""
    <div style='text-align: center; color: #8e735b; font-size: 14px;'>
        تم تطوير هذه الصفحة بكل فخر <br> كجزء من مشروع كود كامب 2026
    </div>
""", unsafe_allow_html=True)