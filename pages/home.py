import streamlit as st
import time
import numpy as np
from streamlit_folium import st_folium
import folium

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0c0c0c 0%, #1a120b 50%, #2d1b0f 100%);
        color: #e2d1ad;
    }
    </style>
""", unsafe_allow_html=True)

# --- الشريط الجانبي ---


# --- العنوان الرئيسي مع تأثير لمعان ---
st.title("")
st.markdown(
    """
    <h1 style='
        font-size: 5rem; 
        background: linear-gradient(45deg, #d4af37, #f4e4bc, #d4af37); 
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        text-shadow: 0 0 30px rgba(212, 175, 55, 0.5);
        font-weight: 700;
        margin-bottom: 0;
        animation: glow 3s ease-in-out infinite alternate;
        font-family: Arial, sans-serif;
    '>Welcome to TimeCraft</h1>
    """, 
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    @keyframes glow {
        from { filter: drop-shadow(0 0 20px #d4af37); }
        to { filter: drop-shadow(0 0 30px #d4af37); }
    }
    </style>
    """, 
    unsafe_allow_html=True
)

st.markdown("### **محاكي الأحداث التاريخية - اكتشف أسرار الماضي وأعد كتابة التاريخ**", text_alignment='center')
st.markdown("---")

# شريط تقدم ترحيبي
progress_bar = st.progress(0)
status_text = st.empty()
for i in range(100):
    progress_bar.progress(i + 1)
    status_text.text(f'جاري تحميل بوابة الزمن... {i+1}%')
    time.sleep(0.03)
status_text.text('✅ جاهز للسفر عبر الزمن!')
time.sleep(1)
progress_bar.empty()
status_text.empty()

# --- الميزات الرئيسية ---
st.markdown("## 🎯 **الميزات الرئيسية**" , text_alignment="right")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style='
        background: rgba(255, 250, 240, 0.1);
        padding: 2rem;
        border-radius: 20px;
        border: 2px solid #d4af37;
        text-align: center;
        height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    '>
        <h1 style='color:#d4af37; font-size: 3rem;'>+50</h1>
        <h3 style='color:#f4e4bc;'>أحداث كبرى</h3>
        <p style='color:#b8a88e; font-size: 2rem;'></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='
        background: rgba(255, 250, 240, 0.1);
        padding: 2rem;
        border-radius: 20px;
        border: 2px solid #d4af37;
        text-align: center;
        height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    '>
        <h1 style='color:#d4af37; font-size: 3rem;'>100+</h1>
        <h3 style='color:#f4e4bc;'>مسارات بديلة</h3>
        <p style='color:#b8a88e; font-size: 2rem;'></p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style='
        background: rgba(255, 250, 240, 0.1);
        padding: 2rem;
        border-radius: 20px;
        border: 2px solid #d4af37;
        text-align: center;
        height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    '>
        <h1 style='color:#d4af37; font-size: 2.5rem;'>تحليل AI</h1>
        <h3 style='color:#f4e4bc;'>عميق</h3>
        <p style='color:#b8a88e; font-size: 2rem;'></p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style='
        background: rgba(255, 250, 240, 0.1);
        padding: 2rem;
        border-radius: 20px;
        border: 2px solid #d4af37;
        text-align: center;
        height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    '>
        <h1 style='color:#d4af37; font-size: 2.5rem;'>دعم كامل</h1>
        <h3 style='color:#f4e4bc;'>24/7</h3>
        <p style='color:#b8a88e; font-size: 2rem;'></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- القسم التفاعلي ---
col_text, col_image = st.columns([1.5, 1])

with col_text:
    st.markdown("## 📜 **بوابة الزمن مفتوحة**")
    
    st.markdown("""
    **TimeCraft** ينقلك إلى قلب التاريخ لتعيش القرارات العظيمة. 
    
    🔮 **هل كنت ستُغيّر مصير روما؟**  
    🏰 **أم تُنقذ الأندلس من السقوط؟**
    
    ✨ **اختر عصرك | خذ قراراتك | شاهد التاريخ الجديد**
    """)
    
    col_btn1, col_btn2 = st.columns(2)
    
    with col_btn1:
        if st.button("🚀 **ابدأ الآن**", type="primary", use_container_width=True):
            st.balloons()
            st.success("⏳ **البوابة الزمنية مفتوحة! استعد للرحلة...**")
            
        
    
    with col_btn2:
        if st.button("📚 **اكتشف التغيرات التاريخية**", use_container_width=True):
           st.switch_page("pages/ex.py")
        st.info("🗺️ **العصور القادمة:** الثوره الفرنسية | الحرب العالميه الثانيه | اكتشاف امريكا | الثورة الصناعية")

with col_image:
    st.markdown("""
    <div style='
        text-align: center;
        animation: float 6s ease-in-out infinite;
    '>
        <img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxIQEhUQEBIVFRUQFRUWFRYVFRAQEBUVFRUWFhUVFRUYHSggGBolHRUVITEhJSkrLi4uFx8zODMsNygtLisBCgoKDg0OGhAQGi8eHyUtLS0tLS0rLS0rLS0tLSstLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSstLS0tLS0tLS0tN//AABEIAPkAywMBIgACEQEDEQH/xAAcAAABBQEBAQAAAAAAAAAAAAABAAIDBAUGBwj/xAA+EAABAwIEAwUFBQgBBQEAAAABAAIRAyEEBRIxQVFhBhMicYEykaGxwUJSYuHwBxQjM3KC0fGSQ1OissI0/8QAGQEAAwEBAQAAAAAAAAAAAAAAAAIDAQQF/8QAJREAAgICAgICAgMBAAAAAAAAAAECEQMhEjEEQSIyE1EUQoEF/9oADAMBAAIRAxEAPwDyVpsjKDdgkmAMpIIrQEnIQnBACRSCKAEEUQEYQA2EUUEAJJFCEAJAohIoACCSULQEnIIhACSToQAWABFIpIAQclKaQktAgbsEkm7IrAEkkkgByISSCACiEITwEAFEhI9LlLEUyIkfoz/hZyQ3F9jS9N1oCkbdbKxTwk7zPAAT8ljkkaoN9EYIQIVs5ZU0h3dmI3CohhFovPxWRmn0bLG12ORKLDO6MJ7EoYiAjpT4hBg0NRhOlCUABJGE0lACKaUU0rQAigUNSDCJuyKI2SWGiSCMJIAIRQCKACE/ZNaFcwFLXUY2NyEs3SseEbdG/knZkva15s4nlMSDc+sLJzjLq1CqadUQRcGZaRwcDx3XrOSYYMAlbdbI8NiW6a1MPAuCZ1NPNrtwvNhllytnoSxrjR8/d29hkja4niN5HMf5Xo3Y/K6VeKtTDFjolrjdruo5LscN2KwlN7S3vA1pkM1nRPOF0b6YA8IgJsknNCwXHRw+c5Y1rSABfpZedZrgdJ2HiIAcTAbFyTxIt8l6n2iqTZefdp2TTgAk8hAHqeSjD4z0Um7Rwz+J5k+5S09lG9sWPBOongvWR5kuyUlIowiWpjBoCAToTUAJyYU8oQgwaknQhC0BkIQnwlpWAQN2RQbsiEAFJJFABARhIIwgAtC0MhbOJpf1fQqg0LV7P1AyvTe77LvmI+qnl+rKY/sj17ANIAkLo8MBpXnOKzdxaSK7aYbuXA6RG4tJKm7N57Xc/S57KlPVpL6ZJ0n8TSAQvKi6XR6j3o9IaWjdGvimBt3ADzC5rtdiHU6YbSnW+dlxLMtrtY/EVzUqNp+01mklu2+s734Cyfl6QnFds7bMWNqSWkHlBBXD5lhyS4FEZk9wmkyoy+kCqGtk9CNvUBXW4eo4A1OX6lQk3Y2jzHF0yx7mu4EqOhvZbObUh+8mRIFyOcJuY6nDvKka9WmANMCJ26bL1MeW6RxTw9yKICMoBJdBAaU2EYSWijUiikgwRCUJwCOlADdKWlSAJQg0z28E5NbsE5BgUQEmpwCAFCcAlCcAg2gtarmDHiHmqzQrWGs4Kc3pjx7PW8BlDD4gxumo0h4gwQTsYW1h8oo4dkspsbHsgA7kATdZPZnMPA0dAt/Mn6qczEEfEheXHqj1OPTMnP2lzqengJ+P5LdwbQ9pOxO4EBYWaEtc0gj2Zk8hZXcpzIGmHc5+BI+iW/kNKOtBq5Aw1BUdJ03Em3oFi9p8W1oIC1syzO1iuB7QYgv2KRu9AotLZz2Kw5rE6QS98Bp2AAkuc47ARzUGf1KbntFN5fpY1peZlxEyb+ceiko4zui5zrgtIjh0nmsprtXi5k+i7cEXe/Rz55fChsIFOITQu5HAMShPhOhbZlEQaiAnaU5oWhQ1rU6EQEYWAANT4SDVJpQBjN2CcAg3gpAFoomhOhODU5rUDDQE8BO0pwalbNSE0KWnYpoClY1Kxkjtuy2JJaADcWXcNqU3U9NSSXRYEgyLggry7IMZ3bxyK7itgWVxrOs2sGucyDzsvLyLjJno4p3FJlDG5A7E1nGrUcKVMW8WmZ2BC2DmVChTFGWgNEN/2s9uTvI0tYwtHB73kTz0C09VZw2S0WGX0aRJ3Ja0+61klnRJKuyPF1g8eHguZxd5810uKp06c6LTw4BctmNYDZTrZKUmYGYU9UtHH3DmT0CzaDoP4eH0K0Mw8MsPtOjVzaN9J6mx6LKc7h1Xo4rolKK7ZaqNUcJ9N82RhdKkcM4OLGAIwnwitsUjhIBPhEMWpmDEQE/QnBiYBrWqXQU5jU8FAGC0WClaEKYspgEGIGlSNakApWtWNjIWhO0qVrFJoU2x6K4YpGhOLVHqWWaT03Qus7N59qGhxgt3XGsqJVH6SHDyUc2NSRbC90epv7QtYIBEKDG5y1zZndecnEO0uqNIc2k0OcCdLg2Q2Qdjdw5KV7a7Rqq93SkAgVKhc+CJB7un4vfC5fwy/Z0ynT4+zfxeYF/hbJ4na3UngPNZ2IxDaLQ+Q6o69MRLQP8AuGdxy58JF1lVMyIGlp1/1NFOjPMUgZeeryfJOy/LcRiSXNY55cZc9xtPNziqLCkENu30Z9cm+97km5JO5JQOCqNaKj2EMdOhxEBx46ea9E7O9j2s/iVgKjuFvA3yB9o9SsT9pjX061JzgdBpwzgA4OOqesQuiKfROeWLlf6OTpsdMNEucTAkCwvMnZWmNJ3jzBlt+q0OyGXNxPeS5veWEEgEU4lxaN7m3SOq1DkT3+GnZjZ4eITvfhJ4FRyeQscuLF4rKrXRz7sM6CYsN4IIHnBUcLp8RXpMJHdl5uCWABnIt1OBkKmzK21fEyWDkQ58GNpaD0sjH5af20JPx2vqY7acJ5atSrlRb/1GHy1D6JlbAOYNVi3iRcT6roj5GOTpMjLFNbozg1Pa26mFNHSrokRtajCdpTtK0wwqbdlIEGCwU1Nqxs2KDTZKnY1JrVMwKbZVITWoohRVSlNG1HKzgst7yS4loAmwk7jf7ovxU+TZeazrDVGzZAk73J2aOJXUdn6LDUqseRUDmEWEUjcamNm7uc9FzZc3y4RK48drkznRg6TbAA9dQJ90rby3L6Zpd29ktqDxfevcGeBFluU+y9IUn1HOJDWktZDQ2RtMC91LlVBoZqIsATdZihJfZjSa/qcnW7KvbOhzarXtLHD2Kul3Pg4gweGyjxvYzF1Kr3mnd7yY10vCCbA3tAhegZXS1w4jd0+jBYf8iPctnDYXVvzVeCG/kS7as8+yn9nQEOrvkC5bT49C8/QLvMDlDRTaxjQ0AbAQ0eQWvTw4IgDzVljNI0tTJJEsmWU+yg3L2tELE7W5WKuGew0m1YggEajYyS38XJdaygBcqLEAJpW1Vk09nmfYrJaH8QjC0iaRAbU7sB7jBJbqdxEC/VcnkXa2tVfVp4hoaSKjwI0lpG9I8TF44iOK927qGryjt3icmL3FxJxAMF2HkP66nDwExzupPCpQ4y2/2a8lStaOPa1xmXm0DeCN9vUJ76paYEw0nZzhO5Gq+9/kq9Gu17S4Elp3n22wfaMbq41rHfwnkNe3U0ulsFpHhM8b2tw32XK009o7FJNWR1K9V3t1nm1tRJvIiRHL5qOliH1CGPLiLgCbeTh+amxGH1ND22BaZFyGubAInkeH5KDDUHA6juG6/wAJjS4E+8j1RqrN2WnUuHzi3RRuatPHV2d4+AQ0uY++w7wEER7vcs6qLldXi5JNVI4/Igk7REiknLtOYwqZsrNIKCkPkFapNhJIeKJBwUjUAE4NspsoFV6yswq9VYuwZoYTHinTFKYa7x1YOkuANmzwGwjzKrntO6nWp1gBDHSWiw7uC0t/4kwFg4itu3kYBvYcuqrO2Pklh4yvkwl5Drij33GVv4IaD/MIjlG8/L3qvWdLQwbJmrwUaXGnTaDwvpA+itUqZWFCxkTpeWfdptI9Xun5BdVhqdrLAy3BBr+8m5pgdPaJXQYcWC0SRZaI2Tmt4pzQigRsY8qAUpOpythi8o/bF2z7sHLcO7xuA/eHD7LTcUgfvHjyBjinirFcjnv2kftDfinuwuEeW4dhhz2ktdWIsbi4p/OOW/nQ6JJK6ikSbscHkbFDWZlBAopBZK3EuGx+nVTNzF42O4g8t593RU0krxxfoZZJL2bGBxRqODDtLXOm5hvXl0WzXqzsuRoVSxwcOC6VlQOAcNiEqxqL0O8jktkiRQSVBTKoCw9FcaFVoDZXWNUpMrFD6LJKfUJVim0WKZUU7KURNChxFO0hWXKrjSRTcRuAfzWLsxrRzsytrsdl4r4pofdlIGq8cCGRAPm4t+KxF1fYsFuoACcQWsFiXaR4rcgTx6K+SXGJzY48pHpeWgvBqHd5n/Cu136W9TYJ+Dptp0wTwsqdQmq6+wv6BR6R1G/lp1AngXQPIQPotygLLJyvD6Wgcd/U3WwCAEMRk8owsjtBmwwtB1X7Qs0G8n8hJ9F5fW7UYrEO01KxLHAlzWCGgAwPZvuQVLJkUCuLxJ5YuS0j13N8wbhqFTEP9mjTc8/2iY9dvVfKWMxT69R9aoZfWc57uPicZMe+F6rnGYO/cxhqVUkVq7nbvENomNB1QQHPHrp6rLyjsmzFP70aWlg16TaYmxuOIiVXDk1dHPPFTas88xOHdTIDty0O9Dsol32N7L6/G9pOmGCHRZkNAnb7JM8mvK4nE4QtqOpiTG1tJIiQY4eqtDKnonKDiV0EklQQSBRQQAFr5JXmaZ4XH1WQpsJW0Pa7gDfyO6GajpUU5zI68o2IRCUYzaHBXaYSw+HsFZ7qAoSZ0RGg2Qc5EhRuSjDieap5s7TSMfage9WZWbnVYBop8Tc9B+pWxVsyb+Jl4agaj2sbu8gD1XruR4VjXDSANDQBAEwLATyXmPZ4EVQ8RLASJuJIgL1DA7SOI63TZJXLiTxRqPI3atXVbgEyjsY3c8N/tHiKZQECVNgTJbPGXD1MD5LGUOkoVNlcadUKhh2rSw4ELRWY3bTKX4nDaaQBdTcHgHjAIIHW68pDHOMNp3ad2OazS2IAkkEXabL2jPcb3NCo6Wg6XRqeKd9NoPPovKXsqOD3VS2DqYZFnPLLucAQ5xAaNzf1XF5CVpnd4mdqDg+uzmziBUquDJAkAg6piCSbmxJd+pM9hkVc+EaWtZeXaQdxJc6SCbSb8t5ssDPKDaWPxAIgGs5pA8IDSfDxsIH64XcPiv4JBhj2kt1Xux4gHnp8XqBzVkq0jlb5bNfG5lBeO7bZ2nXTgUqgJs7TcSQ22/ukLjs/wVSHimBNSCxo8Ac1/tPDj7bzBFzNzC6zDYhpw3dNpkBjRLtDg2A5xnUR4vDeel+Cwu0NDuabWAvlzIg+McDDeIEmwsi6kY1aPPHsLSQQQRuCIIPUJqfUqF13GTEX3jkmrvRxsCCKCDAJJJIA6HIcWXsNM/YuD+E8PT6rS0LH7N0/bd5D6rc0pRuxUhACe8KOi6wlTltlzM6Ss5vNROClcVC9aAwgDfhcrmq9UvcXH7R/0FsZxiNLdI3fI9OKw1bGq2Syyt0dr2MwbRT1uaC55kEgEgbCJXcYOnxXKZJamAB7IA9YH+V1OAqRYqKkm7KqLSou4ypDIHH5K3ljZdJ+wxrfXf6rIx+LaAXOMNZc9eg6q72Wxza+GdWBuXbcr7H0+Sy7Y1aOkpVIV6lWWJQBdsrrGvbwTGMu5hg2Ylnd1NpDhZjocNjD2kGN7heY4/IMeyq6k1riw1YpuDIbpL2kRpBDWCBY8AV6NSxZG4WX2nz+thw3uQ3xAklwJG8RupZeKVyNgndI4HtkwNzLEsILhNKpvEk02gGBxnj5rEdjXlxaC06XECZnlIMGLmPRa/7Q3PFSjmQbpGLoCm7iG1aZcR72kkeS8/wuYvYZmbyDNwd5B81RQ5q0T58XTO/pY+rUHdVTDY2BiZmNZAFvCeHASSFi9rnkgFlXXLRqBJDg77RiAHfE9SueoZk/WXFx8QAN+W0n0hZ5TRwu7bMllVUFAopFdBzgQSSQAkEQggDqcgogUQ4buJJ85iPgtDR1VTs2JoD+p3z/ANrRJWDI5qhUIgnh5rVp4+2nSSRxnnzUAw4IHkFK2nGy53TOhXQ3WXGTbooXuk24bngrAaqeYhrabibFwgdTN/gj2HqzIx2I7x5cNth5c/VV0kl0JaOZvdnpGR0W6Glty+DJibgWHRbL6oYC5xgDcrB7JPmix33Wx7iQnZpVOJrswdPYkd4ecn2fJcdU2kdadqyHP61Ss1j9JbQcSGcNZ+8eQN/OFb7C5n3OINFx8FYf+X6j3ld9isrpVaHclktIAEWLY2LV5dnGW1MLVg2c0hzHbBwvBCSVxlZ6OFQy4nBfZHrJZod0WlQxAIXO5HmbcXh2vBvxHEOG4KvMfpV0ec1RuU3N6KDHU6NT+ZTY/wDqANhw+JVBmJTX1UNWYiv2py1uOwlTCABpcAaRiAyoy7I5Dh5Er54qUy0lrgWuaSHA7ggwQeoK90zvPP3ZuoNLiTYTpAA3J5rzrt9gRUIzGiIZXtWbxZVFtR6OAF+fmmx5I3xEyY3XI45BFBXOcKBSCRQAkEUkABAopIA9AyTB6aFMfhk+Zv8AVT930+CXZdxqYWmd9I0+rbf4WkMOf0QpXspRwuELnAEmZ4SVotas3Amw8gr4f1U32VXQarg0SeS5jGYg1Hlx2+yOQ4LQzjEGA2faufILJVca9k5v0BTMwzzw+iu4DDADW4STsOX5rSo0ydhJOwif1+ajk8inSO/B/wA/lHnkdIuZJmIoUWsc06r8o3K6PsJlTnPfian3toMzHhAn096tdlshDWy4AvdcncjoOQXXU8MabQ2mASTMEkAnmbHopRbk2xckccVUSWjhQCWESAIhznvjp4iUzPslbiqWiAHs/luiwMRB6FXsFhngS9zSTuQCI6XJlX6ZaOIVXFNUTjkcJcl2eNZTjamW4gtqghrjFVvI7B/yv5L0trm1Gh7bgiQQq3bfs4zFMNSmB3rRHD+I37p68lyPYjOjTP7nVJi+gncfhM8fyU4vi+LOnMllj+WP+o7MBPp0S48lHriyRxEKxxkeaZRRqNipqMbQQIPPb0WLmGDpCmcOGzTcCHNN5neTz/XBatfEErJzJxFN7h7QAjbcnh13U3S2bt6PJc+yl2Fqlhksdem77zevUbFZpXo7MGcXTqUq86Ww5rzcsf8AhPkbhcDmWBfh6jqT928Rs4HZw6FXxZeaIZcfBlYJJBJVJCSSSQAEkkCgDsuxeYNZScxzS4h5c25DbtH1C3jnrhYMpgf0yuK7PvhrvP6LVMqElsonoxqVTTtsIn3K02sIn/ajbRGkQBEdVJTwrTw9yRyLJGVmVTU/yAH1+qkyvLzWJuAG7z9FXxrdL3DqruUYkMBk2MTysZ9/D1VJtqGicFc9naZHhsIym6tVIqClvxYOAAadydr81m5K41KzXVABq1PIEAeEwBAsBJdboFRd4KApAzNTW4iY0hoDfifimZbU01QbgFsRMxsd1xRXZ6cpSlA9TyzEgSdloYbGWDjaesQFw9DMRpIB4f4CuNxwdUkhpAAiQHfNNi0jmyO6O5biJ478roOrQudo5wxokNaCOIAHyTqeeAm6tzROjfGKPVcP23yYyMVR8Mka4+y/g/yOxW8/MgdionYoPaWOEtcII5goaUkUxZPxyv0N7N5uMVSh1qtPwvE38+qs13EFcFimVcDWFakSY91Rk7HqP1uu6yzH08ZTFSmfMcQUQdqmGbHxdrp9AlEOhFzCDCY/dNRGyhmT5hvNcf2moMr/AMNv8yn7JtBndhP6uuxxLJIXM9oKOHw7i+rVlxOoUmDxkngXTYW5JG5KXxNpNfI8/c0gwRBG4NiCgrWZ4016hqFobPAbevMqquw5BJJIIASRSSKANvs42Q7z+gXQDRxPxC5nIXXcFslqlNbHiUBSsL3sp6QPA7KAbqwNlzs6kY+b0wHAjfY/RV8O6xBMeasZxx9FksXRHcTnupm+zMIbpAMadMnzmU2m4kSDB4HjKyWq5h9lzzgo9Hp4JWqZt5LVL3VGk30j/wBr/NbDCRy+K57I/wCcf6T82rpuHuSs5sipjxq4H5qxTKrUlYpbpaEssU3HYK4x5CgwyneniYQ42i2qzQ6ehG4PNcrSr1sDW1U/NzfsvHMdV1qwe0O1P+76LZa2Wwu3wfTOwynOKeMp66Z8XEcQUsTVDfaIHmuB7Afzn+f/AMrc/aB/+d/knsizNz/ti1ksw0Odtr3a3y5rhq9Zz3F7yXOduTclU0V0Rikczk2TlJV05MYTJKBJBhMkoUkAamUVNL/NbXfDmuay72lqOU5djI//2Q==" 
             style='
                width: 100%; 
                max-width: 320px;
                border-radius: 25px;
                box-shadow: 0 0 30px rgba(212, 175, 55, 0.6);
             '>
        <p style='
            color:#d4af37; 
            margin-top:15px; 
            font-style:italic; 
            font-size:1.3rem;
            text-shadow: 0 0 10px rgba(212, 175, 55, 0.5);
        '>
            ✨"العظمة تبدأ بقرار واحد "✨
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<style>
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
}
</style>
""", unsafe_allow_html=True)

# --- العصور التاريخية ---
st.markdown("---")
st.markdown("## 🏛️ **العصور المتاحة**", text_alignment='right')

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("👑 **الثورة الفرنسية**", use_container_width=True):
        st.switch_page("pages/chatbot.py")

with col2:
    if st.button("🛡️ **الحرب العالمية الثانية**", use_container_width=True):
       st.switch_page("pages/chatbot.py")

with col3:
    if st.button(" 🌍 **إكتشاف أمريكا**", use_container_width=True):
        st.switch_page("pages/chatbot.py")
with col4:
    if st.button(" 🕒 **الثورة الصناعية**", use_container_width=True):
        st.switch_page("pages/chatbot.py")
        

# --- الخريطة ---
st.markdown("---")
st.markdown("### 🗺️ **خريطة العالم القديم التفاعلية**")


historical_events = [
    {
        "name": "القاهرة - مصر",
        "location": [30.0444, 31.2357],
        "title": "ثورة يوليو 1952",
        "info": "قامت الثورة بقيادة الضباط الأحرار وغيرت نظام الحكم من ملكي إلى جمهوري.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Egypt_1952_Revolution.jpg/300px-Egypt_1952_Revolution.jpg"
    },
    {
        "name": "باريس - فرنسا",
        "location": [48.8566, 2.3522],
        "title": "الثورة الفرنسية",
        "info": "سقوط سجن الباستيل وبداية عهد جديد من الديمقراطية في أوروبا عام 1789.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Prise_de_la_Bastille.jpg/300px-Prise_de_la_Bastille.jpg"
    }
]


st.write("اضغط على الدبوس الذهبي لاستكشاف ما حدث في هذا المكان")

# تقسيم الصفحة لعمودين
col_map, col_details = st.columns([2, 1])

with col_map:
    # 1. إنشاء الخريطة الأساسية بتصميم أثري (Toner أو Terrain)
    m = folium.Map(location=[20, 10], zoom_start=2, tiles="CartoDB positron")

    # 2. إضافة الدبابيس (Markers)
    for event in historical_events:
        folium.Marker(
            location=event["location"],
            popup=event["title"],
            tooltip=event["name"],
            icon=folium.Icon(color="orange", icon="history", prefix="fa")
        ).add_to(m)

    # 3. عرض الخريطة وجعلها تتفاعل مع Streamlit
    # الـ return_on_hover أو الـ Click سيعطينا بيانات النقطة المختارة
    map_data = st_folium(m, width=800, height=500)

with col_details:
    st.subheader("📜 تفاصيل الحدث")
    
    # التحقق إذا كان المستخدم ضغط على دبوس معين
    if map_data and map_data.get("last_object_clicked_popup"):
        clicked_title = map_data["last_object_clicked_popup"]
        
        # البحث عن بيانات الحدث الذي تم الضغط عليه
        event_data = next((e for e in historical_events if e["title"] == clicked_title), None)
        
        if event_data:
            st.markdown(f"### {event_data['title']}")
            st.image(event_data["image"], use_column_width=True)
            st.write(event_data["info"])
            if st.button("اقرأ المزيد عن هذا الحدث"):
                st.write("سيتم توجيهك لصفحة التفاصيل العميقة...")
        else:
            st.info("اضغط على أي أيقونة في الخريطة لرؤية التفاصيل.")
    else:
        st.info("في انتظار اختيارك لمكان على الخريطة...")

# --- إضافة لمسة جمالية (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #fdf5e6; }
    h1 { color: #5d4037; font-family: 'Amiri', serif; }
    </style>
    """, unsafe_allow_html=True)

# --- الفوتر ---
st.markdown("---")
st.markdown("""
<div style='
    text-align:center; 
    padding:3rem 2rem; 
    background:rgba(0,0,0,0.8); 
    border-radius:20px; 
    border:3px solid #d4af37;
    margin-top: 3rem;
'>
    <h2 style='color:#d4af37; margin-bottom:1rem;'>⏳ TimeCraft - أعد كتابة التاريخ</h2>
    <p style='color:#b8a88e; font-size:1.2rem;'>
        © 2024 | جميع الحقوق محفوظة | بوابة الزمن مفتوحة دائماً ✨
    </p>
</div>
""", unsafe_allow_html=True)

# إضافة مؤثرات بصرية خفيفة
st.markdown("""
<style>
.stButton > button {
    border-radius: 50px !important;
    font-weight: bold !important;
    box-shadow: 0 8px 25px rgba(212, 175, 55, 0.4) !important;
    transition: all 0.3s ease !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 12px 35px rgba(212, 175, 55, 0.6) !important;
}
</style>
""", unsafe_allow_html=True)

# رسالة ترحيبية في الأسفل
st.markdown("---")
st.caption("🌟 شكراً لزيارتك | جاهز للسفر عبر الزمن؟")