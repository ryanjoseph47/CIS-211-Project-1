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
st.mardown('''        
              <style>
                  .main-haeder {front-size: 42px; font-weight: bold; text-align:center;}
                  .sub-header {font_size: 24px; text-align:center; color: #666;}
             </style>
           ''', unsafe_allow_html = True)

# Sidebar
st. sidebar.title('📍 Navigation')
page = st.sidebar.radio('Go to')
                        ['🏠 Home', '😇About', '🧳 Projects', '🛠️ Skill', '📈b Resume',📩 Contact'])

# Home Page
if page == '🏠 Home':
  st.mardown('<p class="main-header">Ryan Joseph</p>', unsafe_allow_html=True)
  st.mardown('<p class="sub-header">Ryan Student | Medgar Evers College</p>', unsafe_allow_html=True)
