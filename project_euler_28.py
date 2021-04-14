# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 19:06:03 2020

@author: Carlos Henrique
"""
import sys
sys.setrecursionlimit(530)
def f(n):
    if n == 0:
        return 1
    if n > 0:
        return 4*((2*n+1)**2) -12*n + f(n-1)
        
    
        
print(f(500))