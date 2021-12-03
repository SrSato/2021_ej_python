'''Clase Empleado version 0.2'''
import json
import datetime
import utilidades


class Empleado:
    """Clase que modela un trabajador genérico."""

    HORA_MAX = 23  # Más allá de HORA_MAX:MIN_MAX no se puede trabajar.
    MIN_MAX = 59   # Por defecto, las jornadas acaban a las 23:59

    def __init__(
                    self,
                    matricula=0,
                    nombre="",
                    apellido1="",
                    apellido2="",
                    telefono=0,
                    direccion="",
                    email="",
                    activo=False,
                    servicios=[]
                    ):
        '''Constructor de Empleado. Tiene valores por defecto'''
        self.datos = {}
        if Empleado.valida_campo(matricula, int):
            self.datos["matricula"] = matricula
        if Empleado.valida_campo(nombre, str):
            self.datos["nombre"] = nombre
        if Empleado.valida_campo(apellido1, str):
            self.datos["apellido1"] = apellido1
        if Empleado.valida_campo(apellido2, str):
            self.datos["apellido2"] = apellido2
        if Empleado.valida_campo(telefono, int):
            self.datos["telefono"] = telefono
        if Empleado.valida_campo(direccion, str):
            self.datos["direccion"] = direccion
        if Empleado.valida_campo(email, str):
            self.datos["email"] = email
        if Empleado.valida_campo(activo, bool):
            self.datos["activo"] = activo
        if Empleado.valida_campo(servicios, list):
            self.datos["servicios"] = servicios

    @staticmethod
    def pide_nuevo():
        print("\nIntroduce los datos del nuevo empleado:\n")
        matricula = int(utilidades.pideNumero("Matricula: "))
        nombre = utilidades.pideFrase("Nombre: ")
        apellido1 = utilidades.pideFrase("Primer Apellido: ")
        apellido2 = utilidades.pideFrase("Segundo Apellido: ")
        telefono = int(utilidades.pideNumero("Tfno.: "))
        direccion = input("Dirección: ")
        email = input("E-mail: ")
        activo = bool(utilidades.pideFrase(
            "¿En alta actualmente? (True,False): "))
        trabajador = Empleado(
                                matricula,
                                nombre,
                                apellido1,
                                apellido2,
                                telefono,
                                direccion,
                                email,
                                activo
                                )
        return trabajador

    @staticmethod
    def valida_campo(campo, tipo_ok):
        '''Devuelve True si campo es de tipo tipo_ok y False si no lo es.'''
        res = False
        try:
            if isinstance(campo, tipo_ok):
                res = True
            else:
                raise ValueError()
        except ValueError:
            print(
                f'El valor {str(campo)} es de tipo {str(type(campo))}. Se esperaba {tipo_ok}')
        return res

    def muestra(self):
        print(f'''
                Empleado:
                ---------
                Matricula :     {str(self.datos["matricula"])}
                Nombre :        {str(self.datos["nombre"])}
                1er Apellido :  {str(self.datos["apellido1"])}
                2do Apellido :  {str(self.datos["apellido2"])}
                Tfno :          {str(self.datos["telefono"])}
                Dirección :     {str(self.datos["direccion"])}
                email:          {str(self.datos["email"])}
                Activo:         {str(self.datos["activo"])}
                '''
              )
        self.muestra_servicios()

    def to_str(self):
        return f'''
                Empleado:
                ---------
                Matricula :     {str(self.datos["matricula"])}
                Nombre :        {str(self.datos["nombre"])}
                1er Apellido :  {str(self.datos["apellido1"])}
                2do Apellido :  {str(self.datos["apellido2"])}
                Tfno :          {str(self.datos["telefono"])}
                Dirección :     {str(self.datos["direccion"])}
                email:          {str(self.datos["email"])}
                Activo:         {str(self.datos["activo"])}
                Servicios:      {str(self.datos["servicios"])}
                '''

    def to_json(self):
        res = json.dumps(self.datos, ensure_ascii=False, indent=4)
        return res

    def entrar(self, fecha):
        entrada = fecha
        salida = [entrada[0], entrada[1],
                  entrada[2], self.HORA_MAX, self.MIN_MAX]
        self.datos["servicios"].append([entrada, salida])

    def salir(self, servicio, hora, minuto):
        if hora < 0 or hora > 23 or minuto < 0 or minuto > 59:
            return False
        self.datos["servicios"][servicio][1][3] = hora
        self.datos["servicios"][servicio][1][4] = minuto
        return True

    def muestra_servicios(self):
        servicios = self.datos["servicios"]
        print(
            f"\t\tHoja de Servicios de trabajador nº: {self.datos['matricula']}")
        for servicio in servicios:
            entrada = datetime.datetime(
                        servicio[0][0],
                        servicio[0][1],
                        servicio[0][2],
                        servicio[0][3],
                        servicio[0][4]
                        )
            salida = datetime.datetime(
                        servicio[1][0],
                        servicio[1][1],
                        servicio[1][2],
                        servicio[1][3],
                        servicio[1][4]
                        )
            print(f"\t\t\tServicio num. {servicios.index(servicio)}")
            print(
                f"\t\t\t\tSemana {entrada.isocalendar()[1]} Entrada: {entrada} - Salida: {salida}")

    def servicios_anyo(self, anyo):
        res = []
        servicios = self.datos["servicios"]
        for servicio in servicios:
            if servicio[0][0] == anyo:
                res.append(servicio)
        return res

    def servicios_mes(self, anyo, mes):
        res = []
        servicios = self.servicios_anyo(anyo)
        for servicio in servicios:
            if servicio[0][1] == mes:
                res.append(servicio)
        return res

    def servicios_mes_semanas(self, anyo, mes):
        res = []

        servicios = self.servicios_mes(anyo, mes)
        semana_inicial = datetime.datetime(anyo, mes, 1, 0, 0).isocalendar()[1]
        for semana in range(semana_inicial, semana_inicial+4):
            semanal = []
            for servicio in servicios:
                anyo_ser = servicio[0][0]
                mes_ser = servicio[0][1]
                dia_ser = servicio[0][2]
                num_semana_ser = datetime.datetime(
                    anyo_ser, mes_ser, dia_ser, 0, 0).isocalendar()[1]
                if num_semana_ser == semana:
                    semanal.append(servicio)
            res.append(semanal)
        return semana_inicial, res
