#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 14:19:13 2021

@author: huannn
"""
import re
String=input("please input some string:")
if(len(String)<5):String=input("please input some string:")
if(len(String)>=5):print(f"the string length: {len(String)}")
words=re.split(' ',String)
print(words)

substring=String[2:6]
print(substring)
class Textprocess:
    
    def doc_length(string):
        return len(string)
    
    def doc_split(string):
        words=re.split(' ', string)
        return words
    
    def doc_clean(string):
        words=re.sub(r"[\W_]",' ', string)
        return words


    