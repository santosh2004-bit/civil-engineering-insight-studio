import google.generativeai as genai
from config import GOOGLE_API_KEY
from PIL import Image
import io

# Initialize API
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro-vision')

# Function to get Gemini response
def get_gemini_response(prompt, image):
    response = model.generate_content([prompt, image])
    return response.text

# Function to read image
def read_image(file):
    img = Image.open(file)
    return img

# Prompt for civil analysis
def civil_prompt():
    prompt = """
    You are a Civil Engineering Expert.
    Analyze the given image and provide:

    1. Type of structure
    2. Materials used
    3. Possible defects
    4. Safety suggestions
    5. Civil engineering insights
    """
    return prompt
