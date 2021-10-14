#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 13:38:52 2021

@author: huannn
"""
import os

class FileOperate:
    def filePath(path, name):
        filename = os.path.join(path,name)
        return filename
    def createFile(name,string):
        file = open(name, 'w')
        file.write(string)
        file.close()
    def appendString(name, string):
        file = open(name, 'a')
        file.write(string)
        file.close()
    def readFile(name):
        file = open (name, 'r')
        lines = file.readlines()
        file.close() 
        return lines
    