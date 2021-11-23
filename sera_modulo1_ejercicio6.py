import utilidades


elementos=5
serie=[]
i=0
suma = 0
promedio = 0

print("Necesito",elementos,"números para hacer magias matemáticas...")

while i<elementos :
    ordinal = str(i+1)
    frase="Dame el "+ ordinal +"º: "
    serie.append( utilidades.pideNumero(frase)) 
    suma=suma+serie[i]
    i=i+1

promedio=suma/5

print("La suma de lo introducido es :",suma)
print("El promedio de lo introducido es :", promedio)

