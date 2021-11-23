import random
import copy

lista=[]

while len(lista)<10:
    lista.append(random.randint(1,10))

print(f'1. Trabajaremos con esta lista: {lista}')
print(f'a. Hay {len(lista)} elementos.' )
print(f'b. El último elemento es {lista[len(lista)-1]}' )
inversa = copy.deepcopy(lista)

print(f'c. Lista inversa: {inversa}')
print(lista)

if 5 in lista:
    print("d. Tenemos rimas en la lista")
else:
    print("d. No tenemos rimas")

lista.pop(0)
lista.pop(len(lista)-1)
print(f'e. Eliminando el primer número y el último de la lista: {lista}')

lista.insert(2,5)
lista.insert(7,5)
print(f'f. Metemos el 5 en la posición 3 y en la 8 (3º y 8º): {lista}')
print(f'g. El 5 aparece {lista.count(5)} veces en {lista}')
ordenada = copy.deepcopy(lista)
ordenada.sort()
print(f'h. Esta es la lista modificada y ordenada: {ordenada}')
