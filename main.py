import streamlit as st
from image_info import ImageInfo
from typing import List
import requests as req
import random as rand

@st.cache
def getWords() -> List[str]:
    return req.get(url = "https://raw.githubusercontent.com/googlecreativelab/quickdraw-dataset/master/categories.txt").text.split('\n')

def getImage() -> ImageInfo:
    answers = []
    words = getWords()
    while len(answers) < 3:
        curr = rand.choice(words)
        if curr not in answers:
            answers.append(curr)
    return ImageInfo(image_url="https://safebooru.org//samples/2950/sample_5fbec8e5b4b5099e3ac41b03ca0a31f06ab32c7e.jpg?3072971", answers=answers)

current = getImage()

st.title('Image Guesser')

st.image(current.image_url, width=400)

answer = st.text_input("Your answer")
if st.button("Send"):
    if answer in current.answers:
        st.error("Nice")
    else:
        st.error("Not in list")