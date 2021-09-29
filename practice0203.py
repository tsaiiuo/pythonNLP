#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 17:39:29 2021

@author: huannn
"""


for i in range (20):

    if (i%2!=0):
        for j in range (20-int(i/2)):
            print (" ", end='')
        for k in range (i):
            print ("*", end='')
        print ('')