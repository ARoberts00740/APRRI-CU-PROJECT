# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 19:01:17 2021
@author: Asus
"""
from tkinter import filedialog
from tkinter import Tk
import PIL 
import os
import shutil
import datetime
class ImageOrganizer:
    def __init__(self,dirname=''):
        self.images = os.listdir(dirname)
        self.dirname = dirname
        
    def preprocess_exif(self,data):
        data = data.strip()
        data = data.strip('\x00')
        
        return data
            
    def sort_by_year(self):
        for fname in self.images:
            with PIL.Image.open(os.path.join(self.dirname,fname)) as img:
                exif = img._getexif() 
            
            ts = self.preprocess_exif(exif[306])
            date = ts.split(' ')[0]
            year = datetime.datetime.strptime(date, '%Y:%m:%d').strftime('%Y')
                     
            if not os.path.isdir(self.dirname+'/'+year):
                os.mkdir(self.dirname+'/'+year)
        
            shutil.copy(os.path.join(self.dirname,fname),os.path.join(self.dirname,year,fname))
            print("Image {} moved from {} to {} successfully\n".format(fname,os.path.join(self.dirname,fname),os.path.join(year,fname)))
            

    def sort_by_yr_month(self):
        for fname in self.images:
            with PIL.Image.open(os.path.join(self.dirname,fname)) as img:
                exif = img._getexif() 
            
            ts = self.preprocess_exif(exif[306])
            date = ts.split(' ')[0]
            year = datetime.datetime.strptime(date, '%Y:%m:%d').strftime('%Y')
            month = datetime.datetime.strptime(date, '%Y:%m:%d').strftime('%b')
                     
            if not os.path.isdir(self.dirname+'/'+year):
                os.mkdir(self.dirname+'/'+year)
            
            if not os.path.isdir(os.path.join(self.dirname+'/'+year,month)):
                os.mkdir(os.path.join(self.dirname+'/'+year,month))
        
            shutil.copy(os.path.join(self.dirname,fname),os.path.join(self.dirname+'/'+year,month,fname))
            print("Image {} moved from {} to {} successfully\n".format(fname,os.path.join(self.dirname,fname),os.path.join(year,month,fname)))
def monthOrganise():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    org = ImageOrganizer(folder_selected)
    org.sort_by_yr_month()
def yearOrganise():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    org = ImageOrganizer(folder_selected)
    org.sort_by_year()