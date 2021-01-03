# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:37:46 2020
@author: Asus
"""
import pyttsx3
import speech_recognition
import datetime
import wikipedia
import os

from tkinter.filedialog import askopenfilename
from tkinter import Tk
from facegrouping import face_find
from facegrouping import person_sort
from facegrouping import select
from dateorganisemain import monthOrganise
from dateorganisemain import yearOrganise
from duplicatesimilarnewmain import duplicates
from duplicatesimilarnewmain import similar

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

def speak(sentence):
    engine.say(sentence)
    engine.runAndWait()
    
def inp():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Speak now...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        speak("Please wait...")
        sentence = r.recognize_google(audio, language='en-in')
        print(f"Input: {sentence}\n")
    except Exception as e:
        print("Sorry, kindly repeat...")
        speak("Sorry, kindly repeat...")  
        return " "
    return sentence

def voice_choose():
    print("Choose between assistant voices:")
    input("Hit Enter to listen to sample Voices")
    engine.setProperty('voice', voices[0].id)
    speak("I am APRRI, your AI Assistant")       
    engine.setProperty('voice', voices[1].id)
    speak("I am APRRI, your AI Assistant")       
    vIn=input("Choose between M or F: ")
    if(vIn=='M' or vIn=='m'):
        v=0
    elif(vIn=='F' or vIn=='f'):
        v=1
    engine.setProperty('voice', voices[v].id)

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning")
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        print("Good Afternoon! Hope you are doing well")
        speak("Good Afternoon! Hope you are doing well")   
    else:
        print("Good Evening")
        speak("Good Evening!")  

    speak("How can I help you today?")       

if __name__ == "__main__":
    greet()
    while 1:
        sentence = inp().lower()
        if 'open file' in sentence:
            root = Tk()
            root.withdraw()
            filename = askopenfilename()
            os.startfile(filename)
            
        elif 'change voice' in sentence:
            voice_choose()
            
        elif 'personwise' in sentence:
            speak("Sorting images by face")
            select()
            person_sort()
            
        elif 'selfie' in sentence:
            select()
            face_find()
            
        elif 'sim' in sentence:
            os.system('python similarity.py -f C:/Users/ASUS/Desktop/TESTF/TESTF/')
            
        elif 'duplicates' in sentence:
            duplicates()
            
        elif 'similar' in sentence:
            similar()
        
        elif 'month sort' in sentence:
            monthOrganise()
        
        elif 'year sort' in sentence:
            yearOrganise()
        
        elif 'wikipedia' in sentence:
            speak('Searching Wikipedia...')
            sentence = sentence.replace("wikipedia", "")
            results = wikipedia.summary(sentence, sentences=2)
            speak("Wikipedia says")
            print(results)
            speak(results)

        elif 'play music' in sentence:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in sentence:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")