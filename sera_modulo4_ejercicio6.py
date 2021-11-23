def cambia_mayusculas(texto):
    texto_may=texto.upper()
    texto_min=texto.lower()

    if texto==texto_may:
        return texto_min
    if texto==texto_min:
        return texto_may

    return texto


texto=input("introduce el texto a cambiar: ")

print(cambia_mayusculas(texto))
