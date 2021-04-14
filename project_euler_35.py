# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 16:19:04 2020

@author: Carlos Henrique
"""

circ = []
primes = []
def prime(n):
    if n == 2:
        return True
    if n > 2:
        if any(n%i == 0 for i in range(2,n)):
            return False
        else:
            return True
            

def circular(n):
    a = [int(d) for d in str(n)]
    z = str(n)
    b = []
    b.append(n)
    for j in range(len(a)):
        c = z[j:] + z[:j]
        c = int(c)
        b.append(c)
    if all(prime(c) == True for c in b):
        circ.append(n)
        
        
for k in range(2,1000000):
    circular(k)
    
print("There are", len(circ), "numbers.")
print(prime(4))
            
            

            
            
        
        
    