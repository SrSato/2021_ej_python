#Escribir 6 numeros randoms 1000 veces y sacar datos estadisticos
import random

resultado=[]
prom=[]
mas=[]
mini=[]
freq={}

for vuelta in range(0,1000):
    lista=[]
    for i in range(0,6):
        num=random.randint(1,49)
        #Este if es para poderse usar con la Primitiva
        #porque los num no se pueden repetir en el sorteo :P
        if num not in lista:
            lista.append(num)
            if num not in freq:
                freq[num]=1
            else:
                freq[num]=freq[num]+1

    prom.append(int(sum(lista)/len(lista)))
    mas.append(max(lista))
    mini.append(min(lista))
    resultado.append(lista)
    print(f"Sorteo número {vuelta}: {lista} El más alto es {mas[vuelta]}, el más bajo es {mini[vuelta]} y el promedio es {prom[vuelta]}")

print(f'TOTALES: promedio total: {int(sum(prom)/len(prom))} Valor más alto: {max(mas)} y valor más bajo: {min(mini)}' )
print(f"Frecuencias:")
for i in range(1, len(freq)+1):
    print(f"Para {i}: {freq[i]}")
