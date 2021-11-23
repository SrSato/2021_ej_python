def quitaCosos(lista,texto):
    for i in range(0,len(lista)):
        texto=texto.split(lista[i])
        texto="".join(texto)
    return texto

muestra="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget porta ipsum, id iaculis enim. Maecenas posuere felis nunc, nec convallis purus varius in. Vivamus sodales odio nibh, non viverra urna iaculis vel. Sed vitae sem vitae diam mollis interdum. Suspendisse vel pharetra velit. Curabitur aliquet vestibulum sem tincidunt pharetra. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vestibulum et mauris non tellus semper cursus sed et neque. Nullam blandit eleifend justo. Nullam quis augue neque. Suspendisse consequat, justo vitae luctus pulvinar, nisi sem euismod erat, et ultricies nunc nisi vitae elit. Cras turpis massa, consequat vitae scelerisque ac, venenatis non nibh. Etiam id hendrerit leo, vel euismod erat. Suspendisse eget nisl vestibulum, tempor libero vehicula, interdum arcu."

sobran=[",","."]

texto=quitaCosos(sobran,muestra)
listaTexto=texto.split(" ")

res=[palabra for palabra in listaTexto if len(palabra)<=2]

print(f"En el texto:\n\"{muestra}\"")
print(f"Hay {len(res)} palabras de 2 o menos letras.")
print(f"Son: {res}.")
