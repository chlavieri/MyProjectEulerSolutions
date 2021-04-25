# -*- coding: utf-8 -*-
"""
Created on Sat May 16 21:03:25 2020

@author: Carlos Henrique
"""

from sympy import divisors
i = 0
triangle = 0
div = set()

while len(div) <= 500:
    div = set()
    i += 1
    triangle = triangle + i
    div = list(divisors(triangle))
    # for j in range(1, int(math.sqrt(triangle)+ 1)):
    #     if (triangle % j == 0):
    #         div.update([i, triangle // j])
    if (len(div) >= 500):
        print(triangle)
   
   

   
   
   
   