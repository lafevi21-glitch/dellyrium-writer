import streamlit as app

if not "logged_user" in app.session_state:
    app.error("Please, make sure you are logged!")
    app.switch_page("streamlit_app.py")
    app.stop()

app.markdown(
    """
    <style>
        /* Hides the sidebar entirely */
        [data-testid="stSidebar"] {
            display: none;
        }
        /* Hides the small arrow button that opens the sidebar */
        [data-testid="stSidebarCollapsedControl"] {
            display: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

guest = app.session_state.get("logged_user", "Guest")

def mainpage_main():
    app.header("DellyWrite")
    app.subheader("Welcome " + guest)

    app.divider()

    # ---------------------------------------------------

    app.subheader("Documents 📄")

    app.button("Create a document", icon="➕")

mainpage_main()
