from flask import Flask, request, jsonify
from google_calendar import add_google_calendar_event
from weather import get_weather
from news import get_news
from nlp import process_nlp

app = Flask(__name__)

# Command processing logic
def process_command(command):
    if 'weather' in command:
        return get_weather()
    elif 'schedule' in command:
        return add_google_calendar_event(command)
    elif 'news' in command:
        return get_news()
    else:
        return process_nlp(command)

@app.route('/command', methods=['POST'])
def handle_command():
    data = request.json
    command = data.get('command')
    response = process_command(command)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
