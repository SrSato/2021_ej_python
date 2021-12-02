'''
        utilidades es un módulo pensado para comprobar las entradas
        del usuario en nuestros programas.

        Dependencias: Datetime.
'''
import datetime


def es_numero(cosa):
    '''
        Dado un valor cosa evalua si se podría parsear como FLOAT.
        Devulete True si es posible el parseo o False si no es posible.

        return bool

        Dependencias: No tiene.
    '''
    try:
        float(cosa)
        return True
    except ValueError:
        return False


def es_letra(cosa):
    '''
        Dado una cadena cosa evalua si está compuesta de caracteres alfabéticos.
        Devulete True si sólo hay letras o False si tenemos algún caracter especial.

        return bool
    '''
    return str(cosa).isalpha()


def pideNumero(peticion):
    '''
        Muestra una cadena por consola (peticion) para pedir al usuario
        que nos de input.
        Comprueba que ese input es asimilable a un NÚMERO y nos devuelve
        el FLOAT de ese input.
        Si no es asimilable avisa de que buscamos un NÚMERO y
        vuelve a pedir input hasta que sea asimilable.

        return float

        Dependencias: es_numero(cosa) de este mismo módulo
    '''
    numero = input(peticion)
    while es_numero(numero) is False:
        numero = input('No me has dado un número, por favor dame un número: ')
    return float(numero)


def pideFrase(peticion):
    '''
        Muestra una cadena por consola (peticion) para pedir al usuario
        que nos de input.
        Comprueba que ese input es asimilable a una PALABRA (sin espacios o
        caracteres especiales) y nos devuelve el STR de ese input.
        Si no es asimilable avisa de que buscamos una PALABRA y vuelve a pedir
        input hasta que sea asimilable.

        return str

        Dependencias: es_letra(cosa) de este mismo módulo
    '''
    palabra = input(peticion)
    while es_letra(palabra) is False:
        msg = '''Ups... Por favor, revisa espacios y caracteres raros
                 y vuelve a introducir la palabra: '''
        palabra = input(msg)
    return str(palabra)


def es_fechable(anyo, mes, dia, hora, minutos):
    try:
        print(anyo, mes, dia, hora, minutos)
        fecha = datetime.datetime(anyo, mes, dia, hora, minutos)
        return True
    except Exception:
        print("La fecha no es correcta.")
        return False


def pide_fecha(frase):
    print(frase)
    bueno = False
    while not bueno:
        anyo = int(pideNumero("Año: "))
        mes = int(pideNumero("Mes: "))
        while mes < 1 or mes > 12:
            mes = int(pideNumero("Por favor, entre 1(enero) y 12(diciembre): "))
        dia = int(pideNumero("Día: "))
        while dia < 1 or dia > 31:
            dia = int(pideNumero("Por favor, entre 1 y 31: "))
        hora = int(pideNumero("Hora:"))
        while hora < 0 or hora > 23:
            hora = int(pideNumero("Por favor, de 00 a 23"))
        minutos = int(pideNumero("Minutos: "))
        while minutos < 0 or minutos > 59:
            minutos = int(pideNumero("Por favor, entre 00 y 59"))
        bueno = es_fechable(anyo, mes, dia, hora, minutos)
    fecha = datetime.datetime(anyo, mes, dia, hora, minutos)
    return fecha


def leer(fichero):
    '''Lee ficheros todos a piñon'''
    chicha = ""
    try:
        f = open(fichero, encoding='utf8')
        chicha = f.read()
        f.close()
    except:
        print("No se ha podidio leer el fichero")
    return chicha


def leer_archivo_lista_lineas(path, mode):
    '''
    Abre un archivo de una ubicación dada "path"
    Recibe el modo en el que deseamos abrir "w, r, a"
    Almacena cada línea de texto en una fila.
    Devuelve la lista.
    '''
    try:
        input_file = open(path, mode)
        lines = [line.strip() for line in input_file]
    except FileNotFoundError:
        print('El fichero no existe en la ruta proporcionada.')
    else:
        input_file.close()
        return lines


def escribir(fichero, metodo, chicha):
    '''Escribe en utf8 en el fichero que le digamos'''
    try:
        f = open(fichero, metodo, encoding='utf8')
        f.write(chicha)
        f.close()
        return True
    except:
        print("No se ha podidio abrir el fichero")
        return False


def readme():
    '''Doc de utilidades'''
    info = '''
            utilidades es un módulo pensado para comprobar las entradas
            del usuario en nuestros programas.

            Dependencias: No tiene.

            Funciones:
                        pideNumero(peticion)
                            Muestra una cadena por consola (peticion) para pedir al usuario que nos de input.
                            Comprueba que ese input es asimilable a un NÚMERO y nos devuelve el FLOAT de ese input.
                            Si no es asimilable avisa de que buscamos un NÚMERO y vuelve a pedir input hasta que sea asimilable.

                            return float

                            Dependencias: es_numero(cosa) de este mismo módulo

                        pideFrase(peticion)
                            Muestra una cadena por consola (peticion) para pedir al usuario que nos de input.
                            Comprueba que ese input es asimilable a una PALABRA (sin espacios o caracteres especiales)
                            y nos devuelve el STR de ese input.
                            Si no es asimilable avisa de que buscamos una PALABRA y vuelve a pedir input hasta que sea asimilable.

                            return str

                            Dependencias: es_letra(cosa) de este mismo módulo

                        es_numero(cosa)
                            Dado un valor cosa evalua si se podría parsear como FLOAT.
                            Devulete True si es posible el parseo o False si no es posible.

                            return bool

                            Dependencias: No tiene.

                        es_letra(cosa)
                            Dado una cadena cosa evalua si está compuesta de caracteres alfabéticos.
                            Devulete True si sólo hay letras o False si tenemos algún caracter especial.

                            return bool
                '''
    print(info)


if __name__ == "__main__":
    readme()
