import streamlit as st
import os
from tempfile import NamedTemporaryFile
from bin.audio2text import Speech2Text


st.set_page_config(page_title="Transcribe", page_icon="📈")
st.markdown("# Transcribe an Audio File [FREE] 🔊")
st.markdown("""
            - Upload a wav, mp3 or mp4 file 
            - Press Transcribe 
            - Review and edit
            - Download txt file
            Recommended File Length: less than 10minutes.
            """)


c1, c2, c3 = st.columns([1, 4, 1])

with c2:
    with st.form(key="my_form"):
        f = st.file_uploader("Choose a file", type=['mp3', 'mp4', 'wav'])
        st.info("""Upload a .wav, .mp3 or .mp4 file above UNDER 10MB""")
        submit_button = st.form_submit_button(label="Transcribe")

if f is not None:

    path_in = f.name
    # Get file size from buffer
    # Source: https://stackoverflow.com/a/19079887
    old_file_position = f.tell()
    f.seek(0, os.SEEK_END)
    getsize = f.tell()  # os.path.getsize(path_in)
    f.seek(old_file_position, os.SEEK_SET)
    getsize = round((getsize / 1000000), 1)
    # st.write(getsize)

    if getsize > 5:
        st.error("Sorry, we only allow files below 10MB in this version")
    else:

        with NamedTemporaryFile(dir='.', suffix='.csv') as file:
            file.write(f.getbuffer())
            path = file.name
            Whisper = Speech2Text()
            text = Whisper.transcribe_audio(path)

        if text:
            st.audio(f)
            input = st.text_area("Edit Your Transcription", value=text)
            st.warning(
             "🚨 Before pressing Download, make sure you save by pressing CMD+Enter.")
            st.download_button("Download",
                                input,
                               file_name=None,
                                mime=None,
                                key=None,
                                help=None,
                                on_click=None,
                                args=None,
                                kwargs=None,
                            )
