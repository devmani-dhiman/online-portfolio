import streamlit as st

from apps import about, contact, home, projects, resume, work_ex, resource
from multiapp import MultiApp

app = MultiApp()

app.add_app("Home", home.app)
app.add_app("About Me", about.app)
app.add_app("Projects", projects.app)
app.add_app("Work Experience", work_ex.app)
app.add_app("Resume", resume.app)
app.add_app("Contact Info", contact.app)
app.add_app("Resources", resource.app)


app.run()