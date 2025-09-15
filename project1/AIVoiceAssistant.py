import pyttsx3
import speech_recognition as sr
import pywhatkit
import wikipedia

def speak(command):
    engine=pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    
speak("Welcome to the project")