import streamlit as st
from datetime import datetime as dt
import requests

# Configuration
url = st.secrets['OMDB_ENDPOINT']
API_KEY = st.secrets['OMDB_API_KEY']
TITLE = 'Movie Finder'

# Initialization
if 'movie_details' not in st.session_state:
    st.session_state.movie_details = ''


def search(payload):
    response = requests.get(url=url, params=payload, verify=True).json()
    if response.get("Response") == "True":
        st.session_state.movie_details = f"""
            <div class="container">
                <img src="{response.get('Poster')}" class="poster" alt="Poster is not available"/>
                <div>
                    <h2>{response.get("Title")}</h2>
                    <p>{response.get("Year")} | {response.get("Genre")}</p>
                </div>
            </div>
            <div class="details">
                <h4>Details</h4>
                <p><strong>Released:</strong> {response.get("Released")}</p>
                <p><strong>Runtime:</strong> {response.get("Runtime")}</p>
                <p><strong>Director:</strong> {response.get("Director")}</p>
                <p><strong>Actors:</strong> {response.get("Actors")}</p>
                <p><strong>Language:</strong> {response.get("Language")}</p>
                <p><strong>Country:</strong> {response.get("Country")}</p>
                <p><strong>IMDB Rating:</strong> {response.get("imdbRating")}</p>
                <p><strong>IMDB Votes:</strong> {response.get("imdbVotes")}</p>
            </div>
            <div class="plot">
                <h4>Plot</h4>
                <p>{response.get("Plot")}</p>
            </div>
            """
        st.balloons()
    else:
        st.session_state.movie_details = """
            <div class="details">
                <h4>Movie Not Found</h4>
                <p>Please check the title and year, and try again.</p>
            </div>
            """


def search_without_year():
    title = st.session_state.title
    payload = {
        'apikey': API_KEY,
        't': title,
        'type': 'movie',
        'plot': 'full',
    }
    search(payload=payload)


def search_with_year():
    title = st.session_state.title
    year = st.session_state.year
    if title and year:
        payload = {
            'apikey': API_KEY,
            't': title,
            'type': 'movie',
            'y': year,
            'plot': 'full',
        }
        search(payload=payload)


# Title and styling
st.write(f'<h1 style=text-align:left>{TITLE}</h1><hr>', unsafe_allow_html=True)
st.markdown('<style>' + open('style/movie.css').read() + '</style>', unsafe_allow_html=True)

# Layout
l, r = st.columns(spec=2)

with l:
    st.text_input('Movie Title', placeholder='Enter full or partial movie title', key='title')
    st.write('<br>', unsafe_allow_html=True)
    st.slider('Year of Release', min_value=1900, max_value=dt.now().year, key='year', on_change=search_with_year)

with r:
    st.write('')
    st.write('')
    st.button(label='Search', key='search', type='primary', on_click=search_without_year)

# Display movie details
st.markdown(st.session_state.movie_details, unsafe_allow_html=True)
