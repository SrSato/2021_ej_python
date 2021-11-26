import utilidades

def salir(continuar,catalogo,num_fac,registro):
    print("Sesión cerrada. ¡Adios!")
    continuar=False
    catalogo
    return [continuar,catalogo,num_fac,registro]

def conf(continuar,catalogo,num_fac,registro):
    print("Catálogo actual:\n",catalogo)
    producto = input("Introduce el nombre del producto a añadir o modificar ('salir' para volver al menu): ")
    if producto=="salir":
        return [continuar,catalogo,num_fac,registro]
    if producto in catalogo:
        cambiar=input("¿Quieres cambiarle el nombre? (s/n) :")
        if cambiar=="s":
            del catalogo[producto]
            producto= input("Escribe su nuevo nombre: ")
    precio = utilidades.pideNumero("Introduce su nuevo precio: ")
    catalogo[producto]=precio
    print("El catálogo queda asi:",catalogo,"\n")
    return [continuar,catalogo,num_fac,registro]

def escoge_semana():
    #entendemos que hay 52 semanas por año
    semana=0
    while semana<1 or semana>52:
        semana=int(utilidades.pideNumero("Semana de la venta (1-52): "))
    return semana

def escoge_dia():
    #entendemos que hay 52 semanas por año
    dia=0
    while dia<1 or dia>7:
        dia=int(utilidades.pideNumero("Dia de la venta (1=Lunes - 7=Domingo): "))
    return dia

def venta(continuar,catalogo,num_fac,registro):
    siguiente = True
    lista=[]
    total=0
    ticket=[]


    semana=escoge_semana()
    dia=escoge_dia()
    while siguiente:
        print("Productos disponibles:\n",listar_prod(catalogo))
        producto=input("Introduce el producto vendido: ")
        if producto not in catalogo:
            print("No se encuentra el producto. Por favor revisa el producto introducido e intentalo de nuevo.")
            continue
        else:
            unidades=int(utilidades.pideNumero("Introduce las unidades vendidas: "))
            precio_linea=round(catalogo[producto]*unidades,2)
            lista.append([producto,unidades,catalogo[producto],precio_linea])
            if input("¿Fin de la compra? (s/n): ")=="s":
                num_fac=num_fac+1
                print("Num. ticket: ",num_fac,"\n")
                for i in range(0,len(lista)):
                    total=total + lista[i][3]
                total_iva=round(total*iva,2)
                ticket=[num_fac, semana, dia, total,total_iva,lista]
                siguiente=False
    registro.append(ticket)
    return [continuar,catalogo,num_fac,registro]

def print_ticket(registro,num):
    for i in range(0,len(registro)):
        if registro[i][0]==num:
            print(f"\nTicket de Compra num. {registro[i][0]} Fecha: SEMANA {registro[i][1]} DIA {registro[i][2]}")
            print("==============================================")
            compra=registro[i][5]
            for linea in compra:
                print(f"{linea[0]} ({linea[2]}) x {linea[1]} : {linea[3]}")
            print("==============================================")
            print(f"Total: {registro[i][3]}\nTotal con I.V.A: {registro[i][4]}")
            print("\n¡Gracias por su compra!\n")
            return True
    print("El ticket no existe.")
    return False

def muestra_ticket(continuar,catalogo,num_fac,registro):
    num=int(utilidades.pideNumero("Num. de ticket: "))
    print_ticket(registro,num)
    return [continuar,catalogo,num_fac,registro]


def tickets_semana(num,registro):
    retornable=[]
    for ticket in registro:
        if ticket[1]==num:
            retornable.append(ticket)
    return retornable

def stats(continuar,catalogo,num_fac,registro):
    semana=1
    dia=1
    tickets_acu=0
    total_acu=0
    media_acu=0

    while semana<=52:
        total=0
        total_dia_acu=0
        media_dia_acu=0
        tickets_dia_acu=0
        evaluable=tickets_semana(semana,registro)

        for ticket in evaluable:
            total=total+ticket[3]
        if total!=0:
            media = round(total/len(evaluable),2)
        else:
            media=0
        tickets_acu+=len(evaluable)
        total_acu+=total
        media_acu+=media
        print(f"Semana {semana}: tickets={len(evaluable)} total= {total} media={media}")
        print(f"Acumlado: tickets={tickets_acu} total={total_acu} media={media_acu} ")

        for dia in range(1,8):
            total_dia=0
            media_dia=0
            tickets_dia=0

            for ticket in evaluable:
                if ticket[2]==dia:
                    total_dia=total_dia+ticket[3]
                    tickets_dia=tickets_dia+1
                    total_dia_acu+=total_dia
                    tickets_dia_acu+=tickets_dia
            if total_dia != 0:
                media_dia=round((total_dia/tickets_dia),2)
            else:
                media_dia=0
            media_dia_acu+=media_dia
            print(f"\tDia {dia}: tickets={tickets_dia} total= {total_dia} media={media_dia}")
            print(f"\tAcumulado semanal: tickets={tickets_dia_acu} total={total_dia_acu} media={media_dia_acu}")
        print()
        semana=semana+1
    return [continuar,catalogo,num_fac,registro]

def mejor_grupo(evaluable):
    mayor=0
    escogido=0

    for i in range(0, len(evaluable)):
        if evaluable[i][3] > mayor:
            mayor=evaluable[i][3]
            escogido=evaluable[i][0]
    if mayor!=0:
        print_ticket(evaluable,escogido)
    else:
        print("No hay tickets de venta.")

def mejor_semana(continuar,catalogo,num_fac,registro):
    semana=escoge_semana()
    evaluable=tickets_semana(semana,registro)
    mejor_grupo(evaluable)
    return [continuar,catalogo,num_fac,registro]

def mejor_abs(continuar,catalogo,num_fac,registro):
    mejor_grupo(registro)
    return [continuar,catalogo,num_fac,registro]

def listar_prod(catalogo):
    listado=list(catalogo.keys())
    return listado

def muestra_prod(continuar,catalogo,num_fac,registro):
    print("Catálogo de productos:\n",catalogo,"\n")
    return [continuar,catalogo,num_fac,registro]

def freq_ventas(catalogo,registro):
    productos=listar_prod(catalogo)
    freq=[]

    for producto in productos:
        ventas=0
        for ticket in registro:
            compra=ticket[5]
            for linea in compra:
                if linea[0]==producto:
                    ventas=ventas+1
        freq.append([ventas,producto])

    freq.sort()
    return freq

def top_ventas(continuar,catalogo,num_fac,registro):
    freq=freq_ventas(catalogo,registro)
    print(f"El producto más vendido es {freq[-1][1]} con un total de {freq[-1][0]} impactos.\n")
    return [continuar,catalogo,num_fac,registro]

def chof_ventas(continuar,catalogo,num_fac,registro):
    freq=freq_ventas(catalogo,registro)
    print(f"El producto menos vendido es {freq[0][1]} con un total de {freq[0][0]} impactos.\n")
    return [continuar,catalogo,num_fac,registro]

def print_freq(continuar,catalogo,num_fac,registro):
    freq=freq_ventas(catalogo,registro)
    print("Frecuencia de ventas en formato [ventas,Prod]:\n",freq,"\n")
    return [continuar,catalogo,num_fac,registro]



#VARIABLES E INICIALIZACIONES
opciones=[
    {
        "nombre":"SALIR",
        "metodo":salir
    },
    {
        "nombre":"Catálogo de productos",
        "metodo": muestra_prod
    },
    {
        "nombre":"Configuración de productos y precios",
        "metodo":conf
    },
    {
        "nombre":"Registro de venta",
        "metodo":venta
    },
    {
        "nombre":"Imprime ticket",
        "metodo":muestra_ticket
    },
    {
        "nombre":"Estadísticas",
        "metodo":stats
    },
    {
        "nombre":"Mejor de una semana",
        "metodo":mejor_semana
    },
    {
        "nombre":"Mejor anual",
        "metodo":mejor_abs
    },
    {
        "nombre":"Producto más vendido",
        "metodo":top_ventas
    },
    {
        "nombre":"Producto menos vendido",
        "metodo":chof_ventas
    },
    {
        "nombre":"Frecuencia de ventas del catálogo",
        "metodo":print_freq
    }
]

iva=1.21

# Documentación (EN PROCESO!!!!!)
def readme():
    info='''
            utilidades es un módulo pensado para comprobar las entradas del usuario en nuestros programas.

            Dependencias: No tiene.

            Funciones:
                        pideNumero(peticion)
                            Muestra una cadena por consola (peticion) para pedir al usuario que nos de input.
                            Comprueba que ese input es asimilable a un NÚMERO y nos devuelve el FLOAT de ese input.
                            Si no es asimilable avisa de que buscamos un NÚMERO y vuelve a pedir input hasta que sea asimilable.

                            return float

                            Dependencias: es_numero(cosa) de este mismo módulo

                        pideFrase(peticion)
                            Muestra una cadena por consola (peticion) para pedir al usuario que nos de input.
                            Comprueba que ese input es asimilable a una PALABRA (sin espacios o caracteres especiales)
                            y nos devuelve el STR de ese input.
                            Si no es asimilable avisa de que buscamos una PALABRA y vuelve a pedir input hasta que sea asimilable.

                            return str

                            Dependencias: es_letra(cosa) de este mismo módulo

                        es_numero(cosa)
                            Dado un valor cosa evalua si se podría parsear como FLOAT.
                            Devulete True si es posible el parseo o False si no es posible.

                            return bool

                            Dependencias: No tiene.

                        es_letra(cosa)
                            Dado una cadena cosa evalua si está compuesta de caracteres alfabéticos.
                            Devulete True si sólo hay letras o False si tenemos algún caracter especial.

                            return bool
                '''
    print(info)

if __name__=="__main__":
    readme()
