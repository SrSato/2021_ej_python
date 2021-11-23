import random
import utilidades

inventario={}
cierre="salir"

for i in range(10):
    inventario["Producto"+str(i)] = random.randint(0,100)
menu="Escribe el nombre del producto que quieras consultar o "+cierre+" para acabar: "

while True:
    buscado=input(menu)
    if buscado == cierre:
        break
    if buscado in inventario:
        print(f"{buscado} tiene un preio de {inventario[buscado]}")
    else:
        print("No encontramos ese producto en nuestro inventario.")
