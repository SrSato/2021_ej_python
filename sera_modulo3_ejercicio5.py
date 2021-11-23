import random

lista=[]

while len(lista)<100:
    lista.append(random.randint(1,10))

print(f'5. La lista:\n{lista}')

siguiente=False

indice=0
while indice < len(lista):
    cuantos=lista.count(lista[indice])
    if cuantos > 1:
        lista.pop(indice)
    else:
        indice=indice+1

print(f'Se queda en {lista}')
