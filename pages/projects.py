import streamlit as st
# List of dictionaries for projects
projects = [
  {
    "title": "Project 1 Name",
    "description": "Brief description of what this project does",
    "technologies": ["Python", "Streamlit"],
    "status": "Completed"
  },
  {
    "title": "Project 2 Name",
    "description": "Brief description of what this project does",
    "technologies": ["Excel", "Data Analysis"],
    "status": "In Progress"
  }
]
st.title("My Projects")
# Function to display project cards
def display_project(project):
  with st.expander(project["title"]):
    st.write(f"**Description:** {project['description']}")
    st.write(f"**Technologies Used:** {', '.join(project['technologies'])}")
    st.write(f"**Status:** {project['status']}")
      
    # Add progress bar for in-progress projects
    if project["status"] == "In Progress":
        progress = st.progress(0.6)
        st.write("60% Complete")
    elif project["status"] == "Completed":
        st.success("Project Completed!")

# Display all projects
for project in projects:
  display_project(project)
  st.write("---")  # Separator line

# Add option to filter projects
st.write("### Filter Projects")
status_filter = st.selectbox("Filter by status:", 
                                ["All", "Completed", "In Progress"])

if status_filter != "All":
  filtered = [p for p in projects if p["status"] == status_filter]
  st.write(f"Showing {len(filtered)} projects with status: {status_filter}")