#Randomizamos un texto.

import random

def quitaCosos(lista,texto):
    for i in range(0,len(lista)):
        texto=texto.split(lista[i])
        texto="".join(texto)
    return texto

def ponComas(textoEnLista,num):
    puestas=0
    while puestas < num:
        indice=random.randint(0,len(textoEnLista)-1)
        palabro=list(textoEnLista[indice])
        if palabro[-1] not in sobran:
            palabro.append(",")
            palabro="".join(palabro)
            textoEnLista[indice]=palabro
            puestas=puestas+1
    return textoEnLista

def ponPuntos(textoEnLista,num):

    palabro=list(textoEnLista[-1])
    palabro.append(".")
    palabro="".join(palabro)
    textoEnLista[-1]=palabro
    puestas=0

    while puestas < num:
        indice=random.randint(0,len(textoEnLista)-1)
        palabro=list(textoEnLista[indice])
        quieroEspacio=False
        if palabro[-1] not in sobran:
            palabro.append(".")
            palabro="".join(palabro)
            textoEnLista[indice]=palabro
            puestas=puestas+1
            quieroEspacio=True
        if indice < len(textoEnLista)-1 and quieroEspacio==True:
            textoEnLista[indice+1]=textoEnLista[indice+1].capitalize()

    return textoEnLista
    

muestra="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget porta ipsum, id iaculis enim. Maecenas posuere felis nunc, nec convallis purus varius in. Vivamus sodales odio nibh, non viverra urna iaculis vel. Sed vitae sem vitae diam mollis interdum. Suspendisse vel pharetra velit. Curabitur aliquet vestibulum sem tincidunt pharetra. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vestibulum et mauris non tellus semper cursus sed et neque. Nullam blandit eleifend justo. Nullam quis augue neque. Suspendisse consequat, justo vitae luctus pulvinar, nisi sem euismod erat, et ultricies nunc nisi vitae elit. Cras turpis massa, consequat vitae scelerisque ac, venenatis non nibh. Etiam id hendrerit leo, vel euismod erat. Suspendisse eget nisl vestibulum, tempor libero vehicula, interdum arcu."

sobran=[",","."]

texto=quitaCosos(sobran,muestra)
texto=texto.lower()
listaTexto=texto.split(" ")

random.shuffle(listaTexto)

comas=muestra.count(",")
puntos= muestra.count(".")

listaTexto[0]=listaTexto[0].capitalize()
listaTexto=ponComas(listaTexto,comas)
listaTexto=ponPuntos(listaTexto,puntos)

listaTexto=" ".join(listaTexto)

print(f'De aqui:\n\"{muestra}\"')
print(f'Llegamos a aqui:\n\"{listaTexto}\"')
