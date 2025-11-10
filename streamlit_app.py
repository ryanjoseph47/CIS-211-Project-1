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
st. sidebar.title('📍 Navigation')
page = st.sidebar.radio('Go to',
                        ['🏠 Home', '😇About', '🧳 Projects', '🛠️ Skill', '📈b Resume', '📩 Contact'])

# Home Page
if page =='🏠 Home': 
  st.markdown('<p class="main-header">Ryan Joseph</p>', unsafe_allow_html=True)
  st.markdown('<p class="sub-header">Ryan Student | Medgar Evers College</p>', unsafe_allow_html=True)

# Three Columns for stats
  col1, col2, col3 = st.columns(3)

  with col1:
      st.metric('GPA', '3.8', '📚')
  with col2:
      st.metric('Projects', '5', '💻')
  with col3:
      st.metric('Skills', '10+', '🚀')

  st.write('---')

# Introduction with columns
  col1, col2 = st.columns([2,1])
  with col1:
    st.subheader('Welcome to my digital space!👋')
    st.write('''
                I am a Computer Information Systems student passionate about web development and emerging technologies. Currently learning
                HTML, CSS, JavaScript, and Python to build innovative solutions.
            
                🎯 **Current Focus:** Building interactive web applications with Streamlit
            
                📚 **Currently Learning:** Internet and Emergin Technologies (CIS 211)
            
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
                - Relevant Coursework: Internet & Emerging Technologies, Programming, Database Systems, AI
                - Activities: Basketball, Soccer, Football
            ''')

  with st.expander('2023 - 2025: NYC Museum School'):
    st.write('''
                - Graduated with honors
                - AP Computer Science A (Score: 5)
                - Founded Coding Club
            ''')

  st.subheader('Interests & Hobbies 🏀')
  interests = ['Web Development', 'AI/Machine Learning', 'Photography', 'Basketball', 'Travel', 'Baseball2']

  # Display the interests in columns
  cols = st.columns(3)
  for i, interest in enumerate(interests):
    with cols[i % 3]:
      st.info(f'🔷 {interest}')
elif page == '🧳 Projects':
  st.title('My Ptojects')
  st.write('Here are some projects i have worked on:')

import streamlit as st

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
