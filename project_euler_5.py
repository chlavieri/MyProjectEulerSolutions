# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:19:36 2020

@author: Carlos Henrique
"""

no_remainder = []
i = 2

while i >= 2:
    if all(i%j == 0 for j in range(1,21)):
        no_remainder.append(i)
        break
    else:
        i += 1
    

print(no_remainder)
            
            
        
    