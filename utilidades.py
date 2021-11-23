def es_numero(cosa):
    try:
        float(cosa)
        return True
    except ValueError:
        return False

def es_letra(cosa):
    return str(cosa).isalpha()

def pideNumero(peticion):
    numero=input(peticion)
    while es_numero(numero) == False :
        numero=input('No me has dado un número, por favor dame un número: ')    
    return float(numero)

def pideFrase(peticion):
    palabra=input(peticion)
    while es_letra(palabra) == False:
        palabra=input('Ups... Por favor, revisa espacios y caracteres raros y vuelve a introducir la palabra: ')    
    return str(palabra)