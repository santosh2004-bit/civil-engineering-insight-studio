from flask import Flask, render_template, request
from gemini_model import get_gemini_response, read_image, civil_prompt

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['image']

    img = read_image(file)

    prompt = civil_prompt()

    result = get_gemini_response(prompt, img)

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
