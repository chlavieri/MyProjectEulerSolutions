# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 18:49:44 2020

@author: Carlos Henrique
"""

import numpy as np
import math

solutions1 = []

p = 1
while p <= 1000:
    solutions2 = np.array([0])
    for a in range(1,400):
        for b in range(1,400):
            c = math.sqrt(a**2 + b**2)
            if a+b+c == p and np.size(solutions2) == 1:
                solutions2 = np.array([a,b,c])
            if a+b+c == p and np.size(solutions2) > 1:
                solutions2 = np.append(solutions2, [a,b,c])
    if np.size(solutions2) > np.size(solutions1):
        solutions1 = solutions2
        sol = p
    p += 1        
    
print(sol)
    

                
                