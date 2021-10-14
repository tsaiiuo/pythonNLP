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
'''
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