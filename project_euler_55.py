# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 19:31:29 2020

@author: Carlos Henrique
"""

i = 0

for n in range(10,10000):
    a = 0
    x = str(n)
    while a < 50:
        z = int(x)
        y = x[::-1]
        y = int(y)
        g = z + y
        g = str(g)
        h = g[::-1]
        if g == h:
            i += 1
            break
        else:
            x = g
            a += 1
        
print(i)
        