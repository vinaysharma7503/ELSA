# import pyttsx3
# import datetime
# import speech_recognition as sr
# import wikipedia
# import webbrowser
# import os
# import smtplib
# import platform
# import subprocess

# # Initialize pyttsx3 engine
# engine = pyttsx3.init()

# # Setting up the voice based on the OS
# if platform.system() == 'Windows':
#     engine.setProperty('voice', engine.getProperty('voices')[1].id)  # sapi5 voice for Windows
# else:
#     engine.setProperty('voice', engine.getProperty('voices')[0].id)  # nsss voice for macOS

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# def wishme():
#     hour = int(datetime.datetime.now().hour)
#     if hour >= 0 and hour < 12:
#         speak("Good Morning!")
#     elif hour >= 12 and hour < 18:
#         speak("Good Afternoon!")
#     else:
#         speak("Good Evening!")
#     speak("I am Elsa. Please tell me how may I help you")

# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as mic:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(mic)
#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
#         print("User Said:", query)
#     except Exception as e:
#         print("Say that again please...")
#         return "None"
#     return query

# def sendEmail(to, content):
#     try:
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.ehlo()
#         server.starttls()
#         # Login using your credentials
#         server.login('vinaysharma.7503@gmail.com', 's9818827260')  # replace with correct credentials
#         server.sendmail('vinaysharma.7503@gmail.com', to, content)
#         server.close()
#         speak("Email has been sent!")
#     except Exception as e:
#         print(e)
#         speak("Sorry, I am not able to send the email at this moment.")

# def open_application(path):
#     if platform.system() == 'Windows':
#         os.startfile(path)
#     else:  # For macOS, use subprocess to open apps
#         subprocess.call(['open', path])

# if __name__ == "__main__":
#     wishme()
#     while True:
#         query = takeCommand().lower()

#         if 'elsa' in query:
#             speak("Hey there!")
#         elif 'how are you' in query:
#             speak("I am good, how about you?")
#         elif 'who is your creator' in query:
#             speak("Vinay Sharma")
#         elif 'wikipedia' in query:
#             speak('Searching Wikipedia...')
#             query = query.replace("wikipedia", "")
#             results = wikipedia.summary(query, sentences=2)
#             speak("According to Wikipedia")
#             speak(results)
#         elif 'open youtube' in query:
#             speak('Sure, opening YouTube')
#             webbrowser.open("youtube.com")
#         elif 'open google' in query:
#             speak('Sure, opening Google')
#             webbrowser.open("google.com")
#         elif 'open facebook' in query:
#             speak('Sure, opening Facebook')
#             webbrowser.open("facebook.com")
#         elif 'open stackoverflow' in query:
#             speak('Sure, opening Stack Overflow')
#             webbrowser.open("stackoverflow.com")
#         elif 'play music' in query:
#             music_dir = '/path/to/your/music'  # Set your music directory path
#             songs = os.listdir(music_dir)
#             if songs:
#                 song_to_play = os.path.join(music_dir, songs[0])
#                 open_application(song_to_play)
#             else:
#                 speak("No music files found.")
#         elif 'the time' in query:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")
#             speak(f"The time is {strTime}")
#         elif 'open pycharm' in query:
#             codePath = ""
#             if platform.system() == 'Windows':
#                 codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.3\\bin\\pycharm64.exe"
#             elif platform.system() == 'Darwin':  # macOS
#                 codePath = "/Applications/PyCharm CE.app"
#             open_application(codePath)
#         elif 'email to vinay' in query:
#             try:
#                 speak("What should I say?")
#                 content = takeCommand()
#                 to = "vinay.sunny1994@gmail.com"
#                 sendEmail(to, content)
#             except Exception as e:
#                 speak("Sorry, I am not able to send this email!")

# --------------------------------------Old One--------------------------------

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import platform
import subprocess
import json
import random

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Setting up the voice and adjusting properties
voices = engine.getProperty('voices')
if platform.system() == 'Windows':
    engine.setProperty('voice', voices[1].id)  # sapi5 voice for Windows
elif platform.system() == 'Darwin':  # macOS
    for voice in voices:
        if 'Samantha' in voice.name:  # Choosing a more natural macOS voice
            engine.setProperty('voice', voice.id)
            break
else:  # Linux
    engine.setProperty('voice', voices[0].id)  # espeak voice for Linux

# Adjust voice properties
engine.setProperty('rate', 150)  # Adjust speed for clearer speech
engine.setProperty('volume', 1.0)  # Set volume to max

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Load memory
memory_file = "memory.json"
def load_memory():
    try:
        with open(memory_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_memory(memory):
    with open(memory_file, "w") as file:
        json.dump(memory, file, indent=4)

memory = load_memory()

# Chat responses
responses = {
    "hello": ["Hello! How can I assist you?", "Hey there!", "Hi! What can I do for you?"],
    "how are you": ["I'm great, thanks for asking!", "I'm doing well. What about you?"],
    "who is your creator": ["I was created by Vinay Sharma!"],
    "bye": ["Goodbye! Have a nice day!", "See you later!", "Take care!"]
}

def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Elsa. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(mic)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User Said:", query)
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        sender_email = "your_email@gmail.com"  # Replace with actual email
        sender_password = "your_password"  # Replace with secure storage method
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to send the email at this moment.")

def open_application(path):
    if platform.system() == 'Windows':
        os.startfile(path)
    elif platform.system() == 'Darwin':  # macOS
        subprocess.call(['open', path])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', path])

def learn_new_command(command, response):
    memory[command] = response
    save_memory(memory)
    speak(f"I have learned the command: {command}")

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand()
        
        if query in memory:
            speak(memory[query])
        elif query in responses:
            speak(random.choice(responses[query]))
        elif 'learn' in query:
            speak("Tell me the command to learn")
            new_command = takeCommand()
            speak("Tell me the response for this command")
            new_response = takeCommand()
            learn_new_command(new_command, new_response)
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            speak('Sure, opening YouTube')
            webbrowser.open("https://youtube.com")
        elif 'open google' in query:
            speak('Sure, opening Google')
            webbrowser.open("https://google.com")
        elif 'open facebook' in query:
            speak('Sure, opening Facebook')
            webbrowser.open("https://facebook.com")
        elif 'open stackoverflow' in query:
            speak('Sure, opening Stack Overflow')
            webbrowser.open("https://stackoverflow.com")
        elif 'play music' in query:
            music_dir = '/path/to/your/music'  # Set your music directory path
            songs = os.listdir(music_dir)
            if songs:
                song_to_play = os.path.join(music_dir, songs[0])
                open_application(song_to_play)
            else:
                speak("No music files found.")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open pycharm' in query:
            codePath = ""
            if platform.system() == 'Windows':
                codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.3\\bin\\pycharm64.exe"
            elif platform.system() == 'Darwin':  # macOS
                codePath = "/Applications/PyCharm CE.app"
            elif platform.system() == 'Linux':
                codePath = "pycharm"  # Assuming it's added to PATH
            open_application(codePath)
        elif 'email to vinay' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vinay.sunny1994@gmail.com"
                sendEmail(to, content)
            except Exception as e:
                speak("Sorry, I am not able to send this email!")
        elif 'bye' in query:
            speak(random.choice(responses['bye']))
            break
