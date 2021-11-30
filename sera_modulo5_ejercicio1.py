import utilidades
from agenda import Agenda


def crea_menu(menu):
    ''' Monta el menu que enseñamos al usuario. '''
    for i in range(0, len(opciones)):
        menu = menu + str(i) + " - " + opciones[i]["nombre"] + "\n"
    return menu


def valida_op(num, lista):
    ''' Se encarga de validar que la opción seleccionada esté en el menu. '''

    if num < len(lista) and num > -1:
        return True
    return False


def salir():
    global continuar
    continuar = False
    agenda.guarda_fichero()


continuar = True
menu = "\nE-Agenda:\n"
agenda = Agenda()
agenda.lee_fichero()

opciones = [
    {
        "nombre": "SALIR",
        "metodo": salir
    },
    {
        "nombre": "Añadir contacto",
        "metodo": agenda.pide_nuevo
    },
    {
        "nombre": "Ver agenda",
        "metodo": agenda.leer_agenda
    },
    {
        "nombre": "Buscar por nombre",
        "metodo": agenda.buscar_nombre
    }
]


menu = crea_menu(menu)
while continuar:
    print(menu)
    opcion = int(utilidades.pideNumero("Escoge operación: "))
    if not valida_op(opcion, opciones):
        print("Opción NO valida")
        continue
    opciones[opcion]["metodo"]()
