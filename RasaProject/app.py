from flask import Flask, render_template, request, jsonify
import requests

RASA_API_URL = 'http://localhost:5005/webhooks/rest/webhook'
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    user_message = request.json.get('message')
    print("User Message:", user_message)

    if not user_message:
        return jsonify({'response': 'No message provided'})

    rasa_response = requests.post(RASA_API_URL, json={'message': user_message})
    rasa_response_json = rasa_response.json()

    print("Rasa Response:", rasa_response_json)

    if rasa_response_json:
        bot_response = rasa_response_json[0].get('text', 'Sorry, I didn\'t understand that.')
    else:
        bot_response = 'Sorry, I didn\'t understand that.'

    return jsonify({'response': bot_response})

if __name__ == "__main__":
    app.run(debug=True, port=3000)

