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
import facegrouping as fg
from tkinter.filedialog import askopenfilename
from tkinter import Tk
from youtubesearchpython import VideosSearch

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
    print("1. Male")
    speak("I am APRRI, your AI Assistant")       
    engine.setProperty('voice', voices[1].id)
    print("2. Female")
    speak("I am APRRI, your AI Assistant")       
    vIn=input("Choose between M or F: ")
    vIn=vIn.lower()
    if(vIn=='1' or vIn=='m' or vIn=='male'):
        v=0
    elif(vIn=='2' or 'f' in vIn):
        v=1
    else:
        print("Invalid choice, proceeding with default setting")
        return
    print("\nSuccess")
    engine.setProperty('voice', voices[v].id)
    
def inp():
    r = speech_recognition.Recognizer()
    slowPrint("\nSpeak now ^_^\n")
    with speech_recognition.Microphone() as source:
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        slowPrint("Recognizing...\n")
        speak("Please wait...")
        sentence = r.recognize_google(audio, language='en-in')
        slowPrint(f"Input: {sentence}\n")
    except Exception as e:
        slowPrint("Sorry, kindly repeat...")
        speak("Sorry, kindly repeat...")  
        return "none"
    return sentence

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        slowPrint("Good Morning\n")
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        slowPrint("Good Afternoon!\n")
        speak("Good Afternoon!")
    else:
        slowPrint("Good Evening!\n")
        speak("Good Evening!")  
    slowPrint("Hope you are doing well\n")
    speak("Hope you are doing well")   
    
def bye():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<18:
        slowPrint("Have a good day ahead\n")
        speak("Have a good day ahead") 
    else:
        slowPrint("Bye bye! Good night!")
        speak("Bye bye! Good night!")  

def can_do():
    slowPrint("What APRRI can do:\n")
    can_do_photos()
    print("Other operations include:\n1.Search and play YouTube videos - \'youtube\' \n2.Change input mode - \'change mode\'\n3.Change AI Voice - \'change voice\'\n4.Open a file - \'open\'\n5.Look up Wiki - TERM+\'wikipedia\'\n6.Respond to common questions(BETA)\n")
    
    
def can_do_photos():
    speak("Here's how I can help")
    print("\nAPRRI\'s photo operation commands:\n(you can use other terms with the input, just make sure to include these main tiggers)\n1.Organise photos by face - \'Sort by faces\'\n2.Organise photos by month - \'Sort by month\'\n3.Organise photos by year - \'Sort by year\'\n4.Organise selfies and solo shots - \'Selfie\' or \'Solo\'\n5.Find duplicate images - \'duplicates\'\n6.Find similar images (BETA) - \'similar\'\n")
    
def start():
    hru=0
    error=-1
    print("\n \'help\' for instructions")
    while 1:
        if(mode=='t'or mode=='T'):
            sentence = input("Type Here: ")
        elif(mode=='v'or mode=='V'):
            sentence = inp().lower()
        sentence=sentence.lower()
        if 'open' in sentence:
            root = Tk()
            root.withdraw()
            filename = askopenfilename()
            os.startfile(filename)
            
        elif 'change' in sentence and 'voice' in sentence:
            if(mode=='T' or mode=='t'):
                print("Loaded available voices. Proceeding now")
            voice_choose()
            
        elif 'change' in sentence and 'mode' in sentence:
            mode_choose()
            
        elif 'sort' in sentence and ('person' in sentence or 'face' in sentence):
            print("Let's organise your photos by faces")
            speak("Let's organise your photos by faces")
            slowPrint("Please choose a folder\n")
            speak("Please choose a folder")
            fg.select()
            speak("Working now")
            fg.person_sort()
            print("\nALL DONE! ^_^ Take a look")
            speak("All Done! Take a look")
            os.startfile(fg.location)
            
        elif 'selfie' in sentence or 'solo' in sentence:
            print("Lets create a separate folder for your solo stills")
            speak("Lets create a separate folder for your solo stills")
            slowPrint("Please choose a folder\n")
            speak("Please choose a folder that has images")
            fg.select()
            slowPrint("Working Now...")
            speak("Working now")
            fg.face_find()
            print("\nALL DONE! ^_^")
            speak("All Done! Take a look")
            os.startfile(fg.location)
            
        elif 'similar' in sentence:
            print("I will now analyze images based on their similarity to the image you select")
            print("Please choose the folder where the image is located and then the image\n")
            speak("Please choose the folder where the image is located and then the image")
            dsm.similar()
            print("\nALL DONE! Please see the analysis results above")
            speak("All Done! Please see the analysis results above")
            
        elif 'duplicate' in sentence:
            print("I will now find and delete duplicate images")
            speak("Let's recover some storage")
            slowPrint("Please choose a folder\n")
            speak("Please choose a folder")
            dsm.duplicates()
            print("\nALL DONE! ^_^ \nTake a look")
            speak("All Done! Take a look")
            os.startfile(dsm.location)
        
        elif 'month' in sentence and 'sort' in sentence:
            print("I will now organise your photos according to the month and year in which they were taken")
            slowPrint("Please choose a folder\n")
            speak("Please choose a folder")
            dom.monthOrganise()
            print("ALL DONE! ^_^")
            speak("All Done! Take a look")
            os.startfile(dom.location)
            
        elif 'year' in sentence and 'sort' in sentence:
            print("I will now organise your photos according to the year in which they were taken")
            slowPrint("Please choose a folder\n")
            speak("Please choose a folder")
            dom.yearOrganise()
            print("ALL DONE! ^_^")
            speak("All Done! Take a look")
            os.startfile(dom.location)
            
        elif (sentence=='exit') or 'stop' in sentence or ('bye' in sentence):
            bye()
            break;
            
        elif 'wikipedia' in sentence:
            speak('Searching Wikipedia...')
            sentence = sentence.replace("wikipedia", "")
            sentence = sentence.replace("search", "")
            results = wikipedia.summary(sentence, sentences=2)
            speak("Wikipedia says")
            print(results)
            speak(results)

        elif 'music' in sentence or 'youtube' in sentence:
            slowPrint("Lets get  grooving")
            speak("Lets get grooving")
            searcher=input("Enter search term: ")
            c=-1
            videosSearch = VideosSearch(searcher, limit = 2)
            res=(videosSearch.result()['result'])
            link=[]
            print("Choose a video:\n")
            speak("Choose a song")
            for i in res:
                print(c+2,"."+i['title'])
                c+=1
                link.append('https://youtu.be/'+i['id'])
                print(link[c])
            play=int(input())
            os.startfile(link[play])
            
        elif 'photo' in sentence or 'image' in sentence:
            can_do_photos()

        elif 'the time' in sentence:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")
            
        elif 'help' in sentence:
            can_do()
            
        elif 'hello' in sentence or 'hi' in sentence or 'hey' in sentence:
            slowPrint("Hey there!")
            speak("Hey there")
            
        elif 'what\'s up' in sentence or 'whatsup' in sentence or 'sup' in sentence or 'whassup' in sentence or 'how r u' in sentence or 'how are you' in sentence:
            slowPrint("I am doing well!\n")
            speak("I am doing well")
            slowPrint("And you?")
            speak("and you?")
            hru=1
            
        elif hru==1 and ('good' in sentence or 'fine' in sentence):
            slowPrint("Glad to know!")
            speak("Glad to know")
            
        elif 'what' in sentence and ' doing' in sentence:
            slowPrint("Well, I want to organise more photos")
            speak("I am bored, I want to organise more photos")
    
        elif 'good' in sentence and ('afternoon' in sentence or 'morning' in sentence or 'night' in sentence):
            greet()
            
        elif(sentence=='none' or sentence==''):
            continue
        
        elif sentence!="":
            error+=1
            if(error<1):
                print("Sorry, I don't know how to respond to that. Please try something else...")
                speak("Sorry, I don't know how to respond to that. Please try something else...")
            if(error==1):
                print("I am still learning, please try another command\nType \'help\' for the list of commands\n")
                speak("I am still learning, please try another command")
            if(error>1):
                print("I guess this will help:")
                can_do()
                speak("I guess this will help")
        #elif 'sim' in sentence: os.system('python similarity.py -f C:/Users/ASUS/Desktop/TESTF/TESTF/')
