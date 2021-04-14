# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 22:02:32 2020

@author: Carlos Henrique
"""
distinct = []
for a in range(2,101):
    for b in range(2,101):
        y = a**b
        if y not in distinct:
            distinct.append(y)
            

print(len(distinct))
        