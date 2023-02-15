from xml.dom.minidom import CharacterData
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import wolframalpha
import googlesearch
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
    r = sr.Recognizer()
    with sr.Microphone() as source:
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
                    results = googlesearch.summary(query, sentence=2)
                    speak("According to google......")
                    print(results)
                    speak(results)
                elif 'wolframalpha' in query:
                    speak('searching wolframalpha.....')
                    query =query.replace("wolframalpha","")
                    results =wolframalpha.summary(query, sentence=2)
                    speak("Accirding to wolframalpha......")
                    speak(results)
                elif 'Time' in query:
                    speak("Time ")
                    time()
                elif "exit"in p:
                    pyttsx3.speak(" ")
                    break
            pyttsx3.speak("Thank you for using me.")
    

        elif 'access' in question:
            while True:
                query = takecommand().lower()

                if 'application' in query:
                    speak("Call the name of application:\n")
                    while True:
                        print("Call the name of application: \n")
                        print("\n1. Microsoft Excel\t 2. Brave ")

                        p=takecommand().lower()

                        print(p)

                        if ("DONT" in p) or ("DON'T" in p ) or("NOT " in p):
                            pyttsx3.speak("Type again")
                            print(".")
                            print(".")
                            continue
                        elif 'brave' in p:
                            pyttsx3.speak("starting brave")
                            os.system("start brave")
        
                        elif "microsoft edge" in p:
                            pyttsx3.speak("starting microsoft edge")
                            os.system("start msedge")

                        elif "Notepad" in p:
                            pyttsx3.speak("starting notepad")
                            os.system("start notepad")

                        elif "microsoft word" in p:
                            pyttsx3.speak("starting microsoft word")
                            os.system("start winword")

                        elif "Visual Studio" in p:
                            pyttsx3.speak("starting Visual Studio")
                            os.system("start VSCode")

                        elif "Battleground" in p:
                            pyttsx3.speak("Let's Play")
                            os.system("start PUBG BATTLEGROUNDS")

                        elif "thank you"in p:
                            pyttsx3.speak(" ")
                            break

                        elif "exit"in p:
                            pyttsx3.speak(" ")
                            break

                        else:
                            pyttsx3.speak(p)
                            print("Is invalid . please try again")
                            pyttsx3.speak("Is invalid please try again")

                    pyttsx3.speak("Thank you for using me.")
 
