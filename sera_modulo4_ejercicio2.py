import utilidades

def raizDigital(num):
    while num>9:
        lista=[]
        cadena=str(num)
        for i in range(len(cadena)):
            lista.append(int(cadena[i]))
        num=sum(lista)
    return num


num=int(utilidades.pideNumero("Hacer raiz digital de: "))
rd=raizDigital(num)

print(rd)
