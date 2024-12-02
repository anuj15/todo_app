import streamlit as st

st.set_page_config(layout='wide')

# PAGE SETUP
movie_finder = st.Page(page='pages/movie_finder.py', title='Movie Finder', icon=':material/movie:', default=True)
anime_finder = st.Page(page='pages/anime_finder.py', title='Anime Finder', icon=':material/movie:')
to_do = st.Page(page='pages/to_do.py', title='TO Do App', icon=':material/lists:')
quiz = st.Page(page='pages/quiz.py', title='Quizzes', icon=':material/quiz:')

# NAVIGATION SETUP [WITHOUT SECTIONS]
# pg = st.navigation(
#     page=[to_do, movie_finder, anime_finder, quiz]
#     )

# NAVIGATION SETUP [WITH SECTIONS]
pg = st.navigation(
    {
        'Entertainment': [movie_finder, anime_finder],
        'Apps': [to_do, quiz],
    }
)

# SHARED ACROSS PAGES
st.sidebar.text(body='©️ by Anuj Gupta')

pg.run()
