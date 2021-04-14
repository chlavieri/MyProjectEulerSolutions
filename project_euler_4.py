# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:48:00 2020

@author: Carlos Henrique
"""
def maior_palindromo(digitos):
    lista_palindromos = []
    if digitos == 2:
        for i in range(10,100):
            for j in range(10,100):
                a = i*j
                if str(a) == str(a)[::-1]:
                    lista_palindromos.append(a)
        print(max(lista_palindromos))
    if digitos == 3:
        for i in range(100,1000):
            for j in range(100,1000):
                a = i*j
                if str(a) == str(a)[::-1]:
                    lista_palindromos.append(a)
        print(max(lista_palindromos))
            
    if digitos > 3 or digitos < 2:
        print("Escolha 2 ou 3!")
        
        
maior_palindromo(3)
            
            
    