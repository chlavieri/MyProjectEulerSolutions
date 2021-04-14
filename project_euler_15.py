# -*- coding: utf-8 -*-
"""
Created on Wed May 20 15:37:20 2020

@author: Carlos Henrique
"""
import math
def binomial(n, k):
    x = math.factorial(n)
    y = math.factorial(k)
    z = math.factorial(n-k)
    print(x/(y*z))

binomial(40,20)
    