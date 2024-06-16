import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio
# from distutils.version import LooseVersion as V 


print("Initializing Jarvis")

MASTER = "Rucha"        
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#Speak fun pronounce the passed string
def speak (text):
    engine.say(text)
    engine.runAndWait()

#this fun will wshi you according your current time
def wishMe():
    hour =int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER)
    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)

    speak("I am jarvis. How may I help you?")        

#this fun take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try :
        print("Recognizing...")
        query = r.recognize_google(audio, Language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please")    


#Main program start here......
speak("Initializing Jarvis...")
wishMe()
takeCommand()

