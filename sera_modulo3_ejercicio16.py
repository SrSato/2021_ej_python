import random
import utilidades

bd={"admin":"1234","sera":"password"}

while True:
    print("Sistema de Login.")
    salir=input("¿SALIR?(s): ")
    if salir=="s":
        break
    usuario=input("Usuario: ")
    if usuario in bd:
        pwd=input("Contraseña:")
        if pwd == bd[usuario]:
            print("Bienvenido\n")
            continue
    print("Usuario o contraseña no reconocido.\n")
