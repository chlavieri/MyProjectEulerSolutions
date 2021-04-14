# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 17:11:43 2020

@author: Carlos Henrique
"""

import sympy
primes = list(sympy.primerange(1,1000000))

i = 1
while i >= 1:
    if i%2 != 0:
        if i not in primes:
            for j in range(1,i):
                if j in primes:
                    if any(i == j + 2*(k**2) for k in range(1,i)):
                        pass
                    else:
                        print(i)
                        break
                    
    i += 1
    

                        
                        
                