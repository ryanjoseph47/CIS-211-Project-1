import streamlit as st
import pandas as pd
from datetime import datetime 

# Page Config
st.set_page_config(
  page_title = 'Ryan | portfolio',
  page_icon= '👽',
  layout = 'wide'
)

# Custom CSS (optional - for styling)
st.markdown('''        
              <style>
                  .main-haeder {front-size: 42px; font-weight: bold; text-align:center;}
                  .sub-header {font_size: 24px; text-align:center; color: #666;}
             </style>
           ''', unsafe_allow_html = True)

# Sidebar
st.sidebar.title('📍 Navigation')
page = st.sidebar.radio('Go to',
                        ['🏠 Home', '🤠 About', '💼 Projects', '🛠 Skills' ,'📝 Resume', '📩 Contact' ])

# Home Page
if page =='🏠 Home': 
  st.markdown('<p class="main-header">Ryan Joseph</p>', unsafe_allow_html=True)
  st.markdown('<p class="sub-header">Ryan Student | Medgar Evers College</p>', unsafe_allow_html=True)

  # Three Columns for stats
  col1, col2, col3 = st.columns(3)

  with col1:
      st.metric('GPA', '3.0', '📚')
  with col2:
      st.metric('Projects', '2', '💻')
  with col3:
      st.metric('Skills', '6+', '🚀')

  st.write('---')

  # Introduction with columns
  col1, col2 = st.columns([2,1])
  with col1:
    st.subheader('Welcome to my digital space!👋')
    st.write('''
                I am an Accounting student passionate about web development and Coding. Currently learning
                HTML and Python to build innovative solutions.
            
                🎯 **Current Focus:** Building interactive web applications with Streamlit
            
                📚 **Currently Learning:** Internet and Emerging Technologies (CIS 211)
            
                🌱 **Fun Fact:** I like reading manga !
            ''')
  with col2:
    # Placeholder for image
    st.image('https://wallpapers-clan.com/wp-content/uploads/2025/04/madara-uchiha-blue-flames-naruto-wallpaper-preview.jpg', use_column_width=True)

# About Page
elif page == '🤠 About':
  st.title('About Me')

  # Timeline of my Professional Journey
  st.subheader('My Journey 🗺️')

  with st.expander('2025 - Present: Medgar Evers College'):
    st.write('''
                - Major: Accounting
                - Relevant Coursework: Coursera/Verizon, Capital Markets
                - Activities: Basketball, Soccer, Football
            ''')

  with st.expander('2024 - 2025: It takes Village Academy'):
    st.write('''
                - Graduated with honors
                - Excellence in Algebra II
                - Excellence in Living Environment
            ''')

  st.subheader('Interests & Hobbies 🏀')
  interests = ['Streaming', 'Coding', 'Photography', 'Basketball', 'Travel']

# Display the interests in columns
  cols = st.columns(3)
  for i, interest in enumerate(interests):
    with cols[i % 3]:
      st.info(f'🔷 {interest}')
      
elif page == '💼 Projects':
  st.title('My Projects')
  st.write('Here are some projects I have worked on:')

  # Project 1
  with st.container():
    col1, col2 = st.columns([1, 2])
  
    with col1:
        st.image('https://rclc.nd.edu/assets/534266/tutor_group_experiment.jpg', use_column_width = True)

    with col2:
        st.subheader('🛒 The Hebrew Educational Society')
        st.write('Support daily program activities. Help students with homework and encourage positive learning habits')
        st.caption('**After-School Aide Staff:** crafts,games, and academic assistance')

  # Project 2 
  with st.container():
    col1, col2 = st.columns([1,2])
    with col1:
      st.image('https://artmiamimagazine.com/wp-content/uploads/2023/07/1024px-Sandro_Botticelli_-_La_nascita_di_Venere_-_Google_Art_Project_-_edited.jpg', use_column_width = True)
    with col2:
      st.subheader('🖼️ Student Art In History')
      st.write('Interactive with Art and drawing')
      st.caption('**Art In History:** Painting, Drawing')

elif page == '🛠 Skills':
  st.title('Technical Skills')

  # Skills with progress bars
  st.subheader('Programming Languages')

  skills_data = {
    'Excel (Formulas, PivotTables)': 90,
    'Financial Accounting': 85,
    'Managerial Accounting': 80,
    'Data Analysis (Excel/Python)': 70,
    'SQL Basics': 50
  }

  for skill, level in skills_data.items():
    col1, col2 = st.columns([1,3])
    with col1:
      st.write(skill)
    with col2:
      st.progress(level/50)

  st.subheader('Tools & Technologies')

col1, col2, col3 = st.columns(3)

   with col1:
    st.success('Microsoft Excel')
    st.info('QuickBooks')
    st.warning('SAP (Basic)')

  with col2:
    st.success('Microsoft Word')
    st.info('Google Sheets')
    st.warning('Power BI')

  with col3:
    st.success('Financial Reporting')
    st.info('Data Visualization')
    st.warning('Team Collaboration')
    
elif page == '📝 Resume':
  st.title('Resume')

  # Read PDF from my GitHub repository
  with open('M21.pdf', 'rb') as pdf_file:
    PDFbyte = pdf_file.read()
  
  st.download_button(
    label ='🔻 Download Full Resume (PDF)',
    data = PDFbyte,
    file_name = 'my_resume.pdf',
    mime ='application/pdf'
  )

elif page == '📩 Contact':
  st.title("Let's Connect!")

  col1, = st.columns(1)

  with col1:
    st.subheader('Send me a message.')

    st.write('''
        📧 **Email:** ryanwidmie@gmail.com

        🏢 **LinkedIn:** [www.linkedin.com/in/ryan-joseph-b69009387](https://linkedin.com)

        👩‍💻 **Github:** [https://github.com/ryanjoseph47](https://github.com)

        📷 **Instagram:** [https://www.instagram.com/rya_m37?igsh=em5xeTBycnpjcmVj&utm_source=qr](https://instagram.com)

    ''')

    # Fun interactive element
    st.subheader('Current Status')

    status = st.selectbox(
        "I'm currently:",
        [
            '👩‍💻 Coding',
            '📕 Studying',
            '☕ On Tiktok',
            '🎮 Gaming',
            '😴 Sleeping'
        ]
    )


    st.info(f'Status: {status}')

    # Footer
    st.write('---')
    st.markdown(
        f'<center>Made with 💗 using Streamlit | © {datetime.now().year} Ryan Joseph </center>',
        unsafe_allow_html = True
    )
        
