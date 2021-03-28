# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 11:04:47 2021

@author: Pablo
"""
import re

#diccionario = open('palabras0.txt', 'r') #Viejo
#salida = open("palabras_segundamitad.txt","w+")

#diccionario = open('0_palabras_todas.txt', 'r', encoding='utf-8')
#salida = open("primera_mitad(Full).txt","w+")

diccionario = open('verbos-espanol-conjugaciones.txt', 'r', encoding='utf-8')
salida = open("primera_mitad(Verbos Full).txt","w+")

palabras = diccionario.readlines()
patron = re.compile('^[abcdefghijklmnáéí]+$') 

def me_sirve(s):
    return (lambda x: True if re.search(patron, x) else False)(s)

count = 0

for palabra in palabras:
    if me_sirve(palabra):
        count += 1
        print("{}: {}".format(count, palabra.strip()))
        salida.write(str(palabra))
        
print('Me sirvieron:',count,'palabras')
salida.close()