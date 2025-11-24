import streamlit as st
import pandas as pd
from datetime import datetime

# Page Config
st.set_page_config(
    page_title='Ryan | Portfolio',
    page_icon='👽',
    layout='wide'
)

# Custom CSS
st.markdown('''
    <style>
        .main-header {font-size: 42px; font-weight: bold; text-align:center;}
        .sub-header {font-size: 24px; text-align:center; color: #666;}
    </style>
''', unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title('📍 Navigation')
page = st.sidebar.radio(
    'Go to',
    ['🏠 Home', '🤠 About', '💼 Projects', '🛠 Skills', '📝 Resume', '📩 Contact']
)

# ---------------- HOME PAGE ----------------
if page == '🏠 Home':
    st.markdown('<p class="main-header">Ryan Joseph</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Accounting Student | Medgar Evers College</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric('GPA', '3.0', '📚')
    with col2:
        st.metric('Projects', '2', '💻')
    with col3:
        st.metric('Skills', '6+', '🚀')

    st.write('---')

    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader('Welcome to my digital space! 👋')
        st.write('''
            I am an Accounting student passionate about learning coding and exploring technology.
            Currently expanding my skills in **HTML** and **Python**.

            🎯 **Current Focus:** Learning Streamlit & building interactive apps  
            📚 **Currently Learning:** Internet and Emerging Technologies (CIS 211)  
            🌱 **Fun Fact:** I enjoy reading manga!
        ''')

    with col2:
        st.image(
            'https://wallpapers-clan.com/wp-content/uploads/2025/04/madara-uchiha-blue-flames-naruto-wallpaper-preview.jpg',
            use_column_width=True
        )

# ---------------- ABOUT PAGE ----------------
elif page == '🤠 About':
    st.title('About Me')

    st.subheader('My Journey 🗺️')

    with st.expander('2025 - Present: Medgar Evers College'):
        st.write('''
            - Major: Accounting  
            - Relevant Coursework: Coursera/Verizon Program, Capital Markets  
            - Activities: Basketball, Soccer, Football  
        ''')

    with st.expander('2024 - 2025: It Takes a Village Academy'):
        st.write('''
            - Graduated with honors  
            - Excellence in Algebra II  
            - Excellence in Living Environment  
        ''')

    st.subheader('Interests & Hobbies 🏀')
    interests = ['Streaming', 'Coding', 'Photography', 'Basketball', 'Travel']

    cols = st.columns(3)
    for i, interest in enumerate(interests):
        with cols[i % 3]:
            st.info(f'🔷 {interest}')

# ---------------- PROJECTS PAGE ----------------
elif page == '💼 Projects':
    st.title('My Projects')
    st.write('Here are some projects and experiences:')

    # Project 1
    with st.container():
        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(
                'https://rclc.nd.edu/assets/534266/tutor_group_experiment.jpg',
                use_column_width=True
            )

        with col2:
            st.subheader('🛒 After-School Aide – Hebrew Educational Society')
            st.write('Supported daily program activities, helped students with homework, and encouraged positive learning habits.')
            st.caption('**Role:** Crafts, games, academic assistance.')

    # Project 2
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(
                'https://artmiamimagazine.com/wp-content/uploads/2023/07/1024px-Sandro_Botticelli_-_La_nascita_di_Venere_-_Google_Art_Project_-_edited.jpg',
                use_column_width=True
            )
        with col2:
            st.subheader('🖼️ Student Art in History')
            st.write('Interactive experience exploring art and practicing drawing techniques.')
            st.caption('**Skills:** Painting, Creative Expression.')

# ---------------- SKILLS PAGE ----------------
elif page == '🛠 Skills':
    st.title('Technical & Accounting Skills')

    st.subheader('Core Skills')

    skills_data = {
        'Excel (Formulas, PivotTables)': 90,
        'Financial Accounting': 85,
        'Managerial Accounting': 80,
        'Data Analysis (Excel/Python)': 70,
        'SQL Basics': 50
    }

    for skill, level in skills_data.items():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.write(skill)
        with col2:
            st.progress(level / 100)

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

# ---------------- RESUME PAGE ----------------
elif page == '📝 Resume':
    st.title('Resume')

    # Load PDF from GitHub raw link
    pdf_url = "https://raw.githubusercontent.com/ryanjoseph47/cis-211-project-1/main/M21.pdf"

    import requests
    response = requests.get(pdf_url)

    if response.status_code == 200:
        PDFbyte = response.content
        st.download_button(
            label='🔻 Download Full Resume (PDF)',
            data=PDFbyte,
            file_name='Ryan_Joseph_Resume.pdf',
            mime='application/pdf'
        )
    else:
        st.error("❌ Unable to load resume. Make sure the PDF is uploaded to GitHub.")

# ---------------- CONTACT PAGE ----------------
elif page == '📩 Contact':
    st.title("Let's Connect!")

    st.subheader('Send me a message.')

    st.write('''
        📧 **Email:** ryanwidmie@gmail.com  
        🔗 **LinkedIn:** www.linkedin.com/in/ryan-joseph-b69009387  
        👨‍💻 **Github:** https://github.com/ryanjoseph47  
        📷 **Instagram:** @rya_m37  
    ''')

    st.subheader('Current Status')

    status = st.selectbox(
        "I'm currently:",
        ['👩‍💻 Coding', '📕 Studying', '☕ On Tiktok', '🎮 Gaming', '😴 Sleeping']
    )

    st.info(f'Status: {status}')

    st.write('---')
    st.markdown(
        f'<center>Made with 💗 using Streamlit | © {datetime.now().year} Ryan Joseph </center>',
        unsafe_allow_html=True
    )
