#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 13:36:29 2021

@author: huannn
"""
dic1={"lemon":1,"apple":2,"pitch":3}
for key, value in dic1.items():
    if(key=="lemon"):print(f"key={key}; value={value}")
for items in dic1.items():
    print(items)
dic2=dic1.copy()
#for items in dic2.items():
    #print(items)

dic1.pop("lemon") 
dic1.update({"pear":4})
for items in dic1.items():
    print(items)
    
    
#tuple(item,item.....)
t=("chicken","duck","dog","chicken")
print(t[0])
for i in range(len(t)):
    print(t[i])
  
    