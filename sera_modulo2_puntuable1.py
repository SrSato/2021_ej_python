import utilidades
import datetime
import random

fecha=datetime.datetime.now()
nombre_cliente=""
nombre="Anon"
apellido="Anon"
numero_pedido="????????"
total_importe=0
importe_iva=0
iva=0.21
opcion=0
unidades=0
precio=0
total_sin_iva=0
opciones=[1,2,3,4]


menu=f'''Generador de Cartas de Pedidos

OPCIONES:
=========
1. Introducir nombre de cliente.
2. Añadir línea de producto (unidades y precio).
3. Generar carta.
4. SALIR
'''

carta=f'''Hola {nombre_cliente},
Tu pedido {numero_pedido} se ha realizado con éxito. El importe total es de {total_importe}€ con {importe_iva}€ de IVA incluido.
Esperamos que disfrutes de tu compra {nombre_cliente}.'''


while opcion != len(opciones):
    print(menu)
    opcion=int(utilidades.pideNumero("Escoge una opción: "))
    print("\n")
    if opcion<1 or opcion > len(opciones):
        continue
    if opcion == 1:
        nombre=utilidades.pideFrase("Introduce el nombre del cliente: ")
        nombre=nombre.lower().capitalize()
        apellido=utilidades.pideFrase("Introduce el apellido del cliente: ")
        apellido=apellido.lower().capitalize()
        nombre_cliente=nombre+" "+apellido
    if opcion == 2:
        confirmar="x"
        while confirmar!="s" and confirmar != "n":
            confirmar=utilidades.pideFrase("¿Añadir línea producto?(s/n): ")
        if confirmar == "s":
            unidades=utilidades.pideNumero("Marca el número de unidades del pedido: ")
            precio=utilidades.pideNumero("Marca el precio por unidad para este pedido: ")

            parcial_sin_iva=unidades*precio
            parcial_iva=parcial_sin_iva*iva
            parcial_importe=parcial_sin_iva + parcial_iva

            total_sin_iva=total_sin_iva+parcial_sin_iva
            importe_iva=importe_iva+parcial_iva
            total_importe=total_importe+parcial_importe
            
            if numero_pedido=="????????":
                numero_pedido=f'{fecha.year}{fecha.month}{fecha.day}{nombre[0]}{apellido[0]}-{random.randint(1000,10000)}'
    if opcion == 3:
        carta=f'''Hola {nombre_cliente},\nTu pedido {numero_pedido} se ha realizado con éxito. El importe total es de {total_importe}€ con {importe_iva}€ de IVA incluido.\nEsperamos que disfrutes de tu compra {nombre_cliente}.'''
        print(carta+"\n")
    if opcion == 4:
        print("Cerrando sesión...\n¡Adios!")
