import streamlit as st

st.title("Options")
st.subheader("Made by Ritik in India")
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

