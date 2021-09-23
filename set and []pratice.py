#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 15:24:16 2021

@author: huannn
"""

#list[item1,item2....]
a=['apple','melon','orange','apple']
a.append('tomato')
a.insert(3, 'tomato')
print(a)
a.remove('apple')
print(a)
a.pop(0)#pop out a certain position
print(a)
a1=['fish','pork']
#a.append(a1) will be['fish'....]
a.extend(a1)
print(a)

print(a.index('fish'))#find the index
print(a.count('tomato'))#count q

a.reverse()#tenet
print(a)
a.sort()#abc order
print(a)
a2=a.copy()
print(a2)

#set function
b=set(a2)#make a set from a list
print(b)
#b.remove('apple')#if the set doesnt exist item will be error need use discard
b.discard('apple')
print(b)

b.update(a)#use update to append a list
print(b)
set1={'1','2','3'}
set2={'3','4','5'}
print(set1|set2)#same as below
#print(set1.union(set2))

print(set1-set2)#remove item appear in set2
print(set1&set2)

print(set1.difference(set2))#set1 be base


for fruit in a:#string item
    print(fruit)
    
a.clear()
print(f"final list:{a}")