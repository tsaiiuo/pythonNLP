#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 13:29:46 2021

@author: huannn
"""

# -*- coding: utf-8 -*-

# pip install beautifulsoup4
# pip install requests
# pip install lxml, a third party parser for document in xml
# pip install html5lib, a third party parser for document in html


from bs4 import BeautifulSoup
import requests

url = "https://www.bbc.com/news"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
#soup = BeautifulSoup(page.text, "html.parser")
'''
print(page.encoding) 
page.encoding = "gb18030" #change the page encoding if needed
print(page.encoding)
print(soup.prettify())#page in html structure
'''
'''
#soup.title
# <title>The Dormouse's story</title>
print(f"title: {soup.title}")
#soup.title.name
# <title> tag name
print(f"title name: {soup.title.name}")
#soup.title.text# equals to print(soup.title.string)
# string inside <title> tag
print(f"title string: {soup.title.string}")
#use find 
print(soup.find("title"))
print(soup.find("h1"))#print(soup.find.h1) note: doesn't work this way
print (soup.find(id="link3"))
div = soup.find("div")
print(div)
print(div.select("a"))
print(soup.find("title").text)
print(soup.find("title").string)
soup.title.parent.name
# <title> tag's parent tag
print(f"title parent's name': {soup.title.parent.name}")
#next_node = soup.find("div",id="10")#this is a fake id
#previous_node = next_node.find_previous_siblings("div")
#print(previous_node)
soup.p
# everything inside p tag
print(f"pargraph: {soup.p}")
soup.a
# find first hyper link
print(f"hyper link: {soup.a}")
soup.find_all('a')
# find all hyper links
print(f"hyper links: {soup.find_all('a')}")
find_all = soup.find_all("h1",id="abc", limit = 2)
print (f"hyper link:{find_all}")
#print nothing if the find_all found nothing
for link in soup.find_all('a'):
    print(link.get('href'))
    
 
# remove all tags only the text you can see on the page not from the source code
print(soup.get_text())
 
'''