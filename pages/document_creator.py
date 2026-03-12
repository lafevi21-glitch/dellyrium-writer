import streamlit as app
from streamlit_quill import st_quill

app.markdown("""
    <style>
    /* Change the toolbar background and icon colors */
    .ql-toolbar {
        background-color: #1a1a1a !important;
        border-color: #333 !important;
    }
    .ql-toolbar .ql-stroke {
        stroke: #fff !important;
    }
    .ql-toolbar .ql-fill {
        fill: #fff !important;
    }
    .ql-toolbar .ql-picker {
        color: #fff !important;
    }

    /* Change the main text area background */
    .ql-container {
        background-color: #000000 !important;
        border-color: #333 !important;
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

document_body = st_quill(
    placeholder="Blank body",
    html=True,
    key="quill_editor"
)

with document_body(border=True):
    app.markdown("### Preview")
    app.write(document_body, unsafe_allow_html=True)
