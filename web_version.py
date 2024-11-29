import streamlit as st

import common_functions as cf

to_dos = cf.read_file()
st.set_page_config(layout="wide", page_title="My To-Do App")


def add_todo():
    new_todo = st.session_state.new_todo
    to_dos.append(new_todo + "\n")
    cf.write_file(to_dos)
    st.session_state.new_todo = ""


def remove_todo(i, value):
    to_dos.pop(i)
    cf.write_file(to_dos)
    del st.session_state[value]


st.title("My To-Do App")

for index, to_do in enumerate(to_dos):
    st.checkbox(to_do, key=to_do, on_change=remove_todo, args=(index, to_do,))

st.text_input(label="", placeholder="Add a new task", on_change=add_todo, key="new_todo")
