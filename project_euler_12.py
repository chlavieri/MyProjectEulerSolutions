# -*- coding: utf-8 -*-
"""
Created on Sat May 16 21:03:25 2020

@author: Carlos Henrique
"""

list_triangle_numbers = []

# def triangle_numbers(n):
#     for i in range(1,n):
#         j = (i*(i+1))/2
#         j = int(j)
#         list_triangle_numbers.append(j)
   
#     for j in list_triangle_numbers:
#         divisors = []
#         for k in range(1, j):
#             if j%k == 0:
#                 divisors.append(k)
#                 if len(divisors) == 5:
#                     print("The value of the number with over 5 divisors is", j)
#                     break
    
    
# triangle_numbers(10)
        

import math

for n in range(100000):
    divisors = []
    triangle = (n*(n+1))/2
    triangle = int(triangle)
    i = 1
    while (i <= math.sqrt(triangle)):
        if n%i == 0:
            if (n/i == i):
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(n/i)
            if len(divisors) > 500:
                print(triangle)
                break
        i += 1
           
   
   
   
   
   
   
   
   
   
   