# Flask AI Chat Integration with Gemini API


This Flask web application integrates with the Google Gemini API to provide a chat interface. It allows users to send messages to the AI model, receive responses, and interact with it in real time.

## Features

- **Chat Interface**: Interact with Google's Gemini API-powered AI model.
- **Real-time Messaging**: Send and receive messages in real time.
- **Error Handling**: Graceful error handling for user requests.
- **API Endpoint**: A simple API for testing the Flask server.

## Tech Stack

This project uses several open-source libraries and tools:

- **Flask**: Lightweight web framework for building web apps.
- **Google Gemini API**: AI-powered chat model for generating responses.
- **Flask-CORS**: For enabling Cross-Origin Resource Sharing (CORS) to allow cross-origin requests.
- **Python 3.8+**: The required version of Python for running this application.
- **pip**: Python's package manager for installing dependencies.

## Installation

To get started, clone the repository and install the dependencies.

1. **Clone the repository**:
    ```sh
    git clone https://github.com/lumenrps/Aethera.git
    cd Aethera
    ```
2. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up your API key**:
    Replace the placeholder `you api` with your actual Gemini API key in `app.py`:
    ```python
    genai.configure(api_key="your_api_key")
    ```

4. **Run the Flask app**:
    ```sh
    python app.py
    ```

    The app will be running at `http://127.0.0.1:5000`.
