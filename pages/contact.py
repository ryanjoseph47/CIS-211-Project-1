import streamlit as st
st.title("Contact Me")
   
# Create a form
with st.form("contact_form"):
  name = st.text_input("Your Name")
  email = st.text_input("Your Email")
  subject = st.selectbox("Subject", 
                          ["General Inquiry", "Project Collaboration", 
                          "Job Opportunity", "Other"])
  message = st.text_area("Message", height=150)
  
  submitted = st.form_submit_button("Send Message")
    
  if submitted:
    if name and email and message:
      st.success(f"Thank you {name}! Your message has been received.")
      # In a real application, you would send an email here
      st.write("**Message Summary:**")
      st.write(f"From: {name} ({email})")
      st.write(f"Subject: {subject}")
      st.write(f"Message: {message[:100]}...")
    else:
      st.error("Please fill in all required fields.")