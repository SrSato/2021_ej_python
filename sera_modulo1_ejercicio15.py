import utilidades
salir="salir"
nombre=False
seleccion=999
instalaciones=[{"nombre":"Sofá","estado":"Disponible"},{"nombre":"Siestódromo","estado":"Disponible"} ,{"nombre": "Sauna del tiempo","estado":"Disponible"}, {"nombre": "Barra fija de bar","estado":"Disponible"}]

while nombre!= salir:
    print("Bienvenido a la reserva de espacios deportivos. Teclea \'",salir,"\'como nombre para terminar.")
    nombre=input("Dime tu nombre: ")
    if nombre==salir:
        break
    edad = int(utilidades.pideNumero("Dime tu edad: "))
    if edad < 18 :
        print("Necesitas que un adulto reserve por tí.")
        break    
    while seleccion!=0:
        print("Nuestras instalaciones: ")
        for instalacion in instalaciones :
            print(int(instalaciones.index(instalacion)+1),"-",instalacion["nombre"],":",instalacion["estado"])
        print("¿Quieres reservar alguna instalación? (escoge 0 si prefieres no reservar)")
        seleccion=utilidades.pideNumero("Número de la instalación: ")
        if seleccion==0 :
            seleccion=999
            break
        if seleccion<0 or seleccion>len(instalaciones):
            continue    
        if instalaciones[int(seleccion)-1]["estado"] == "Disponible":   
            instalaciones[int(seleccion)-1]["estado"]="Reservado por "+nombre
        else:
            print("OJO: Esa instalación ya está reservada.")
print("Adios!")
    
    
