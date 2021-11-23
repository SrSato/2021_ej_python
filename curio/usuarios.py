import json
import codecs

def leer(fichero):
    chicha=""
    try:
        f = open(fichero)
        chicha=f.read()
        f.close()
    except:
        print("No se ha podidio leer el fichero")
    return chicha

def escribir(fichero, chicha):
    try:
        f = open(fichero,"w")
        f.write(chicha)
        f.close()
        return True
    except:
        print("No se ha podidio abrir el fichero")
        return False



modelo=leer("bd.json")
if modelo!="":
    modelo=json.loads(modelo)

modelo["usuarios"][1]["usuario"]="Josefo"
modelo=json.dumps(modelo, indent=4)

escribir("bd.json",modelo)
