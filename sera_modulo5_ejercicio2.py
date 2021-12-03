import utilidades
from directorio import Directorio


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
    directorio.guardar()


def mambo():
    empleado = directorio.buscar_id(2)
    semana, servicios = empleado.servicios_mes_semanas(2021, 1)
    print(semana)
    print(servicios)


continuar = True
menu = "\nDirectorio Activo de Trukutú Biolabs:\n"
directorio = Directorio()
directorio.cargar()

opciones = [
    {
        "nombre": "SALIR",
        "metodo": salir
    },
    {
        "nombre": "Añadir trabajador",
        "metodo": directorio.pide_nuevo
    },
    {
        "nombre": "Ver directorio",
        "metodo": directorio.leer_directorio
    },
    {
        "nombre": "Buscar por nombre",
        "metodo": directorio.buscar_nombre
    },
    {
        "nombre": "Fichar entrada [ADMIN]",
        "metodo": directorio.fichar_entrada
    },
    {
        "nombre": "Fichar salida [ADMIN]",
        "metodo": directorio.fichar_salida
    },
    {
        "nombre": "Horas mensuales",
        "metodo": directorio.horas_mes
    },
    {
        "nombre": "Dale mambo",
        "metodo": mambo
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
