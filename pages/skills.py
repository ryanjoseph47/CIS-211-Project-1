import streamlit as st
st.title("Skills & Experience")
# List of skills
technical_skills = ["Python", "Financial Analysis", "Data Analysis", "Streamlit", "Accounting", "Problem Solving"]
soft_skills = ["Communication", "Team Work", "Time Management", "Leadership"]

# Create two columns
col1, col2 = st.columns(2)

with col1:
  st.write("### Technical Skills")
  for skill in technical_skills:
    st.write(f"- {skill}")
  
  # Add skill proficiency bars
  st.write("### Skill Proficiency")
  python_level = st.slider("Python", 0, 100, 60, disabled=True)
  excel_level = st.slider("Excel", 0, 100, 80, disabled=True)
  html_level = st.slider("HTML/CSS", 0, 100, 40, disabled=True)
    
with col2:
  st.write("### Soft Skills")
  for skill in soft_skills:
    st.write(f"- {skill}")
      
  # Add a simple chart
  st.write("### Skills Distribution")
  import random
  chart_data = {
    "Skill Category": ["Technical", "Analytical", "Communication", "Leadership"],
    "Proficiency": [70, 65, 80, 60]
  }
  st.bar_chart(data=chart_data, x="Skill Category", y="Proficiency")