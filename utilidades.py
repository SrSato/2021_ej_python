'''
        utilidades es un módulo pensado para comprobar las entradas
        del usuario en nuestros programas.

        Dependencias: No tiene.
'''


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
