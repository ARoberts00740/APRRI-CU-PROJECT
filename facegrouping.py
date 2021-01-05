# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 13:42:33 2020
@author: Asus
"""
import cv2
import face_recognition
import os
import glob
import shutil
from tkinter import filedialog
from tkinter import Tk
persons_list = []
index = {}
potraits = {}
faces_in_image = {}
location=''
def select():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    global dir_path
    dir_path = folder_selected+'/'
    global location
    location=folder_selected

def sort(file_name):
    '''
    Checks if a given file contains faces, if any new found, then add to persons_list
    '''
    global persons_list, index
    image = face_recognition.load_image_file(dir_path + file_name)
    try:
        face_encodings = face_recognition.face_encodings(image)
        faces_in_image[file_name] = len(face_encodings)
        print(f'{len(face_encodings)} faces found in {file_name}')
    except IndexError:
        print("I wasn't able to locate any faces in at least one of the images.")
    if face_encodings:
        if not persons_list:
            persons_list += face_encodings
            for i, f in enumerate(face_encodings):
                index[f'person{i+1}'] = [file_name]

        else:
            for f in face_encodings:
                results = face_recognition.compare_faces(
                    persons_list, f, tolerance=0.6)

                if True not in results:
                    persons_list.append(f)

                    index[f'person{len(index)+1}'] = [file_name]

                else:
                    ind = results.index(True)
                    index[f'person{ind+1}'].append(file_name)

def getFiles():
    files = []
    with os.scandir(dir_path) as entries:
        for entry in entries:
            if entry.is_file():
                files.append(entry.name)
    if '.DS_Store' in files:
        files.remove('.DS_Store')
    return files


def move():
    if (1 in faces_in_image.values()):
        print('\nMoving...')
        potraits_list = []
        for file, faces in faces_in_image.items():
            if faces == 1:
                potraits_list.append(file)
        for p in potraits_list:
            for person, files in index.items():
                if p in files:
                    if person not in potraits.keys():
                        potraits[person] = [p]
                    else:
                        potraits[person].append(p)
        for person, files in potraits.items():
            os.mkdir(dir_path + person)
            for file in files:
                shutil.move(dir_path + file, dir_path + person)
                print(f'Moving {file} to {dir_path + person}')
    else:
        print('\nNo potraits found!')

def displayIndex():
    for person, files in index.items():
        print(f'\n{person} has {len(files)} images:')
        for i, file in enumerate(files):
            print(f'  ({i+1}) {file}')

def face_find():
    folder_selected = dir_path
    print(os.getcwd())
    os.chdir(folder_selected)
    newpath=folder_selected+'/Solo shots'
    photos=glob.glob(folder_selected+'/*.jpg')
    i=1
    face_cascade=cv2.CascadeClassifier('C:\ProgramData\Anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
    for photo in photos:
        print(str(i)+'.'+photo)
        photopath=os.path.join(newpath,photo)
        print(photopath)
        img=cv2.imread(photopath,cv2.IMREAD_UNCHANGED)
        scale_percent=20;
        width=int(img.shape[1]*scale_percent/100)
        height=int(img.shape[0]*scale_percent/100)
        dim=(width,height)
        rimage=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
        gray=cv2.cvtColor(rimage,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,1.04,4)
        numface=len(faces)
        if(numface>0):
            if not os.path.isdir(newpath):
                os.mkdir(folder_selected+'/Solo shots')
            shutil.copy(photopath,newpath)
        i=i+1

def person_sort():
    files = getFiles()
    for file in files:
        sort(file)
    print(f'\n[ {len(persons_list)} unique faces found in total ]\n')
    displayIndex()
    move()