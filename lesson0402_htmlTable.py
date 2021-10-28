#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 13:25:18 2021

@author: huannn
"""
# -*- coding: utf-8 -*-
import webbrowser

# open an HTML file on my own (Windows) computer
# Display html tables

from methodbox import FileOperate as fo

name = 'example.html'
path = '/Users/fennieliang/Documents/GitHub/python/week07'
string = """<Content-Type: text/html>
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <title>HTML Tutorial</title>
  <meta charset="UTF-8">
  <meta name="description" content="Free Web tutorials">
  <meta name="keywords" content="HTML, CSS, JavaScript">
  <meta name="author" content="Fennie Liang">

</head>

<body>
  
  <hr>
<table style="width:80%" align="center" border="1">
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
    <th>Age</th>
  </tr>
  <tr>
    <td>Mary</td>
    <td>Tomson</td>
    <td>50</td>
  </tr>
  <tr>
    <td>John</td>
    <td>Tait</td>
    <td>80</td>
  </tr>
</table>

</body>
</html>
"""
  
fo.create(path, name, string)


# open an HTML file on my own (Windows) computer
url = "file:///Users/fennieliang/Documents/GitHub/python/week07/example.html"

webbrowser.open_new(url)

# open a public URL, in this case, the webbrowser docs
#url = "http://google.com"
#webbrowser.open_new(url)
