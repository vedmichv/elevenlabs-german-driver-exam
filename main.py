import os
import csv
import datetime
from elevenlabs_client import generate_audio
from dotenv import load_dotenv
import re
import glob
from pydub import AudioSegment
import tempfile

# Load environment variables
load_dotenv()

ELEVENLABS_VOICE_ID_GERMAN = os.getenv('ELEVENLABS_VOICE_ID_GERMAN')
ELEVENLABS_VOICE_ID_RUSSIAN = os.getenv('ELEVENLABS_VOICE_ID_RUSSIAN')

INPUT_CSV = 'inputs/German-Russian_01.csv'
OUTPUT_DIR = 'outputs'
CSV_SOURCE = 'german-russian_01'
DATECODE = datetime.datetime.now().strftime('%Y-%m-%d')


def build_ssml(german, russian):
    """
    Build SSML text for ElevenLabs API: German, 1s break, Russian, 2s break, German, 2s break, German, 1s break, Russian, 2s break, German, 2s break, German.
    """
    return f'{german}. <break time="1s" /> {russian}. <break time="2s" /> {german}. <break time="2s" /> {german}. <break time="1s" /> {russian}. <break time="2s" /> {german}. <break time="2s" /> {german}.'


def build_segments(german, russian):
    """
    Returns a list of (text, voice_id, pause_seconds) tuples for the sequence:
    German, 1s pause, Russian, 2s pause, German, 2s pause, German
    """
    G = (german, ELEVENLABS_VOICE_ID_GERMAN)
    R = (russian, ELEVENLABS_VOICE_ID_RUSSIAN)
    return [
        (G[0], G[1], 0),
        (None, None, 1),
        (R[0], R[1], 0),
        (None, None, 2),
        (G[0], G[1], 0),
        (None, None, 2),
        (G[0], G[1], 0),
    ]


def main():
    csv_files = glob.glob(os.path.join('inputs', '*.csv'))
    for csv_file in csv_files:
        with open(csv_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for idx, row in enumerate(reader, 1):
                german = row['germanphrase'].strip()
                russian = row['russiantranslation'].strip()
                if not german or not russian:
                    continue
                first5 = '_'.join(re.sub(r'[^ -äöüß ]', '', german.lower()).split()[:5])
                filename = f"{idx:03d}-{first5}.mp3"
                output_path = os.path.join(OUTPUT_DIR, filename)
                print(f"Generating audio for: {german} from {os.path.basename(csv_file)} ...")
                segments = build_segments(german, russian)
                audio_segments = []
                for i, (text, voice_id, pause) in enumerate(segments):
                    if text:
                        try:
                            audio_bytes = generate_audio(text, None, text, voice_id=voice_id)
                            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tempf:
                                tempf.write(audio_bytes)
                                temp_path = tempf.name
                            audio = AudioSegment.from_file(temp_path, format='mp3')
                            os.unlink(temp_path)
                        except Exception as e:
                            print(f"Error generating audio for '{text}': {e}")
                            continue
                        audio_segments.append(audio)
                    if pause > 0:
                        silence = AudioSegment.silent(duration=int(pause * 1000))
                        audio_segments.append(silence)
                if audio_segments:
                    final_audio = audio_segments[0]
                    for seg in audio_segments[1:]:
                        final_audio += seg
                    final_audio.export(output_path, format='mp3')
                    print(f"Saved: {output_path}")

if __name__ == "__main__":
    main() 