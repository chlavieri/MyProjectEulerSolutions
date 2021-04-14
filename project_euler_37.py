# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:03:06 2020

@author: Carlos Henrique
"""

import sympy

trunc = []
primes = list(sympy.primerange(1,100))
for i in primes:
    l = []
    a = float(i)
    a = int(a)
    a = str(a)
    b = [int(d) for d in str(i)]
    for j in range(len(b)):
        c = a[:j]
        d = a[j:]
        l.append(c)
        l.append(d)
    if all(x in primes for x in l):
        trunc.append(i)
        
print(sum(trunc) - 17)