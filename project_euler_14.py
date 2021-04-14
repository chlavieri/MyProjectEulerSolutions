# -*- coding: utf-8 -*-
"""
Created on Tue May 19 18:07:36 2020

@author: Carlos Henrique
"""
collatz_sequence = []
collatz_sequence_2 = []
def start():
    global collatz_sequence
    global collatz_sequence_2
    global i
    collatz_sequence_2.append(i)
    if i%2 == 0:     
        while i%2 == 0:
            i = i/2
            if i%2 == 0:
                collatz_sequence_2.append(i) 
            if i == 1:
                collatz_sequence_2.append(i)
                if len(collatz_sequence_2) >= len(collatz_sequence):
                    collatz_sequence = collatz_sequence_2
                collatz_sequence_2 = []
            if i%2 != 0 and i !=1:
                start()
    if i%2 != 0 and i !=1:
        i = 3*i + 1
        collatz_sequence_2.append(i)
        while i%2 == 0:
            i = i/2
            if i%2 == 0:
                collatz_sequence_2.append(i)
            if i%2 != 0 and i != 1:
                start()
            if i == 1:
                collatz_sequence_2.append(i)
                if len(collatz_sequence_2) >= len(collatz_sequence):
                    collatz_sequence = collatz_sequence_2
                collatz_sequence_2 = []
        

for i in range(2,1000000):
    start()
            
                
                
        
print(collatz_sequence)
print("The starting number which provides the longest chain is", collatz_sequence[0])
print("The lenght of the sequence is", len(collatz_sequence))

                
            
            
            
        
        
        
    