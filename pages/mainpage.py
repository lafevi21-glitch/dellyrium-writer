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

    app.divider()

    app.subheader("Welcome " + guest)

    app.divider()

    # ---------------------------------------------------

    app.subheader("Documents 📄")
    app.write("You may either create or open a document, please note that currently DellyWrite only accepts **.txt**. \n We are currently developing a way to upload a **.csv** file. \n *Happy Writing 😀*")

    app.button("Create a document", icon="➕")


mainpage_main()
