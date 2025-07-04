# German-Russian Audio Generator with ElevenLabs

## 📚 Goal

This project will generate audio files where:

- The German phrase is spoken.
- 1 second pause.
- Russian translation is spoken.
- 2 seconds pause.
- German phrase is spoken.
- 2 seconds pause.
- German phrase is spoken.

We will use **ElevenLabs API** to synthesize the audio.  
Input: German phrases + Russian translations (from `.md` or `.csv` file).  
Output: Ready MP3 audio files for each phrase.

---

## 📁 Project Structure

```
/inputs          # Input MD or CSV files (phrases)
/outputs         # Final audio files (MP3)
/temp            # (Optional) Temporary files if needed
main.py          # Main script
parser.py        # Parsing input files
elevenlabs_client.py # API interactions
requirements.txt # Python dependencies
README.md        # This file
```

---

## 🛠 Tasks Checklist

### 🗂️ 1. Prepare the Input

~SKIPPED~ (CSV file already exists: `inputs/German-Russian_01.csv`)

---

### 📝 2. Build the Speaking Script

For each phrase:

- [x] Create a full text script for audio generation.
- [x] Add pause instructions:
    - German phrase
    - <break time="1s" />
    - Russian translation
    - <break time="2s" />
    - German phrase (repeat)
- [x] Output file naming: include the CSV file name as the source and a timecode (YYYY-MM-DD) in the filename.
    - Example: `german-russian_01_YYYY-MM-DD_guten_morgen.mp3`

✅ Example built text:
```
Guten Morgen. <break time="1s" /> Доброе утро. <break time="2s" /> Guten Morgen. <break time="2s" /> Guten Morgen. <break time="1s" /> Доброе утро. <break time="2s" /> Guten Morgen. <break time="2s" /> Guten Morgen.
```

---

### 🌐 3. Integrate with ElevenLabs API

- [x] Create a Python client (`elevenlabs_client.py`) to talk to ElevenLabs.
- [x] Load API Key from `.env` file.
- [x] Send the prepared text to ElevenLabs.
- [x] Handle timeouts, retries, and errors properly.
- [x] Receive the audio stream.

✅ Hint: Use `requests` library.

---

### 💾 4. Save the Audio Files

- [x] Save the generated audio files in `/outputs` folder.
- [x] File naming: use German phrase in lowercase with underscores.
    - Example: `guten_morgen.mp3`

---

### 🧹 5. Add Logging

- [x] Print clear messages during the script execution.
    - Example: "Generating audio for: Guten Morgen..."
- [x] Print errors separately if generation fails.

---

### 📦 6. Final Touches

- [x] Create a `requirements.txt` listing all Python packages.
- [x] Make sure the project can run by using `python main.py`.

✅ Required libraries:
```
pandas
requests
python-dotenv
markdown
pydub (optional, for custom pauses)
```

---

## 🚀 How to Run the App

1. **Install dependencies (Python 3.12 required):**
   ```sh
   uv pip install -r requirements.txt
   ```
   > **Note:** You must use Python 3.12 (not 3.13+) for compatibility with pydub. If you need to create a new environment:
   > ```sh
   > uv venv --python=3.12 venv
   > source venv/bin/activate
   > uv pip install -r requirements.txt
   > ```
   > Also, make sure you have `ffmpeg` installed on your system (required by pydub).

2. **Set up your `.env` file:**
   - Make sure you have your `ELEVENLABS_API_KEY`, `ELEVENLABS_VOICE_ID_GERMAN`, and `ELEVENLABS_VOICE_ID_RUSSIAN` set in the `.env` file.

3. **Run the app:**
   ```sh
   python main.py
   ```
   The generated audio files will appear in the `outputs/` directory.

---

## 🔊 Audio Generation Sequence

For each phrase, the generated audio will follow this sequence:
- German phrase (German voice)
- 1 second pause
- Russian translation (Russian voice)
- 2 seconds pause
- German phrase (German voice)
- 2 seconds pause
- German phrase (German voice)

---

## 🔊 How to Change the ElevenLabs Voice ID

To use a different voice for audio generation, update the `ELEVENLABS_VOICE_ID` in your `.env` file.

### 1. Edit the `.env` file manually:
Open the `.env` file in your favorite editor and set:
```
ELEVENLABS_VOICE_ID=your_new_voice_id_here
```
Replace `your_new_voice_id_here` with the actual voice ID you want to use (find it in your ElevenLabs dashboard).

### 2. Or use this command in your terminal:
```sh
echo 'ELEVENLABS_VOICE_ID=your_new_voice_id_here' >> .env
```
*(This will add or update the variable. If it already exists, you may want to edit the file manually to avoid duplicates.)*

---

## 💬 Notes

- Pauses might be added by using ElevenLabs' native <break> tags if they support it, or handled manually in audio editing (later task).
- If needed, later we can split audio files or add background sounds.

