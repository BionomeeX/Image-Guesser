import streamlit as st
from image_info import ImageInfo

def getImage() -> ImageInfo:
    return ImageInfo(image_url="https://safebooru.org//samples/2950/sample_5fbec8e5b4b5099e3ac41b03ca0a31f06ab32c7e.jpg?3072971", answers=["donut", "fishing pole"])

current = getImage()

st.title('Image Guesser')

st.image(current.image_url, width=400)

answer = st.text_input("Your answer")
if st.button("Send"):
    if answer in current.answers:
        st.error("Nice")
    else:
        st.error("Not in list")