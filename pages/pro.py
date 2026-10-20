import streamlit as st

# 1. إعداد الصفحة بشكل احترافي
st.set_page_config(page_title="موسوعة العظماء", layout="wide")

# 2. لمسة جمالية بالعناوين
st.markdown("<h1 style='text-align: center; color: #eeee;'>🏛️ موسوعة الشخصيات التاريخية العالمية</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>استكشف سير العظماء الذين غيروا مجرى التاريخ</p>", unsafe_allow_html=True)
st.markdown("---")

# 3. قاعدة البيانات المطورة (بيانات دسمة + تفاصيل إضافية)
historical_figures = [
    {
        "الاسم": "ابن خلدون",
        "اللقب": "عبقري علم الاجتماع",
        "العصر": "العصر الإسلامي (القرن 14)",
        "الإنجازات": "مؤسس علم الاجتماع وواضع كتاب 'المقدمة' الذي أسس لقواعد التاريخ الحديث.",
        "الصورة": "https://www.aldiwan.net/public/images/cat_images/17510641891.png",
        "أثر_باقي": "نظريات العمران البشري والدول."
    },
    {
        "الاسم": "ماري كوري",
        "اللقب": "سيدة الإشعاع",
        "العصر": "العصر الحديث",
        "الإنجازات": "اكتشفت الراديوم والبولونيوم، وهي الشخص الوحيد الذي فاز بنوبل في مجالين علميين مختلفين.",
        "الصورة": "data:image/jpeg;base64,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",
        "أثر_باقي": "تطوير الأشعة السينية في الطب."
    },
    {
        "الاسم": "ابن سينا",
        "اللقب": "أمير الأطباء",
        "العصر": "العصر الذهبي للإسلام",
        "الإنجازات": "ألف كتاب 'القانون في الطب' الذي ظل المرجع الأساسي في جامعات أوروبا لقرون.",
        "الصورة": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS13UJ_hDrakAS4j06sAh5eiEiGH4Fy15gnqw&s",
        "أثر_باقي": "تطوير طرق العلاج النفسي والجراحة."
    },
    {
        "الاسم": "ألبرت أينشتاين",
        "اللقب": "أيقونة الفيزياء",
        "العصر": "العصر الحديث",
        "الإنجازات": "صاحب النظرية النسبية التي غيرت مفهومنا عن الكون تماماً، وحصل على نوبل عام 1921.",
        "الصورة": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Albert_Einstein_Head.jpg",
        "أثر_باقي": "الطاقة النووية وفهم الجاذبية."
    },
    {
        "الاسم": "صلاح الدين الأيوبي",
        "اللقب": "القائد النبيل",
        "العصر": "العصور الوسطى",
        "الإنجازات": "قائد فذ وحد الجبهة الإسلامية، عُرف بنبله حتى مع أعدائه واستعاد القدس.",
        "الصورة": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3--Biw3h9V8n04oBzVtpRiw8qEDi8Y8A8hQ&s",
        "أثر_باقي": "نموذج الفروسية والقيادة الأخلاقية."
    },
    {
        "الاسم": "عباس بن فرناس",
        "اللقب": "حكيم الأندلس",
        "العصر": "الأندلس",
        "الإنجازات": "رائد محاولات الطيران الأولى، مخترع الساعة المائية ومبتكر صناعة الزجاج من الرمل.",
        "الصورة": "https://akhbarelsyaha.com/storage/2020/11/IMG-20201127-WA0013.jpg",
        "أثر_باقي": "إلهام البشرية نحو غزو الفضاء."
    },
    {
        "الاسم": "ليوناردو دا فينشي",
        "اللقب": "الرجل الموسوعي",
        "العصر": "عصر النهضة",
        "الإنجازات": "رسام الموناليزا، مهندس، ومخترع صمم نماذج أولية للدبابات والمروحيات.",
        "الصورة": "data:image/jpeg;base64,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",
        "أثر_باقي": "دمج الفن بالعلم والتشريح."
    },
    {
        "الاسم": "الملكة زنوبيا",
        "اللقب": "قاهرة الرومان",
        "العصر": "العصر الروماني",
        "الإنجازات": "حكمت تدمر بذكاء وقوة، وسيطرت على مصر والشام متحديةً أعظم إمبراطورية وقتها.",
        "الصورة": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyiMV-CR0C3tjPcbqxKm_OHpkKtgpcGZXHNw&s",
        "أثر_باقي": "رمز للقوة والسيادة النسائية في التاريخ."
    }
]

# 4. شريط البحث التفاعلي
search = st.text_input("🔍 ابحث في ذاكرة التاريخ (ادخل اسم الشخصية):", "")

# 5. عرض البطاقات بتنسيق احترافي
filtered_figures = [f for f in historical_figures if search in f["الاسم"]]

if not filtered_figures:
    st.warning("لم يتم العثور على شخصية بهذا الاسم، جرب اسماً آخر.")
else:
    cols = st.columns(3)
    for index, figure in enumerate(filtered_figures):
        with cols[index % 3]:
            # حاوية لكل شخصية (بطاقة)
            with st.container(border=True):
                st.image(figure["الصورة"], use_container_width=True)
                st.subheader(figure["الاسم"])
                st.markdown(f"**🏷️ اللقب:** `{figure['اللقب']}`")
                st.write(f"📍 **العصر:** {figure['العصر']}")
                st.write(f"🌟 **الأثر الباقي:** {figure['أثر_باقي']}")
                
                with st.expander("📝 عرض الإنجازات"):
                    st.info(figure["الإنجازات"])
                
                # الإضافة الجديدة (تفاعل المستخدم)
                col_fav, col_rate = st.columns(2)
                with col_fav:
                    if st.button(f"❤️ أعجبني", key=f"fav_{index}"):
                        st.toast(f"تمت إضافة {figure['الاسم']} للمفضلة!")
                with col_rate:
                    st.feedback("stars", key=f"star_{index}")

# 6. تذييل الصفحة
st.markdown("---")
st.markdown("<center>تم إعداد هذه الموسوعة لغرض تعليمي | جميع الحقوق محفوظة 2026 🚀</center>", unsafe_allow_html=True)