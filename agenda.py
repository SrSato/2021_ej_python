import utilidades
import json
from contacto import Contacto


class Agenda:
    """docstring for Agenda."""

    def __init__(self):
        self.contactos = []

    def add_contacto(self, contacto):
        if contacto not in self.contactos:
            self.contactos.append(contacto)
            return True
        return False

    def pide_nuevo(self):
        nombre = utilidades.pideFrase("Nombre : ")
        apellido1 = utilidades.pideFrase("Apellido 1: ")
        apellido2 = utilidades.pideFrase("Apellido 2: ")
        telefono = int(utilidades.pideNumero("Tfno: "))
        direccion = input("Dirección: ")
        email = utilidades.pideFrase("E-Mail: ")
        nuevo_contacto = Contacto(
            nombre, apellido1, apellido2, telefono, direccion, email)
        self.add_contacto(nuevo_contacto)
        return nuevo_contacto

    def leer_agenda(self):
        print("\nAgenda:\n===============================================")
        for contacto in self.contactos:
            contacto.muestra()

    def actualizar_contacto(self, contacto):
        if contacto in self.contactos:
            contacto.nombre = utilidades.pideFrase("Nuevo nombre: ")
            contacto.apellido = utilidades.pideFrase("Nuevo apellido: ")
            contacto.telefono = utilidades.pideNumero("Nuevo teléfono: ")
            return True
        else:
            return False

    def elimina_contacto(self, contacto):
        if contacto in self.contactos:
            self.contactos.remove(contacto)
            return True
        else:
            return False

    def buscar_nombre(self):
        nombre = utilidades.pideFrase("Nombre a buscar: ")
        res = []
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                res.append(contacto)
        print(f"Contactos con ese nombre: ({len(res)})\n")
        for contacto in res:
            contacto.muestra()
        print("-------FIN---------")

    def guarda_fichero(self):
        stream = "{\"contactos\":["
        for contacto in self.contactos:
            procesado = json.dumps(contacto.to_json())
            if self.contactos.index(contacto) != len(self.contactos)-1:
                procesado = procesado + ","
            stream = stream + procesado
        stream = stream + "]}"
        utilidades.escribir("agenda.json", "w", stream)

    def lee_fichero(self):
        guardados = utilidades.leer("agenda.json")
        guardados = json.loads(guardados)
        listado = list(guardados['contactos'])
        for persona in listado:
            nuevo_contacto = Contacto(
                                        persona['nombre'],
                                        persona['apellido1'],
                                        persona['apellido2'],
                                        persona['telefono'],
                                        persona['direccion'],
                                        persona['email'])
            self.add_contacto(nuevo_contacto)
