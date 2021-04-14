# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 22:20:17 2020

@author: Carlos Henrique
"""

nums = []

a = 1
b = 2
c = 5
d = 10
e = 20
f = 50
g = 100
h = 200

for i in range(0, 201):
    for j in range(0, 101):
        for k in range(0,41):
            for l in range(0,21):
                for m in range(0,11):
                    for n in range(0,5):
                        for o in range(0,3):
                            for p in range(0,2):
                                q = a*i +b*j + c*k + d*l + e*m + f*n + g*o + h*p
                                if q == 200:
                                    nums.append(q)
                                    
                                    
print(len(nums))
            
            