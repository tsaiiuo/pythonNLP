#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 14:52:14 2021

@author: huannn
"""

class Lesson:
    teacher="Ian"
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
         
         
        
p=Lesson("John","selly")

print(Lesson.teacher)
print(p.firstname)
print(p.lastname)