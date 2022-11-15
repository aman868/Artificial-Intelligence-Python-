import pyttsx3


engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[2].id)
engine.setProperty('voice',voices[2].id)

for voice in voices:
    print(voice.id)
    engine.setProperty('voice',voice.id)
    engine.say("hello")