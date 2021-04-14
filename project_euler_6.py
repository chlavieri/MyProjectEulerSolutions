# -*- coding: utf-8 -*-
"""
Created on Tue May  5 23:55:17 2020

@author: Carlos Henrique
"""

def sum_of_squares(n):
    list_of_squares = [i*i for i in range(n+1)]
    return sum(list_of_squares)

def square_of_sums(n):
    a = sum(range(0,n+1)) ** 2
    return int(a)

def difference(n):
    print((square_of_sums(n) - sum_of_squares(n)))

difference(100)