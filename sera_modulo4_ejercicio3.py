def primera_diferencia(str1,str2):
    iguales=True
    indice=0
    larga=False

    if len(str1)>len(str2):
        lim=len(str2)
        larga=str1
    if len(str1)==len(str2):
        lim=len(str1)
    if len(str1)<len(str2):
        lim=len(str1)
        larga=str2

    while iguales and indice<lim:
        if str1[indice]!=str2[indice]:
            iguales=False
            return indice
        else:
            indice=indice+1

    if indice==lim and larga:
        return indice
    else:
        return -1



texto1=input("Dame una cadena de texto: ")
texto2=input("Dame otra cadena de texto: ")

print(primera_diferencia(texto1,texto2))
