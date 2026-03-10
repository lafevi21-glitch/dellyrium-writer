import streamlit as app

guest = app.session_state.get("logged_user", "Guest")

def mainpage_main():
    app.header("DellyWrite")
    app.subheader("Welcome " + guest)

    app.divider()

    # ---------------------------------------------------

    app.subheader("Documents 📄")

    app.button("Create a document", icon="+")

mainpage_main()
