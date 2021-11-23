#Roshambo!!! (Piedra - Papel - Tijera)
# Piedra gana a Paepel que gana a Tijera que gana a papel
# 1 w 2 w 3 w 1

#import
import utilidades
import random

#funciones
def montarMenu(base,lista):
    for opcion in lista:
        base=base+ "\n       " +str(lista.index(opcion)+1)+"-" + opcion +"\n"  
    return base    

def recogeP1():
    p1=""
    while p1 == "":
        p1=input(pidePlayer)
    return p1

def recogeJugada(lista):
    jugadaP1=999999
    while jugadaP1<0 or jugadaP1>len(lista):
        print(menu)
        jugadaP1=int(utilidades.pideNumero(pideJugada)-1)
    return jugadaP1

def quienGana(jugada1,jugada2):
    ganadora="empate"
    if jugada1 == 0 and jugada2 == 1 :       
        ganadora = jugada2
    if jugada1 == 0 and jugada2 == 2 :
        ganadora = jugada1
    if jugada1 == 1 and jugada2 == 0 :
        ganadora = jugada1
    if jugada1 == 1 and jugada2 == 2 :
        ganadora = jugada2
    if jugada1==2 and jugada2 == 1 :
        ganadora = jugada1
    if jugada1==2 and jugada2 == 0 :
        ganadora = jugada2
    return ganadora


#variables
p1=""
cpu="Skynet v0.1"
jugadaP1=999
jugadaCPU=""
p1Wins=0
cpuWins=0
over=5
opciones=("piedra","papel","tijera") #Puedes cambiar los nombres, pero ojo con las posiciones: 1 w 2 w 3 w1 ;)
presentacion='''\nROSHAMBO!!! \n\nJuegas al mejor de '''+str(over)+ ''' contra ''' +str(cpu)
pidePlayer="P1 dime tu nombre: "
menu="\nPosibles jugadas:\n"
pideJugada="Escoge la jugada: "
comentaP1="Tú has escogido "
comentaCPU="Yo he escogido "
comentaGanar=" gana a "
comentaEmpatar="Ni pa ti ni pa mi... Empate"
comentaRondaCPU= "Jugamos al mejor de "+str(over)+"\nYo llevo ganadas " 
comentaRondaP1= " y tú llevas ganadas "
comentaFinal= "Se acabó. Gracias por jugar!!!"
comentaCampeon= "El campeón de la ronda es... "

# main
menu=montarMenu(menu,opciones)

print(presentacion)
p1 = recogeP1()

while (p1Wins + cpuWins) < over :    

    jugadaCPU=random.randint(0,2)
    jugadaP1 = recogeJugada(opciones)    

    print("\n\t\t"+comentaCPU+opciones[jugadaCPU])
    print("\t\t"+comentaP1+opciones[jugadaP1])
    print("==================================================================")

    ganadora=quienGana(jugadaP1,jugadaCPU)
    
    if ganadora == jugadaP1 :
        p1Wins=p1Wins + 1
        print("\t\t"+opciones[jugadaP1] + comentaGanar + opciones[jugadaCPU])
    if ganadora == jugadaCPU :
        cpuWins=cpuWins + 1
        print("\t\t"+opciones[jugadaCPU] + comentaGanar + opciones[jugadaP1])
    if ganadora == "empate" :
        print("\t\t"+comentaEmpatar)
    print("==================================================================")    
    
    print(comentaRondaCPU+str(cpuWins)+comentaRondaP1+str(p1Wins))
    jugadaP1=999

if cpuWins > p1Wins:
    campeon=cpu
else:
    campeon=p1 
print(comentaCampeon + campeon)   
print(comentaFinal)
    
    
    

