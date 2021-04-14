# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 14:50:47 2020

@author: Carlos Henrique
"""

from num2words import num2words

nums = []
lens = []


for i in range(1,1001):
    x = num2words(i)
    x = x.replace(" ", "")
    x = x.replace("-", "")
    x = x.replace(",", "")
    nums.append(x)
    
for num in nums:
    y = len(num)
    lens.append(y)
    
print("The amount of letters used is", sum(lens))
    
    

    
    