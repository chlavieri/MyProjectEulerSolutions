# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 11:46:42 2020

@author: Carlos Henrique
"""

palind = []
def dec_to_bin(x):
    return int(bin(x)[2:])

def palindromic(x):
    if str(x) == str(x)[::-1]:
        if str(dec_to_bin(x)) == str(dec_to_bin(x))[::-1]:
            palind.append(x)
            
            
for i in range(1000000):
    palindromic(i)
    
summation = sum(palind)
print("The sum is", summation)