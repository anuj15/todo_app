import streamlit as st

import common_functions as cf

to_dos = cf.read_file()


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

st.write("<hr>", unsafe_allow_html=True)

st.text_input(label="Enter new To Do here:", placeholder="Add a new task", on_change=add_todo,
              key="new_todo")
st.write("<br>", unsafe_allow_html=True)

with st.expander("How To Use"):
    st.markdown("""
    - <sub style=color:cyan>Click on the checkbox to remove the task from the list of tasks</sub>
    - <sub style=color:cyan>Write a task in the text box and press enter to add it to the list of tasks</sub>
    """, unsafe_allow_html=True)
