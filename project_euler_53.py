# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 18:15:44 2020

@author: Carlos Henrique
"""

import math

def comb(n,r):
    return math.factorial(n)/(math.factorial(r) * math.factorial(n-r))

i = 0

for n in range(23,101):
    for r in range(1,n):
        if comb(n,r) > 1000000:
            i += 1
            
print(i)
    