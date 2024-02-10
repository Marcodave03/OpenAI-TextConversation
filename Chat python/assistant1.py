import whisper
import openai
import simpleaudio as sa
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

# Initialize Whisper model
model = whisper.load_model("medium")

# Set your OpenAI API key (use environment variable in production)
openai.api_key = "sk-ExOU6qhNJuG5JMwyiS28T3BlbkFJeZFYd7a7Ck0zxFF2rBICy"

# Function to record audio from microphone
def record_audio(duration=5, filename='temp.wav'):
    fs = 44100  # Sample rate
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
    sd.wait()  # Wait for the recording to finish
    # Convert the float64 recording to int16 for WAV file compatibility
    int_recording = np.int16(recording / np.max(np.abs(recording)) * 32767)
    write(filename, fs, int_recording)  # Save as WAV file
    print("Finished recording.")
    return filename

# Function for text-to-speech
def text_to_speech(text, filename='output.wav'):
    # Assuming you have an instance of TTS and a method to save the output to a file
    tts = TTS()
    tts.tts_to_file(text=text, file_path=filename)
    return filename

# Main function for voice chat
def voice_chat():
    print("Please speak into the microphone after the beep.")
    input("Press Enter to start recording...")
    user_voice = record_audio()

    # Transcribe voice to text using Whisper
    result = model.transcribe(user_voice)
    user_message = result["text"]
    print(f"You said: {user_message}")

    # Append user message to messages list
    messages = [
        {"role": "system", "content": "You are a kind helpful assistant."},
        {"role": "user", "content": user_message},
    ]

    # Get reply from OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    reply = response.choices[0].message.content
    print(f"OpenAI replied: {reply}")

    # Convert reply to speech
    tts_filename = text_to_speech(reply)

    # Play the response
    wave_obj = sa.WaveObject.from_wave_file(tts_filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing

if __name__ == "__main__":
    voice_chat()
