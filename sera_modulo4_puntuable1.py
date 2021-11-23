import utilidades

def valida_op(num,lista):
    if num <len(lista) and num >-1:
        return True
    return False

def salir():
    global continuar
    print("Aqui ando")
    continuar=False

def conf():
    global catalogo
    producto = input("Introduce el nuevo producto: ")
    precio = utilidades.pideNumero("Introduce su precio: ")
    catalogo.append({producto:precio})
    return True




opciones=[
    {
        "nombre":"SALIR",
        "metodo":salir
    },
    {
        "nombre":"Configuración de productos y precios",
        "metodo":conf
    },

]
menu="Gestor de Fruteria:\n============\n"
menu_frase="¿Opción?: "
aviso_opcion="Tu opción no está disponible. Escoge de nuevo.\n"
continuar=True
catalogo=[{"Pera":1.25},{"Manzana":1.45},{"Melocotón":1.90},{"Naranja":0.60},{"Mandarina":1.65},{"Plátano": 1.25},{"Tomate": 1.15},{"Lechuga": 0.45}]

for i in range(0,len(opciones)):
    menu=menu + str(i) + " - " + opciones[i]["nombre"]+"\n"

while continuar:
    print(menu)
    opcion=int(utilidades.pideNumero(menu_frase))
    if not valida_op(opcion,opciones):
        print(aviso_opcion)
        continue
    opciones[opcion]["metodo"]()
