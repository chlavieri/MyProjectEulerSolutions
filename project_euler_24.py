# -*- coding: utf-8 -*-
"""
Created on Sat May 23 23:32:55 2020

@author: Carlos Henrique
"""
from itertools import permutations
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
permut = list(permutations(nums))
permut = sorted(permut)
print(permut[999999])

        