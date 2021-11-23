lista=[1,2,3,4,5,6,7,8,9]

indice=4

for indice in range(indice,len(lista)):
    print("Hola" ,lista[indice])

res=[elem-1 if elem%2==0 and elem>3 else "patata" for elem in lista ]

print(res)

mas3=len([elem for elem in lista if elem>3])

print(mas3)

matriz=[[1,2,3],[3,4,5],[6,7,8]]

print(matriz)


trunca=[[1,2,3],[4,5],[4,7,8,9],[10,11,12]]

print([trunca[i][j] for i in range(0, len(trunca)) for j in range(0, len(trunca[i]))])

try:
    f = open("demofile.txt")
except:
    print("No se ha podidio leer el fichero")
