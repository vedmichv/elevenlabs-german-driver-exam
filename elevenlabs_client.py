import os
import requests
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
VOICE_ID = os.getenv('ELEVENLABS_VOICE_ID', 'YOUR_TEACHER_VOICE_ID')
ELEVENLABS_API_URL = 'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}'

# Set your preferred voice_id in the .env file as ELEVENLABS_VOICE_ID
MODEL_ID = 'eleven_multilingual_v2'
SPEED = 0.6
STABILITY = 0.9
SIMILARITY_BOOST = 0.85


def generate_audio(ssml_text, output_path, phrase, retries=3):
    if not ELEVENLABS_API_KEY:
        raise ValueError('ELEVENLABS_API_KEY not set in environment!')
    if not VOICE_ID or VOICE_ID == 'YOUR_TEACHER_VOICE_ID':
        raise ValueError('ELEVENLABS_VOICE_ID not set in environment or is using the default placeholder!')
    url = ELEVENLABS_API_URL.format(voice_id=VOICE_ID)
    headers = {
        'xi-api-key': ELEVENLABS_API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'audio/mpeg',
    }
    payload = {
        'text': ssml_text,
        'model_id': MODEL_ID,
        'voice_settings': {
            'stability': STABILITY,
            'similarity_boost': SIMILARITY_BOOST,
            'style': 0.0,
            'use_speaker_boost': True
        },
        'speed': SPEED,
        'output_format': 'mp3_44100_128',
        'text_type': 'ssml',
    }
    for attempt in range(1, retries + 1):
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            if response.status_code == 200:
                return response.content
            else:
                print(f"[Attempt {attempt}] Error: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"[Attempt {attempt}] Exception: {e}")
        time.sleep(2 * attempt)
    raise RuntimeError(f"Failed to generate audio for '{phrase}' after {retries} attempts.")

# Set ELEVENLABS_VOICE_ID in your .env file to your ElevenLabs teacher/narrator voice ID. 