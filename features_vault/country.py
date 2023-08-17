import speech_recognition as sr
from gtts import gTTS
import os

def create_countries_list():
    countries_and_capitals = [
        ("Afghanistan", "Kabul"),
        ("Albania", "Tirana"),
        # Add more countries and capitals here...
    ]
    return dict(countries_and_capitals)

def get_country_capital(country, countries_data):
    country = country.capitalize()  # Normalize input
    if country in countries_data:
        return countries_data[country]
    else:
        return "Country not found in the list."

def speak(text):
    tts = gTTS(text)
    tts.save("output.mp3")
    os.system("mpg321 output.mp3")  # Use mpg321 or any other audio player

def main():
    recognizer = sr.Recognizer()

    countries_data = create_countries_list()

    with sr.Microphone() as source:
        print("Speak a country name:")
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        print("You said:", user_input)
        capital = get_country_capital(user_input, countries_data)
        response = f"The capital of {user_input} is {capital}"
        print(response)
        speak(response)  # Speak the response
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your speech.")
    except sr.RequestError:
        print("Sorry, I'm having trouble connecting to the speech recognition service.")

if __name__ == "__main__":
    main()
