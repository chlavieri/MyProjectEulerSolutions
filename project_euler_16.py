# -*- coding: utf-8 -*-
"""
Created on Wed May 20 17:07:54 2020

@author: Carlos Henrique
"""

def sum_digits(n):
    digits = []
    x = 2**n
    for d in str(x):
        d = int(d)
        digits.append(d)
    print(sum(digits))
    
sum_digits(1000)
    