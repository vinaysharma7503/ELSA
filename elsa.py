import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
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
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vinaysharma.7503@gmail.com', 's9818827260')
    server.sendmail('vinaysharma.7503@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'elsa' in query:
            speak("hey there")
        elif 'how are you' in query:
            speak("i am good and you")
        elif 'who is your creator' in query:
            speak("vinay sharma")
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            speak('sure starting youtube')
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak('sure starting google')
            webbrowser.open("google.com")
        elif 'open facebook' in query:
            speak('sure starting facebook')
            webbrowser.open("facebook.com")
        elif 'open stackoverflow' in query:
            speak('sure starting stackoverflow')
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = ''
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir, the time is", strTime)
        elif 'open pycharm' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.3\\bin\\pycharm64.exe"
            os.startfile(codePath)
        elif 'email to vinay' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vinay.sunny1994@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Sorry my friend vinay bhai. I am not able to send this email!")
