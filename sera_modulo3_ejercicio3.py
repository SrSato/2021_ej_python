lista=[8,9,10]

print(f'3. La lista es: {lista}')

lista[1]=17

print(f'\ta. El segundo valor será 17 {lista}.')

for i in range(4,7):
    lista.append(i)

print(f'\tb. Añadimos 4,5,6 al final: {lista}.')

lista.pop(0)
print(f'\tc. Eliminamos el primer valor: {lista}.')

lista.sort()
print(f'\td. La ordenamos: {lista}.')

lista=lista*2
print(f'\te. Duplicamos la lista (NO el valor de cada elemento): {lista}.')

lista.insert(11,25)
print(f'\tf. Metemos 25 en la duodécima posición: {lista}.')

for i in range(len(lista)):
    lista[i]=lista[i]*3

print(f'\te. Multiplicamos valores por 3: {lista}.')

centenarios=[]
for valor in lista:
    if valor>100:
        centenarios.append(valor)
print(f'\tf Los elementos que pasan de valor 100 son: {centenarios}')
