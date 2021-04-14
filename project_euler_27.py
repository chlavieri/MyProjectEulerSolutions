# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 16:14:43 2020

@author: Carlos Henrique
"""

import sympy

def quad(n, a, b):
    return n**2 + a*n + b

primes = list(sympy.primerange(1,100000))
times1 = []
times2 = []
coef1 = []
coef2 = []

for i in range(-1000, 1000):
    for j in range(-1001, 1001):
        coef1.append(i)
        coef1.append(j)
        k = 0
        while quad(k, i, j) in primes:
            times2.append(0)
            k += 1
        if len(times2) > len(times1):
            times1 = times2
            coef2 = coef1
        coef1 = []
        times2 = []
        
x = coef2[0]*coef2[1]
print(x)
            
            
            