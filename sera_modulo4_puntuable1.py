#IMPORTAMOS
import utilidades
from fruteria_controller import *
import random

#DEFINICION DE FUNCIONES
def asienta_cambios(cambios):
    global continuar
    continuar=cambios[0]
    global catalogo
    catalogo=cambios[1]
    global num_fac
    num_fac=cambios[2]
    global registro
    registro=cambios[3]

def valida_op(num,lista):
    if num <len(lista) and num >-1:
        return True
    return False

def siembra_tickets():
    global num_fac
    global registro
    for i in range(1,53):
        for j in range(1,8):
            num_fac=num_fac+1
            muestra,coste_m = random.choice(list(catalogo.items()))
            registro.append([num_fac,i,j,coste_m,round(coste_m*1.21,2),[[muestra,1,coste_m,coste_m]]])

def crea_menu(menu):
    for i in range(0,len(opciones)):
        menu=menu + str(i) + " - " + opciones[i]["nombre"]+"\n"

    return menu

continuar=True
menu="Gestor de Fruteria:\n============\n"
menu_frase="¿Opción?: "
aviso_opcion="Tu opción no está disponible. Escoge de nuevo.\n"
catalogo={"Pera":1.25 ,"Manzana":1.45,"Melocotón":1.90,"Naranja":0.60,"Mandarina":1.65,"Plátano": 1.25,"Tomate": 1.15,"Lechuga": 0.45}
num_fac=0
registro=[]
explotacion=[]

# MAIN o PRINCIPAL

# Metemos datos falsos para poder testear
siembra_tickets()

#Montamos el menu
menu=crea_menu(menu)

while continuar:
    print(menu)
    opcion=int(utilidades.pideNumero(menu_frase))
    if not valida_op(opcion,opciones):
        print(aviso_opcion)
        continue
    cambios=opciones[opcion]["metodo"](continuar,catalogo,num_fac,registro)
    asienta_cambios(cambios)
