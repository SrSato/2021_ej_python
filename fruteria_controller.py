"""
    Modulo controlador de la fruteria.
    Pensado para el puntuable 1 del Mod 4.
    Contiene las funciones de control.

    ¡OJO! (Pendiente de refactorizar):
    Actualmente todas las funciones que aparecen en la lista de opciones
    -funciones de interfaz con el usuario- usan como
    argumentos (continuar, catalogo, num_fac, registro)
    y devuelven [continuar, catalogo, num_fac, registro].

    Esto es INDEPENDIENTE  de que necesiten o no todos esos argumentos
    o de que generen o no datos nuevos para el retorno.
"""
import utilidades


def salir(continuar, catalogo, num_fac, registro):
    '''
        return: [continuar, catalogo, num_fac, registro]
        argumentos: (continuar, catalogo, num_fac, registro)

        INTERFAZ: cambia el valor del flag continuar a false para marcar que
        se quiere salir del programa (Modifica continuar)
    '''

    print("Sesión cerrada. ¡Adios!")
    continuar = False
    return [continuar, catalogo, num_fac, registro]


def conf(continuar, catalogo, num_fac, registro):
    '''
        return: [continuar, catalogo, num_fac, registro]
        argumentos: (continuar, catalogo, num_fac, registro)

        INTERFAZ: Permite introducir, modificar o elminar productos y
        precios. (Modifica catalogo)
    '''

    print("Catálogo actual:\n", catalogo)
    producto = input(
        "Introduce el nombre del producto a añadir o modificar ('salir' para volver al menu): ")
    if producto == "salir":
        return [continuar, catalogo, num_fac, registro]
    if producto in catalogo:
        cambiar = input("¿Quieres cambiarle el nombre? (s/n) :")
        if cambiar == "s":
            del catalogo[producto]
            producto = input("Escribe su nuevo nombre: ")
    precio = utilidades.pideNumero("Introduce su nuevo precio: ")
    catalogo[producto] = precio
    print("El catálogo queda asi:", catalogo, "\n")
    input(pausa)
    return [continuar, catalogo, num_fac, registro]


def escoge_semana():
    '''
        return: int entre 1 y 52
        argumentos: ()

        Pide y recoge del usuario el número de semana.
        Asume que las semanas se numeran del 1 al 52
    '''

    semana = 0
    while semana < 1 or semana > 52:
        semana = int(utilidades.pideNumero("Semana de la venta (1-52): "))
    return semana


def escoge_dia():
    '''
        return: int entre 1 y 7
        argumentos: ()

        Pide y recoge del usuario el número de día de la semana.
        Asume que los días se numeran del 1 (Lunes) al 7 (Domingo)
    '''

    dia = 0
    while dia < 1 or dia > 7:
        dia = int(utilidades.pideNumero(
            "Dia de la venta (1=Lunes - 7=Domingo): "))
    return dia


def venta(continuar, catalogo, num_fac, registro):
    '''
        return: [continuar, catalogo, num_fac, registro]
        argumentos: (continuar, catalogo, num_fac, registro)

        INTERFAZ: Permite introducir ventas (tickets).
        Modifica el num_fac y los datos que se guardan en el registro.
    '''
    siguiente = True
    lista = []
    total = 0
    ticket = []

    semana = escoge_semana()
    dia = escoge_dia()
    while siguiente:
        print("Productos disponibles:\n", listar_prod(catalogo))
        producto = input("Introduce el producto vendido: ")
        if producto not in catalogo:
            print(
                    "No se encuentra el producto.",
                    "Por favor revisa el producto introducido",
                    "e intentalo de nuevo.")
            continue
        unidades = int(utilidades.pideNumero(
            "Introduce las unidades vendidas: "))
        precio_linea = round(catalogo[producto]*unidades, 2)
        lista.append(
            [producto, unidades, catalogo[producto], precio_linea])
        if input("¿Fin de la compra? (s/n): ") == "s":
            num_fac = num_fac+1
            print("Num. ticket: ", num_fac, "\n")
            for i in range(0, len(lista)):
                total = total + lista[i][3]
            total_iva = round(total*iva, 2)
            ticket = [num_fac, semana, dia, total, total_iva, lista]
            siguiente = False
    registro.append(ticket)
    input(pausa)
    return [continuar, catalogo, num_fac, registro]


def print_ticket(registro, num):
    '''
        return: bool
            False si no hay tiquet y True si existe.
        argumentos: (registro, num)
            registro es el listado de tiquets
            num es el id del tiquet en el listado

        Imprime un tiquet por pantalla dada una colección de tickets
        y el id del que se quiere imprimir.
    '''
    for i in range(0, len(registro)):
        if registro[i][0] == num:
            print(
                f"\nTicket de Compra num. {registro[i][0]} Fecha: SEMANA {registro[i][1]} DIA {registro[i][2]}")
            print("================================================")
            compra = registro[i][5]
            for linea in compra:
                print(f"{linea[0]} ({linea[2]}) x {linea[1]} : {linea[3]}")
            print("================================================")
            print(
                f"Total: {registro[i][3]}\nTotal con I.V.A: {registro[i][4]}")
            print("\n¡Gracias por su compra!\n")
            return True
    print("El ticket no existe.")
    return False


def muestra_ticket(continuar, catalogo, num_fac, registro):
    '''
        return: [continuar, catalogo, num_fac, registro]
        argumentos: (continuar, catalogo, num_fac, registro)

        INTERFAZ: Pide y recoge el id del ticket que el usuario quiera
        imprimir y se lo pasa a print_ticket para imprimirlo.

        No modifica nada, los mismos datos que entran de argumentos
        salen de retorno.
    '''

    num = int(utilidades.pideNumero("Num. de ticket: "))
    print_ticket(registro, num)
    input(pausa)
    return [continuar, catalogo, num_fac, registro]


def tickets_semana(num, registro):
    '''
        return: retornable
            retornable es la colección de tickets correspondientes a
            esa semana en el registro.
        argumentos: ( num, registro)
            num es el número de la semana (1-52) que evaluamos
            registro es la colección de tickets de la fruteria

        Selecciona todos los tickets de una misma semana. Está pensada
        como una función de apoyo que no modifica los datos maestros.
    '''

    retornable = []
    for ticket in registro:
        if ticket[1] == num:
            retornable.append(ticket)
    return retornable


def stats(continuar, catalogo, num_fac, registro):
    '''
        return: [continuar, catalogo, num_fac, registro]
        argumentos: (continuar, catalogo, num_fac, registro)

        INTERFAZ: Saca por pantalla las estadísticas de venta del año,
        pormenorizadas por semanas y días: Acumulados semanales y diarios

        No modifica los datos maestros. NECESITA REFACTORIZAR.
    '''

    semana = 1
    dia = 1
    tickets_acu = 0
    total_acu = 0
    media_acu = 0

    while semana <= 52:
        total = 0
        total_dia_acu = 0
        media_dia_acu = 0
        tickets_dia_acu = 0
        evaluable = tickets_semana(semana, registro)

        for ticket in evaluable:
            total = total+ticket[3]
        if total != 0:
            media = round(total/len(evaluable), 2)
        else:
            media = 0
        tickets_acu += len(evaluable)
        total_acu += total
        media_acu += media
        total=round(total,2)
        total_acu=round(total_acu,2)
        media_acu=round(media_acu,2)
        print(
            f"Semana {semana}: tickets={len(evaluable)} total= {total} media={media}")
        print(
            f"Acumlado: tickets={tickets_acu} total={total_acu} media={media_acu} ")

        for dia in range(1, 8):
            total_dia = 0
            media_dia = 0
            tickets_dia = 0

            for ticket in evaluable:
                if ticket[2] == dia:
                    total_dia = total_dia+ticket[3]
                    tickets_dia = tickets_dia+1
                    total_dia_acu += total_dia
                    tickets_dia_acu += tickets_dia
            if total_dia != 0:
                media_dia = round((total_dia/tickets_dia), 2)
            else:
                media_dia = 0
            media_dia_acu += media_dia
            media_dia_acu=round(media_dia_acu)
            total_dia_acu=round(total_dia_acu)

            print(
                f"\tDia {dia}: tickets={tickets_dia} total= {total_dia} media={media_dia}")
            print(
                f"\tAcumulado semanal: tickets={tickets_dia_acu} total={total_dia_acu} media={media_dia_acu}")
        print()
        semana = semana+1
    input(pausa)
    return [continuar, catalogo, num_fac, registro]


def mejor_grupo(evaluable):
    '''
        return: bool
            Devuelve True si encuentra un mejor ticket y
            False si no encuentra un mejor ticket.
        argumentos: (evaluable)
            evaluable es una colección de tickets

        Muestra el mejor ticket (mayor total) de la colección a evaluar.
    '''

    mayor = 0
    escogido = 0

    for i in range(0, len(evaluable)):
        if evaluable[i][3] > mayor:
            mayor = evaluable[i][3]
            escogido = evaluable[i][0]
    if mayor != 0:
        print_ticket(evaluable, escogido)
        return True
    else:
        print("No hay tickets de venta.")
        return False


def mejor_semana(continuar, catalogo, num_fac, registro):
    '''
        return: [continuar, catalogo, num_fac, registro]
        argumentos: (continuar, catalogo, num_fac, registro)

        INTERFAZ: Permite al usuario escoger una semana y
        muestra el mejor ticket (mayor total).

        No modifica datos.
    '''

    semana = escoge_semana()
    evaluable = tickets_semana(semana, registro)
    mejor_grupo(evaluable)
    input(pausa)
    return [continuar, catalogo, num_fac, registro]


def mejor_abs(continuar, catalogo, num_fac, registro):
    '''
        return: [continuar, catalogo, num_fac, registro]
        argumentos: (continuar, catalogo, num_fac, registro)

        INTERFAZ: Muestra el mejor ticket (mayor total).

        No modifica datos.
    '''

    mejor_grupo(registro)
    input(pausa)
    return [continuar, catalogo, num_fac, registro]


def listar_prod(catalogo):
    '''
        return: listado
            lista de las keys del catalogo
        argumentos: catalogo
            diccionario de {producto:precio}

        Devuelve una nueva lista con todos los nombres de los productos.
        No modifica datos maestros.
    '''
    listado = list(catalogo.keys())
    return listado


def muestra_prod(continuar, catalogo, num_fac, registro):
    '''
        return: [continuar, catalogo, num_fac, registro]
        argumentos: (continuar, catalogo, num_fac, registro)

        INTERFAZ: Muestra el catálogo de productos.

        No modifica datos.
    '''
    print("Catálogo de productos:\n", catalogo, "\n")
    input(pausa)
    return [continuar, catalogo, num_fac, registro]


def freq_ventas(catalogo, registro):
    '''
        return: freq
            freq es una lista [ventas,producto] para todo el catalogo
        argumentos: (catalogo, registro)
            catalogo es el diccionario con todos los productos y precios
            registro es la coleccion de tickets

        Crea una lista [ventas,producto] ordenada por ventas para
        todo el catalogo.

        No modifica datos maestros.
    '''
    productos = listar_prod(catalogo)
    freq = []

    for producto in productos:
        ventas = 0
        for ticket in registro:
            compra = ticket[5]
            for linea in compra:
                if linea[0] == producto:
                    ventas = ventas+1
        freq.append([ventas, producto])

    freq.sort()
    return freq


def top_ventas(continuar, catalogo, num_fac, registro):
    '''
        return: [continuar, catalogo, num_fac, registro]
        argumentos: (continuar, catalogo, num_fac, registro)

        INTERFAZ: Muestra el producto más vendido de todo el catalogo.

        No modifica datos.
    '''

    total_ventas = 0
    freq = freq_ventas(catalogo, registro)
    for prod in freq:
        total_ventas = total_ventas + prod[0]
    print(
        f"El producto más vendido es {freq[-1][1]} con un total de {freq[-1][0]} ventas sobre {total_ventas}.\n")
    input(pausa)
    return [continuar, catalogo, num_fac, registro]


def chof_ventas(continuar, catalogo, num_fac, registro):
    '''
        return: [continuar, catalogo, num_fac, registro]
        argumentos: (continuar, catalogo, num_fac, registro)

        INTERFAZ: Muestra el producto menos vendido de todo el catalogo.

        No modifica datos.
    '''
    total_ventas = 0
    freq = freq_ventas(catalogo, registro)
    for prod in freq:
        total_ventas = total_ventas + prod[0]
    print(
        f"El producto menos vendido es {freq[0][1]} con un total de {freq[0][0]} ventas sobre {total_ventas} .\n")
    input(pausa)
    return [continuar, catalogo, num_fac, registro]


def print_freq(continuar, catalogo, num_fac, registro):
    '''
        return: [continuar, catalogo, num_fac, registro]
        argumentos: (continuar, catalogo, num_fac, registro)

        INTERFAZ: Muestra la frecuencia de ventas de todo el catalogo.

        No modifica datos.
    '''
    total_ventas = 0
    freq = freq_ventas(catalogo, registro)
    for prod in freq:
        total_ventas = total_ventas + prod[0]
    print(" Total de ventas:", total_ventas, "\n",
          "Frecuencia en formato [ventas,Prod]:\n", freq, "\n")
    input(pausa)
    return [continuar, catalogo, num_fac, registro]


# VARIABLES E INICIALIZACIONES
opciones = [
    {
        "nombre": "SALIR",
        "metodo": salir
    },
    {
        "nombre": "Catálogo de productos",
        "metodo": muestra_prod
    },
    {
        "nombre": "Configuración de productos y precios",
        "metodo": conf
    },
    {
        "nombre": "Registro de venta",
        "metodo": venta
    },
    {
        "nombre": "Imprime ticket",
        "metodo": muestra_ticket
    },
    {
        "nombre": "Estadísticas",
        "metodo": stats
    },
    {
        "nombre": "Mejor de una semana",
        "metodo": mejor_semana
    },
    {
        "nombre": "Mejor anual",
        "metodo": mejor_abs
    },
    {
        "nombre": "Producto más vendido",
        "metodo": top_ventas
    },
    {
        "nombre": "Producto menos vendido",
        "metodo": chof_ventas
    },
    {
        "nombre": "Frecuencia de ventas del catálogo",
        "metodo": print_freq
    }
]

iva = 1.21
pausa = "\tPresiona ENTER para continuar ... \n"


# Documentación (EN PROCESO!!!!!)

def readme():
    ''' doc del modulo '''
    info = """
            Modulo controlador de la fruteria.
            Pensado para el puntuable 1 del Mod 4.
            Contiene las funciones de control.

            ¡OJO! (Pendiente de refactorizar):
            Actualmente todas las funciones que aparecen en la lista de opciones
            -funciones de interfaz con el usuario- usan como
            argumentos (continuar, catalogo, num_fac, registro)
            y devuelven [continuar, catalogo, num_fac, registro].

            Esto es INDEPENDIENTE  de que necesiten o no todos esos argumentos
            o de que generen o no datos nuevos para el retorno.
            """
    print(info)


if __name__ == "__main__":
    readme()
