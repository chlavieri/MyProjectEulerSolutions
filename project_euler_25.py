# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:16:53 2020

@author: Carlos Henrique
"""

fibonacci = [1,1]

for i in fibonacci:
    a = fibonacci[-1] + fibonacci[-2]
    b = str(a)
    fibonacci.append(a)
    if len(b) == 1000:
        print(len(fibonacci))
        break
