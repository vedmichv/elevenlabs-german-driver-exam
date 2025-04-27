## Best Practices for Interacting with the ElevenLabs API for Teacher-Style, Slow, and Pronunciation-Focused Speech

To generate speech with ElevenLabs API that sounds like a careful, attentive teacher-speaking slowly, emphasizing pronunciation, and using natural pauses-follow these best practices:

**1. Choose the Right Voice and Model**
- Select a voice from the ElevenLabs library that matches a clear, articulate, and friendly teaching style. Consider voices designed for narration or e-learning, as these are often optimized for clarity and instructional tone[1][7][8].
- For the highest quality and most nuanced delivery, use the `multilingual_v2` model[1][8].

**2. Control Speech Speed**
- Use the API’s `speed` parameter to slow down the speech. The default is `1.0`; set it between `0.7` and `0.9` for a slower, more deliberate pace[3][5].
- Example:  
  ```json
  {
    "voice_id": "UgBBYS2sOqTuMpoF3BR0",
    "text": "Let's learn how to pronounce this word.",
    "speed": 0.8
  }
  ```
- Slower speeds help with clarity and allow listeners to follow along, especially for language learning or pronunciation exercises[3][5][6].

**3. Add Pauses for Emphasis and Clarity**
- Insert SSML `<break time="x.xs" />` tags to create natural pauses, up to 3 seconds each[2][5].
- Example:  
  ```
  "First, let's say the word. <break time=\"1.5s\" /> Now, repeat after me."
  ```
- Use pauses at key points: before/after important words, between instructions, or to allow repetition[2][5].
- Alternatively, you can use dashes (-) or ellipses (...) for shorter, less formal pauses, but SSML tags are more reliable for precise timing[5][4].

**4. Emphasize Pronunciation**
- For tricky words, consider breaking them into syllables with short pauses, e.g.,  
  ```
  "Let's say the word: pro <break time=\"0.5s\" /> nun <break time=\"0.5s\" /> ci <break time=\"0.5s\" /> a <break time=\"0.5s\" /> tion."
  ```
- Use phonetic spelling or explicit instructions in the text to guide the AI’s pronunciation[8].
- Use punctuation (commas, periods) to encourage the AI to enunciate and pause naturally[8].

**5. Adjust Voice Settings for Clarity and Consistency**
- Set `stability` higher for a steady, teacher-like tone; lower it slightly if you want more natural expressiveness[3][7][8].
- Use `similarity_boost` to ensure the voice closely matches your chosen teacher persona[3][8].
- If available, adjust the `style` parameter to enhance the instructional delivery[3][8].

**6. Write Clear, Instructional Text**
- Use short, simple sentences and proper punctuation for the best results[7][8].
- Write as you would speak when teaching:  
  - "Listen carefully. <break time=\"1s\" /> Now, repeat after me."
- For emphasis, use capitalization sparingly or add SSML `<emphasis>` tags if supported.

**7. Test and Iterate**
- Experiment with different voices, speeds, and pause placements to achieve the most natural and effective delivery for your use case[5][7][8].
- Listen to the generated audio and adjust your prompts and settings as needed.

---

## Example API Prompt for a Teacher Role

```json
{
  "voice_id": "teacher_voice_id",
  "text": "Let's practice together. <break time=\"1s\" /> Please repeat: pro <break time=\"0.5s\" /> nun <break time=\"0.5s\" /> ci <break time=\"0.5s\" /> a <break time=\"0.5s\" /> tion. <break time=\"2s\" /> Excellent! Now, let's try it in a sentence.",
  "speed": 0.8,
  "stability": 0.9,
  "similarity_boost": 0.85
}
```

---

## Summary Table: Key Controls

| Feature           | How to Use                                       | Effect                                  |
|-------------------|--------------------------------------------------|-----------------------------------------|
| Voice selection   | Choose teacher/narrator voice                    | Sets tone and clarity                   |
| Speed             | Set `speed` to 0.7–0.9                           | Slows down speech                       |
| Pauses            | Use `<break time="x.xs" />` in text              | Adds natural pauses                     |
| Pronunciation     | Break words with pauses, use phonetic spelling   | Improves clarity                        |
| Stability         | Set higher for steady tone                       | Consistent, teacher-like delivery       |
| Similarity_boost  | Adjust for closer match to chosen voice          | Maintains intended persona              |
| Punctuation       | Use commas, periods for natural phrasing         | Guides pacing and pronunciation         |

---

By combining these best practices-thoughtful text design, strategic use of pauses, speed control, and careful voice selection-you can create highly effective, teacher-style audio with ElevenLabs API that is slow, clear, and attentive to pronunciation[1][2][3][5][7][8].

Sources
[1] Text to Speech | ElevenLabs Documentation https://elevenlabs.io/docs/capabilities/text-to-speech
[2] Pause support via API and speech synthesis editor - ElevenLabs https://elevenlabs.io/blog/pause-support-via-api-and-speech-synthesis-editor
[3] Get voice settings | ElevenLabs Documentation https://elevenlabs.io/docs/api-reference/voices/get-settings
[4] ElevenLabs: How to Add Pauses - YouTube https://www.youtube.com/watch?v=HIw95j_hbt4
[5] elevenlabs-docs/fern/docs/pages/best-practices/prompting/controls ... https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/best-practices/prompting/controls.mdx?plain=1
[6] Eleven Labs: How To Slow Down Voice - YouTube https://www.youtube.com/watch?v=827IgrKAmXE
[7] A Complete Guide to ElevenLabs: Create Natural, Human-Like Voices https://learnprompting.org/blog/guide-elevenlabs
[8] ElevenLabs Voice AI Guide: TTS and Voice Synthesis | APIpie https://apipie.ai/docs/Models/Eleven_Labs
[9] Prompting — ElevenLabs Documentation https://elevenlabs.io/docs/best-practices/prompting
[10] Controls | ElevenLabs Documentation https://elevenlabs.io/docs/best-practices/prompting/controls
[11] Create speech | ElevenLabs Documentation https://elevenlabs.io/docs/api-reference/text-to-speech/convert
[12] Give Your Web Apps a Voice with Eleven Labs AI - Vue School Articles https://vueschool.io/articles/vuejs-tutorials/nuxt-content-text-to-speech-with-eleven-labs/
[13] ElevenLabs Speech Synthesis Prompting Guide (Full Tutorial) https://www.youtube.com/watch?v=YXdNidCUdrk
[14] Text to Speech - ElevenLabs https://help.elevenlabs.io/hc/en-us/sections/23795023293073-Text-to-Speech
[15] How to Build an Audio Chatbot with Nextjs, OpenAI, and ElevenLabs https://blog.bolajiayodeji.com/how-to-build-an-audio-chatbot-with-nextjs-openai-and-elevenlabs
[16] Adjusting speed? : r/ElevenLabs - Reddit https://www.reddit.com/r/ElevenLabs/comments/113gl18/adjusting_speed/
[17] A Beginner's Guide to the ElevenLabs API: Transform Text and ... https://www.datacamp.com/tutorial/beginners-guide-to-elevenlabs-api
[18] Elevenlabs Text To Speech Voice API: Easy Starter Guide - PlayHT https://play.ht/blog/elevenlabs-text-to-speech-voice-api/
[19] Voices | ElevenLabs Documentation https://elevenlabs.io/docs/capabilities/voices
[20] Models | ElevenLabs Documentation https://elevenlabs.io/docs/models
