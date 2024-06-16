import pyttsx3
import speech_recognition as sr 
import pyaudio #pip install setuptools
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes
from requests import get
import sys

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good morning!")
    elif hour >=12 and hour <18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("Hello, I am your desktop assisstant. How may I help you?")


def takeCommand():
    # it takes microphone input and gives string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please....")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query=takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia ")
            print(results)
            speak(results)

        elif 'name' in query:
            speak("My name is Zero")
            
        elif 'old are you' in query:
            speak("I am six months old newly developed desktop assistant.")
            
        elif 'help' in query:
            speak("I can help you in your minimum tasks when you will give me an instruction")
            
        elif 'open youtube' in query or 'youtube kholo' in query:
            webbrowser.open("youtube.com")
            speak("Opening youtube.")
        elif 'open google' in query or 'google kholo' in query:
            #speak("What shuold I search on google?")
            #cm=takeCommand().lower()
            webbrowser.open("google.com")
            speak("Opening google.")
        elif 'open msu website' in query or 'msu ki website kholo' in query:
            webbrowser.open("https://msub.digitaluniversity.ac/")
            speak("You are been directed to msu baroda official website")
        elif 'time' in query or 'abhi time kya ho raha hai' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open email' in query or 'email kholo' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            speak("Your gmail account is opening.")
            #webbrowser.open("gmail.com")
        elif 'joke' in query or 'ek joke sunao' in query:
            joke1=pyjokes.get_joke(language='en',category='chuck')
            print(joke1)
            speak(joke1)
        elif 'command prompt' in query or 'command prompt kholo' in query:
            os.system("start cmd")
        elif 'ip address' in query or 'ip address batao' in query:
            ip=get('https://api.ipify.org').text
            speak(f"Your Ip address is {ip}")
            print(f"Your ip address is {ip}")
        elif 'open whatsapp' in query or 'whatsapp kholo' in query:
            webbrowser.open('https://web.whatsapp.com/')
            speak("Opening Whatsapp...")
        elif 'stop' in query or 'band ho jao' in query:
            speak("Thank you for using me, have a good day.")
            sys.exit()
        else:
            speak("Sorry, I am not able to perform your command as I am too young to do.")
        

    