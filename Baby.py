import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import os
import smtplib

engine = pyttsx3.init('SAPIS')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")
    elif hour >= 12 and hour < 18:
        speak("good noon")
    else:
        speak("good evening")
    speak("i am here to listen u ....please tell me how may i help u....")


def takeCommand():
    r = sr.Recognizer()
    with sr.microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print("user said:{query}\n", )
    except Exception as e:
        print("say that again.....")
        return "none"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('lubnaaggarwal2001@gmail.com', 'password')
    server.sendmail('lubnaaggarwal2001@gmail.com', to, content)
    server.close()


wishMe()
'if__name__' == "__main__"
while True:
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak('searching wikipedia....')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    elif 'play music' in query:
        music_dir = 'C:\Users\lubna\OneDrive\Desktop'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"time is {strTime}")

    elif 'pycharm' in query:
        pycharm = "C:\Program Files\JetBrains\PyCharm 2020.3.5\bin\pycharm64.exe"
        os.startfile(pycharm)

    elif 'send email' in query:
        try:
            speak("what should i say ?....")
            content = takeCommand()
            to = "lubnaaggarwal2001@gmail.com"
            sendEmail(to, content)
            speak("email has been sent!...")
        except Exception as e:
            print(e)
        speak("sorry, i am not able to send the mail ....")
