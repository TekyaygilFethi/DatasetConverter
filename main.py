import streamlit as st
from helpers import streamlit_helper as sh, streamlit_events as se
from dotenv import load_dotenv


load_dotenv()

sh.SetInitialStreamlitStates()

st.header("Dataset Converter")
st.caption("This project allows you to convert your data into one of the following data type: csv, xlsx and parquet.")

payload = {}

payload["from_file_type"] = st.selectbox(label="From", options=st.session_state.allowed_from_file_types,
                                         index=st.session_state.from_file_index,
                                         key="from_file_ext",
                                         on_change=se.from_file_selectbox_change)

payload["to_file_type"] = st.selectbox(label="To", options=st.session_state.allowed_to_file_types,
                                       index=st.session_state.to_file_index,
                                       key="to_file_ext",
                                       on_change=se.to_file_selectbox_change)

payload["uploaded_file"] = st.file_uploader(label="Upload a file", type=st.session_state.allowed_file_extensions,
                                            accept_multiple_files=False, on_change=se.uploaded_file_changed)

st.button("Convert", key="submit_button", on_click=se.on_submit_button_click, args=(payload,))

if st.session_state.download_ready:
    st.download_button(
        label="Download converted file",
        data=st.session_state.download_file,
        file_name=st.session_state.download_file_name,
        mime="application/octet-stream"
    )

if st.session_state.is_success:
    st.success('Your files have been converted!', icon="✅")
if st.session_state.is_error:
    st.error(st.session_state.error_message, icon="🚨")
