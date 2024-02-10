#listenToMe.py

import speech_recognition as sr
import os
import keyboard
import openai
import pyttsx3
import subprocess


# Initialize the text-to-speech engine

engine = pyttsx3.init()


# Set the rate of speech
 
rate = engine.getProperty('rate')

engine.setProperty('rate', rate - 20)


# Set the voice

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)



# Function to speak the given text

def speak(text):

    engine.say(text)

    engine.runAndWait()


# Initialize the recognizer

r = sr.Recognizer()


# Use the default microphone as the audio source

with sr.Microphone() as source:

    while True:

        print("Ready for speech...")

         # Wait for the keyboard combination to start listening

        keyboard.wait("ctrl+alt+s")

        print("Listening...")


        # Start listening for audio

        audio_data = r.listen(source, phrase_time_limit=5)


        # Wait for the keyboard combination to stop listening

        print("Recognizing...")


        try:

            # Use Google speech recognition to convert audio to text

            text = r.recognize_google(audio_data)

            print(f"You said: {text}")


            # Perform an action based on the recognized text

            if "open notepad" in text.lower():

                speak("Opening notepad")

                subprocess.Popen(['C:\Windows\System32\\notepad.exe'])

            elif "like this song" in text.lower() or "like song" in text.lower():

                speak("Liking Song")

                exec(open(r"C:\Users\Hjosh\BOC_Python\Spotify_Testing\likeSong.py").read())

            elif "start music" in text.lower():

                speak("opening music")

                exec(open(r"C:\Users\Hjosh\BOC_Python\Spotify_Testing\openAndPlay.py").read())

            elif "pause music" in text.lower() or "pause song" in text.lower() or "play music" in text.lower() or "resume music" in text.lower():

                exec(open(r"C:\Users\Hjosh\BOC_Python\Spotify_Testing\pausePlayMusic.py").read())

            elif "search google for" in text.lower():

                query = text.lower().split("search google for ")[1]

                speak(f"searching google for {query}")

                query = query.replace(" ", "+")

                os.system(f"start https://www.google.com/search?q={query}")

            elif "good night computer" in text.lower():

                speak("sweet dreams}")

            elif "welcome everyone" in text.lower():

                speak("Welcome........To Bytes Of Code")

            elif "gpt " in text.lower():

                #use openai key

                openai.api_key = "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"


                #setup gpt-3

                model_engine = "davinci"

                query = text.lower().split("gpt ")[1]

               

                temperature = 0.7

                max_tokens = 256

           

                response=openai.Completion.create(

                    model="text-davinci-003",

                    prompt=query,

                    temperature=temperature,

                    max_tokens=max_tokens

                )


                print(response.choices[0].text.strip())

                speak(response.choices[0].text.strip())


            elif "computer" in text.lower():

                openai.api_key = "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"

                query = text.lower().split("computer ")[1]

               

                conversation.append({"role":"user","content":query})

                response = openai.ChatCompletion.create(

                    model="gpt-3.5-turbo",

                    messages=conversation


                )

                chatGPT_response = response['choices'][0]['message']['content']

                print(chatGPT_response)

                speak(chatGPT_response)

            elif "copilot" in text.lower():

                openai.api_key = "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"

                query = text.lower().split("copilot ")[1]

                query = query + "Do not respond with additional text. respond in python code only. Do not respond with any explination or greeting whatsoever. Your response in its entirety should only have python code."

                conversation.append({"role":"user","content":query})

                response = openai.ChatCompletion.create(

                    model="gpt-3.5-turbo",

                    messages=conversation


                )

                chatGPT_response = response['choices'][0]['message']['content']

                print(chatGPT_response)

                #speak(chatGPT_response)

                pyautogui.write(chatGPT_response)


            elif "stop listening" in text.lower():

                speak('goodbye')

                exit()

            else:

                speak('Command not recognized')

                print("Command not recognized")

       


        except sr.UnknownValueError:

            print("Unable to recognize speech")

        except sr.RequestError as e:

            print(f"Error occurred: {e}")



#instal pipwin
#pipwin install pyaudio
