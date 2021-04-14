# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:09:26 2020

@author: Carlos Henrique
"""

pentagonal = []
for n in range(1,900):
    p = (n*(3*n - 1))/2
    p = int(p)
    pentagonal.append(p)
    
diff1 = 1000000000
for i in range(0,899):
    for j in range(0,899):
        if j != i:
            summ = pentagonal[j] + pentagonal[i]
            diff2 = pentagonal[j] - pentagonal[i]
            diff3 = pentagonal[i] - pentagonal[j]
            if diff2 < 0:
                diff2 = diff2*(-1)
            if diff3 < 0:
                diff3 = diff3*(-1)
            if (summ in pentagonal and diff2 in pentagonal):
                if (diff2 < diff1):
                    diff1 = diff2
            if (summ in pentagonal and diff3 in pentagonal):
                if (diff3 < diff1):
                    diff1 = diff3

print(diff1)
    