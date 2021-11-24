#IMPORTAMOS (algunos más que otros)
import utilidades

#DEFINICION DE FUNCIONES
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
    print("Catálogo actual:",catalogo)
    producto = input("Introduce el nombre del producto a añadir o modificar: ('salir' para volver al menu) ")
    if producto=="salir":
        return True
    precio = utilidades.pideNumero("Introduce su precio: ")
    catalogo[producto]=precio
    print("El catálogo queda asi:",catalogo,"\n")
    return True

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

def venta():
    continuar = True
    lista=[]
    total=0
    ticket=[]
    global registro
    global num_fac

    semana=escoge_semana()
    dia=escoge_dia()
    while continuar:
        print("Productos disponibles:\n",listar_prod())
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
                continuar=False
    registro.append(ticket)
    return True

def print_ticket(num):
    for i in range(0,len(registro)):
        if registro[i][0]==num:
            print(f"\nTicket de Compra num. {registro[i][0]} Fecha: SEMANA {registro[i][1]} DIA {registro[i][2]}")
            print("==============================================")
            compra=registro[i][5]
            for linea in compra:
                print(f"{linea[0]} ({linea[2]}) x {linea[1]} : {linea[3]}")
            print("==============================================")
            print(f"Total: {registro[i][3]} Total con I.V.A: {registro[i][4]}")
            print("\n¡Gracias por su compra!\n")
            return True
    print("El ticket no existe.")
    return False

def muestra_ticket():
    num=int(utilidades.pideNumero("Num. de ticket: "))
    print_ticket(num)


def tickets_semana(num):
    retornable=[]
    for ticket in registro:
        if ticket[1]==num:
            retornable.append(ticket)
    return retornable

def stats():
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
        evaluable=tickets_semana(semana)

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
                media_dia=round(total_dia/tickets_dia,2)
            else:
                media_dia=0
            media_dia_acu+=media_dia
            print(f"\tDia {dia}: tickets={tickets_dia} total= {total_dia} media={media_dia}")
            print(f"\tAcumulado semanal: tickets={tickets_dia_acu} total={total_dia_acu} media={media_dia_acu}")
        print()
        semana=semana+1

def mejor_grupo(evaluable):
    mayor=0
    escogido=0

    for i in range(0, len(evaluable)):
        if evaluable[i][3] > mayor:
            mayor=evaluable[i][3]
            escogido=evaluable[i][0]
    if mayor!=0:
        print_ticket(escogido)
    else:
        print("No hay tickets de venta.")

def mejor_semana():
    semana=escoge_semana()
    evaluable=tickets_semana(semana)
    mejor_grupo(evaluable)
    return True

def mejor_abs():
    mejor_grupo(registro)
    return True

def listar_prod():
    listado=list(catalogo.keys())
    return listado

def freq_ventas():
    productos=listar_prod()
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


def top_ventas():
    freq=freq_ventas()
    print(freq[-1])







#VARIABLES E INICIALIZACIONES
opciones=[
    {
        "nombre":"SALIR",
        "metodo":salir
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
        "nombre":"Catálogo de productos",
        "metodo": listar_prod
    },
    {
        "nombre":"Producto más vendido",
        "metodo":top_ventas
    },
    {
        "nombre":"Frecuencia de ventas del catálogo",
        "metodo":freq_ventas
    }

]

menu="Gestor de Fruteria:\n============\n"
menu_frase="¿Opción?: "
aviso_opcion="Tu opción no está disponible. Escoge de nuevo.\n"
continuar=True
catalogo={"Pera":1.25 ,"Manzana":1.45,"Melocotón":1.90,"Naranja":0.60,"Mandarina":1.65,"Plátano": 1.25,"Tomate": 1.15,"Lechuga": 0.45}
iva=1.21
num_fac=0
registro=[]
explotacion=[]

# MAIN o PRINCIPAL
for i in range(0,len(opciones)):
    menu=menu + str(i) + " - " + opciones[i]["nombre"]+"\n"

while continuar:
    print(menu)
    opcion=int(utilidades.pideNumero(menu_frase))
    if not valida_op(opcion,opciones):
        print(aviso_opcion)
        continue
    opciones[opcion]["metodo"]()
