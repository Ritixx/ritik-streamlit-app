import streamlit as st
import pandas as pd
st.image("https://cdn-icons-png.flaticon.com/128/563/563169.png", width = 100)
st.title("After 10th")
st.subheader("🟧⬜🟩 Made in India • ❤️ Designed in Punjab")
st.text("Lets see")

bag = st.radio("Pick your stream: ", ["Arts","Science","Commerce"],
                 index=None
)
st.write(f"Selected stream is {bag}")

if bag == "Arts":

    subtype = st.radio(
        "Pick Arts subtype:",
        ["Humanities", "Fine Arts", "Economics"],
        index=None
    )

    if subtype == "Humanities":
        degree = st.selectbox(
            "Your degree:",
            [
                "BA",
                "BA English",
                "BA History",
                "BA Political Science",
                "BA Psychology"
            ],
            index=None
        )

    elif subtype == "Fine Arts":
        degree = st.selectbox(
            "Your degree:",
            [
                "BFA",
                "B.Des",
                "BA Fine Arts"
            ],
            index=None
        )

    elif subtype == "Economics":
        degree = st.selectbox(
            "Your degree:",
            [
                "BA Economics",
                "BA Economics (Hons.)",
                "BBA"
            ],
            index=None
        )

elif bag == "Science":

    subtype = st.radio(
        "Pick Science subtype:",
        ["PCM", "PCB", "PCMB"],
        index=None
    )

    if subtype == "PCM":
        degree = st.selectbox(
            "Your degree:",
            ["B.Tech", "B.Sc", "BCA", "B.Arch"],
            index=None
        )

    elif subtype == "PCB":
        degree = st.selectbox(
            "Your degree:",
            ["MBBS", "BDS", "B.Pharm", "B.Sc Nursing"],
            index=None
        )

    elif subtype == "PCMB":
        degree = st.selectbox(
            "Your degree:",
            ["MBBS", "B.Tech", "B.Sc", "B.Pharm"],
            index=None
        )

elif bag == "Commerce":

    subtype = st.radio(
        "Pick Commerce subtype:",
        ["With Maths", "Without Maths"],
        index=None
    )

    if subtype == "With Maths":
        degree = st.selectbox(
            "Your degree:",
            ["B.Com", "BBA", "BMS", "BCA", "BA Economics"],
            index=None
        )

    elif subtype == "Without Maths":
        degree = st.selectbox(
            "Your degree:",
            ["B.Com", "BBA", "BMS", "BA"],
            index=None
        )
percent = st.select_slider(
    "Tell me your expected percentage",
    options=[60, 70, 80, 90, 100],
    value=None
)
name = st.sidebar.text_input("Enter your name")
if name:
    st.sidebar.write(f" A Very Warm Welcome, {name}!")
st.title("Top 15 Choice of India")

if st.button("Show Data"):
    url ="https://raw.githubusercontent.com/Ritixx/ritik-streamlit-app/c1c0e0a4fdc7f85a4a09d4e89f453221c7a07bc4/top_15_bachelor_degrees_india.csv"
    df = pd.read_csv(url)
    st.dataframe(df, hide_index=True)
import streamlit as st
import requests

st.title("Indian University Finder")

@st.cache_data
def get_universities():
    url = "http://universities.hipolabs.com/search?country=India"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()


universities = get_universities()

names = [uni["name"] for uni in universities]

university = st.selectbox(
    "Choose a university:",
    names,
    index=None
)

if university is not None:

    selected = next(
        uni for uni in universities
        if uni["name"] == university
    )

    st.success(f"You have chosen {university}")

    st.write("University:", selected["name"])
    st.write("Country:", selected["country"])
    st.write("Website:", selected["web_pages"][0])
