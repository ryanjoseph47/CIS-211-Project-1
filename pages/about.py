import streamlit as st
st.title("About Me")
# Dictionary for personal information
personal_info = {
  "name": "Ryan M. Joseph",
  "title": "Accounting Student",
  "email": "ryan.joseph@gmail.com",
  "location": "Brooklyn, NY",
  "graduation": "Planned for 2028"
}
st.markdown("""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.8/js/bootstrap.min.js" integrity="sha512-nKXmKvJyiGQy343jatQlzDprflyB5c+tKCzGP3Uq67v+lmzfnZUi/ZT+fc6ITZfSC5HhaBKUIvr/nTLCV+7F+Q==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
""", unsafe_allow_html=True)
# Add tabs for organization
tab1, tab2, tab3 = st.tabs(["Education", "Interests", "Goals"])

with tab1:
  st.write("### Educational Background")
  st.write("**Medgar Evers College, CUNY**")
  st.write("Bachelor of Science in Accounting")
  st.write("Expected Graduation: " + personal_info['graduation'])
  
  # Add GPA or relevant coursework
  st.write("**Relevant Coursework:**")
  courses = ["Accounting", "Financial Analysis", 
              "Business Analysis", "Programming Fundamentals"]
  for course in courses:
    st.write(f"- {course}")

with tab2:
  st.write("### My Interests")
  # Add your interests here
  st.write("I really enjoy being involved in my community and finding ways to make a positive difference. Whether it’s helping out at local events, mentoring younger students, or supporting small projects that bring people together, I love seeing how teamwork and kindness can create real impact.")
  st.write("I’m also curious about how technology can help improve everyday life. I like learning new things, meeting people with fresh ideas, and using creativity to solve problems that matter.")
  st.write("   * Volunteering and mentoring")
  st.write("   * Community service and teamwork")
  st.write("   * Technology for social good")
  st.write("   * Environmental care and sustainability")
  st.write("   * Learning new skills and connecting with others")
  
with tab3:
  st.write("### Career Goal")
  # Add your goals here
  st.write("My goal is to build a career that combines my love for numbers with my passion for technology. I’m interested in exploring how digital tools and data can make accounting more efficient, transparent, and impactful for both organizations and communities.")
  st.write("In the future, I hope to work at the intersection of finance and tech—using innovation to simplify financial processes, support smarter decision-making, and help people and businesses grow responsibly. I want to be part of the new generation of accountants who see technology not just as a tool, but as a way to create positive change.")