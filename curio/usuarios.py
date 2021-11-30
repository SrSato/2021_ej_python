import json


def leer(fichero):
    chicha = ""
    try:
        f = open(fichero)
        chicha = f.read()
        f.close()
    except:
        print("No se ha podidio leer el fichero")
    print(chicha)
    return chicha


def escribir(fichero, metodo, chicha):
    try:
        f = open(fichero, metodo, encoding='utf8')
        f.write(chicha)
        f.close()
        return True
    except:
        print("No se ha podidio abrir el fichero")
        return False


modelo = leer("bd.json")
print(modelo)

if modelo == "Joñefo":
    modelo = "Será"
else:
    modelo = "Joñefo"

# Falta mirar json.dumps

escribir("bd.json", "w", modelo)
