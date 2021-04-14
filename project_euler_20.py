# -*- coding: utf-8 -*-
"""
Created on Thu May 21 09:12:19 2020

@author: Carlos Henrique
"""

import math
digits = []

def sum_fact(n):
    for i in str(math.factorial(n)):
        i = int(i)
        digits.append(i)
    print(sum(digits))
    
sum_fact(100)
        