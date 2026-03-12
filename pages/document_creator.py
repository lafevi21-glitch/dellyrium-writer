import streamlit as app
from streamlit_quill import st_quill

app.markdown("""
    <style>
    /* The Toolbar */
    .ql-toolbar.ql-snow {
        background-color: #1E1E1E !important;
        border: 1px solid #333 !important;
        border-radius: 8px 8px 0 0;
    }
    /* Toolbar Icons & Text */
    .ql-snow .ql-stroke { stroke: #E0E0E0 !important; }
    .ql-snow .ql-fill { fill: #E0E0E0 !important; }
    .ql-snow .ql-picker { color: #E0E0E0 !important; }

    /* The Editor Background */
    .ql-container.ql-snow {
        background-color: #0F0F0F !important;
        border: 1px solid #333 !important;
        border-radius: 0 0 8px 8px;
        color: #FFFFFF !important;
    }

    /* Hover effects for buttons */
    .ql-snow.ql-toolbar button:hover .ql-stroke { stroke: #FF4B4B !important; }
    </style>
    """, unsafe_allow_html=True)

document_body = st_quill(
    placeholder="Blank body",
    html=True,
    key="quill_editor"
)

with app.container(border=True):
    app.markdown("### Preview")
    app.write(document_body, unsafe_allow_html=True)
