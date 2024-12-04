import streamlit as st

st.set_page_config(layout='wide')

# PAGE SETUP
movie_finder = st.Page(page='pages/movie_finder.py', title='Movie Finder', icon=':material/movie:', default=True)
anime_finder = st.Page(page='pages/anime_finder.py', title='Anime Finder', icon=':material/movie:')
to_do = st.Page(page='pages/to_do.py', title='TO Do App', icon=':material/lists:')
quiz = st.Page(page='pages/quiz.py', title='Quizzes', icon=':material/quiz:')
bmi_calculator = st.Page(page='pages/bmi_calculator.py', title='BMI Calculator', icon=':material/health_and_safety:')
unit_converter = st.Page(page='pages/unit_converter.py', title='Unit Converter', icon=':material/square_foot:')
recipe_finder = st.Page(page='pages/recipe_finder.py', title='Recipe Finder', icon=':material/restaurant_menu:')
filter_image = st.Page(page='pages/filter_image.py', title='Filter Image', icon=':material/photo_filter:')
stock_price = st.Page(page='pages/stock_price.py', title='Stock Price', icon=':material/monetization_on:')
calculator = st.Page(page='pages/calculator.py', title='Calculator', icon=':material/calculate:')

# NAVIGATION SETUP [WITHOUT SECTIONS]
# pg = st.navigation(
#     page=[to_do, movie_finder, anime_finder, quiz, bmi_calculator, unit_converter, recipe_finder, filter_image, stock_price],
#     )

# NAVIGATION SETUP [WITH SECTIONS]
pg = st.navigation(
    {
        'Entertainment': [movie_finder, anime_finder, filter_image],
        'Study': [quiz, bmi_calculator, unit_converter, calculator],
        'Others': [to_do, recipe_finder],
        'Finance': [stock_price],
    }
)

# SHARED ACROSS PAGES
# st.sidebar.text(body='©️ by Anuj Gupta')

pg.run()
