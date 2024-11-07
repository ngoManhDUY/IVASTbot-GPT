import openai
from gtts import gTTS
import os
import pyaudio
import wave
from datetime import datetime
from main import text_to_speech

# Manually set the API key
api_key = "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"

# Initialize the OpenAI client with the API key
openai.api_key = api_key


def ask_question(question):
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the appropriate model
        messages=[
            {"role": "system", "content": f"Hiện tại là {current_datetime}."},
            {"role": "system", "content": "Tên tôi là IVASTBot đến từ nhóm IOP Robotics của viện Vật lý, viện hàn lâm khoa học quốc gia Việt Nam."},
            {"role": "user", "content": question}
        ]
    )
    answer = response.choices[0].message['content'].strip()
    return answer

if __name__ == "__main__":
    while True:
        question = input("Enter your question (or type 'exit' to stop): ")
        if question.lower() == 'exit':
            break
        answer = ask_question(question)
        print("Answer:", answer)
        text_to_speech(answer, lang='vi')