import random

lista4x4=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

while True:
    opcion=input("Calculo de la media entre 2 elementos aleatorios de una matriz 4*4. Pulse s para salir.")
    if opcion=="s":
        break
    x=random.randint(0,len(lista4x4)-1)
    y=random.randint(0,len(lista4x4)-1)

    i=random.randint(0,len(lista4x4)-1)
    j=random.randint(0,len(lista4x4)-1)

    elem1=lista4x4[x][y]
    elem2=lista4x4[i][j]

    res= (elem1+elem2)/2
    print(f"Se ha escogido a los elementos matriz[{x}][{y}]->{elem1} y matriz[{i}][{j}]->{elem2}.\nLA media entre estos dos elementos es: {res}")
