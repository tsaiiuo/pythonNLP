#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 15:19:52 2021

@author: huannn
"""

a=1;b=2
print(f"1. a+b={a+b}")
a=38.5
print(f"2. a+b={a+b}")
b=1e+3
print(f"3. b={b}")
print(f"4. a+b={a+b}")
sum=a+b
print(f"5. a+b={sum}")
#n1=int(input("Enter the first number: "))
#n2=int(input("Enter the second number: "))
n1=input("Enter the first number: ")
n2=input("Enter the second number: ")
sum=int(n1)+int(n2)
print(f"n1 +n2={sum}")
y=0
for i in range(1,6):
    x=input("Enter a number")
    y+=int(x)
print(f"the result={y}")