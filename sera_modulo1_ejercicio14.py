import utilidades
import random

num=utilidades.pideNumero("Bienvenido a tu Banko. Dime cuánto te queda en la cuenta, anda: ")

print("Temporada de comisiones bancarias!!!:")
while num>0 :
    quedan=num
    quito = random.randint(1,10)
    num=quedan-quito
    print("Si a",quedan,"€ le quito",quito,"ahora tienes",num,"€")

print("Ale, ya debes dinero. Te quedan",num,"€. De nada!")