import streamlit as st

st.set_page_config(page_title="TimeCraft | What If? Scenarios", layout="wide", page_icon="🕰️")

st.title("🕰️ The Time Portal")
st.write("Choose a historical turning point and explore an educational alternative-history prompt.")

scenarios = {
    "French Revolution (1789)": {
        "year": "1789",
        "place": "Paris, France",
        "summary": "The French Revolution challenged the monarchy and transformed political life in France and beyond.",
        "question": "How might European politics have developed if the revolutionary movement had ended earlier?",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Jacques_Bertaux_-_Prise_du_palais_des_Tuileries_-_1793.jpg/800px-Jacques_Bertaux_-_Prise_du_palais_des_Tuileries_-_1793.jpg",
    },
    "World War II (1939)": {
        "year": "1939–1945",
        "place": "Global conflict",
        "summary": "World War II involved countries across the world and reshaped international institutions and borders.",
        "question": "Which post-war developments might have changed if the conflict had ended sooner?",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/World_War_II_Montage.PNG/800px-World_War_II_Montage.PNG",
    },
    "The Age of Discovery (1492)": {
        "year": "1492",
        "place": "Atlantic Ocean and the Americas",
        "summary": "The voyages across the Atlantic initiated sustained contact between Europe and the Americas, with profound consequences for Indigenous societies.",
        "question": "How could the histories of the Americas have changed if these voyages had been delayed?",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Columbus_Taking_Possession.jpg/800px-Columbus_Taking_Possession.jpg",
    },
    "The Industrial Revolution (c. 1760 onward)": {
        "year": "c. 1760 onward",
        "place": "Britain, then many regions",
        "summary": "Industrialization changed production, transport, cities, and labor across generations.",
        "question": "How might societies have developed if mechanized production had spread more slowly?",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Powerloom_weaving_in_1835.jpg/800px-Powerloom_weaving_in_1835.jpg",
    },
    "The Islamic Golden Age": {
        "year": "Approximately 8th–13th centuries",
        "place": "A network of cities across the Islamic world",
        "summary": "Scholars working in diverse regions contributed to mathematics, medicine, astronomy, philosophy, and other fields.",
        "question": "What might have changed if major scholarly institutions had remained continuously supported?",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Aristotle_Rossello_Ardit.jpg/800px-Aristotle_Rossello_Ardit.jpg",
    },
}

with st.sidebar:
    st.subheader("Scenario controls")
    selected_era = st.selectbox("Choose an era", ["Select an era", *scenarios.keys()])
    detail_level = st.select_slider(
        "Reflection prompt level",
        options=["Introductory", "Intermediate", "Advanced", "In-depth"],
    )

if selected_era == "Select an era":
    st.info("Choose an era in the sidebar to open its scenario.")
else:
    scenario = scenarios[selected_era]
    st.success(f"Scenario selected: {selected_era}")
    image_column, content_column = st.columns([1, 2], vertical_alignment="center")
    with image_column:
        st.image(scenario["image"], caption=selected_era, width="stretch")
    with content_column:
        st.header(selected_era)
        metric_columns = st.columns(2)
        metric_columns[0].metric("Period", scenario["year"])
        metric_columns[1].metric("Region", scenario["place"])
        st.subheader("Historical context")
        st.write(scenario["summary"])
        st.subheader("Alternative-history question")
        st.write(scenario["question"])
        st.caption(f"Reflection level: {detail_level}")

    st.warning(
        "These are discussion prompts, not predictions or claims that an alternative outcome would have occurred."
    )
