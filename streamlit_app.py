import streamlit as st

# Configure the page
st.set_page_config(
  page_title = 'Ryan | portfolio',
  page_icon= '👽',
  layout="wide"
)

# Define the pages
home = st.Page("pages/home.py", title="Ryan Joseph")
about = st.Page("pages/about.py", title="About me")
contact = st.Page("pages/contact.py", title="Contact me")
projects = st.Page("pages/projects.py", title="Projects")
skills = st.Page("pages/skills.py", title="Skills")

# Set up navigation
pg = st.navigation([home, about, skills, projects, contact])

# Run the selected page
pg.run()
