import random
import copy

lista=[]

while len(lista)<20:
    lista.append(random.randint(1,100))

print(f'2. La lista es: {lista}')

media=sum(lista)/len(lista)

print(f'\ta. La media de los valores es {media}.')
print(f'\tb. El valor mayor es {max(lista)} y el menor es {min(lista)}.')

if 5 in lista:
    cinco="Si"
else:
    cinco="No"

print(f'\tc. ¿Está el 5 en la lista?: {cinco}.')

ordenada=copy.copy(lista)
ordenada.sort()

print(f'\td. El segundo valor mayor es {ordenada[-2]} y el segundo valor menor es {ordenada[1]}.')

pares=0
for elem in lista:
    if elem%2 == 0:
        pares=pares + 1

print(f'\te. El número de pares es {pares}.')
