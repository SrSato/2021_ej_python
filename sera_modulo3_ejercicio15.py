import random
import utilidades

inventario={}

for i in range(10):
    inventario["Producto"+str(i)] = random.randint(0,100)
listado=list(inventario.items())


precios=[]
for i in range(len(listado)):
    precios.append([listado[i][1],listado[i][0]])

precios.sort()

temp=[]
for i in range(len(precios)):
    temp.append([precios[i][1],precios[i][0]])

precios=temp
print(f"Mas caro: {precios[-1]}")
print(f"Más barato: {precios[0]}")
print(precios)
