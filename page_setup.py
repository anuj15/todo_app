import streamlit as st

st.set_page_config(layout='wide')

# PAGE SETUP
movie_finder = st.Page(page='pages/movie_finder.py', title='Movie Finder', icon=':material/movie:', default=True)
anime_finder = st.Page(page='pages/anime_finder.py', title='Anime Finder', icon=':material/movie:')
to_do = st.Page(page='pages/to_do.py', title='TO Do App', icon=':material/lists:')
quiz = st.Page(page='pages/quiz.py', title='Quizzes', icon=':material/quiz:')
bmi_calculator = st.Page(page='pages/bmi_calculator.py', title='BMI Calculator', icon=':material/health_and_safety:')
unit_converter = st.Page(page='pages/unit_converter.py', title='Unit Converter', icon=':material/square_foot:')

# NAVIGATION SETUP [WITHOUT SECTIONS]
# pg = st.navigation(
#     page=[to_do, movie_finder, anime_finder, quiz, bmi_calculator],
#     )

# NAVIGATION SETUP [WITH SECTIONS]
pg = st.navigation(
    {
        'Entertainment': [movie_finder, anime_finder],
        'Apps': [to_do, quiz, bmi_calculator, unit_converter],
    }
)

# SHARED ACROSS PAGES
# st.sidebar.text(body='©️ by Anuj Gupta')

pg.run()
