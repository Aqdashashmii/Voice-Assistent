import speech_recognition as sr
import webbrowser
import pyttsx3
import pygame
import time
from gtts import gTTS
from openai import OpenAI

client = OpenAI(
    api_key="Api-key"
)


def gpt(query):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a virtual assistant named jarvis skilled in general task like alexa and google.Give short responses"},
            {"role": "user", "content": query}
        ]
    )
    speak(completion.choices[0].message)


recognizer = sr.Recognizer()
engine = pyttsx3.init()


# Can also use gTTS from gtts using pygame
def speakOld(text):
    engine.say(text)
    engine.runAndWait()


def speak(text, lang='en'):
    # Create a gTTS object
    tts = gTTS(text=text)

    # Save the audio to a file
    tts.save("output.mp3")

    pygame.init()

    # Load MP3 file
    pygame.mixer.music.load('output.mp3')

    # Play MP3 file
    pygame.mixer.music.play()

    # Wait while the music is playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Stop playing the music
    pygame.mixer.music.stop()

    # Quit pygame
    pygame.quit()


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open chat gpt" in c.lower():
        webbrowser.open("https://chat.openai.com/")
    elif "open gmail" in c.lower():
        webbrowser.open("https://mail.google.com/mail/u/2/#inbox")

    elif "exit loop" in c.lower():
        exit()

    else:
        gpt(c)


if __name__ == "__main__":
    speak("Initialising Jarvez")

    r = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening")
                audio = r.listen(source)
            word = r.recognize_google(audio)
            if word.lower() == "start":
                speak("ya")
                with sr.Microphone() as source:
                    print("Say Something")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print(F" Error {e}")
