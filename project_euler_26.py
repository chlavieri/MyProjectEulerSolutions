# -*- coding: utf-8 -*-
"""
Created on Sun May 24 21:54:03 2020

@author: Carlos Henrique
"""

maximumstr = []

for i in range(2,1000):
    x = 1/i
    xdgts = str(x)
    xdgts = xdgts.replace("0.", "")
    for j in range(len(xdgts)):
        for k in range(len(xdgts)):
            if xdgts[j:k] == xdgts[k:j+k]:
                if xdgts[j:k] != xdgts[j+1:k+1]:
                    same_lst = [int(d) for d in (xdgts[j:k])]
                    if len(same_lst) > len(maximumstr):
                        print(len(same_lst))
                        maximumstr = same_lst
                        num = i
                
print(num)
print(1/num)

                
            
            
            
        
        
        