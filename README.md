# IVASTbot-GPT

IVASTbot-GPT is a voice-based chatbot that uses speech-to-text (STT) and text-to-speech (TTS) technologies to interact with users. It leverages the OpenAI GPT-3.5 model for generating responses and supports Vietnamese language.

## Features

- Record audio and convert it to text using the PhoWhisper model.
- Generate responses using the OpenAI GPT-3.5 model.
- Convert text responses to speech using the gTTS library.
- Supports Vietnamese language.

## Requirements

- Python 3.6+
- `openai`
- `gtts`
- `pyaudio`
- `wave` (standard library)
- `datetime` (standard library)
- `transformers`
- `noisereduce`
- `numpy`
- `librosa`

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/ngoManhDUY/IVASTbot-GPT.git
   cd IVASTbot-GPT
