import streamlit as st

st.title("BMI Calculator")
st.markdown("---")
st.markdown("Calculate your BMI using the metric system")

# Input for weight
st.number_input(label="Enter your weight in kg", label_visibility="hidden", key="weight", step=1.0, value=None,
                placeholder="Enter your weight in kg")

# Input for height
st.number_input(label="Enter your height in cm", label_visibility="hidden", key="height", step=1.0, value=None,
                placeholder="Enter your height in cm")

# Calculate BMI
if st.button("Calculate BMI"):
    bmi = st.session_state.weight / (st.session_state.height / 100) ** 2
    st.markdown(f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5:
        st.markdown("BMI Categories:")
        st.markdown("- Since BMI is less than 18.5, you are Underweight.")
    elif 18.5 <= bmi < 25:
        st.markdown("BMI Categories:")
        st.markdown("- Since BMI is 18.5 to 24.9, your weight is normal.")
    elif 25 <= bmi < 30:
        st.markdown("BMI Categories:")
        st.markdown("- Since BMI is 25 to 29.9, you are Overweight.")
    else:
        st.markdown("BMI Categories:")
        st.markdown("- Since BMI is 30 or more, you are Obese.")

with st.expander("Tips to maintain a healthy weight:"):
    st.markdown("""
        <p style="color: cyan; font-size: 14px; margin-bottom: 0px;">- Eat a balanced diet</p>
        <p style="color: cyan; font-size: 14px; margin-bottom: 0px;">- Exercise regularly</p>
        <p style="color: cyan; font-size: 14px; margin-bottom: 0px;">- Get enough sleep</p>
        <p style="color: cyan; font-size: 14px; margin-bottom: 0px;">- Stay hydrated</p>
        <p style="color: cyan; font-size: 14px; margin-bottom: 0px;">- Manage stress</p>
        <p style="color: cyan; font-size: 14px; margin-bottom: 0px;">- Avoid smoking and limit alcohol consumption</p>
        <p style="color: cyan; font-size: 14px; margin-bottom: 0px;">- Monitor your weight regularly</p>
        <p style="color: cyan; font-size: 14px; margin-bottom: 0px;">- Consult a healthcare provider if needed</p>
        <p style="color: cyan; font-size: 14px; margin-bottom: 0px;">- Stay positive and motivated</p>
        <p style="color: cyan; font-size: 14px; margin-bottom: 0px;">- Remember that health is wealth</p>
    """, unsafe_allow_html=True)
