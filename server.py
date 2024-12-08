import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__, template_folder="templates")
CORS(app)


def configure_api():
    try:
        genai.configure(api_key="you api")
    except Exception as e:
        raise Exception(f"Error configuring API: {str(e)}")


def create_model():
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    try:
        model = genai.GenerativeModel(
            model_name="gemini-pro",
            generation_config=generation_config
        )
        return model
    except Exception as e:
        raise Exception(f"Error creating model: {str(e)}")

def initialize_chat(model):
    try:
        chat = model.start_chat(history=[])
        return chat
    except Exception as e:
        raise Exception(f"Error initializing chat: {str(e)}")

SAFETY_SETTINGS = [
    {"category": "HARM_CATEGORY_SEXUAL", "threshold": "BLOCK_ONLY_HIGH"},
    {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_ONLY_HIGH"},
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_ONLY_HIGH"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_ONLY_HIGH"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_ONLY_HIGH"},
]


configure_api()
model = create_model()
chat_session = initialize_chat(model)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({"message": "Flask API is working!"})


@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        user_input = request.json['message']  # Get the message from the frontend
        response = ""
        # Send the message to the AI model
        for chunk in chat_session.send_message(user_input, stream=True):
            response += chunk.text
        return jsonify({'response': response})  # Return AI response to frontend
    except Exception as e:
        return jsonify({'error': f"An error occurred: {str(e)}"})

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
