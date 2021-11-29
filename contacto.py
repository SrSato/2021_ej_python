'''Clase Contacto'''


class Contacto:
    """docstring for Contacto."""

    def __init__(self, nombre, apellido, telefono, direccion, email):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.email = email

    def muestra(self):
        print(f'''
                Contacto:
                ---------
                Nombre :    {str(self.nombre)}
                Apellido :  {str(self.apellido)}
                Tfno :      {str(self.telefono)}
                Dirección : {str(self.direccion)}
                email:      {str(self.email)}
                '''
              )
