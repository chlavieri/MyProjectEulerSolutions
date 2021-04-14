# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 20:25:39 2020

@author: Carlos Henrique
"""

x = str(1)

for i in range(2,1000000):
    x = x + str(i)
    

y = int(x[0])*int(x[9])*int(x[99])*int(x[999])*int(x[9999])*int(x[99999])*int(x[999999])

print(y)