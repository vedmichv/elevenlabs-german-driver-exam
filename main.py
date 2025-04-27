import os
import csv
import datetime
from elevenlabs_client import generate_audio
from dotenv import load_dotenv
import re
import glob

# Load environment variables
load_dotenv()

INPUT_CSV = 'inputs/German-Russian_01.csv'
OUTPUT_DIR = 'outputs'
CSV_SOURCE = 'german-russian_01'
DATECODE = datetime.datetime.now().strftime('%Y-%m-%d')


def build_ssml(german, russian):
    """
    Build SSML text for ElevenLabs API: German, 1s break, Russian, 2s break, German, 2s break, German, 1s break, Russian, 2s break, German, 2s break, German.
    """
    return f'{german}. <break time="1s" /> {russian}. <break time="2s" /> {german}. <break time="2s" /> {german}. <break time="1s" /> {russian}. <break time="2s" /> {german}. <break time="2s" /> {german}.'


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
                ssml_text = build_ssml(german, russian)
                # Get first 5 words from German phrase, lowercase, underscores, remove punctuation
                first5 = '_'.join(re.sub(r'[^\wäöüß ]', '', german.lower()).split()[:5])
                filename = f"{idx:03d}-{first5}.mp3"
                output_path = os.path.join(OUTPUT_DIR, filename)
                print(f"Generating audio for: {german} from {os.path.basename(csv_file)} ...")
                try:
                    audio_content = generate_audio(ssml_text, output_path, german)
                    with open(output_path, 'wb') as f:
                        f.write(audio_content)
                    print(f"Saved: {output_path}")
                except Exception as e:
                    print(f"Error generating audio for '{german}': {e}")

if __name__ == "__main__":
    main() 