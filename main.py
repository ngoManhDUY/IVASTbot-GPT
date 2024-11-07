import openai
from gtts import gTTS
import os
import pyaudio
import wave
from datetime import datetime
from transformers import pipeline, AutoModelForSpeechSeq2Seq, AutoTokenizer, AutoFeatureExtractor
import noisereduce as nr
import numpy as np

# Parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1  # Mono
RATE = 16000
CHUNK = 1024
OUTPUT_FILENAME = "output.wav"

# Load the model, tokenizer, and feature extractor separately
model = AutoModelForSpeechSeq2Seq.from_pretrained("vinai/PhoWhisper-tiny")
tokenizer = AutoTokenizer.from_pretrained("vinai/PhoWhisper-tiny")
feature_extractor = AutoFeatureExtractor.from_pretrained("vinai/PhoWhisper-tiny")

# Initialize the ASR pipeline with model, tokenizer, and feature extractor
transcriber = pipeline("automatic-speech-recognition", model=model, tokenizer=tokenizer, feature_extractor=feature_extractor)

# Manually set the API key
api_key = "API key"

# Initialize the OpenAI client with the API key
openai.api_key = api_key

def record_audio(duration, output_filename):
    audio = pyaudio.PyAudio()

    # Start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("Recording...")

    frames = []

    for i in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording finished.")

    # Stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Convert frames to numpy array
    audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)

    # Apply noise reduction
    reduced_noise = nr.reduce_noise(y=audio_data, sr=RATE)

    # Save the reduced noise audio to a file
    wf = wave.open(output_filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(reduced_noise.tobytes())
    wf.close()

    print(f"Audio saved as {output_filename}")

def transcribe_audio(audio_path):
    
    output = transcriber(audio_path)
    return output['text']

def ask_question(question):
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M')
    response = openai.ChatCompletion.create(
        model="gpt-4o",  
        messages=[
            {"role": "system", "content": f"Hiện tại là {current_datetime}."},
            {"role": "system", "content": "Tên tôi là IVASTBot"},
            {"role": "system", "content": "Tôi đến từ nhóm IOP Robotics của viện Vật lý, thuộc viện hàn lâm khoa học quốc gia Việt Nam."},
            {"role": "user", "content": question}
        ]
    )
    answer = response.choices[0].message['content'].strip()
    return answer

def text_to_speech(text, lang='vi'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output_tts.mp3")
    os.system("mpg321 output_tts.mp3")

if __name__ == "__main__":

    while True:
        # Record audio
        print("Please ask your question:")
        record_audio(5, OUTPUT_FILENAME)
        
        # Transcribe audio to text
        question = transcribe_audio(OUTPUT_FILENAME)
        print("Transcribed Question:", question)
        
        # Check if no question was detected
        if not question.strip():
            print("Tôi không nghe rõ, bạn có thể hỏi lại được không?")
            text_to_speech("Tôi không nghe rõ, bạn có thể hỏi lại được không?", lang='vi')
            continue
        
        # Check if the question is "Chào tạm biệt"
        if question.strip().lower() == "chào tạm biệt":
            print("Goodbye!")
            text_to_speech("Chào tạm biệt", lang='vi')
            break
        
        # Ask question to ChatGPT
        answer = ask_question(question)
        # Convert answer to speech
        text_to_speech(answer, lang='vi')
