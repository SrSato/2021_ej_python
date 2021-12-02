'''Clase Empleado version 0.2'''
import json
import datetime
import utilidades


class Empleado:
    """docstring for Empleado."""

    def __init__(
                    self,
                    matricula=0,
                    nombre="",
                    apellido1="",
                    apellido2="",
                    telefono=0,
                    direccion="",
                    email="",
                    activo=False
                    ):
        '''Constructor de Empleado. Tiene valores por defecto'''
        self.datos = {}
        self.servicios = []
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
                '''

    def to_json(self):
        res = json.dumps(self.datos, ensure_ascii=False, indent=4)
        return res

    def entrar(self, fecha):
        entrada = fecha
        # salida = datetime.datetime(
        #     entrada.year(), entrada.month(), entrada.day(), 23, 59)
        salida = "jas jas"
        self.servicios.append([entrada, salida])
