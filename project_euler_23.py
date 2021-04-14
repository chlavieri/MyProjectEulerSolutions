# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 17:57:16 2020

@author: Carlos Henrique
"""

abundant = []
cannot = []

for i in range(2, 28124):
    divisors = []
    for j in range(1, i):
        if i%j == 0:
            divisors.append(j)
    if sum(divisors) > i:
        abundant.append(i)
        
for i in range(2, 28124):
    abundant2 = []
    for item in abundant:
        if item < i:
            abundant2.append(item)
    for j in abundant2:
        if (all(i != j+k) for k in abundant2):
            if i not in cannot:
                cannot.append(i)

print("The sum of the numbers which cannot be written as the sum of two abundant numbers is", sum(cannot))
