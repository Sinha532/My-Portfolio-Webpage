import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide",initial_sidebar_state="collapsed")
from streamlit_navigation_bar import st_navbar
import pages as pg


def run_app():
    # Rest of your Streamlit app code
    pages = ["Home", "About Me", "My Projects", "Education", "Experience","Certifications","Contact"]
    styles = {
        "nav": {
            "background-color": "rgb(123, 209, 146)",
        },
        "div": {
            "max-width": "52rem",
        },
        "span": {
            "border-radius": "0.5rem",
            "color": "rgb(49, 51, 63)",
            "margin": "0 0.125rem",
            "padding": "0.3rem 0.5rem",
        },
        "active": {
            "background-color": "rgba(255, 255, 255, 0.25)",
        },
        "hover": {
            "background-color": "rgba(255, 255, 255, 0.35)",
        },
    }

    page = st_navbar(pages, styles=styles)

    functions ={
        "Home": pg.show_home,
        "About Me": pg.about,
        "My Projects":pg.projects,
        "Education":pg.education,
        "Experience":pg.experience,
        "Certifications":pg.certifications,
        "Contact":pg.contact_form,
        "Social":pg.media
    }

    go_to=functions.get(page)
    if go_to==pg.show_home:
        go_to()
        for i in functions.keys():
            if i!=page:
                go_to=functions.get(i)
                go_to()
    else:
        go_to()
    

if __name__ == "__main__":
    run_app()