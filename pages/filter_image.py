import streamlit as st
from PIL import Image

st.title("Filter Image")
st.markdown("---")
with st.expander("Capture image & convert it to gray scale"):
    image = st.camera_input("Camera")
    if image:
        image = Image.open(image)
        gray_image = image.convert("L")
        st.image(image=gray_image, width=300)

with st.expander("Upload image & convert it to gray scale"):
    image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    if image:
        st.image(image=image, width=300)
        image = Image.open(image)
        gray_image = image.convert("L")
        st.image(image=gray_image, width=300)
