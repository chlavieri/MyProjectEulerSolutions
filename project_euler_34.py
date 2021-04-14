# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 16:02:08 2020

@author: Carlos Henrique
"""

import math
nums = []
for i in range(3,100000):
    b = []
    a = [int(d) for d in str(i)]
    for digits in a:
        digits = int(digits)
        c = math.factorial(digits)
        b.append(c)
    if sum(b) == i:
        nums.append(i)
        
print(sum(nums))