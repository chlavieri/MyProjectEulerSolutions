# -*- coding: utf-8 -*-
"""
Created on Thu May 21 09:21:41 2020

@author: Carlos Henrique
"""

def d(a):
    nums = []
    for j in range(1,a):
        if a%j == 0:
            nums.append(j)
    return sum(nums)

amicable = []

for n in range(1,1000):
    for i in range(1,n):
        if d(n) == d(i) and i not in amicable and n not in amicable:
            amicable.append(i)
            amicable.append(n)

print(sum(amicable))
            
    
    
    
            
    
            