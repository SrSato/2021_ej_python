import json

def leer(fichero):
    chicha=""
    try:
        f = open(fichero)
        chicha=f.read()
        f.close()
    except:
        print("No se ha podidio leer el fichero")
    return chicha



modelo=leer("bd.json")
if modelo!="":
    modelo=json.loads(modelo)

print(modelo)
