import streamlit as st
import google.generativeai as genai
from duckduckgo_search import DDGS

# --- 1. إعدادات واجهة المستخدم ---
st.set_page_config(page_title="AI Genius Pro", page_icon="🎓", layout="centered")

# لمسة جمالية للويندوز
st.markdown("""
    <style>
    .stApp { background-color: black; }
    .stChatMessage { border-radius: 15px; border: 1px solid #eee; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. إعدادات الجيمناي (Gemini) ---
API_KEY = st.secrets.get("GOOGLE_API_KEY", "")

if not API_KEY:
    st.error("أضيفي GOOGLE_API_KEY في إعدادات Secrets لتفعيل المساعد الذكي.")
    st.stop()

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 3. إدارة الذاكرة (Session State) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 4. عرض المحادثة ---
st.title("🎓 مساعدك الذكي")
st.info("اسأليني عن أي معلومة، وإذا أردتِ صوراً اكتبي كلمة 'صور' في سؤالك.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "images" in message and message["images"]:
            cols = st.columns(len(message["images"]))
            for i, img_url in enumerate(message["images"]):
                cols[i].image(img_url, use_container_width=True)

# --- 5. استقبال المدخلات وتوليد الرد ---
if prompt := st.chat_input("بماذا يمكنني مساعدتك اليوم؟"):
    
    # 1. إضافة سؤال المستخدم للذاكرة والعرض
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. توليد رد المساعد
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        try:
            # تشغيل الرد بشكل متدفق (Streaming) للسرعة
            result = model.generate_content(prompt, stream=True)
            for chunk in result:
                full_response += chunk.text
                response_placeholder.markdown(full_response + "▌")
            response_placeholder.markdown(full_response)
            
            # 3. البحث عن الصور (اختياري بناءً على السؤال)
            found_images = []
            trigger_words = ["صورة", "صور", "image", "وريني"]
            if any(word in prompt.lower() for word in trigger_words):
                with st.status("🔍 جاري جلب الصور من الإنترنت...") as status:
                    # تنقية نص البحث
                    clean_query = prompt
                    for w in trigger_words: clean_query = clean_query.replace(w, "")
                    
                    with DDGS() as ddgs:
                        # تحويل النتائج لقائمة لأخذ أول 3 صور
                        search_results = list(ddgs.images(clean_query.strip(), max_results=3))
                        if search_results:
                            cols = st.columns(len(search_results))
                            for idx, res in enumerate(search_results):
                                img_url = res['image']
                                found_images.append(img_url)
                                cols[idx].image(img_url, use_container_width=True)
                        status.update(label="تم العثور على الصور!", state="complete")

            # 4. حفظ الرد النهائي مع الصور في الذاكرة
            st.session_state.messages.append({
                "role": "assistant", 
                "content": full_response, 
                "images": found_images
            })
            
        except Exception as e:
            st.error(f"خطأ: تأكدي من المفتاح أو اتصالك بالإنترنت. التفاصيل: {e}")