from pathlib import Path

import streamlit as st


ASSET_DIR = Path(__file__).resolve().parent.parent / "images"
st.set_page_config(page_title="TimeCraft | Historical Figures", layout="wide", page_icon="👤")

st.title("🏛️ Historical Figures Encyclopedia")
st.write("Explore people whose ideas, work, and leadership influenced history.")

historical_figures = [
    {
        "name": "Ibn Khaldun",
        "title": "Pioneer of social thought",
        "period": "14th century",
        "contributions": "His Muqaddimah developed influential ideas about society, state formation, and the writing of history.",
        "image": "https://www.aldiwan.net/public/images/cat_images/17510641891.png",
        "legacy": "His work continues to inform historical and sociological discussions.",
    },
    {
        "name": "Marie Curie",
        "title": "Pioneering physicist and chemist",
        "period": "Modern era",
        "contributions": "Her research on radioactivity led to the discovery of polonium and radium. She received Nobel Prizes in two scientific fields.",
        "image": str(ASSET_DIR / "portrait-marie-curie.jpg"),
        "legacy": "Her research helped establish new directions in physics, chemistry, and medical science.",
    },
    {
        "name": "Avicenna (Ibn Sina)",
        "title": "Physician and philosopher",
        "period": "Islamic Golden Age",
        "contributions": "His Canon of Medicine became an influential medical reference across the Middle East and Europe.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/7/7c/Avicenna_miniature.jpg",
        "legacy": "His writings connected medical practice with systematic observation and scholarship.",
    },
    {
        "name": "Albert Einstein",
        "title": "Theoretical physicist",
        "period": "Modern era",
        "contributions": "His work on relativity transformed modern physics. He received the 1921 Nobel Prize in Physics.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Albert_Einstein_Head.jpg",
        "legacy": "His theories continue to shape how scientists understand space, time, and gravity.",
    },
    {
        "name": "Saladin (Salah ad-Din)",
        "title": "Ruler and military leader",
        "period": "12th century",
        "contributions": "He founded the Ayyubid dynasty and led the recapture of Jerusalem in 1187.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Saladin_coin.jpg/320px-Saladin_coin.jpg",
        "legacy": "His leadership became an enduring subject in the histories of the medieval Middle East.",
    },
    {
        "name": "Abbas ibn Firnas",
        "title": "Inventor and scholar",
        "period": "9th-century al-Andalus",
        "contributions": "He is remembered in historical accounts for work in engineering, glassmaking, and experiments related to flight.",
        "image": "https://akhbarelsyaha.com/storage/2020/11/IMG-20201127-WA0013.jpg",
        "legacy": "Stories about his experiments remain part of the history of science in al-Andalus.",
    },
    {
        "name": "Leonardo da Vinci",
        "title": "Artist, engineer, and observer",
        "period": "Renaissance",
        "contributions": "His notebooks and works joined artistic practice with detailed study of anatomy, mechanics, and the natural world.",
        "image": str(ASSET_DIR / "portrait-leonardo-da-vinci.jpg"),
        "legacy": "His work is often cited as an example of Renaissance-era interdisciplinary inquiry.",
    },
    {
        "name": "Zenobia of Palmyra",
        "title": "Ruler of the Palmyrene Empire",
        "period": "3rd century CE",
        "contributions": "She ruled Palmyra and expanded its influence during a period of political instability in the Roman Empire.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Zenobia_coin.jpg/320px-Zenobia_coin.jpg",
        "legacy": "Her reign is an important case study in the political history of the Roman East.",
    },
]

query = st.text_input("Search by name", placeholder="For example: Marie Curie")
filtered_figures = [
    figure for figure in historical_figures if query.casefold() in figure["name"].casefold()
]

if not filtered_figures:
    st.warning("No figures match that search. Try another name.")
else:
    columns = st.columns(3)
    for index, figure in enumerate(filtered_figures):
        with columns[index % 3], st.container(border=True):
            st.image(figure["image"], width="stretch")
            st.subheader(figure["name"])
            st.caption(f"{figure['title']} · {figure['period']}")
            st.write(figure["legacy"])
            with st.expander("Read more"):
                st.write(figure["contributions"])
            st.feedback("stars", key=f"rating_{index}")

st.divider()
st.caption("This introductory encyclopedia is a starting point for further research, not a source-cited reference work.")
