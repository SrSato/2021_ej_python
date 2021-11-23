import utilidades

def pideEntero(frase):
    return int(utilidades.pideNumero(frase))

num1=pideEntero("Dame un entero: ")
num2=pideEntero("Dame otro: ")

print(f"Me has dado {num1} y {num2}")
