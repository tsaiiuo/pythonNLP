#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 12:36:56 2021

@author: huannn
"""
import re
#a=re.match('nccumis','nccumis').group()
#print(a)
a=re.search('.s$','109306084nccumis').group(0)#$lastword .== a word 
print(a)
a=re.search('n.*', 'nccumis').group()#*==0~n +==1~n ?==0or1
print(a)
a=re.search('c{2}','nccumis').group()#n{m} search n have m n{m,b} n must between m~b
print(a)
a=re.search('abc\*', 'abc*def').group()#\ search for unique data 
print(a)
a=re.search('[0-9].*','123456778').group()#[0-9][a-z]
print(a)
a=re.search('[a-z].*', '109306084nccumis').group()
print(a)