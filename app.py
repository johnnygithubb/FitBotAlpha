import Flask
import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
openai.api_key = "your_openai_api_key_here"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['text']
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=user_input,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return jsonify({'response': response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(debug=True)