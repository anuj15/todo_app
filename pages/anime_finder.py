import time
from datetime import datetime as dt

import requests
import streamlit as st
import urllib3

urllib3.disable_warnings()

KITSU_API_ENDPOINT = st.secrets['KITSU_API_ENDPOINT']

TITLE = 'Anime Finder'
st.write(f'<h1 style=text-align:left>{TITLE}</h1><hr>', unsafe_allow_html=True)
st.markdown('<style>' + open('style/movie.css').read() + '</style>', unsafe_allow_html=True)

# Initialization
if 'anime_details' not in st.session_state:
    st.session_state.anime_details = ''


def search():
    try:
        anime_title = st.session_state.title
        headers = {
            'Accept': 'application/vnd.api+json',
            'Content-Type': 'application/vnd.api+json',
        }
        payload = {
            'filter[text]': anime_title
        }
        response = requests.get(url=KITSU_API_ENDPOINT, params=payload, headers=headers, verify=False)
        if response.status_code == 200:
            response = [x for x in response.json()['data']]
            response = sorted(response, key=lambda x: int(x['id']))
            response = response[0]['attributes']
            start_date = dt.strptime(response['startDate'], '%Y-%m-%d').strftime('%b %Y')
            end_date = dt.strptime(response['endDate'], '%Y-%m-%d').strftime('%b %Y')
            st.session_state.anime_details = f"""
                <div class="container">
                    <img src="{response['posterImage']['original']}" class="poster" alt="Poster is not available"/>
                    <div>
                        <h2>{response['titles']['en']}</h2>
                        <p>{start_date} - {end_date}</p>
                    </div>
                </div>
                <div class="details">
                    <h4>Details</h4>
                    <p><strong>Rating:</strong> {response['averageRating']}</p>
                    <p><strong>Popularity Rank:</strong> {response['popularityRank']}</p>
                    <p><strong>Age Rating:</strong> {response['ageRatingGuide']}</p>
                    <p><strong>Status:</strong> {response['status']}</p>
                    <p><strong>Episode Count:</strong> {response['episodeCount']}</p>
                    <p><strong>Episode Length:</strong> {response['episodeLength']}</p>
                    <p><strong>Youtube Video Id:</strong> {response['youtubeVideoId']}</p>
                </div>
                <div class="plot">
                    <h4>Plot</h4>
                    <p>{response['synopsis']}</p>
                </div>
                """
            st.balloons()
        else:
            st.session_state.anime_details = """
                        <div class="details">
                            <h4>Anime Not Found</h4>
                            <p>Please check the title, and try again.</p>
                        </div>
                        """
    except (IndexError, KeyError):
        st.session_state.anime_details = """
                    <div class="details">
                        <h4>Anime Not Found</h4>
                        <p>Please check the title, and try again.</p>
                    </div>
                    """


st.text_input(label='Anime Title', placeholder='Enter complete or partial anime name and press enter', key='title',
              on_change=search)
time.sleep(1)
show_details = st.markdown(st.session_state.anime_details, unsafe_allow_html=True)
