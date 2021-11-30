'''Clase Contacto'''


class Contacto:
    """docstring for Contacto."""

    def __init__(
                    self,
                    nombre="",
                    apellido1="",
                    apellido2="",
                    telefono=0,
                    direccion="",
                    email="",
                    ):
        '''Constructor de Contacto. Tiene valores por defecto'''
        if Contacto.valida_campo(nombre, str):
            self.nombre = nombre
        if Contacto.valida_campo(apellido1, str):
            self.apellido1 = apellido1
        if Contacto.valida_campo(apellido2, str):
            self.apellido2 = apellido2
        if Contacto.valida_campo(telefono, int):
            self.telefono = telefono
        if Contacto.valida_campo(direccion, str):
            self.direccion = direccion
        if Contacto.valida_campo(email, str):
            self.email = email

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
                Contacto:
                ---------
                Nombre :        {str(self.nombre)}
                1er Apellido :  {str(self.apellido1)}
                2do Apellido :  {str(self.apellido2)}
                Tfno :          {str(self.telefono)}
                Dirección :     {str(self.direccion)}
                email:          {str(self.email)}
                '''
              )

    def to_str(self):
        return f'''
                Contacto:
                ---------
                Nombre :        {str(self.nombre)}
                1er Apellido :  {str(self.apellido1)}
                2do Apellido :  {str(self.apellido2)}
                Tfno :          {str(self.telefono)}
                Dirección :     {str(self.direccion)}
                email:          {str(self.email)}
                '''

    def to_json(self):
        res = {
                "nombre": self.nombre,
                "apellido1": self.apellido1,
                "apellido2": self.apellido2,
                "telefono": self.telefono,
                "direccion": self.direccion,
                "email": self.email
        }
        return res
