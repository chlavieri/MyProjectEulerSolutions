# -*- coding: utf-8 -*-
"""
Created on Sun May  3 21:13:49 2020

@author: Carlos Henrique
"""
import numpy as np
# n = 13195
n = 600851475143
i = 2
factor_prime = []
while n != 1:
    if n%i == 0:
        n = n/i
        factor_prime.append(i)
    else:
        i+=1
print(factor_prime)
print(np.max(factor_prime))
            