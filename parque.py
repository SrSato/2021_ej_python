#parque atracciones
#imports
import time
import utilidades

#Funciones
def tienesEdad(Atraccion, edad):
    if edad < Atraccion.edad_min or edad > Atraccion.edad_max:
        return False
    return True

def muestraAtracciones(listado):
    i=0
    texto=""
    for atraccion in listado :
        texto=texto + str(listado.index(atraccion)+1) +"- " + atraccion.nombre +"\n"
    return texto

#Clases
class Atraccion:
    def __init__(self, nombre, edad_min, edad_max,apto,no_apto):
        self.nombre = nombre
        self.edad_min = edad_min
        self.edad_max = edad_max
        self.apto = apto
        self.no_apto = no_apto

#Variables
a1=Atraccion("Paseo por el rio",0,100,"¡Disfruta del rio!","Demasiada agua para tí, no cumples los requisitos de edad")
a2=Atraccion("Carrusel de carnaval",5,100,"¡Subete al carrusel!","Es fácil perderse en este carnaval y tu no tienes la edad apropiada")
a3=Atraccion("Aventura en la jungla de agua",8,100,"¡Monos de agua!!!Lo más!!!","Esta atracción es movidita para alguien de tu edad. Mejor no arriesgarse.")
a4=Atraccion("Rápidos en las Montañas Rocosas",12,100,"Ojo con las salpicadas!!!", "Si no tienes entre 12 y 100 años mejor no subas. ")
a5=Atraccion("El Velocirraptor",12,70, "Nada como unas carreritas por la jaula", "A estos bichos les encantan los niños y los yayos. NO es para tí")
a6=Atraccion("Irme a casa",0,100, "Ha sido un placer tenerte aquí, ¡¡¡Hasta la próxima!!!", "Con esa edad no te vas solo")
atracciones=[a1,a2,a3,a4,a5,a6]

edad=False
atra_seleccion=False
apto="Puedes disfrutar de la aventura!"
no_apto="Lo siento, no cumples los requisitos para disfrutar de esta atracción"
pregunta_edad="¿Cuántos años tienes?: "
pregunta_atra="¡Escoge tu aventura!: "
escogido="Has escogido"

salir=len(atracciones)-1
menu_app='''\nBienvenido a nuestro Parque

Estas son las atracciones disponibles:

''' + muestraAtracciones(atracciones)

#Main
while atra_seleccion!=salir :
    
    print(menu_app)
    if edad==False:
        edad=utilidades.pideNumero(pregunta_edad)
    atra_seleccion=int(utilidades.pideNumero(pregunta_atra) - 1)
    if atra_seleccion < 0 or atra_seleccion>len(atracciones):
        continue
    print(escogido, atracciones[atra_seleccion].nombre)
    if tienesEdad(atracciones[atra_seleccion], edad) :
        print(atracciones[atra_seleccion].apto)
    else :
        print(atracciones[atra_seleccion].no_apto)
    time.sleep(1)


