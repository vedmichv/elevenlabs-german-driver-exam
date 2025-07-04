TITLE: Generate Speech with Text to Speech API
DESCRIPTION: Demonstrates how to use the ElevenLabs Text to Speech API to convert text into lifelike audio using the SDK.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/quickstart.mdx#_snippet_1

LANGUAGE: python
CODE:
```
from elevenlabs import generate, play

audio = generate(
    text="Hello! My name is Adam, and I'm a voice assistant.",
    voice="Adam"
)

play(audio)
```

LANGUAGE: typescript
CODE:
```
import { generate, play } from 'elevenlabs';

async function main() {
  const audio = await generate({
    text: "Hello! My name is Adam, and I'm a voice assistant.",
    voice: "Adam"
  });

  play(audio);
}

main();
```

----------------------------------------

TITLE: Add Instant Voice Clone via ElevenLabs API (Python, TypeScript)
DESCRIPTION: This code snippet demonstrates how to programmatically create an Instant Voice Clone using the ElevenLabs API. It initializes the ElevenLabs client with an API key and then calls the `voices.add` method, providing a name for the voice and paths to audio files. The quality of the cloned voice improves with more audio input files.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/voices/clone-voice.mdx#_snippet_0

LANGUAGE: python
CODE:
```
# example.py
import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from io import BytesIO

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

voice = elevenlabs.voices.add(
    name="My Voice Clone",
    # Replace with the paths to your audio files.
    # The more files you add, the better the clone will be.
    files=[BytesIO(open("/path/to/your/audio/file.mp3", "rb").read())]
)

print(voice.voice_id)
```

LANGUAGE: typescript
CODE:
```
// example.mts
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
import "dotenv/config";
import fs from "node:fs";

const elevenlabs = new ElevenLabsClient();

const voice = await elevenlabs.voices.add({
    name: "My Voice Clone",
    // Replace with the paths to your audio files.
    // The more files you add, the better the clone will be.
    files: [
        fs.createReadStream(
            "/path/to/your/audio/file.mp3",
        ),
    ],
});

console.log(voice.voice_id);
```

----------------------------------------

TITLE: Install ElevenLabs SDK for Speech-to-Text
DESCRIPTION: Instructions to install the ElevenLabs SDK for Python using pip or for JavaScript using npm, a prerequisite for speech-to-text functionalities.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/speech-to-text/streaming.mdx#_snippet_0

LANGUAGE: bash Python
CODE:
```
pip install elevenlabs
```

LANGUAGE: bash JavaScript
CODE:
```
npm install @elevenlabs/elevenlabs-js
```

----------------------------------------

TITLE: Install ElevenLabs SDK
DESCRIPTION: This snippet demonstrates how to install the ElevenLabs SDK for text-to-speech conversion using pip for Python and npm for TypeScript/Node.js. It's a prerequisite for using the ElevenLabs API.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/text-to-speech/streaming.mdx#_snippet_0

LANGUAGE: bash
CODE:
```
pip install elevenlabs
```

LANGUAGE: bash
CODE:
```
npm install @elevenlabs/elevenlabs-js
```

----------------------------------------

TITLE: Define Function to Convert Text to Speech and Save as MP3
DESCRIPTION: This function demonstrates how to convert text into speech using the ElevenLabs SDK and save the output as an MP3 file. It utilizes specific voice settings and handles the API response by writing chunks to a local file. The Python version uses `elevenlabs.text_to_speech.convert` and the TypeScript version uses `elevenlabs.textToSpeech.convert`.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/text-to-speech/streaming.mdx#_snippet_3

LANGUAGE: Python
CODE:
```
import os
import uuid
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
elevenlabs = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)


def text_to_speech_file(text: str) -> str:
    # Calling the text_to_speech conversion API with detailed parameters
    response = elevenlabs.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB", # Adam pre-made voice
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2_5", # use the turbo model for low latency
        # Optional voice settings that allow you to customize the output
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
            speed=1.0,
        ),
    )

    # uncomment the line below to play the audio back
    # play(response)

    # Generating a unique file name for the output MP3 file
    save_file_path = f"{uuid.uuid4()}.mp3"

    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")

    # Return the path of the saved audio file
    return save_file_path
```

LANGUAGE: TypeScript
CODE:
```
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';
import * as dotenv from 'dotenv';
import { createWriteStream } from 'fs';
import { v4 as uuid } from 'uuid';

dotenv.config();

const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;

const elevenlabs = new ElevenLabsClient({
  apiKey: ELEVENLABS_API_KEY,
});

export const createAudioFileFromText = async (text: string): Promise<string> => {
  return new Promise<string>(async (resolve, reject) => {
    try {
      const audio = await elevenlabs.textToSpeech.convert('JBFqnCBsd6RMkjVDRZzb', {
        modelId: 'eleven_multilingual_v2',
        text,
        outputFormat: 'mp3_44100_128',
        // Optional voice settings that allow you to customize the output
        voiceSettings: {
          stability: 0,
          similarityBoost: 0,
          useSpeakerBoost: true,
          speed: 1.0,
        },
      });

      const fileName = `${uuid()}.mp3`;
      const fileStream = createWriteStream(fileName);

      audio.pipe(fileStream);
      fileStream.on('finish', () => resolve(fileName)); // Resolve with the fileName
      fileStream.on('error', reject);
    } catch (error) {
      reject(error);
    }
  });
};
```

----------------------------------------

TITLE: List Batch Calls API
DESCRIPTION: Retrieve a list of all batch calls associated with your workspace using the ElevenLabs API. This endpoint provides an overview of all initiated batch calls, including their status and progress.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/guides/batch-calls.mdx#_snippet_0

LANGUAGE: APIDOC
CODE:
```
GET /docs/api-reference/batch-calling/list
Description: Retrieve all batch calls in your workspace.
```

----------------------------------------

TITLE: Convert Audio to Text using ElevenLabs Speech to Text API
DESCRIPTION: This snippet demonstrates how to use the ElevenLabs SDK to convert an audio file from a URL into text. It shows fetching audio, initializing the client, and calling the `speech_to_text.convert` method with various options like model ID, audio event tagging, language code, and diarization.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/speech-to-text/quickstart.mdx#_snippet_0

LANGUAGE: python
CODE:
```
# example.py
import os
from dotenv import load_dotenv
from io import BytesIO
import requests
from elevenlabs.client import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio_url = (
    "https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3"
)
response = requests.get(audio_url)
audio_data = BytesIO(response.content)

transcription = elevenlabs.speech_to_text.convert(
    file=audio_data,
    model_id="scribe_v1", # Model to use, for now only "scribe_v1" is supported
    tag_audio_events=True, # Tag audio events like laughter, applause, etc.
    language_code="eng", # Language of the audio file. If set to None, the model will detect the language automatically.
    diarize=True, # Whether to annotate who is speaking
)

print(transcription)
```

LANGUAGE: typescript
CODE:
```
// example.mts
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
import "dotenv/config";

const elevenlabs = new ElevenLabsClient();

const response = await fetch(
  "https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3"
);
const audioBlob = new Blob([await response.arrayBuffer()], { type: "audio/mp3" });

const transcription = await elevenlabs.speechToText.convert({
  file: audioBlob,
  modelId: "scribe_v1", // Model to use, for now only "scribe_v1" is supported.
  tagAudioEvents: true, // Tag audio events like laughter, applause, etc.
  languageCode: "eng", // Language of the audio file. If set to null, the model will detect the language automatically.
  diarize: true // Whether to annotate who is speaking
});

console.log(transcription);
```

----------------------------------------

TITLE: Configure ElevenLabs API Key in .env
DESCRIPTION: Demonstrates how to set up the `ELEVENLABS_API_KEY` in a `.env` file, ensuring secure access to the ElevenLabs API.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/speech-to-text/synchronous.mdx#_snippet_2

LANGUAGE: python
CODE:
```
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

----------------------------------------

TITLE: Install Node.js Dependencies for Conversational AI
DESCRIPTION: Lists and installs the core `npm` packages required for the application, including Fastify for web server functionality, `ws` for WebSocket communication, `dotenv` for environment variable management, and Fastify plugins.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/guides/twilio-custom-server.mdx#_snippet_1

LANGUAGE: bash
CODE:
```
npm install @fastify/formbody @fastify/websocket dotenv fastify ws
```

----------------------------------------

TITLE: Start a conversational AI session
DESCRIPTION: Initiate the conversation session with the configured ElevenLabs agent.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/libraries/python.mdx#_snippet_8

LANGUAGE: python
CODE:
```
conversation.start_session()
```

----------------------------------------

TITLE: Expose Local Application with ngrok
DESCRIPTION: This shell command uses ngrok to create a publicly accessible URL for a local application running on port 5000. This is necessary for Twilio to be able to send requests to your local development server.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/text-to-speech/twilio.mdx#_snippet_8

LANGUAGE: shell
CODE:
```
ngrok http 5000
```

----------------------------------------

TITLE: Define Custom LLM Parameters for ElevenLabs Conversation in Python
DESCRIPTION: This snippet demonstrates how to define custom parameters using a Python dictionary and pass them to the `ConversationConfig` object for use with ElevenLabs conversational AI.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/customization/custom-llm/overview.mdx#_snippet_10

LANGUAGE: python
CODE:
```
from elevenlabs.conversational_ai.conversation import Conversation, ConversationConfig

extra_body_for_convai = {
    "UUID": "123e4567-e89b-12d3-a456-426614174000",
    "parameter-1": "value-1",
    "parameter-2": "value-2",
}

config = ConversationConfig(
    extra_body=extra_body_for_convai,
)
```

----------------------------------------

TITLE: Send Text to ElevenLabs Text-to-Speech WebSocket API
DESCRIPTION: This snippet demonstrates how to establish a WebSocket connection and send the initial voice settings, followed by the actual text content to be converted to speech. It also shows how to send an empty string to signal the end of the text sequence and close the connection.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/websockets.mdx#_snippet_3

LANGUAGE: python
CODE:
```
async def text_to_speech_ws_streaming(voice_id, model_id):
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({
            "text": " ",
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.8, "use_speaker_boost": False},
            "generation_config": {
                "chunk_length_schedule": [120, 160, 250, 290]
            },
            "xi_api_key": ELEVENLABS_API_KEY,
        }))

        text = "The twilight sun cast its warm golden hues upon the vast rolling fields, saturating the landscape with an ethereal glow. Silently, the meandering brook continued its ceaseless journey, whispering secrets only the trees seemed privy to."
        await websocket.send(json.dumps({"text": text}))

        // Send empty string to indicate the end of the text sequence which will close the WebSocket connection
        await websocket.send(json.dumps({"text": ""}))
```

LANGUAGE: typescript
CODE:
```
const text =
  'The twilight sun cast its warm golden hues upon the vast rolling fields, saturating the landscape with an ethereal glow. Silently, the meandering brook continued its ceaseless journey, whispering secrets only the trees seemed privy to.';

websocket.on('open', async () => {
  websocket.send(
    JSON.stringify({
      text: ' ',
      voice_settings: {
        stability: 0.5,
        similarity_boost: 0.8,
        use_speaker_boost: false,
      },
      generation_config: { chunk_length_schedule: [120, 160, 250, 290] },
    })
  );

  websocket.send(JSON.stringify({ text: text }));

  // Send empty string to indicate the end of the text sequence which will close the websocket connection
  websocket.send(JSON.stringify({ text: '' }));
});
```

----------------------------------------

TITLE: Initiate Asynchronous Speech-to-Text with Webhooks (Python/TypeScript)
DESCRIPTION: This code demonstrates how to start an asynchronous speech-to-text transcription using the ElevenLabs SDKs. By setting the `webhook` parameter to `true`, you enable notifications to your configured webhook endpoint upon task completion, eliminating the need for continuous polling.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/speech-to-text/webhooks.mdx#_snippet_0

LANGUAGE: python
CODE:
```
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

def transcribe_with_webhook(audio_file):
  try:
    result = elevenlabs.speech_to_text.convert(
      file=audio_file,
      model_id="scribe_v1",
      webhook=True,
    )
    print(f"Transcription started: {result.task_id}")
    return result
  except Exception as e:
    print(f"Error starting transcription: {e}")
    raise e
```

LANGUAGE: typescript
CODE:
```
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';

const elevenlabs = new ElevenLabsClient({
  apiKey: process.env.ELEVENLABS_API_KEY,
});

async function transcribeWithWebhook(audioFile) {
  try {
    const result = await elevenlabs.speechToText.convert({
      file: audioFile,
      modelId: 'scribe_v1',
      webhook: true,
    });

    console.log('Transcription started:', result.taskId);
    return result;
  } catch (error) {
    console.error('Error starting transcription:', error);
    throw error;
  }
}
```

----------------------------------------

TITLE: Install ElevenLabs SDK
DESCRIPTION: Instructions to install the ElevenLabs SDK for Python and TypeScript, including dependencies for audio playback.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/quickstart.mdx#_snippet_0

LANGUAGE: python
CODE:
```
pip install elevenlabs
```

LANGUAGE: typescript
CODE:
```
npm install elevenlabs
```

----------------------------------------

TITLE: Perform Streaming Speech-to-Text Transcription
DESCRIPTION: Code examples in Python and JavaScript demonstrating how to use the ElevenLabs SDK's `speech_to_text.stream` method to transcribe audio from a URL in real-time, printing the transcribed text chunks.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/speech-to-text/streaming.mdx#_snippet_3

LANGUAGE: python
CODE:
```
import os
from typing import IO
from io import BytesIO
from elevenlabs.client import ElevenLabs
import requests

from dotenv import load_dotenv
load_dotenv()

elevenlabs = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio_url = (
    "https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3"
)
response = requests.get(audio_url)
audio_data = BytesIO(response.content)

# Perform the text-to-speech conversion
transcription = elevenlabs.speech_to_text.stream(
    model_id="scribe_v1",
    file=audio_data
)

for chunk in transcription:
    # If you want to extract just the text:
    print(chunk.text)
```

LANGUAGE: javascript
CODE:
```
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';
import * as dotenv from 'dotenv';

dotenv.config();

const elevenlabs = new ElevenLabsClient();

const response = await fetch(
  'https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3'
);
const audioBlob = new Blob([await response.arrayBuffer()], { type: 'audio/mp3' });

const transcription = await elevenlabs.speechToText.stream({
  file: audioBlob,
  modelId: 'scribe_v1',
  maximumSpeakers: 1, // Number of speakers in the audio file
  tagAudioEvents: true, // Tag audio events like laughter, applause, etc.
  speechToTextLanguageCode: 'en', // Language of the audio file
  transcribeVerbatim: false, // Transcribe verbatim sounds like "um" and "ah"
});

for await (const chunk of transcription) {
  console.log(chunk.text);
}
```

----------------------------------------

TITLE: Starting Conversation Session with Agent ID
DESCRIPTION: Illustrates how to initialize a conversation session by directly providing an `agentId`. This method is suitable for public agents or scenarios where authorization is handled externally, with the Agent ID acquired from the ElevenLabs UI.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/libraries/javascript.mdx#_snippet_3

LANGUAGE: js
CODE:
```
const conversation = await Conversation.startSession({
  agentId: '<your-agent-id>'
});
```

----------------------------------------

TITLE: Create ElevenLabs Transcription Model
DESCRIPTION: Illustrates how to create a transcription model instance using the `elevenlabs.transcription()` factory method, specifying the model ID.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/speech-to-text/vercel-ai-sdk.mdx#_snippet_4

LANGUAGE: ts
CODE:
```
const model = elevenlabs.transcription('scribe_v1');
```

----------------------------------------

TITLE: Install ElevenLabs React SDK
DESCRIPTION: Instructions to install the ElevenLabs React SDK using common package managers like npm, yarn, or pnpm.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/libraries/react.mdx#_snippet_0

LANGUAGE: shell
CODE:
```
npm install @elevenlabs/react
# or
yarn add @elevenlabs/react
# or
pnpm install @elevenlabs/react
```

----------------------------------------

TITLE: Agent Response Correction Event and Handler
DESCRIPTION: This event provides a truncated version of the agent's response, typically sent after an interruption. It is used to update the displayed message, ensuring conversation accuracy and reflecting real-time changes.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/customization/client-events.mdx#_snippet_5

LANGUAGE: javascript
CODE:
```
{
  "type": "agent_response_correction",
  "agent_response_correction_event": {
    "original_agent_response": "Let me tell you about the complete history...",
    "corrected_agent_response": "Let me tell you about..."
  }
}
```

LANGUAGE: javascript
CODE:
```
websocket.on('agent_response_correction', (event) => {
  const { agent_response_correction_event } = event;
  const { corrected_agent_response } = agent_response_correction_event;
  displayAgentMessage(corrected_agent_response);
});
```

----------------------------------------

TITLE: Handle Incoming Twilio Calls and Initiate WebSocket Stream
DESCRIPTION: This TypeScript code excerpt details the Express POST endpoint (`/call/incoming`) that Twilio invokes upon an incoming call. It constructs a TwiML response that instructs Twilio to connect the call to a WebSocket stream, redirecting the audio flow to the application's `/call/connection` endpoint for real-time processing.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/text-to-speech/twilio.mdx#_snippet_5

LANGUAGE: ts
CODE:
```
function startApp() {
  app.post('/call/incoming', (_, res: Response) => {
    const twiml = new VoiceResponse();

    twiml.connect().stream({
      url: `wss://${process.env.SERVER_DOMAIN}/call/connection`,
    });

    res.writeHead(200, { 'Content-Type': 'text/xml' });
    res.end(twiml.toString());
  });
```

----------------------------------------

TITLE: Passing Dynamic Variables to ElevenLabs Conversational AI in JavaScript
DESCRIPTION: This JavaScript snippet illustrates how to start an ElevenLabs Conversation session, including requesting microphone access and providing dynamicVariables to the startSession method. It highlights the use of the @elevenlabs/client SDK.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/customization/dynamic-variables.mdx#_snippet_1

LANGUAGE: JavaScript
CODE:
```
import { Conversation } from '@elevenlabs/client';

class VoiceAgent {
  ...

  async startConversation() {
    try {
        // Request microphone access
        await navigator.mediaDevices.getUserMedia({ audio: true });

        this.conversation = await Conversation.startSession({
            agentId: 'agent_id_goes_here', // Replace with your actual agent ID

            dynamicVariables: {
                user_name: 'Angelo'
            },

            ... add some callbacks here
        });
    } catch (error) {
        console.error('Failed to start conversation:', error);
        alert('Failed to start conversation. Please ensure microphone access is granted.');
    }
  }
}
```

----------------------------------------

TITLE: Passing Dynamic Variables to ElevenLabs Conversational AI in Swift
DESCRIPTION: This Swift example shows how to define various types of dynamic variables (string, number, int, boolean) and pass them within a SessionConfig object when starting an ElevenLabs Conversation session.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/customization/dynamic-variables.mdx#_snippet_2

LANGUAGE: Swift
CODE:
```
let dynamicVars: [String: DynamicVariableValue] = [
  "customer_name": .string("John Doe"),
  "account_balance": .number(5000.50),
  "user_id": .int(12345),
  "is_premium": .boolean(true)
]

// Create session config with dynamic variables
let config = SessionConfig(
    agentId: "your_agent_id",
    dynamicVariables: dynamicVars
)

// Start the conversation
let conversation = try await Conversation.startSession(
    config: config
)
```

----------------------------------------

TITLE: Execute Streaming Speech-to-Text Script
DESCRIPTION: Commands to run the Python or JavaScript script that performs streaming speech-to-text transcription.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/speech-to-text/streaming.mdx#_snippet_4

LANGUAGE: bash Python
CODE:
```
python speech_to_text_stream.py
```

LANGUAGE: bash TypeScript
CODE:
```
node speechToTextStream.js
```

----------------------------------------

TITLE: Install Core Production Dependencies for ElevenLabs Twilio App
DESCRIPTION: This command installs the essential production libraries required for the application. It includes `@elevenlabs/elevenlabs-js` for interacting with the ElevenLabs API, `express` and `express-ws` for building the web server with WebSocket capabilities, and `twilio` for integrating with Twilio's services.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/text-to-speech/twilio.mdx#_snippet_1

LANGUAGE: bash
CODE:
```
npm install @elevenlabs/elevenlabs-js express express-ws twilio
```

----------------------------------------

TITLE: Integrating Conversational AI Component into Main Page (Next.js)
DESCRIPTION: This snippet demonstrates how to integrate the Conversation component into the main Home page of a Next.js application. It imports the component and renders it within the page's layout, making the conversational AI interface accessible to users.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/guides/nextjs.mdx#_snippet_5

LANGUAGE: tsx
CODE:
```
import { Conversation } from './components/conversation';

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm">
        <h1 className="text-4xl font-bold mb-8 text-center">
          ElevenLabs Conversational AI
        </h1>
        <Conversation />
      </div>
    </main>
  );
}
```

----------------------------------------

TITLE: Installing ElevenLabs Client SDK
DESCRIPTION: Instructions for installing the ElevenLabs JavaScript SDK using common Node.js package managers (npm, yarn, pnpm). This is the initial step to integrate the SDK into your project.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/libraries/javascript.mdx#_snippet_0

LANGUAGE: shell
CODE:
```
npm install @elevenlabs/client
# or
yarn add @elevenlabs/client
# or
pnpm install @elevenlabs/client
```

----------------------------------------

TITLE: Install PyAudio system dependencies on Debian-based Linux
DESCRIPTION: Commands to install necessary system dependencies for PyAudio on Debian-based Linux distributions using `apt-get`.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/libraries/python.mdx#_snippet_2

LANGUAGE: shell
CODE:
```
sudo apt-get update
sudo apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev libasound-dev libsndfile1-dev -y
```

----------------------------------------

TITLE: Environment Variable Configuration for ElevenLabs API Key
DESCRIPTION: This snippet demonstrates how to set the ElevenLabs API key as an environment variable within a .env file. This approach is recommended for securely storing sensitive API keys, preventing them from being hardcoded directly into application source code.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/snippets/quickstart-api-key.mdx#_snippet_0

LANGUAGE: js
CODE:
```
ELEVENLABS_API_KEY=<your_api_key_here>
```

----------------------------------------

TITLE: Initialize Python Project Directory
DESCRIPTION: Commands to create and navigate into the project directory for the Python implementation of the conversational AI application.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/guides/twilio-custom-server.mdx#_snippet_5

LANGUAGE: bash
CODE:
```
mkdir conversational-ai-twilio
cd conversational-ai-twilio
```

----------------------------------------

TITLE: Process Voice, Audio, and Video Messages with grammY Bot
DESCRIPTION: This code shows how a grammY bot can listen for specific message types (voice, audio, video). It extracts file metadata, provides an immediate user response, and uses Supabase Background Tasks (`EdgeRuntime.waitUntil`) to asynchronously initiate transcription of the received media file.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/speech-to-text/telegram-bot.mdx#_snippet_7

LANGUAGE: ts
CODE:
```
bot.on([':voice', ':audio', ':video'], async (ctx) => {
  try {
    const file = await ctx.getFile();
    const fileURL = `https://api.telegram.org/file/bot${telegramBotToken}/${file.file_path}`;
    const fileMeta = ctx.message?.video ?? ctx.message?.voice ?? ctx.message?.audio;

    if (!fileMeta) {
      return ctx.reply('No video|audio|voice metadata found. Please try again.');
    }

    // Run the transcription in the background.
    EdgeRuntime.waitUntil(
      scribe({
        fileURL,
        fileType: fileMeta.mime_type!,
        duration: fileMeta.duration,
        chatId: ctx.chat.id,
        messageId: ctx.message?.message_id!,
        username: ctx.from?.username || '',
      })
    );

    // Reply to the user immediately to let them know we received their file.
    return ctx.reply('Received. Scribing...');
  } catch (error) {
    console.error(error);
    return ctx.reply(
      'Sorry, there was an error getting the file. Please try again with a smaller file!'
    );
  }
});
```

----------------------------------------

TITLE: Install ElevenLabs SDK with PyAudio for audio I/O
DESCRIPTION: Install the `pyaudio` extra for default audio input/output functionality. This may require additional system dependencies.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/libraries/python.mdx#_snippet_1

LANGUAGE: shell
CODE:
```
pip install "elevenlabs[pyaudio]"
# or
poetry add "elevenlabs[pyaudio]"
```

----------------------------------------

TITLE: Python Twilio WebSocket Handlers
DESCRIPTION: Asynchronous Python functions for managing real-time audio streams with Twilio. This includes handling incoming 'start' and 'media' events, decoding audio data, sending processed audio back to Twilio via WebSocket, and sending 'clear' messages to terminate streams. These functions are typically part of a larger WebSocket server application.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/guides/twilio-custom-server.mdx#_snippet_12

LANGUAGE: python
CODE:
```
async def handle_twilio_message(self, data):
    try:
        if data["event"] == "start":
            self.stream_sid = data["start"]["streamSid"]
            print(f"Started stream with stream_sid: {self.stream_sid}")
        if data["event"] == "media":
            audio_data = base64.b64decode(data["media"]["payload"])
            if self.input_callback:
                self.input_callback(audio_data)
    except Exception as e:
        print(f"Error in input_callback: {e}")

def _output_thread(self):
    while not self.should_stop.is_set():
        asyncio.run(self._send_audio_to_twilio())

async def _send_audio_to_twilio(self):
    try:
        audio = self.output_queue.get(timeout=0.2)
        audio_payload = base64.b64encode(audio).decode("utf-8")
        audio_delta = {
            "event": "media",
            "streamSid": self.stream_sid,
            "media": {"payload": audio_payload}
        }
        await self.websocket.send_json(audio_delta)
    except queue.Empty:
        pass
    except Exception as e:
        print(f"Error sending audio: {e}")

async def _send_clear_message_to_twilio(self):
    try:
        clear_message = {"event": "clear", "streamSid": self.stream_sid}
        await self.websocket.send_json(clear_message)
    except Exception as e:
        print(f"Error sending clear message to Twilio: {e}")
```

----------------------------------------

TITLE: Full Express Server for Twilio Call and ElevenLabs TTS Streaming
DESCRIPTION: This comprehensive TypeScript code defines the core Express server application. It handles incoming Twilio calls, establishes a WebSocket connection, uses the ElevenLabs SDK to generate speech from text, and streams the audio back to Twilio in real-time. It includes all necessary imports, server setup, and helper functions for audio processing.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/text-to-speech/twilio.mdx#_snippet_3

LANGUAGE: ts
CODE:
```
// src/app.ts
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';
import 'dotenv/config';
import express, { Response } from 'express';
import ExpressWs from 'express-ws';
import { Readable } from 'stream';
import VoiceResponse from 'twilio/lib/twiml/VoiceResponse';
import { type WebSocket } from 'ws';

const app = ExpressWs(express()).app;
const PORT: number = parseInt(process.env.PORT || '5000');

const elevenlabs = new ElevenLabsClient();
const voiceId = '21m00Tcm4TlvDq8ikWAM';
const outputFormat = 'ulaw_8000';
const text = 'This is a test. You can now hang up. Thank you.';

function startApp() {
  app.post('/call/incoming', (_, res: Response) => {
    const twiml = new VoiceResponse();

    twiml.connect().stream({
      url: `wss://${process.env.SERVER_DOMAIN}/call/connection`,
    });

    res.writeHead(200, { 'Content-Type': 'text/xml' });
    res.end(twiml.toString());
  });

  app.ws('/call/connection', (ws: WebSocket) => {
    ws.on('message', async (data: string) => {
      const message: {
        event: string;
        start?: { streamSid: string; callSid: string };
      } = JSON.parse(data);

      if (message.event === 'start' && message.start) {
        const streamSid = message.start.streamSid;
        const response = await elevenlabs.textToSpeech.convert(voiceId, {
          modelId: 'eleven_flash_v2_5',
          outputFormat: outputFormat,
          text,
        });

        const readableStream = Readable.from(response);
        const audioArrayBuffer = await streamToArrayBuffer(readableStream);

        ws.send(
          JSON.stringify({
            streamSid,
            event: 'media',
            media: {
              payload: Buffer.from(audioArrayBuffer as any).toString('base64'),
            },
          })
        );
      }
    });

    ws.on('error', console.error);
  });

  app.listen(PORT, () => {
    console.log(`Local: http://localhost:${PORT}`);
    console.log(`Remote: https://${process.env.SERVER_DOMAIN}`);
  });
}

function streamToArrayBuffer(readableStream: Readable) {
  return new Promise((resolve, reject) => {
    const chunks: Buffer[] = [];

    readableStream.on('data', (chunk) => {
      chunks.push(chunk);
    });

    readableStream.on('end', () => {
      resolve(Buffer.concat(chunks).buffer);
    });

    readableStream.on('error', reject);
  });
}

startApp();
```

----------------------------------------

TITLE: Import ElevenLabs Conversational AI dependencies
DESCRIPTION: Import required modules for setting up a conversational AI agent, including `ElevenLabs` client, `Conversation`, and `DefaultAudioInterface`.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/libraries/python.mdx#_snippet_4

LANGUAGE: python
CODE:
```
import os
import signal

from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
```

----------------------------------------

TITLE: Initiate Speaker Separation for PVC Samples
DESCRIPTION: This Python code demonstrates how to initiate speaker separation for uploaded audio samples, which is a necessary step if your audio files contain multiple speakers. It iterates through the samples, calls the separation API, and then polls the status of each separation job until it's completed or failed, with a 5-second delay between polls.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/voices/professional-voice-cloning.mdx#_snippet_2

LANGUAGE: python
CODE:
```
sample_ids_to_check = []
for sample in samples:
    if sample.sample_id:
        print(f"Starting separation for sample: {sample.sample_id}")
        elevenlabs.voices.pvc.samples.speakers.separate(
            voice_id=voice.voice_id,
            sample_id=sample.sample_id
        )
        sample_ids_to_check.append(sample.sample_id)

while sample_ids_to_check:
    # Create a copy of the list to iterate over, so we can remove items from the original
    ids_in_batch = list(sample_ids_to_check)
    for sample_id in ids_in_batch:
        status_response = elevenlabs.voices.pvc.samples.speakers.get(
            voice_id=voice.voice_id,
            sample_id=sample_id
        )
        status = status_response.status
        print(f"Sample {sample_id} status: {status}")
        if status == "completed" or status == "failed":
            sample_ids_to_check.remove(sample_id)

    if sample_ids_to_check:
        # Wait before the next poll cycle
        time.sleep(5) # Wait for 5 seconds
```

----------------------------------------

TITLE: Initialize Node.js Project for Twilio Outbound Calls
DESCRIPTION: This command sequence sets up a new Node.js project directory, navigates into it, initializes a package.json file, and configures the project to use ES modules.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/guides/twilio-outbound-calling.mdx#_snippet_0

LANGUAGE: bash
CODE:
```
mkdir conversational-ai-twilio
cd conversational-ai-twilio
npm init -y; npm pkg set type="module";
```

----------------------------------------

TITLE: Load Agent ID and API Key from environment variables
DESCRIPTION: Retrieve the `AGENT_ID` and `ELEVENLABS_API_KEY` from environment variables. The API key is optional for public agents.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/libraries/python.mdx#_snippet_5

LANGUAGE: python
CODE:
```
agent_id = os.getenv("AGENT_ID")
api_key = os.getenv("ELEVENLABS_API_KEY")
```

----------------------------------------

TITLE: Execute Instant Voice Clone creation script
DESCRIPTION: Provides command-line instructions to execute the previously defined Instant Voice Clone creation script. This snippet shows how to run the Python script (`example.py`) and the TypeScript script (`example.mts`) from the terminal.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/voices/instant-voice-cloning.mdx#_snippet_1

LANGUAGE: python
CODE:
```
python example.py
```

LANGUAGE: typescript
CODE:
```
npx tsx example.mts
```

----------------------------------------

TITLE: Configure ElevenLabs API Key
DESCRIPTION: Creates a `.env` file to securely store the ElevenLabs API key, preventing it from being hardcoded directly in the application.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/dubbing/basics.mdx#_snippet_2

LANGUAGE: .env
CODE:
```
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

----------------------------------------

TITLE: Install ElevenLabs Python SDK
DESCRIPTION: Installs the official ElevenLabs Python SDK using pip, which is required to interact with the ElevenLabs API for dubbing services.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/dubbing/basics.mdx#_snippet_0

LANGUAGE: bash
CODE:
```
pip install elevenlabs
```

----------------------------------------

TITLE: Configure ElevenLabs API Key in .env File
DESCRIPTION: Create a `.env` file in your project root and add your ElevenLabs API key. This allows the application to securely access your credentials without hardcoding them directly into the source code.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/text-to-speech/pronunciation-dictionaries.mdx#_snippet_2

LANGUAGE: plaintext
CODE:
```
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

----------------------------------------

TITLE: Execute Sound Effect Generation Code
DESCRIPTION: This snippet provides the commands to execute the previously created Python or TypeScript code files. Running these commands will trigger the sound effect generation and playback.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/sound-effects/quickstart.mdx#_snippet_1

LANGUAGE: python
CODE:
```
python example.py
```

LANGUAGE: typescript
CODE:
```
npx tsx example.mts
```

----------------------------------------

TITLE: Configure ElevenLabs Agent with Skip Turn Tool via API
DESCRIPTION: This code demonstrates how to initialize the ElevenLabs client and configure a conversational agent to include the `skip_turn` system tool. The `skip_turn` tool allows the agent to pause and wait for user input, enhancing natural conversation flow. The `description` field for the tool is optional and can be used to customize its trigger conditions.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/customization/tools/skip-turn.mdx#_snippet_0

LANGUAGE: python
CODE:
```
from elevenlabs import (
    ConversationalConfig,
    ElevenLabs,
    AgentConfig,
    PromptAgent,
    PromptAgentInputToolsItem_System
)

# Initialize the client
elevenlabs = ElevenLabs(api_key="YOUR_API_KEY")

# Create the skip turn tool
skip_turn_tool = PromptAgentInputToolsItem_System(
    name="skip_turn",
    description=""  # Optional: Customize when the tool should be triggered, or leave blank for default.
)

# Create the agent configuration
conversation_config = ConversationalConfig(
    agent=AgentConfig(
        prompt=PromptAgent(
            tools=[skip_turn_tool]
        )
    )
)

# Create the agent
response = elevenlabs.conversational_ai.agents.create(
    conversation_config=conversation_config
)
```

LANGUAGE: javascript
CODE:
```
import { ElevenLabs } from '@elevenlabs/elevenlabs-js';

// Initialize the client
const elevenlabs = new ElevenLabs({
  apiKey: 'YOUR_API_KEY',
});

// Create the agent with skip turn tool
await elevenlabs.conversationalAi.agents.create({
  conversationConfig: {
    agent: {
      prompt: {
        tools: [
          {
            type: 'system',
            name: 'skip_turn',
            description: '', // Optional: Customize when the tool should be triggered, or leave blank for default.
          },
        ],
      },
    },
  },
});
```

----------------------------------------

TITLE: Create Instant Voice Clone using ElevenLabs SDK
DESCRIPTION: Demonstrates how to create an Instant Voice Clone using the ElevenLabs SDK in Python and TypeScript. This code initializes the ElevenLabs client, specifies the desired voice name, and provides paths to local audio files for the cloning process. An API key is required for authentication.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/voices/instant-voice-cloning.mdx#_snippet_0

LANGUAGE: python
CODE:
```
# example.py
import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from io import BytesIO

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

voice = elevenlabs.voices.ivc.create(
    name="My Voice Clone",
    # Replace with the paths to your audio files.
    # The more files you add, the better the clone will be.
    files=[BytesIO(open("/path/to/your/audio/file.mp3", "rb").read())]
)

print(voice.voice_id)
```

LANGUAGE: typescript
CODE:
```
// example.mts
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
import "dotenv/config";
import fs from "node:fs";

const elevenlabs = new ElevenLabsClient();

const voice = await elevenlabs.voices.ivc.create({
    name: "My Voice Clone",
    // Replace with the paths to your audio files.
    // The more files you add, the better the clone will be.
    files: [
        fs.createReadStream(
            "/path/to/your/audio/file.mp3",
        ),
    ],
});

console.log(voice.voice_id);
```

----------------------------------------

TITLE: Complete Python Script: Text-to-Speech, S3 Upload, and URL
DESCRIPTION: This comprehensive Python script integrates text-to-speech conversion, S3 audio upload, and presigned URL generation. It demonstrates the full workflow from converting text to an audio stream, uploading it to AWS S3, and then printing a time-limited URL to access the uploaded audio file.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/text-to-speech/streaming.mdx#_snippet_13

LANGUAGE: python
CODE:
```
import os

from dotenv import load_dotenv

load_dotenv()

from text_to_speech_stream import text_to_speech_stream
from s3_uploader import upload_audiostream_to_s3, generate_presigned_url


def main():
    text = "This is James"

    audio_stream = text_to_speech_stream(text)
    s3_file_name = upload_audiostream_to_s3(audio_stream)
    signed_url = generate_presigned_url(s3_file_name)

    print(f"Signed URL to access the file: {signed_url}")


if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Call Function to Generate Presigned URL for S3 Object
DESCRIPTION: These examples show how to use the presigned URL generation function. Given an S3 object key (file name), it produces a secure, time-limited URL that allows temporary access to the corresponding audio file stored in S3.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/text-to-speech/streaming.mdx#_snippet_12

LANGUAGE: python
CODE:
```
signed_url = generate_presigned_url(s3_file_name)
print(f"Signed URL to access the file: {signed_url}")
```

LANGUAGE: typescript
CODE:
```
const presignedUrl = await generatePresignedUrl(s3path);
console.log('Presigned URL:', presignedUrl);
```

----------------------------------------

TITLE: Execute Text to Speech File Conversion Function
DESCRIPTION: This snippet shows how to call the previously defined text-to-speech function with a sample text. It demonstrates the simple execution of the audio file generation process.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/cookbooks/text-to-speech/streaming.mdx#_snippet_4

LANGUAGE: Python
CODE:
```
text_to_speech_file("Hello World")
```

LANGUAGE: TypeScript
CODE:
```
await createAudioFileFromText('Hello World');
```

----------------------------------------

TITLE: Initialize ElevenLabs Node.js Client with API Key
DESCRIPTION: Demonstrates how to initialize the `ElevenLabsClient` in Node.js using the `@elevenlabs/elevenlabs-js` package, passing the API key for authentication.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/api-reference/pages/authentication.mdx#_snippet_3

LANGUAGE: javascript
CODE:
```
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';

const elevenlabs = new ElevenLabsClient({
  apiKey: 'YOUR_API_KEY',
});
```

----------------------------------------

TITLE: Configure Agent RAG with JavaScript
DESCRIPTION: This JavaScript snippet illustrates how to enable Retrieval Augmented Generation (RAG) for an ElevenLabs conversational AI agent. It initializes the ElevenLabs client, initiates document indexing for RAG, polls the indexing status, retrieves the agent's current configuration, updates it to enable RAG with an embedding model, adjusts document usage mode, and then updates the agent.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/customization/rag.mdx#_snippet_3

LANGUAGE: javascript
CODE:
```
// First, index a document for RAG
async function enableRAG(documentId, agentId, apiKey) {
  try {
    // Initialize the ElevenLabs client
    const { ElevenLabs } = require('elevenlabs');
    const elevenlabs = new ElevenLabs({
      apiKey: apiKey,
    });

    // Start document indexing for RAG
    let response = await elevenlabs.conversationalAi.knowledgeBase.document.computeRagIndex(
      documentId,
      {
        model: 'e5_mistral_7b_instruct',
      }
    );

    // Check indexing status until completion
    while (response.status !== 'SUCCEEDED' && response.status !== 'FAILED') {
      await new Promise((resolve) => setTimeout(resolve, 5000)); // Wait 5 seconds
      response = await elevenlabs.conversationalAi.knowledgeBase.document.computeRagIndex(
        documentId,
        {
          model: 'e5_mistral_7b_instruct',
        }
      );
    }

    if (response.status === 'FAILED') {
      throw new Error('RAG indexing failed');
    }

    // Get current agent configuration
    const agentConfig = await elevenlabs.conversationalAi.agents.get(agentId);

    // Enable RAG in the agent configuration
    const updatedConfig = {
      conversation_config: {
        ...agentConfig.agent,
        prompt: {
          ...agentConfig.agent.prompt,
          rag: {
            enabled: true,
            embedding_model: 'e5_mistral_7b_instruct',
            max_documents_length: 10000,
          },
        },
      },
    };

    // Update document usage mode if needed
    if (agentConfig.agent.prompt.knowledge_base) {
      agentConfig.agent.prompt.knowledge_base.forEach((doc, index) => {
        if (doc.id === documentId) {
          updatedConfig.conversation_config.prompt.knowledge_base[index].usage_mode = 'auto';
        }
      });
    }

    // Update the agent configuration
    await elevenlabs.conversationalAi.agents.update(agentId, updatedConfig);

    console.log('RAG configuration updated successfully');
    return true;
  } catch (error) {
    console.error('Error configuring RAG:', error);
    throw error;
  }
}

// Example usage
// enableRAG('your-document-id', 'your-agent-id', 'your-api-key')
//   .then(() => console.log('RAG setup complete'))
//   .catch(err => console.error('Error:', err));
```

----------------------------------------

TITLE: Initialize Node.js Project for Conversational AI
DESCRIPTION: Provides the necessary `bash` commands to create a new directory, navigate into it, and initialize a Node.js project with module support, preparing the environment for the conversational AI application.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/guides/twilio-custom-server.mdx#_snippet_0

LANGUAGE: bash
CODE:
```
mkdir conversational-ai-twilio
cd conversational-ai-twilio
npm init -y; npm pkg set type="module";
```

----------------------------------------

TITLE: Generate Signed URL for Conversational AI Session (Server-side)
DESCRIPTION: Server-side example demonstrating how to generate a signed URL for a Conversational AI session using the ElevenLabs REST API, which is necessary for authorized conversations.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/libraries/react.mdx#_snippet_6

LANGUAGE: javascript
CODE:
```
// your server
const requestHeaders: HeadersInit = new Headers();
requestHeaders.set("xi-api-key", process.env.XI_API_KEY); // use your ElevenLabs API key

const response = await fetch(
  "https://api.elevenlabs.io/v1/convai/conversation/get-signed-url?agent_id={{agent id created through ElevenLabs UI}}",
  {
    method: "GET",
    headers: requestHeaders,
  }
);

if (!response.ok) {
  return Response.error();
}

const body = await response.json();
const url = body.signed_url; // use this URL for startSession method.
```

----------------------------------------

TITLE: Creating a Conversational AI Component with ElevenLabs React
DESCRIPTION: This component, Conversation, utilizes the useConversation hook from @elevenlabs/react to manage real-time audio conversations. It handles connection status, messages, and errors, and provides functions to request microphone access, start a session with a specified agent ID, and end the session. UI buttons control the conversation flow.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/guides/nextjs.mdx#_snippet_4

LANGUAGE: tsx
CODE:
```
'use client';

import { useConversation } from '@elevenlabs/react';
import { useCallback } from 'react';

export function Conversation() {
  const conversation = useConversation({
    onConnect: () => console.log('Connected'),
    onDisconnect: () => console.log('Disconnected'),
    onMessage: (message) => console.log('Message:', message),
    onError: (error) => console.error('Error:', error),
  });


  const startConversation = useCallback(async () => {
    try {
      // Request microphone permission
      await navigator.mediaDevices.getUserMedia({ audio: true });

      // Start the conversation with your agent
      await conversation.startSession({
        agentId: 'YOUR_AGENT_ID', // Replace with your agent ID
      });

    } catch (error) {
      console.error('Failed to start conversation:', error);
    }
  }, [conversation]);

  const stopConversation = useCallback(async () => {
    await conversation.endSession();
  }, [conversation]);

  return (
    <div className="flex flex-col items-center gap-4">
      <div className="flex gap-2">
        <button
          onClick={startConversation}
          disabled={conversation.status === 'connected'}
          className="px-4 py-2 bg-blue-500 text-white rounded disabled:bg-gray-300"
        >
          Start Conversation
        </button>
        <button
          onClick={stopConversation}
          disabled={conversation.status !== 'connected'}
          className="px-4 py-2 bg-red-500 text-white rounded disabled:bg-gray-300"
        >
          Stop Conversation
        </button>
      </div>

      <div className="flex flex-col items-center">
        <p>Status: {conversation.status}</p>
        <p>Agent is {conversation.isSpeaking ? 'speaking' : 'listening'}</p>
      </div>
    </div>
  );
}
```

----------------------------------------

TITLE: Configure Agent RAG with Python
DESCRIPTION: This Python snippet demonstrates how to enable Retrieval Augmented Generation (RAG) for an ElevenLabs conversational AI agent. It covers indexing a document, polling its status until completion, retrieving the agent's current configuration, enabling RAG with a specified embedding model, and updating the agent's knowledge base document usage mode to 'auto' before saving the changes.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/customization/rag.mdx#_snippet_2

LANGUAGE: python
CODE:
```
# Check indexing status
while response.status not in ["SUCCEEDED", "FAILED"]:
    time.sleep(5)  # Wait 5 seconds before checking status again
    response = elevenlabs.conversational_ai.knowledge_base.document.compute_rag_index(
        documentation_id=document_id,
        model=embedding_model
    )

# Then update agent configuration to use RAG
agent_id = "your-agent-id"

# Get the current agent configuration
agent_config = elevenlabs.conversational_ai.agents.get(agent_id=agent_id)

# Enable RAG in the agent configuration
agent_config.agent.prompt.rag = {
    "enabled": True,
    "embedding_model": "e5_mistral_7b_instruct",
    "max_documents_length": 10000
}

# Update document usage mode if needed
for i, doc in enumerate(agent_config.agent.prompt.knowledge_base):
    if doc.id == document_id:
        agent_config.agent.prompt.knowledge_base[i].usage_mode = "auto"

# Update the agent configuration
elevenlabs.conversational_ai.agents.update(
    agent_id=agent_id,
    conversation_config=agent_config.agent
)
```

----------------------------------------

TITLE: Install Python Dependencies
DESCRIPTION: Command to install required Python packages for the conversational AI project, including FastAPI, Uvicorn, python-dotenv, Twilio, ElevenLabs, and WebSockets.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/guides/twilio-custom-server.mdx#_snippet_6

LANGUAGE: bash
CODE:
```
pip install fastapi uvicorn python-dotenv twilio elevenlabs websockets
```

----------------------------------------

TITLE: Defining User Message Event Structure - JavaScript
DESCRIPTION: This snippet outlines the JSON structure for a `user_message` event. This event type allows the application to send text directly to the conversation, which is processed as if the user had spoken it. It specifies the event `type` and a `text` field for the user's message, triggering the same response flow as spoken input.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/conversational-ai/pages/customization/client-to-server-events.mdx#_snippet_2

LANGUAGE: javascript
CODE:
```
// User message event structure
{
  "type": "user_message",
  "text": "I would like to upgrade my account"
}
```

----------------------------------------

TITLE: Execute ElevenLabs Text-to-Speech WebSocket Scripts
DESCRIPTION: This snippet provides the command-line instructions to run the Python and TypeScript example scripts. Upon execution, an MP3 audio file containing the generated speech will be saved in the `output` directory.
SOURCE: https://github.com/elevenlabs/elevenlabs-docs/blob/main/fern/docs/pages/developer-guides/websockets.mdx#_snippet_5

LANGUAGE: python
CODE:
```
python text-to-speech-websocket.py
```

LANGUAGE: typescript
CODE:
```
npx tsx text-to-speech-websocket.ts
```