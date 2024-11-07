# IVASTbot-GPT

IVASTbot-GPT is a voice-based chatbot that uses speech-to-text (STT) and text-to-speech (TTS) technologies to interact with users. It leverages the OpenAI GPT-3.5 model for generating responses and supports Vietnamese language.

## Features

- Record audio and convert it to text using the PhoWhisper model.
- Generate responses using the OpenAI GPT-3.5 model.
- Convert text responses to speech using the gTTS library.
- Supports Vietnamese language.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/ngoManhDUY/IVASTbot-GPT.git
   cd IVASTbot-GPT
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:
   - Create a file named `api_key.txt` in the root directory of the project.
   - Add your OpenAI API key to the `api_key.txt` file.

## Usage

1. Run the main script:
   ```sh
   python main.py
   ```

2. Follow the prompts to interact with the chatbot:
   - Speak your question into the microphone.
   - The chatbot will transcribe your question, generate a response, and speak the response back to you.

3. To stop the chatbot, say "Chào tạm biệt".

## File Structure

- `main.py`: Main script for recording audio, transcribing it, generating responses, and converting responses to speech.
- `chat_gpt.py`: Script for interacting with the OpenAI GPT-3.5 model.
- `requirements.txt`: List of required Python packages.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [OpenAI](https://www.openai.com/) for the GPT-3.5 model.
- [gTTS](https://gtts.readthedocs.io/) for the text-to-speech functionality.
- [PhoWhisper](https://github.com/vinai/PhoWhisper) for the speech-to-text model.
- [Hugging Face Transformers](https://huggingface.co/transformers/) for the ASR pipeline.
- [Noisereduce](https://github.com/timsainb/noisereduce) for noise reduction.
- [Librosa](https://librosa.org/) for additional audio processing.
