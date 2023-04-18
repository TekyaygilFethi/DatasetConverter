import streamlit as st
from helpers import streamlit_helper as sh, file_helper as fh, GLOBALS
import os


def on_submit_button_click(payload):
    try:
        st.session_state.is_error = False
        uploaded_file = payload["uploaded_file"]
        from_file_extension = payload["from_file_type"]
        to_file_extension = payload["to_file_type"]

        if uploaded_file is not None:
            last_index = uploaded_file.name.rfind(from_file_extension)
            if last_index != -1:
                first_part = uploaded_file.name[:last_index]
                second_part = uploaded_file.name[last_index + len(from_file_extension):]

                new_file_name = first_part + to_file_extension + second_part

            df = fh.read_file(uploaded_file, from_file_extension)
            st.session_state.download_file = fh.convert_file(df, new_file_name, to_file_extension)

            st.session_state.download_file_name = new_file_name
            st.session_state.download_ready = True
    except Exception as e:
        sh.PopupError(e);


def from_file_selectbox_change():
    selected_from_ext = st.session_state.from_file_ext
    selected_to_ext = st.session_state.to_file_ext
    st.session_state.is_error = False
    __HandleExtensions(selected_from_ext, selected_to_ext)


def to_file_selectbox_change():
    selected_from_ext = st.session_state.from_file_ext
    selected_to_ext = st.session_state.to_file_ext
    st.session_state.is_error = False
    __HandleExtensions(selected_from_ext, selected_to_ext)


def __HandleExtensions(selected_from_ext, selected_to_ext):
    extensions = __CheckExtensions(selected_from_ext, selected_to_ext)

    if extensions is None:
        st.session_state.allowed_file_extensions = [selected_from_ext]
    else:
        st.session_state.allowed_file_extensions = [extensions[0]]


def __CheckExtensions(selected_from_ext, selected_to_ext):
    if selected_from_ext == selected_to_ext:
        sh.PopupError(GLOBALS.EXTENSION_SAME_ERROR_MESSAGEE)

        default_from_file_ext = os.getenv(GLOBALS.DEFAULT_FROM_FILE_EXTENSION_ENV_KEY)
        default_to_file_ext = os.getenv(GLOBALS.DEFAULT_TO_FILE_EXTENSION_ENV_KEY)

        st.session_state.from_file_ext = default_from_file_ext
        st.session_state.to_file_ext = default_to_file_ext

        return [default_from_file_ext, default_to_file_ext]


def uploaded_file_changed():
    st.session_state.download_ready = False
    st.session_state.download_file_name = ""
    st.session_state.download_file = None
