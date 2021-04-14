# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 11:08:39 2020

@author: Carlos Henrique
"""

import sympy
#primes = [2]
circ = []
#for n in range(2,1000000):
#    if any(n%i == 0 for i in range(2,n)):
#        next
#    else:
#        primes.append(n)
primes = list(sympy.primerange(1,1000000))

        
for j in primes:
    a = [int(d) for d in str(int(j))]
    z = str(j)
    b = []
    for j in range(len(a)):
        c = z[j:] + z[:j]
        c = int(c)
        b.append(c)
    if all(x in primes for x in b):
        circ.append(j)
        
print("The are", len(circ), "numbers.")
print(primes)