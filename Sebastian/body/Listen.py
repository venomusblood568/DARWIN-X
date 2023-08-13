import datetime
import speech_recognition as sr
from googletrans import Translator
import os
import pygame
import pytemperature
import sys

# Listen function
def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening Sir...")
        r.pause_threshold = 4
        audio = r.listen(source)

    try:
        print("Recognizing Sir...")
        query = r.recognize_google(audio, language="hi-IN")

    except:
        return ""

    query = str(query).lower()
    return query

# Translation function
def TranslationHinTong(text):
    translator = Translator()
    translation = translator.translate(text, dest='en').text
    print(f"You: {translation}.")
    return translation

# Speak function
def speak(data):
    voice = 'en-US-ChristopherNeural'
    command = f'edge-tts --voice "{voice}" --text "{data}" --write-media "data.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(5)
    except Exception as e:
        print(e)

    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

# Greeting function
def greet():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning sir, Sebastian At your service")
    elif hour >12 and hour<=18:
        speak("Good Afternoon sir, Sebastian At your service")

    else:
        speak("Good Evening sir, Sebastian At your service")

# Get current date and time
def get_date_time():
    now = datetime.datetime.now()
    current_date = now.strftime('%Y-%m-%d')
    current_time = now.strftime('%H:%M:%S')
    return current_date, current_time

# Get current temperature
def get_temperature():
    temperature_celsius = 25  # Replace with the actual temperature in Celsius
    temperature_fahrenheit = pytemperature.c2f(temperature_celsius)
    return temperature_fahrenheit

# Sleep function
def sleep():
    speak("Goodbye, sir! Take care.")
    # Add any additional actions you want to perform before sleeping

def terminate():    
    sys.exit(0)  # this will terminate the system

def wait():
    global waiting
    waiting = True
    speak("I'm waiting for you to say 'daddies home'.")

# MicExecution function
def MicExecution():
    global waiting
    waiting = False  # Initialize waiting variable
    
    greet()
    current_date, current_time = get_date_time()
    temperature = get_temperature()

    # speak(f"The current date is {current_date}.")
    # speak(f"The current time is {current_time}.")
    # speak(f"The current temperature is {temperature} degrees Fahrenheit.")
    # speak("How can I assist you today, sir?")
    
    while True:
        query = listen()
        if query:
            translation = TranslationHinTong(query)
            if "Go to sleep" in translation:
                sleep()
                break  # Exit the while loop and end the program
            elif "Fuck off" in translation:
                terminate()    
            elif "Hold on" in translation:
                wait()
                while waiting:
                    query = listen()
                    if query:
                        translation = TranslationHinTong(query)
                        if "Daddy's Home" in translation:
                            waiting = False
                            speak("Welcome back sir! sebastian at your service")
                            break
            elif waiting:
                speak("I'm still waiting.")
            else:
                speak("I'm sorry, I cannot assist with that.")

if __name__ == "__main__":
    MicExecution()
