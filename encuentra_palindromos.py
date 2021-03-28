# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 14:10:53 2021

Dado un archivo de texto utf-8 donde cada línea es una palabra,
obtiene y cuenta todos los palíndromos de ese archivo

@author: Pablo R. Alves
"""


ubicacion_diccionario = input("Introduce el directorio de tu txt: ")
diccionario = open(ubicacion_diccionario, 'r', encoding='utf-8')
palabras = diccionario.readlines()

def es_palindromo(cadena):
    return cadena == cadena[::-1]


palindromos_encontrados = 0

for palabra in palabras:
    palabra = palabra.rstrip() # Eliminamos caracter de salto de línea
    if es_palindromo(palabra):
        print("{}: {}".format(palindromos_encontrados, palabra.strip()))
        palindromos_encontrados += 1

print('Encontré:',palindromos_encontrados,'palabras palíndromo en',diccionario.name)
