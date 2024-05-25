from xml.dom.minidom import CharacterData
from googlesearch import search as s
import pywhatkit
import googlescrap
import pyttsx3
import datetime
import speech_recognition
import wikipedia
import wolframalpha
import os

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



speak("I am ready to help. Waiting for your command")

def takecommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("************ ...........Listening.......... ************")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)

    try:
        print("*********........... RECONGNIZNING ...........*********")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
            print(e)
            speak("Say that again please....")
            return "none"
    return query

if __name__ == "__main__":
    while True:
        question = takecommand().lower()
        if 'search' in question:  
            while True:
                query = takecommand().lower()

                if 'wikipedia' in query:
                    speak('Searching Wikipedia....')
                    query =query.replace("Wikipedia","")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia......")
                    speak(results)
                elif 'google' in query:
                    speak('searching google....')
                    query =query.replace("google","")
                    speak("This is what I found on google....")
                    try:
                        pywhatkit.search(query)
                        results = googlescrap.summary(query, sentence=2)
                        print(results)
                        speak(results)
                    except:
                        speak("No speakable Output avilable....")
                


                elif 'wolframalpha' in query:
                    speak('searching wolframalpha.....')
                    query =query.replace("wolframalpha","")
                    results =wolframalpha.summary(query, sentence=2)
                    speak("Accirding to wolframalpha......")
                    speak(results)

      

                elif "exit" in query:
                    pyttsx3.speak(" ")
                    break
            pyttsx3.speak("Thank you for using me.")

        elif 'Time' in question:
            speak("Time ")
            time()

        elif 'Date' in question:
            speak("Todays Date is  ")
            date()
    
        elif 'access' in question:
            while True:
                query = takecommand().lower()

                if 'application' in query:
                    speak("Call the name of application:\n")
                    while True:
                        print("Call the name of application: \n")

                        p=takecommand().lower()

                        print(p)

                        if ("DONT" in p) or ("DON'T" in p ) or("NOT " in p):
                            pyttsx3.speak("Type again")
                            print(".")
                            print(".")
                            continue
                        elif 'Brave' in p:
                            pyttsx3.speak("starting Brave")
                            os.system("start Brave")
        
                        elif "microsoft edge" in p:
                            pyttsx3.speak("starting microsoft edge")
                            os.system("start msedge")
                        
                        elif "notepad" in p:
                            pyttsx3.speak("staerting notepad")
                            os.system("start Notepad")
                        
                        elif "photoshop" in p:
                            pyttsx3.speak("starting photoshop")
                            os.system("start Photoshop.exe 2024")
                        
                        elif "exit" in p:
                            pyttsx3.speak(" ") 
                            pyttsx3.speak("Thank you for using me.")
                            break
                        
                            
       

                    
 
