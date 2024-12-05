import streamlit as st

op = {
    'Addition': lambda a, b: a + b,
    'Subtraction': lambda a, b: a - b,
    'Multiplication': lambda a, b: a * b,
    'Division': lambda a, b: a / b
}
st.title('Calculator')
st.markdown("---")
st.number_input(label="Enter first number", value=None, key='first_number')
st.number_input(label="Enter second number", value=None, key='second_number')

st.text(body='Select operation')
st.radio(label="Operation", label_visibility="hidden", options=['Addition', 'Subtraction', 'Multiplication', 'Division']
         , key='operation')
st.button(label='Calculate', key='calculate')
if st.session_state.calculate:
    if st.session_state.first_number is not None and st.session_state.second_number is not None:
        try:
            answer = op[st.session_state.operation](st.session_state.first_number, st.session_state.second_number)
            st.markdown(body=f'<p style=color:green>Answer: {answer}', unsafe_allow_html=True)
        except ZeroDivisionError:
            st.error('Cannot divide by zero')
    else:
        st.error('Please enter both numbers')
