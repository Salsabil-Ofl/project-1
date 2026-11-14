from pathlib import Path

import folium
import streamlit as st
from streamlit_folium import st_folium


IMAGE_DIR = Path(__file__).resolve().parent.parent / "images"

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0c0c0c 0%, #1a120b 55%, #2d1b0f 100%);
    }
    .timecraft-title {
        background: linear-gradient(45deg, #d4af37, #f4e4bc, #d4af37);
        background-clip: text;
        color: transparent;
        font-size: clamp(2.5rem, 6vw, 5rem);
        font-weight: 800;
        text-align: center;
        margin-bottom: 0;
    }
    .timecraft-subtitle {
        color: #e2d1ad;
        text-align: center;
        font-size: 1.2rem;
        margin-top: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<h1 class="timecraft-title">Welcome to TimeCraft</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="timecraft-subtitle">Explore the turning points, people, and ideas that shaped our world.</p>',
    unsafe_allow_html=True,
)
st.divider()

st.subheader("Explore the past")
feature_columns = st.columns(4)
features = [
    ("📜", "Historical events", "Discover selected moments from different eras."),
    ("👤", "Remarkable people", "Browse a short encyclopedia of historical figures."),
    ("🕰️", "Alternative history", "Explore educational “what if?” scenarios."),
    ("🌐", "World updates", "Read current international headlines from BBC News."),
]
for column, (icon, title, detail) in zip(feature_columns, features):
    with column, st.container(border=True):
        st.markdown(f"### {icon} {title}")
        st.write(detail)

st.divider()
intro_column, image_column = st.columns([1.4, 1], vertical_alignment="center")
with intro_column:
    st.header("The time portal is open")
    st.write(
        "Choose an era, explore a historical event, and consider how a different decision "
        "might have changed the course of history. TimeCraft is an educational prototype "
        "built for curious learners."
    )
    button_columns = st.columns(2)
    with button_columns[0]:
        if st.button("Start exploring", type="primary", width="stretch"):
            st.switch_page("pages/chatbot.py")
    with button_columns[1]:
        if st.button("Browse historical events", width="stretch"):
            st.switch_page("pages/ex.py")
with image_column:
    st.image(
        str(IMAGE_DIR / "timecraft-hero.jpg"),
        caption="Every journey through history begins with a question.",
        width="stretch",
    )

st.divider()
st.subheader("Featured eras")
era_columns = st.columns(4)
featured_eras = [
    "The French Revolution",
    "World War II",
    "The Age of Discovery",
    "The Industrial Revolution",
]
for column, era in zip(era_columns, featured_eras):
    with column:
        if st.button(era, width="stretch"):
            st.switch_page("pages/chatbot.py")

st.divider()
st.subheader("Historical places on the map")
st.write("Select a marker to see a short introduction to the event.")

historical_events = [
    {
        "name": "Cairo, Egypt",
        "location": [30.0444, 31.2357],
        "title": "Egyptian Revolution of 1952",
        "summary": "The Free Officers Movement ended the monarchy and led to the establishment of a republic.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Egypt_1952_Revolution.jpg/300px-Egypt_1952_Revolution.jpg",
    },
    {
        "name": "Paris, France",
        "location": [48.8566, 2.3522],
        "title": "French Revolution",
        "summary": "The storming of the Bastille in 1789 became a defining symbol of the French Revolution.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Prise_de_la_Bastille.jpg/300px-Prise_de_la_Bastille.jpg",
    },
]
map_column, details_column = st.columns([2, 1])
with map_column:
    historical_map = folium.Map(location=[25, 15], zoom_start=2, tiles="OpenStreetMap")
    for event in historical_events:
        folium.Marker(
            location=event["location"],
            popup=event["title"],
            tooltip=event["name"],
            icon=folium.Icon(color="orange", icon="book", prefix="fa"),
        ).add_to(historical_map)
    map_data = st_folium(historical_map, width=800, height=450)

with details_column:
    st.markdown("### Event details")
    clicked_title = (map_data or {}).get("last_object_clicked_popup")
    event_data = next((event for event in historical_events if event["title"] == clicked_title), None)
    if event_data:
        st.markdown(f"#### {event_data['title']}")
        st.write(event_data["summary"])
        st.image(event_data["image"], width="stretch")
    else:
        st.info("Choose a marker on the map to view an event.")

st.divider()
st.caption("TimeCraft is an educational prototype. Verify historical details with reliable sources.")
