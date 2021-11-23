import random
import utilidades

def encuentra_todas(letra,texto):
    res=[]
    texto=list(texto)
    for i in range(0, len(texto)):
        if texto[i]==letra:
            res.append(i)
    return res

def pide_un_char(frase):
    char="Aquí va tu char"

    while len(char)!=1:
        char=input(frase)
        if len(char)!=1:
            print("Por favor, introduce sólo uno.")
    return char


texto=input("Introduce el texto: ")
char=pide_un_char("Introduce un char: ")
print(encuentra_todas(char,texto))
