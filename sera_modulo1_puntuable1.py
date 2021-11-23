''' 1. Enseñamos la fecha (dia mes año y nombre del dia)
    2. Calorias ingeridas en el desayuno (aleatorio<300)
    3. Calorias comida pedidas al usuario
    4. Calorias cena pedidas al user
    5. Calorias tentempie
    6. Mostrar calorias pormenorizadas y sumadas para ese dia
    7. Con un total de 15000, hacer el plan semanal
    8. Iniciales SMQ en binario
    OJO: Todo sin decimales'''

import datetime
import random
import utilidades


nom_semana=["Domingo","Lunes","Martes","Miércoles","Jueves","Viernes", "Sábado"]
fecha=datetime.datetime.now()

print("\nHoy es",fecha.day,"del",fecha.month,"del año",fecha.year,",",nom_semana[eval(fecha.strftime("%w"))])

totalSemana = 15000
desayuno = random.randint(0,300)
comida = utilidades.pideNumero("\nDime cuántas calorias has tomado en la comida: ")
cena = utilidades.pideNumero("Dime cuántas calorias has tomado en la cena: ")
tentempie = utilidades.pideNumero("Dime cuántas calorias has tomado de picoteo: ")
total = desayuno+comida+cena+tentempie
diasFaltan=7-eval(fecha.strftime("%w"))
promedio = (totalSemana-total)/diasFaltan
promedio = round(promedio,0)
promedio = int(promedio)
dev=["S","M","Q"]


print("\nInforme del dia:\n------------------------")
print("para desayunar...",desayuno)
print("para comer...",comida)
print("para cenar...",cena)
print("de tentempié...",tentempie)
print("------------------------\nEn total consumidas hoy:",total,"\n")
print("Como hoy es", nom_semana[eval(fecha.strftime("%w"))] ,
      ", nos quedan",diasFaltan,"días en esta semana.\nCada día deberías comer no más de",
       promedio,"calorias para ajustarte a las", totalSemana, "calorias de tu plan semanal.\n")

for letra in dev:
    print("Binario de",letra, ":")
    print(bin(ord(letra)))