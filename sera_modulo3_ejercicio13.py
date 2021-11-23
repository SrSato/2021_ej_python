import random
import utilidades

lista10x10=[]
#
# for exterior in range(0,9):
#     fila=[]
#     for interior in range(0,9):
#         fila.append(random.randint(0,100))
#     lista10x10.append(fila)
# Esto de arriba es lo mismo que:
lista10x10=[[random.randint(0,1) for i in range(10)] for j in range(10)]

print("Buscaminas!!!!\nPara salir escoge 99 en fila o columna.")
while True:
    fila=int(utilidades.pideNumero("Escoge una fila del 0 al 9: "))
    if fila==99:
        break
    if fila<0 or fila>9:
        print("Del cero al nueeeeeve... Prueba otra vez")
        continue
    col=int(utilidades.pideNumero("Escoge una columna del 0 al 9: "))
    if col==99:
        break
    if col<0 or col>9:
        print("Del cero al nueeeeeve... Prueba otra vez")
        continue
    if lista10x10[fila][col]==1:
        print("Ups... había mina. BOOOOM.")
        break
    else:
        print("Correcto, no hay mina... sigue probando... MUAHAHAHA!")
