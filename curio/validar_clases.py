class Padresito:
    """docstring for Padresito."""

    def __init__(self, a):
        if Padresito.validar(a):
            self.a = a
        else:
            print("mala a, no creamos el objeto")

    @staticmethod
    def validar(a):
        try:
            if type(a) == str:
                return True
            else:
                raise ValueError()
        except ValueError:
            print('No es una cadena')
            return False


# p1 = Padresito("Pepe")
# p2 = Padresito(33)

Padresito.validar(33)
