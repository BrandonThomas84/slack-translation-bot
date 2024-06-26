import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from google.cloud import translate_v2 as translate

load_dotenv()

app = Flask(__name__)

# Slack and Google API credentials from environment variables
SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

slack_client = WebClient(token=SLACK_BOT_TOKEN)
translate_client = translate.Client()

@app.route('/slack/events', methods=['POST'])
def slack_events():
    data = request.json

    if 'challenge' in data:
        return jsonify({'challenge': data['challenge']})

    if 'event' in data:
        event = data['event']
        
        if event.get('type') == 'message_action':
            user_id = event.get('user')
            message_text = event.get('message').get('text')
            channel_id = event.get('channel')
            message_ts = event.get('message_ts')

            if user_id and message_text and channel_id:
                translated_text = translate_text(message_text, target_language='uk' if is_english(message_text) else 'en')
                post_translation(channel_id, message_ts, translated_text)

    return jsonify({'status': 'ok'})

def translate_text(text, target_language):
    result = translate_client.translate(text, target_language=target_language)
    return result['translatedText']

def is_english(text):
    # A simple heuristic to determine if the text is in English
    # This can be improved with more sophisticated language detection
    return all(ord(c) < 128 for c in text)

def post_translation(channel_id, message_ts, translated_text):
    try:
        slack_client.chat_postMessage(
            channel=channel_id,
            text=f"Translated text: {translated_text}",
            thread_ts=message_ts
        )
    except SlackApiError as e:
        print(f"Error posting message: {e.response['error']}")

if __name__ == '__main__':
    app.run(port=3000)
