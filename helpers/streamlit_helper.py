import streamlit as st
import os
from helpers import GLOBALS


def SetInitialStreamlitStates():
    selectable_extension_types = os.getenv(GLOBALS.ALLOWED_FILE_EXTENSIONS_ENV_KEY).split(",")
    default_from_file_ext = os.getenv(GLOBALS.DEFAULT_FROM_FILE_EXTENSION_ENV_KEY)
    default_to_file_ext = os.getenv(GLOBALS.DEFAULT_TO_FILE_EXTENSION_ENV_KEY)

    if 'allowed_from_file_types' not in st.session_state:
        st.session_state.allowed_from_file_types = selectable_extension_types

    if 'allowed_to_file_types' not in st.session_state:
        st.session_state.allowed_to_file_types = selectable_extension_types

    if 'allowed_file_extensions' not in st.session_state:
        st.session_state.allowed_file_extensions = [default_from_file_ext]

    if 'from_file_index' not in st.session_state:
        st.session_state.from_file_index = selectable_extension_types.index(default_from_file_ext)

    if 'to_file_index' not in st.session_state:
        st.session_state.to_file_index = selectable_extension_types.index(default_to_file_ext)

    if 'download_file' not in st.session_state:
        st.session_state.download_file = None

    if 'download_file_name' not in st.session_state:
        st.session_state.download_file_name = ""

    if 'download_ready' not in st.session_state:
        st.session_state.download_ready = False


    if 'is_success' not in st.session_state:
        st.session_state.is_success = False

    if 'is_error' not in st.session_state:
        st.session_state.is_error = False

    if 'error_message' not in st.session_state:
        st.session_state.error_message = ""


def PopupError(error_message):
    st.session_state.is_error = True
    st.session_state.is_success = False
    st.session_state.error_message = error_message


def PopupSuccess():
    st.session_state.is_success = True
    st.session_state.is_error = False