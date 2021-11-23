import random

lista10x10=[]
#
# for exterior in range(0,9):
#     fila=[]
#     for interior in range(0,9):
#         fila.append(random.randint(0,100))
#     lista10x10.append(fila)
# Esto de arriba es lo mismo que:
lista10x10=[[random.randint(0,100) for i in range(10)] for j in range(10)]

print(lista10x10)
for i in range(len(lista10x10)):
    print(lista10x10[i])

print(f"Valor más alto de la 3ªFila: {max(lista10x10[2])}")

for i in range(len(lista10x10)):
    mayor=0
    if lista10x10[i][5] > mayor:
        mayor=lista10x10[i][5]

print(f"Valor más alto de la 6ªColumna: {mayor}")
