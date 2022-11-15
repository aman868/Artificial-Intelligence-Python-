import pyttsx3
import datetime
import speech_recognition as sr

engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[2].id)
engine.setProperty('voice',voices[2].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%H:%M")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(day)
    speak(month)
    speak(year)

speak("Today's Date is ")
date()
hour = datetime.datetime.now().hour
if hour >= 6 and hour <12:
    speak("Good Morning! Current time is ")
    time()
elif hour >= 12 and hour <18:
    speak("Good Afternoon! Current time is ")
    time()
elif hour >= 18 and hour <24:
    speak("Good Evening! Current time is ")
    time()
else:
    speak("This Time is to Sleep! Does you need any help.")
    time()