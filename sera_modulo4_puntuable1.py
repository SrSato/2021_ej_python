'''
    Archivo principal del puntuable1 del modulo 4:
    Main de la Fruteria
'''
# IMPORTAMOS
import random
import utilidades
from fruteria_controller import *


# DEFINICION DE FUNCIONES
# Aqui dejo las funciones que directamente tocan el menu, fijan el valor de
# nuestros datos maestros o que son de apoyo al testeo.
# Las de control de la fruteria estan en fruteria_controller


def asienta_cambios(cambios):
    '''
        Return: none
        argumentos: cambios
            cambios es una lista de valores devuelta por
            las funciones de fruteria_controller

        Recoge los datos generados por fruteria_controller y los asienta en el
        las variables del archivo principal (este archivo ;) )
    '''
    global continuar
    continuar = cambios[0]
    global catalogo
    catalogo = cambios[1]
    global num_fac
    num_fac = cambios[2]
    global registro
    registro = cambios[3]


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


def siembra_tickets():
    '''
        Inventa unos cuantos tickets para testear sin tener que meter datos
        a mano
        ¡¡¡Eliminar antes de subir a producción!!!
    '''
    global num_fac
    global registro
    for i in range(1, 53):
        for j in range(1, 8):
            num_fac = num_fac+1
            muestra, coste_m = random.choice(list(catalogo.items()))
            registro.append([num_fac, i, j, coste_m, round(coste_m*1.21, 2),
                            [[muestra, 1, coste_m, coste_m]]])


# DEFINICION DE VARIABLES
continuar = True
menu = "Gestor de Fruteria:\n=======================\n"
menu_frase = "¿Opción?: "
aviso_opcion = "Tu opción no está disponible. Escoge de nuevo.\n"
catalogo = {
                "Pera": 1.25, "Manzana": 1.45, "Melocotón": 1.90,
                "Naranja": 0.60, "Mandarina": 1.65, "Plátano": 1.25,
                "Tomate": 1.15, "Lechuga": 0.45
            }
num_fac = 0
registro = []

# MAIN o PRINCIPAL

# Metemos datos falsos para poder testear
siembra_tickets()

# Montamos el menu
menu = crea_menu(menu)

# flujo principal: mientras queramos continuar, ejecutará una opción del programa
# y asentará los cambios en los datos que produzca esa opcion
while continuar:
    print(menu)
    opcion = int(utilidades.pideNumero(menu_frase))
    if not valida_op(opcion, opciones):
        print(aviso_opcion)
        continue
    cambios = opciones[opcion]["metodo"](
                continuar, catalogo, num_fac, registro
                )
    asienta_cambios(cambios)
