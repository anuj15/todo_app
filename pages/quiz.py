import streamlit as st

from common_functions import get_quiz_data

NO_DATA_IMAGE = 'images/oops.png'
TITLE = 'Quiz'
st.write(f'<h1 style=text-align:left>{TITLE}</h1><hr>', unsafe_allow_html=True)

quiz_category = {'G.K.': 9, 'Books': 10, 'Movies': 11, 'Music': 12, 'Musicals': 13, 'Television': 14, 'Video Games': 15,
                 'Board Games': 16, 'Nature': 17, 'Computers': 18, 'Maths': 19, 'Mythology': 20, 'Sports': 21,
                 'Geography': 22, 'History': 23, 'Politics': 24, 'Arts': 25, 'Celebrities': 26, 'Animals': 27,
                 'Vehicles': 28, 'Comics': 29, 'Gadgets': 30, 'Anime & Manga': 31, 'Cartoons': 32}
quiz_difficulty = {'Easy': 'easy', 'Medium': 'medium', 'Hard': 'hard'}
quiz_type = {'Multiple Choice': 'multiple', 'True / False': 'boolean'}

st.selectbox(label='Category', options=quiz_category.keys(), key='category')
st.selectbox(label='Difficulty', options=quiz_difficulty.keys(), key='difficulty')
st.selectbox(label='Type', options=quiz_type.keys(), key='q_type')

category = st.session_state.category
difficulty = st.session_state.difficulty
q_type = st.session_state.q_type

# Initialize session state variables if they don't exist
if 'is_data_available' not in st.session_state:
    st.session_state.is_data_available = None
if 'show_results' not in st.session_state:
    st.session_state.show_results = False
if 'score' not in st.session_state:
    st.session_state.score = ''
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = []


# Function to reset the quiz state
def reset_quiz_state():
    st.session_state.is_data_available = None
    st.session_state.show_results = False
    st.session_state.score = ''
    st.session_state.user_answers = []
    for j in range(10):
        if f'answer_{j}' in st.session_state:
            del st.session_state[f'answer_{j}']


# Fetch quiz data when the button is clicked
if st.button('Get Quiz Data'):
    reset_quiz_state()
    st.session_state.is_data_available = get_quiz_data(quiz_category[category], quiz_difficulty[difficulty],
                                                       quiz_type[q_type])

if st.session_state.is_data_available:
    questions, answers, options = st.session_state.is_data_available


    def check_answers():
        user_answers = []
        for j in range(len(questions)):
            user_answers.append(st.session_state.get(f'answer_{j}', None))
        score = 0
        for j, user_answer in enumerate(user_answers):
            if user_answer == answers[j]:
                score += 1
        st.session_state.score = score
        st.session_state.user_answers = user_answers
        st.session_state.show_results = True


    with st.form(key='quiz_form', clear_on_submit=False):
        for i in range(len(questions)):
            st.write(f'Q.{i + 1} {questions[i]}')
            if st.session_state.show_results:
                for option in sorted(options[i]):
                    if option == answers[i]:
                        st.write(f'<span style="color:green;">{option}</span>', unsafe_allow_html=True)
                    elif option == st.session_state.user_answers[i]:
                        st.write(f'<span style="color:red;">{option}</span>', unsafe_allow_html=True)
                    else:
                        st.write(option)
            else:
                st.radio(
                    label=f'Options for Q{i + 1}',
                    options=sorted(options[i]),
                    label_visibility='visible',
                    index=None,
                    key=f'answer_{i}',
                )
            st.write('<hr>', unsafe_allow_html=True)
        submit_button = st.form_submit_button(label='Submit', type='primary', on_click=check_answers)

    if st.session_state.score != '':
        st.write(f'<h3 style=color:green>You scored: {st.session_state.score}/10</h3>', unsafe_allow_html=True)

else:
    st.image(image=NO_DATA_IMAGE, width=300)
    st.write('No Questions found for this combination. Try something else.')
