import streamlit as st

st.title("Model")

st.multiselect(
    "Which models are needed? (max 3.)",
    ["Object detection", "Face detection", "Vibration detection", "anomally detection"],
    max_selections=3,
)
