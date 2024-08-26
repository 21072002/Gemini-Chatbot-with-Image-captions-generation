import os
import json
import google.generativeai as genai
from PIL import Image

#to get the working directory
working_directory = os.path.dirname(os.path.abspath(__file__))
config_file_path = f"{working_directory}/config.json"
config_data = json.load(open(config_file_path))


#loading the API key
GOOGLE_API_KEY = config_data["GOOGLE_API_KEY"]
genai.configure(api_key= GOOGLE_API_KEY)

#function to load gemini pro model
def load_gemini_pro():
    gemini_pro_model = genai.GenerativeModel("gemini-1.5-flash")
    return gemini_pro_model

# Function to load image vision model
def gemini_pro_vision_responce(prompt, image):
    gemini_pro_vision_model = genai.GenerativeModel("gemini-1.5-pro")
    responce = gemini_pro_vision_model.generate_content([prompt, image])
    result = responce.text
    return result

