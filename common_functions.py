import requests
import streamlit as st

FILEPATH = "data/todos.txt"
OPEN_TRIVIA_ENDPOINT = st.secrets['OPEN_TRIVIA_ENDPOINT']


def read_file(file_path=FILEPATH):
    try:
        with open(file_path) as f:
            return f.readlines()
    except FileNotFoundError:
        with open(file_path, "w"):
            return []


def write_file(to_do, file_path=FILEPATH):
    with open(file_path, "w") as f:
        f.writelines(to_do)


def get_quiz_data(category, difficulty, q_type):
    try:
        url = OPEN_TRIVIA_ENDPOINT
        payload = {
            'amount': '10',
            'category': category,
            'difficulty': difficulty,
            'type': q_type,
        }
        quiz_data = requests.get(url=url, params=payload, verify=False).json()['results']
        questions = []
        answers = []
        options = []
        if quiz_data:
            for i in quiz_data:
                questions.append(i['question'])
                answers.append(i['correct_answer'])
                options.append(i['incorrect_answers'])
            for ans, opt in zip(answers, options):
                opt.append(ans)
            return questions, answers, options
        else:
            return None
    except KeyError:
        return
