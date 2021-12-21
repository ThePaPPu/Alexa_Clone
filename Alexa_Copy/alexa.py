from math import inf
from os import times
import speech_recognition as sr
import pyttsx3 
import datetime
import pywhatkit
import wikipedia
import pyjokes

listner = sr.Recognizer()

alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[2].id)

def talkAlexa(text):
    print('Alexa: ')
    alexa.say(text)
    alexa.runAndWait()

def takeCommand():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            # if 'alexa' in command:
            print(command)
            command = command.replace('alexa', '')
    except:
        pass
    return command

def runAlexa():
    command = takeCommand()
    
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talkAlexa('Current time is ' + time)
    
    elif 'play' in command:
        song = command.replace('play', '')
        talkAlexa('Playing...' + song)
        pywhatkit.playonyt(song)
    
    elif 'tell me about' in command:
        lookingFor = command.replace('tell me about', '')
        info = wikipedia.summary(lookingFor, 1)
        print(info)
        talkAlexa(info)
        
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talkAlexa(joke)
    
    else:
        sorry = 'Sorry I did not undertand, Please tell again'
        
        print(sorry)
        talkAlexa(sorry)
        
        
while True:      
    runAlexa()

