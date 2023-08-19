import datetime
import webbrowser
import pyjokes
import pyttsx3
import speech_recognition as sre

recognizer= sre.Recognizer()
engine= pyttsx3.init()


def listen():
    with sre.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sre.UnknownValueError:
        print("Sorry, I didn't understand.")
    except sre.RequestError as e:
        print("Sorry, there was an error retrieving the audio:", str(e))

    return ""


def speak(text):
    engine.say(text)
    engine.runAndWait()
    print("Assistant said:", text)


speak("Hello! How can I assist you?")

while True:
    command= listen()
    if "hello" in command.lower():
        speak("Hello! How can I assist you?")
    elif "goodbye" in command.lower():
        speak("Goodbye!")
        break
    elif 'how are you' in command.lower():
        speak("I am fine, Thank you")
        speak("How are you, Sir")
    elif 'fine' in command.lower() or "good" in command.lower():
        speak("It's good to know that your fine")
    elif "what's your name" in command.lower():
        speak("My name is Jarvis.")
    elif "tell me a joke" in command.lower():
        speak(pyjokes.get_joke())
    elif 'the time' in command.lower():
        strTime= datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
    elif 'open google' in command.lower():
        speak("Here you go to Google\n")
        webbrowser.open("google.com")
    elif 'open youtube' in command.lower():
        speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")
    elif "what's the weather like" in command.lower():
        speak("It's sunny today.")
    else:
        speak("Sorry, I don't know how to respond to that.")
