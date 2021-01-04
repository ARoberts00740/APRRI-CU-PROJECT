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
import sys
import time
import dateorganisemain as dom
import duplicatesimilarnewmain as dsm

from tkinter.filedialog import askopenfilename
from tkinter import Tk
from facegrouping import face_find
from facegrouping import person_sort
from facegrouping import select
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
mode=''

def slowPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)
def speak(sentence):
    engine.say(sentence)
    engine.runAndWait()
    
def mode_choose():
    global mode
    mode=input("Please Choose Command Mode For This Session:\nV for Voice\nT for Manual Typing\n") 
    if(mode!='v' and mode!='V' and mode!='T' and mode!='t'):
        print("Try Again")
        mode_choose()
    
def voice_choose():
    slowPrint("\nChoose between assistant voices:")
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
    
def inp():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        slowPrint("Speak now ^_^")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        slowPrint("Recognizing...")
        speak("Please wait...")
        sentence = r.recognize_google(audio, language='en-in')
        slowPrint(f"Input: {sentence}\n")
    except Exception as e:
        slowPrint("Sorry, kindly repeat...")
        speak("Sorry, kindly repeat...")  
        return " "
    return sentence

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        slowPrint("Good Morning")
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        slowPrint("Good Afternoon! Hope you are doing well")
        speak("Good Afternoon! Hope you are doing well")   
    else:
        slowPrint("Good Evening")
        speak("Good Evening!")  
    slowPrint("\nHow can I help you today?")       
    speak("How can I help you today?")       
    
def bye():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<18:
        slowPrint("Have a good day ahead")
        speak("Have a good day ahead") 
    else:
        slowPrint("Bye bye! Good night!")
        speak("Bye bye! Good night!")  

def can_do():
    slowPrint("What APRRI can do:\n")
    
def start():
    error=-1
    while 1:
        if(mode=='t'or mode=='T'):
            sentence = input("Type Here: ")
        elif(mode=='v'or mode=='V'):
            sentence = inp().lower()
        if 'open file' in sentence:
            root = Tk()
            root.withdraw()
            filename = askopenfilename()
            os.startfile(filename)
            
        elif 'change voice' in sentence:
            if(mode=='T' or mode=='t'):
                slowPrint("Command Mode changed to voice for this response only. Proceeding now")
            voice_choose()
            
        elif 'change mode' in sentence:
            mode_choose()
            
        elif 'personwise' in sentence:
            print("Let's organise your photos by faces")
            speak("Let's organise your photos by faces")
            slowPrint("Please choose a folder")
            speak("Please choose a folder")
            select()
            speak("Working now")
            person_sort()
            print("ALL DONE! ^_^")
            speak("All Done!")
            
        elif 'selfie' in sentence:
            print("Lets create a separate folder for your solo stills")
            speak("Lets create a separate folder for your solo stills")
            slowPrint("Please choose a folder")
            speak("Please choose a folder that has images")
            select()
            speak("Working now")
            face_find()
            print("ALL DONE! ^_^")
            speak("All Done!")
            
        elif 'similar' in sentence:
            print("I will now analyze images based on their similarity to the image you select")
            print("Please choose the folder where the image is located and then the image")
            speak("Please choose the folder where the image is located and then the image")
            dsm.similar()
            print("ALL DONE! Please see the analysis results above")
            speak("All Done! Please see the analysis results above")
            
        elif 'duplicates' in sentence:
            print("I will now find and delete duplicate images")
            speak("Let's recover some storage")
            slowPrint("Please choose a folder")
            speak("Please choose a folder")
            dsm.duplicates()
            print("ALL DONE! ^_^")
            speak("All Done! Take a look")
            os.startfile(dsm.location)
        
        elif 'month sort' in sentence:
            print("I will now organise your photos according to the month and year in which they were taken")
            slowPrint("Please choose a folder")
            speak("Please choose a folder")
            dom.monthOrganise()
            print("ALL DONE! ^_^")
            speak("All Done! Take a look")
            os.startfile(dom.location)
            
        elif 'year sort' in sentence:
            print("I will now organise your photos according to the year in which they were taken")
            slowPrint("Please choose a folder")
            speak("Please choose a folder")
            dom.yearOrganise()
            print("ALL DONE! ^_^")
            speak("All Done! Take a look")
            os.startfile(dom.location)
            
        elif (sentence=='exit') or ('bye' in sentence):
            bye()
            break;
            
        elif 'wikipedia' in sentence:
            speak('Searching Wikipedia...')
            sentence = sentence.replace("wikipedia", "")
            results = wikipedia.summary(sentence, sentences=2)
            speak("Wikipedia says")
            print(results)
            speak(results)

        elif 'play music' in sentence:
            ...

        elif 'the time' in sentence:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")
            
        elif 'help' in sentence:
            can_do()
            
        elif sentence!="":
            error+=1
            if(error<1):
                print("Sorry, I don't know how to respond to that. Please try something else...")
                speak("Sorry, I don't know how to respond to that. Please try something else...")
            if(error==1):
                print("I am still learning, please try another command")
                speak("I am still learning, please try another command")
            if(error==2):
                print("Are you sure this is in english? *insert nervous face here*")
                speak("Are you sure this is in english? insert nervous face here")
            if(error>2):
                print("I guess this will help:")
                can_do()
                speak("I guess this will help")
        elif(sentence==''):
            continue
        #elif 'sim' in sentence: os.system('python similarity.py -f C:/Users/ASUS/Desktop/TESTF/TESTF/')