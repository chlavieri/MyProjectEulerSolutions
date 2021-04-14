# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 22:07:05 2020

@author: Carlos Henrique
"""
nums = []
for i in range(2,1000000):
    i_list = [int(d) for d in str(i)]
    i_list = [d**5 for d in i_list]
    if sum(i_list) == i:
        nums.append(i)
        
print(sum(nums))
        