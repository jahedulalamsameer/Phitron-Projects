import streamlit as st
from PIL import Image
from api_backend import note_generator, audio_trancriber, quiz_generator

st.title("Notes and Quiz AI Assistant",anchor=False,text_alignment="center")
st.divider()

with st.sidebar:
    if images := st.file_uploader("Upload images",type=("jpg","jpeg","png"),accept_multiple_files=True):
        if len(images)>5:
            st.error("Upload at max 5 images.")
        column = st.columns(len(images))
        for i,img in enumerate(images):
            with column[i]:
                st.image(img)
    
    difficulty_level = st.selectbox("Select difficulty level",options=("Easy","Medium","Hard"),index=None)
    
    upload = st.button("Upload",type="primary")

if upload:
    if not images:
        st.error("No image uploaded.")
    if len(images)>5:
        st.error("Maximum 5 images supported at a time.")
    if not difficulty_level:
        st.error("No difficulty level chosen.")


    if 1<=len(images)<=5 and difficulty_level:

        pil_images = [Image.open(img) for img in images]


        with st.container(border=True):
            st.subheader("Notes")
            with st.spinner("AI is generating notes for you..."):
                response = note_generator(pil_images)
                st.markdown(response)

            st.divider()

            st.subheader("Audio Transcription")
            with st.spinner("AI is transcribing audio for you..."):
                response = response.replace("#","").replace("*","")
                st.audio(audio_trancriber(response))

        st.divider()

        with st.container(border=True):
            st.subheader("Quiz")
            with st.spinner("AI is generating quiz for you..."):
                st.markdown(quiz_generator(pil_images,notes=response,level=difficulty_level))
