import utilidades
import random

numero=random.randint(1,10)
intento=utilidades.pideNumero("A ver cómo vas de telepatía... He pensado un número del 1 al 10, ¿cuál es? :")
contador=1

while numero != intento :
    intento=utilidades.pideNumero("Noooop... Inténtalo otra vez :")
    contador=contador + 1

print("Tenemos un mago en la sala!!! Era el ",numero,"\n Lo has conseguido en",contador,"intentos")
