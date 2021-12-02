'''Clase Directorio'''
import json
from empleado import Empleado
import utilidades


class Directorio:
    """docstring for Directorio."""

    def __init__(self):
        self.empleados = []
        self.registro = []

    def add_empleado(self, empleado):
        if empleado not in self.empleados:
            self.empleados.append(empleado)
            return True
        return False

    def leer_directorio(self):
        print("\tDirectorio de Empleados:")
        print("\t=========================")
        for empleado in self.empleados:
            empleado.muestra()

    def buscar_nombre(self):
        ''' ToDO: Cambiar el pideFrase() '''
        nombre = utilidades.pideFrase("Nombre a buscar: ")
        res = []
        for empleado in self.empleados:
            if empleado.datos["nombre"] == nombre:
                res.append(empleado)
        print(f"empleados con ese nombre: ({len(res)})\n")
        for empleado in res:
            empleado.muestra()
        print("-------FIN---------")

    def buscar_id(self, id):
        ''' '''
        for empleado in self.empleados:
            if empleado.datos["matricula"] == id:
                return empleado
        return None

    def fichar_entrada(self):
        id = utilidades.pideNumero("Dame tu matícula: ")
        empleado = self.buscar_id(id)
        entrada = utilidades.pide_fecha(
            "Dame la fecha de inicio de servicio: ")
        empleado.entrar(entrada)
        print(empleado.servicios)

    def fichar_salida(self):
        id = utilidades.pideNumero("Dame tu matícula: ")
        empleado = self.buscar_id(id)
        entrada = utilidades.pide_fecha(
            "Dame la fecha de fin de servicio: ")

    def to_json(self):
        res = json.dumps(self.empleados, ensure_ascii=False, indent=4)
        return res

    def guardar(self):
        stream = "{\"empleados\":["
        for empleado in self.empleados:
            procesado = empleado.to_json()
            if self.empleados.index(empleado) != len(self.empleados)-1:
                procesado = procesado + ","
            stream = stream + procesado
        stream = stream + "]}"
        utilidades.escribir("directorio.json", "w", stream)

    def cargar(self):
        guardados = utilidades.leer("directorio.json")
        guardados = json.loads(guardados)
        listado = list(guardados['empleados'])
        for empleado in listado:
            nuevo_empleado = Empleado(
                                        empleado['matricula'],
                                        empleado['nombre'],
                                        empleado['apellido1'],
                                        empleado['apellido2'],
                                        empleado['telefono'],
                                        empleado['direccion'],
                                        empleado['email'],
                                        empleado['activo'])
            self.add_empleado(nuevo_empleado)

    def pide_nuevo(self):
        nuevo = Empleado.pide_nuevo()
        self.add_empleado(nuevo)
