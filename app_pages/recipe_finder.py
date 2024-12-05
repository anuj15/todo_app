import time

import requests
import streamlit as st
import urllib3

urllib3.disable_warnings()

API_ENDPOINT = st.secrets['THE_MEAL_DB_API_ENDPOINT']

TITLE = 'Recipe Finder'
st.write(f'<h1 style=text-align:left>{TITLE}</h1><hr>', unsafe_allow_html=True)
st.markdown('<style>' + open('style/styles.css').read() + '</style>', unsafe_allow_html=True)

# Initialization
if 'recipe_details' not in st.session_state:
    st.session_state.recipe_details = ''


def search():
    try:
        response = requests.get(url=f"{API_ENDPOINT}{st.session_state.name}", verify=False)
        if response.status_code == 200 and response.json()['meals']:
            response = response.json()['meals'][0]
            ingredients = []
            for i in range(1, 21):
                ingredient = response.get(f'strIngredient{i}')
                measurement = response.get(f'strMeasure{i}')
                if ingredient and ingredient.strip():
                    ingredients.append(f"{measurement} {ingredient}".strip())

            ingredients_html = "<br>".join(ingredients)
            st.session_state.recipe_details = f"""
                <div class="container">
                    <img src="{response['strMealThumb']}" class="poster" alt="Poster is not available"/>
                    <div>
                        <h2>Dish: {response['strMeal']}</h2>
                        <h4>Category: {response['strCategory']}</h4>
                        <h4>Locale: {response['strArea']}</h4>
                    </div>
                </div>
                <div class="details">
                    <h4>Ingredients</h4>
                    <p>{ingredients_html}</p>
                    <h4>Instructions</h4>
                    <p>{response['strInstructions']}</p>
                </div>
                """
        else:
            st.session_state.recipe_details = """
                                <div class="details">
                                    <h4>Recipe Not Found</h4>
                                    <p>Please search a different dish.</p>
                                </div>
                                """

    except (IndexError, KeyError):
        st.session_state.recipe_details = """
                            <div class="details">
                                <h4>Recipe Not Found</h4>
                                <p>Please search a different dish.</p>
                            </div>
                            """


st.text_input(label='Recipe Name', placeholder='Enter complete or partial recipe name and press enter', key='name',
              on_change=search)
time.sleep(1)
show_details = st.markdown(st.session_state.recipe_details, unsafe_allow_html=True)
