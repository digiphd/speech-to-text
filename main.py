import streamlit as st

st.set_page_config(
    page_title="Instructions",
    page_icon="👋",
)

st.write('# Welcome to Prod Tools!')

st.sidebar.success("Select a tool above.")

st.markdown(
    """
    Prod Tools is an open-source collection of commonly used tools in my day built specifically for
    digital marketers, VA's and/or developers who just want to go to one place.

    **👈 Select a tool from the dropdown on the left**!

    ### Tools include

    - Transcribe - Convert audio to text
    - Social Sentiment - Enter a hashtag or topic, see what the general public sentiment is
    - Inspirational Quotes - Get inspired
    - Compress images - batch compress images
    - Pomodoro Timer - Get productive
    - Image Background Remove
"""
)
