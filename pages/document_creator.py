import streamlit as app
from streamlit_quill import st_quill

document_body = st_quill(
    placeholder="Blank body",
    html=True,
    key="quill_editor"
)

if document_body:
    st.markdown("### Preview")
    st.write(document_body, unsafe_allow_html=True)
