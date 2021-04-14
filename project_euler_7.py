# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:33:42 2020

@author: Carlos Henrique
"""
l = []
i = 2
while len(l) < 10001:
    if not (any(i%j == 0 for j in range(2,i))):
        l.append(i)
        i += 1
    else:
        i += 1

    
print(l[10000])

        