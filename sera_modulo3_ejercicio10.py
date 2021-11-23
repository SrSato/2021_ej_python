#Escribir unas cuantas preguntas con sus respuestas y que se muestren de forma aleatoria.
import random

preguntas=[["¿1+1?","2"],["¿Abril?","Cerral"],["Cú cú","Tras tras"],["¿3*2?","6"],["Raiz de -1","i"],["¿Qué tengo en el bolsillo?","Mi tesoro"],["¿Qué tiempo hace fuera?","TypeError: Fuera--- EZo que ez lo que ez????"]]
aciertos=0
random.shuffle(preguntas)
print("El Preguntón!!! Aciertalas todas si puedes...")
for i in range(0, len(preguntas)):
    print(f"PREGUNTA - {preguntas[i][0]} :")
    respuesta = input("RESPUESTA: ")
    if respuesta == preguntas[i][1]:
        print("Respuesta correcta!!!")
        aciertos=aciertos+1
    else:
        print(f"Incorrecto. La respuesta correcta era {preguntas[i][1]}")

print(f"Has acertado {aciertos} de {len(preguntas)}\nGracias por participar")
