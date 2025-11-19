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
elif page == '🧳 Projects':
  st.title('My Ptojects')
  st.write('Here are some projects i have worked on:')

    # Project 1
  with st.container():
      col1, col2 = st.columns([1, 2])
    
      with col1:
          st.image('https://assets.capsolver.com/prod/images/post/2024-05-07/80292cb6-05db-4611-bdcc-f93ce05ba0ae.jpeg')
        
      with col2:
          st.subheader('🛒 E-Commerce Price Tracker')
          st.write('Python web scraper that monitors Amazon prices and sends alerts')
          st.caption('**Technologies:** Python, BeautifulSoup, Streamlit')

  
  # Project 2
  with st.container():
      col1, col2 = st.columns([1, 2])
      with col1:
          st.image('https://i.pinimg.com/736x/95/75/91/957591296622900be1b004289d040dae.jpg')
      with col2:
          st.subheader('📊 Student Grade Calculator')
          st.write('Interactive web app for calculating and visualizing grades')
          st.caption('**Technologies:** Python, Pandas, Plotly')


elif page == '🛠 Skills':
  st.title('Technical Skills')

  # Skills with progress bars
  st.subheader('Programming Languages')

  skills_data = {
    'Python' : 25,
    'HTML/CSS' : 30,
    'JavaScript' : 20,
    'SQL' : 30,
    'Technical Writing' : 15
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
    st.success('Excel')
    st.info('Word')
    st.warning('Access')

  with col2:
    st.success('PowerPoint')
    st.info('Google Docs')
    st.warning('ChatGPT/AI Tools')
    
  with col3:
    st.success('Presentations')
    st.info('Writing')
    st.warning('Social Media')
    
elif page == '📝 Resume':
    st.title('Resume')

    # Load PDF directly from GitHub
    pdf_url = "https://raw.githubusercontent.com/avinashjairam/cis211_project1/refs/heads/main/my_resume.pdf"

    import requests
    response = requests.get(pdf_url)

    if response.status_code == 200:
        PDFbyte = response.content

        st.download_button(
            label='🔻 Download Full Resume (PDF)',
            data=PDFbyte,
            file_name='my_resume.pdf',
            mime='application/pdf'
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

        📷 **Instagram:** [@yourhandle](https://www.instagram.com/rya_m37?igsh=em5xeTBycnpjcmVj&utm_source=qr)

    ''')

    # Fun interactive element
    st.subheader('Current Status')

    status = st.selectbox(
        "I'm currently:",
        [
            '👩‍💻 Coding',
            '📕 Studying',
            '☕ On a coffee break',
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
        
