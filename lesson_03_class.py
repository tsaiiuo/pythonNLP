#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 13:34:27 2021

@author: huannn
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 15:34:15 2021

@author: fennieliang
"""


import re
import tkinter as tk
import os

class Text_process:         
    def doc_length(string):
        return len(string)
 
    def doc_split_word(string):
        words = re.split('\W',string) #import re package first
        return words  
    
    def doc_clean(string):
        c_string =re.sub(r'\W',' ', string)#replace non-word character from the string
        c_string =re.sub(r' +',' ', c_string).strip()
        return c_string

    def bag_word(words):  
        counts = dict()

        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1        
        return counts
    
    def find_name(string):
        matches = re.finditer('([A-Z][a-z]+\s){1,}', string)
        return matches

    def find_digit(string):
        matches = re.finditer('(\d+,){0,}(\d+.)(\d+)', string)
        return matches
               
    
class FileOperate:
    
    def filePath(path, name):
        # ***** join file path and file name ************
        filename = os.path.join(path, name)
        return filename
        
    def createFile(filename, string):
        # ***** create a new file ************
        file = open(filename, 'w') #the file is open from the current location   
        file.write(string)
        file.close()
        
    def appendString(filename, string):
        # ***** append a string to an existing file ************
        file = open(filename, 'a')
        file.write(string)
        file.close()
        
    def readFile(filename):
        # ***** read a file ************
        file = open (filename, 'r')
        lines = file.readlines()
        file.close() 
        return lines
    

class Tkinter_GUI:
     
    def centre_math(mywidth,myheight):
        
        #import tkinter as tk
        window = tk.Tk()
        
        # get screen height and width
        scr_w = window.winfo_screenwidth()
        scr_h = window.winfo_screenheight()

        # write formula for center screen
        xLeft = int((scr_w/2) - (mywidth/2))
        yTop = int((scr_h/2) - (myheight/2))
        
        return (xLeft,yTop)   
      