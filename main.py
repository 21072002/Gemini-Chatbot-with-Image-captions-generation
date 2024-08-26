import os
import streamlit as st
from streamlit_option_menu import option_menu
from gemini_utility import (load_gemini_pro, 
                            gemini_pro_vision_responce)
from PIL import Image

# To get the working directory
working_directory = os.path.dirname(os.path.abspath(__file__))

# Setting the page config
st.set_page_config(
    page_title="Gemini AI",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    selected = option_menu("Gemini AI",
                           ["Chatbot",
                            "Image Captioning",
                            ],
                           menu_icon="robot", 
                           icons=['chat-dots-fill', 'image-fill'],
                           default_index=0)

def translate_role_to_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

if selected == "Chatbot":
    model = load_gemini_pro()

    # Initialize chat session in Streamlit if not present
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    # Streamlit page title
    st.title("Gemini Chatbot 🤖")

    # Display the chatbot history
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_to_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    # Input field for user's message
    user_prompt = st.chat_input("Ask Gemini Pro...")

    if user_prompt:
        st.chat_message("user").markdown(user_prompt)
        gemini_response = st.session_state.chat_session.send_message(user_prompt)

        # Display the chatbot response
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)


if selected == "Image Captioning":

    # Streamlit title
    st.title("Image Caption Generation📸")

    upload_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

    if upload_image and st.button("Generate"):
        image = Image.open(upload_image)

        col1, col2 = st.columns(2)

        with col1:
            st.image(image, caption="Uploaded Image", use_column_width=True)

        default_prompt = "Write a caption for this image"

        # Getting the response from gemini
        caption = gemini_pro_vision_responce(default_prompt, image)

        with col2:
            st.info(caption)
