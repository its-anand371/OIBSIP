import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

def speak(text):
    engine.say(text)
    engine.runAndWait()
    print("Assistant : ", text)

recognizer = sr.Recognizer()
Microphone = sr.Microphone(device_index=0)
engine = pyttsx3.init()

print("Hello, I am your Personal Voice Assistant")
print("I am Listening")

engine.say("Hello I am Your Personal Voice Assistant")
engine.say("I am Listening .....")
engine.runAndWait()

while True:
    with Microphone as source:
        print("I am Listening...")
        speech = recognizer.listen(source, timeout=10)

    try:
        text = recognizer.recognize_google(speech).lower()
    except sr.UnknownValueError:
        speak("Sorry I didn't catch that. Can you repeat again.")
        continue

    speak(text)

    if "exit" in text or "stop" in text:
        speak("Goodbye! Have a great day,We will meet soon ")
        break

    elif "hello" in text:
        speak("Hello, how can I help you today?")

    elif "time" in text:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is: {now}")

    elif "date" in text:
        today = datetime.datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today's date is: {today}")

    elif "search" in text:
        topic = text.replace("search for", "").replace("search", "").strip()
        if topic:
            speak(f"Searching for {topic}")
            webbrowser.open(f"https://www.google.com/search?q={topic}")
        else:
            speak("What would you like me to search for?")

    else:
        speak("Sorry, I can't help with that yet.")
