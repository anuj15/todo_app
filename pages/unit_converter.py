import streamlit as st

st.title("Unit Converter")

# Length Converter
st.write("<hr>", unsafe_allow_html=True)
st.markdown("### Length Converter")
length = st.number_input(label="", label_visibility="hidden", value=None, step=1.0,
                         placeholder="Enter the length in meters")
unit = st.selectbox("Select the unit", ["Feet", "Inches", "Centimeters"])
if length is not None:
    if unit == "Feet":
        result = length * 3.28084
    elif unit == "Inches":
        result = length * 39.3701
    else:
        result = length * 100
    st.write(f"The length in {unit} is {result}")

# Weight Converter
st.write("<hr>", unsafe_allow_html=True)
st.markdown("### Weight Converter")
weight = st.number_input(label="", label_visibility="hidden", value=None, step=1.0,
                         placeholder="Enter the weight in kilograms")
unit = st.selectbox("Select the unit", ["Pounds", "Ounces", "Grams"])
if weight is not None:
    if unit == "Pounds":
        result = weight * 2.20462
    elif unit == "Ounces":
        result = weight * 35.274
    else:
        result = weight * 1000
    st.write(f"The weight in {unit} is {result}")

# Temperature Converter
st.write("<hr>", unsafe_allow_html=True)
st.markdown("### Temperature Converter")
temperature = st.number_input(label="", label_visibility="hidden", value=None, step=1.0,
                              placeholder="Enter the temperature in Celsius")
unit = st.selectbox("Select the unit", ["Fahrenheit", "Kelvin"])
if temperature is not None:
    if unit == "Fahrenheit":
        result = temperature * 9 / 5 + 32
    else:
        result = temperature + 273.15
    st.write(f"The temperature in {unit} is {result}")
