import random
import copy

listaEnteros=[]
listaCuad=[]
abc=[]

for i in range(0,41):
    listaEnteros.append(i)

print(f'6.a La lista de enteros {listaEnteros}')

for i in range(5,51):
    listaCuad.append(i*i)
print(f'6.b La lista de cuadrados de 5 a 50 {listaCuad}')

for i in range(0,26):
    z=i
    while z>=0:
        abc.append(chr(97+i))
        z=z-1

print(abc)
