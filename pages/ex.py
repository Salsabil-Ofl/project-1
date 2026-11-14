from pathlib import Path

import streamlit as st


IMAGE_DIR = Path(__file__).resolve().parent.parent / "images"
st.set_page_config(page_title="TimeCraft | Historical Events", layout="wide", page_icon="📜")

st.title("📜 Historical Events Archive")
st.write("Explore selected events and moments that shaped the course of history.")

section = st.sidebar.radio(
    "Choose a collection",
    ["Overview", "Early Islamic history", "World War I"],
)

if section == "Overview":
    st.subheader("Start exploring")
    st.write(
        "This page presents a small selection of historical topics. The summaries are introductory "
        "and are not a substitute for source-based historical research. Choose a collection from the sidebar."
    )
    st.info("Featured collections: early Islamic history and World War I.")

elif section == "Early Islamic history":
    st.header("The Conquest of Mecca")
    image_column, text_column = st.columns([1, 2], vertical_alignment="center")
    with image_column:
        st.image(str(IMAGE_DIR / "m.jpg"), caption="An artistic depiction of Mecca")
    with text_column:
        st.markdown("### A turning point in 630 CE")
        st.write(
            "The entry of the Muslim community into Mecca in 630 CE was a major turning point "
            "in the early history of Islam. This overview highlights the event's historical context "
            "and its place in the growth of the early Muslim community."
        )
        st.info("For academic or religious study, consult primary sources and specialist scholarship.")

elif section == "World War I":
    st.header("The First Battle of the Marne")
    image_column, text_column = st.columns([1, 2], vertical_alignment="center")
    with image_column:
        st.image(str(IMAGE_DIR / "m1.jpg"), caption="Paris taxis helped move French troops in 1914")
    with text_column:
        st.markdown("### September 1914")
        st.write(
            "The First Battle of the Marne halted the German advance toward Paris and helped "
            "shape the Western Front. The battle is remembered for its strategic consequences "
            "and the transition to prolonged trench warfare."
        )
        st.markdown(
            "- French and British forces counterattacked German troops.\n"
            "- Paris taxis were used to transport soldiers to the front.\n"
            "- The German advance was stopped east of Paris."
        )

st.divider()
st.caption("TimeCraft history content is introductory. Check reliable sources for dates and interpretation.")
