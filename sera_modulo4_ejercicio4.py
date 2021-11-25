import random
import utilidades

def loteria(bolas):
    if bolas==0:
        return None
        
    num=[]
    num.append(str(random.randint(1,9)))
    bolas=bolas-1

    for index in range(bolas):
        num.append(str(random.randint(0,9)))

    num=int("".join(num))

    return num

digitos=int(utilidades.pideNumero("Dame la cantidad de dígitos: "))
print(loteria(digitos))
