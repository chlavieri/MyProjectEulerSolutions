# -*- coding: utf-8 -*-
"""
Created on Wed May 20 17:27:43 2020

@author: Carlos Henrique
"""
import num2word
list_written = []
list_lenght = []
def lenght(x):
    x.replace("-", "")
    x.replace(" ", "")
    x.replace(",", "")
    len(x)
    
for i in range(1,1001):
    x = num2word.to_card(i)
    list_written.append(x)

for j in range(len(list_written)):
    y = int(lenght(list_written[j]))
    list_lenght.append(y)
    
print(sum(list_lenght))
    

        
        
        