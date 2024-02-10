import os
import requests
import json
import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write

# Function to record audio and save it as a WAV file
def record_audio(duration=5, filename='temp.wav', fs=44100):
    print("Listening...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    write(filename, fs, recording)  # Save as WAV file
    return filename

# Initialize speech recognition
recognizer = sr.Recognizer()

# Function to recognize speech from audio file
def recognize_speech_from_audio(file):
    with sr.AudioFile(file) as source:
        audio_data = recognizer.record(source)
        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Google could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google service; {e}")

# Function to chat with OpenAI using text input
def chat_with_openai(message):
    api_key = "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"
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    data = {
        'model': "gpt-3.5-turbo",
        'messages': [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    }
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    if response.status_code == 200:
        response_data = response.json()
        chat_message = response_data['choices'][0]['message']['content']
        print(f"OpenAI: {chat_message}")
    else:
        print(f"Error: {response.text}")

# Main function to handle the voice input
def main():
    print("OpenAI Chat Terminal (speak 'exit' to quit)")
    while True:
        audio_file = record_audio()
        user_input = recognize_speech_from_audio(audio_file)
        os.remove(audio_file)  # Remove the temp file
        
        if user_input and user_input.lower() == 'exit':
            break
        chat_with_openai(user_input)

if __name__ == '__main__':
    main()
