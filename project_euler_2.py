# -*- coding: utf-8 -*-
"""
Created on Sun May  3 13:38:47 2020

@author: Carlos Henrique
"""
    
fibonacci = [0, 1, 2]
even = []

i = 2

while i <= 4000000:
    x = fibonacci[-1]
    y = fibonacci[-2]
    i = x+y
    fibonacci.append(i)
    
for j in fibonacci:
    if j%2 == 0:
        even.append(j)
        
print(sum(even))
    
    