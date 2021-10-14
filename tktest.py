#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:29:39 2021

@author: huannn
"""
'''
import tkinter as tk

main = tk.Tk() #declare a main window

main.title("My Python Window")


#  add button to the window
button = tk.Button(main, #widget
                   text = "hello", 
                   width = 20,
                   height=5)

button.pack(side='bottom')#every widget needs to be packed in the main window
main.mainloop()#mainloop is for the window to active

import tkinter as tk
from tkinter import messagebox

def button_event():
    #print(var.get())
    if var.get() == '':
        tk.messagebox.showerror('message', 'Please Give your answer')
    elif var.get() == '我大哥':
        tk.messagebox.showinfo('message', 'Correct')
    else:
        tk.messagebox.showerror('message', 'Wrong')

root = tk.Tk()
root.title('My Python Class')

mylabel = tk.Label(root, text='陳威是誰')
mylabel.grid(row=0, column=0)

var = tk.StringVar()
myentry = tk.Entry(root, textvariable=var)
myentry.grid(row=0, column=1)

mybutton = tk.Button(root, text='Submit', command=button_event)
mybutton.grid(row=1, column=1)

root.mainloop()
'''
import tkinter as tk
#from tkinter import *
from tkinter import filedialog

def openFile():
    tf = filedialog.askopenfilename(
        #change to your own directory below to have a correct path
        initialdir="/Users/huannn/Documents/GitHub/pythonNLP/file_list.txt", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    path.insert(tk.END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    txtarea.insert(tk.END, data)
    tf.close()

ws = tk.Tk()
ws.title("My Python Class")
ws.geometry("500x500")
ws['bg']='#5CF9F2'

txtarea = tk.Text(ws, width=100, height=20)
txtarea.pack(pady=20)

path = tk.Entry(ws)
path.pack(side="left", expand="yes", fill="x")



tk.Button(
    ws, height=1, width=10,
    text="Open File", 
    command=openFile
    ).pack(side="right",  expand="yes", fill="x")


ws.mainloop()