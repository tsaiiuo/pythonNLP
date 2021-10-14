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

import tkinter as tk
from tkinter import *
from tkinter import filedialog  
from methodclass import Text_process as T



def word_fre_label(fict):
    dic_text = ""
    for i in fict :
        dic_text = dic_text +  i +" : "+ str(fict[i]) + "\n"
    return dic_text


def process():
    global content_label, dict_label, a
    content = textarea.get('0.0','end')
    word_dic = T.bag_word(T.doc_split_word(content))
    del word_dic['']
    print(word_dic)
    dict_label['text'] =  word_fre_label(word_dic)
    path.grid(column = 0, row = 2  , sticky=tk.W)
    read_file_bt.grid(column = 0, row = 2  , sticky=tk.E)
    process_bt.grid(column = 0, row = 3  , sticky=tk.E)
 
    return 
    

def openFile():
    tf = filedialog.askopenfilename(
        initialdir="/Users/fennieliang/Documnets/GitHub/python/lesson03", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    path.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    textarea.insert(END, data)
    tf.close()

# Create a GUI app
wd = tk.Tk()

# Give a title to your app
wd.title("My Python Class")
wd.geometry("570x600") 

textarea = tk.Text(wd)
textarea.grid(column = 0, row = 0, sticky=tk.W)

dict_label = tk.Label(wd, justify = 'left' )
dict_label.grid(column = 0, row = 1, sticky=tk.W+tk.N)


path = tk.Entry(wd)
path.grid(column = 0, row = 2, sticky=tk.W)


read_file_bt = tk.Button(wd, height=1, width=10, text="Read File", command=openFile)
read_file_bt.grid(column = 0, row = 2, sticky=tk.E)


process_bt = tk.Button(wd, text = "Process", command=process)
process_bt.grid(column = 0, row = 3, sticky=tk.E)
 
wd.mainloop()
'''
import webbrowser
# open an HTML file on my own (Windows) computer

from methodbox import FileOperate as fo

name = 'example.html'
path = '/Users/huannn/Documents/GitHub/pythonNLP'
string = """<Content-Type: text/html>
 
<!DOCTYPE html>
<html lang="en">
<head>
  <title>HTML Tutorial</title>
  <meta charset="UTF-8">
  <meta name="description" content="Free Web tutorials">
  <meta name="keywords" content="HTML, CSS, JavaScript">
  <meta name="author" content="Fennie Liang">
</head>
<body>
  <h1 style="color:red">Hello World</h1>
  <h2>Heading 2</h2>
  <h3 style="color:blue">Heading h3</h3>
  <h4>Heading h4</h4>
  <h5>Heading 5</h5>
  <h6>Heading 6</h6>
  <h7>Heading 7</h7>
  <p>
    Our first <b>HTML</b>, <mark>lesson</mark>, taught by Dr. <a href="https://sites.google.com/site/example/"><ins>Fennie Liang</ins></a>.
  </p>
  <p> 
    <del>cross line</del>
  </p>
  <p>
    This <br> is    a paragraph <br> with <br> line     breaks <!-- 這裹的註解文字不會出現在網頁中 -->
  </p>
  <p style="color:green">
    Add green colour to this paragraph.
  </p>
  <p>bullet points:</p>
  <ul>
    <li>Lesson 1</li>
    <li>Lesson 2</li>
    <li>Lesson 3</li>
  </ul>
<p>Auto numbered list:</p>
  <ol>
    <li>Taiwan </li>
    <li>America </li>
    <li>United Kingdom </li>
    <li>France</li>
  </ol>
</body>
</html>
"""
fo.create(path, name, string)

# open an HTML file on my own (Windows) computer, change the path to suit yours
url = "file:///Users/huannn/Documents/GitHub/pythonNLP/example.html"

webbrowser.open_new(url)

