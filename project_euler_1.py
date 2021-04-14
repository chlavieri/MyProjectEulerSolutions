# -*- coding: utf-8 -*-
"""
Created on Sun May  3 13:10:30 2020

@author: Carlos Henrique
"""

l = []
for i in range(1,1000):
    if i%3 == 0:
        if i not in l:
            l.append(i)
    elif i%5 == 0:
        if i not in l:
            l.append(i)
            

print(sum(l))