import streamlit as st

st.set_page_config(layout='wide')

# PAGE SETUP
movie_finder = st.Page(page='app_pages/movie_finder.py', title='Movie Finder', icon=':material/movie:', default=True)
anime_finder = st.Page(page='app_pages/anime_finder.py', title='Anime Finder', icon=':material/movie:')
to_do = st.Page(page='app_pages/to_do.py', title='TO Do App', icon=':material/lists:')
quiz = st.Page(page='app_pages/quiz.py', title='Quizzes', icon=':material/quiz:')
bmi_calculator = st.Page(page='app_pages/bmi_calculator.py', title='BMI Calculator', icon=':material/health_and_safety:')
unit_converter = st.Page(page='app_pages/unit_converter.py', title='Unit Converter', icon=':material/square_foot:')
recipe_finder = st.Page(page='app_pages/recipe_finder.py', title='Recipe Finder', icon=':material/restaurant_menu:')
filter_image = st.Page(page='app_pages/filter_image.py', title='Filter Image', icon=':material/photo_filter:')
stock_price = st.Page(page='app_pages/stock_price.py', title='Stock Price', icon=':material/monetization_on:')
calculator = st.Page(page='app_pages/calculator.py', title='Calculator', icon=':material/calculate:')
graph_explorer = st.Page(page='app_pages/graph_explorer.py', title='Graph Explorer', icon=':material/monitoring:')

# NAVIGATION SETUP [WITHOUT SECTIONS]
# pg = st.navigation(
#     page=[to_do, movie_finder, anime_finder, quiz, bmi_calculator, unit_converter, recipe_finder, filter_image, stock_price, calculator, graph_explorer],
#     )

# NAVIGATION SETUP [WITH SECTIONS]
pg = st.navigation(
    {
        'Finance': [stock_price],
        'Entertainment': [movie_finder, anime_finder, filter_image],
        'Study': [quiz, bmi_calculator, unit_converter, calculator, graph_explorer],
        'Others': [to_do, recipe_finder],
    }
)

# SHARED ACROSS PAGES
# st.sidebar.text(body='©️ by Anuj Gupta')

pg.run()
