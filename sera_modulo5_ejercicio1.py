import utilidades
from agenda import Agenda


def crea_menu(menu):
    '''
        return: str
            cadena con el menu montado.
        argumentos: str
            cadena de base (nombre de la app, versión, etc...) sobre
            la que añadir las opciones de menu para el usuario.

        Monta el menu que enseñamos al usuario
    '''
    for i in range(0, len(opciones)):
        menu = menu + str(i) + " - " + opciones[i]["nombre"] + "\n"
    return menu


def valida_op(num, lista):
    '''
        return: bool
            True si el valor es bueno (De 0 hasta la última opción).
            False si no esta en el rango.
        arg: int, []
            num es el int que ha seleccionado nuestro usuario.
            lista es la lista de opciones de nuestro menú.

        Se encarga de validar que la opción seleccionada esté en el menu
    '''

    if num < len(lista) and num > -1:
        return True
    return False


def salir():
    global continuar
    continuar = False


continuar = True
menu = "\nE-Agenda:\n"
agenda = Agenda()
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
