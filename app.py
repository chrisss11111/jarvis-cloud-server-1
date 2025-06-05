from flask import Flask, request, jsonify
from gtts import gTTS
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/process_audio', methods=['POST'])
def process_audio():
    audio_text = request.form.get("text", "")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": audio_text}]
    )
    answer = response.choices[0].message["content"]
    tts = gTTS(answer)
    tts.save("response.mp3")
    with open("response.mp3", "rb") as f:
        return f.read(), 200, {'Content-Type': 'audio/mpeg'}

@app.route("/")
def index():
    return "Jarvis Cloud Server is running."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)