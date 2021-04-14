# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 18:19:18 2020

@author: Carlos Henrique
"""

lnum = []
lden = []


for i in range(11,100):
    for j in range(11,i):
        a = str(i)
        b = str(j)
        if (a[-1] == "0" or b[-1] == "0"):
            next
        else:
            if (a[0] == b[0]):
                if ((j/i) == (int(b[-1])/int(a[-1]))):
                    lnum.append(j)
                    lden.append(i)
            if (a[0] == b[-1]):
                if ((j/i) == (int(b[0])/int(a[-1]))):
                    lnum.append(j)
                    lden.append(i)
            if (a[-1] == b[-1]):
                if ((j/i) == (int(b[0])/int(a[0]))):
                    lnum.append(j)
                    lden.append(i)
            if (a[-1] == b[0]):
                if ((j/i) == (int(b[-1])/int(a[0]))):
                    lnum.append(j)
                    lden.append(i)
                
print(lnum)
print(lden)

x = (lnum[0]/lden[0])*(lnum[1]/lden[1])*(lnum[2]/lden[2])*(lnum[3]/lden[3])

print(x)