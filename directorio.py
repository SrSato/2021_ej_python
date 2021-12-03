'''Clase Directorio'''
import json
import datetime
from empleado import Empleado
import utilidades


class Directorio:
    """Clase para la gestión de personal de una empresa."""

    def __init__(self):
        ''' Crea el directorio vacio'''
        self.empleados = []
        self.registro = []

    def add_empleado(self, empleado):
        ''' Añade un empleado existente al directorio'''
        if empleado not in self.empleados:
            self.empleados.append(empleado)
            return True
        return False

    def pide_nuevo(self):
        ''' Pide inputs para crear un empleado y lo añade al directorio'''
        nuevo = Empleado.pide_nuevo()
        self.add_empleado(nuevo)

    def leer_directorio(self):
        ''' Muestra por pantalla todo el directorio '''
        print("\tDirectorio de Empleados:")
        print("\t=========================")
        for empleado in self.empleados:
            empleado.muestra()

    def buscar_nombre(self):
        ''' ToDO: Cambiar el pideFrase()
            Pide un nombre y muestra todos los empleados que coinciden'''
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
        ''' Dada una id nos devuelve el empleado que correponde
            o None si no existe '''
        for empleado in self.empleados:
            if empleado.datos["matricula"] == id:
                return empleado
        return None

    def fichar_entrada(self):
        ''' Pide numero de matricula y fecha. Crea un servicio en
            el empleado con esa matricula con entrada=fecha que le digamos
            y salida=a la misma fecha, pero a la HORA_MAX y MIN_MAX'''
        id = utilidades.pideNumero("Dame la matícula: ")
        empleado = self.buscar_id(id)
        entrada = utilidades.pide_fecha(
            "Dame la fecha de inicio de servicio: ")
        empleado.entrar(entrada)
        empleado.muestra_servicios()

    def fichar_salida(self):
        ''' Pide num de matricula, num de servicio y hora y minutaje del cierre.
            Modifica la hora y minuto de la salida de ese servicio'''
        id = utilidades.pideNumero("Dame la matícula: ")
        empleado = self.buscar_id(id)
        num = int(utilidades.pideNumero(
            "Dame el num del servicio: "))
        hora = int(utilidades.pideNumero(
            "Dame la hora de salida: "))
        minuto = int(utilidades.pideNumero(
            "Dame el minutaje de salida: "))
        empleado.salir(num, hora, minuto)

    def horas_ser(self, servicio):
        entrada = datetime.datetime(
                                    servicio[0][0],
                                    servicio[0][1],
                                    servicio[0][2],
                                    servicio[0][3],
                                    servicio[0][4])
        salida = datetime.datetime(
                                    servicio[1][0],
                                    servicio[1][1],
                                    servicio[1][2],
                                    servicio[1][3],
                                    servicio[1][4])
        return salida-entrada

    def horas_mes(self):
        anyo = int(utilidades.pideNumero(
            "Dame el año a estudiar: "))
        mes = int(utilidades.pideNumero(
            "Dame el mes a estudiar: "))
        listado = []
        for empleado in self.empleados:
            horas_sem_emp = 0
            inicial, servicios = empleado.servicios_mes_semanas(anyo, mes)
            for servicio in servicios:
                horas_sem_emp = horas_sem_emp + self.horas_ser(servicio)

        # for empleado in self.empleados:
        #     servicios = empleado.servicios_mes(anyo, mes)
        #     if servicios:
        #         listado.append([empleado.datos["matricula"], servicios])
        # if not listado:
        #     print("No hay registros para ese mes.")
        #     return False
        # print(listado)
        # # Hasta aquí funciona 03/12/2021
        # semana_inicial = datetime.datetime(
        #     anyo, mes, 1, 0, 0).isocalendar()[1]
        # for i in range(semana_inicial, semana_inicial+4):
        #     semanal = []
        #     curris_semana = []
        #     totales = datetime.datetime(
        #         2020, 1, 1, 0, 0, 1) - datetime.datetime(2020, 1, 1, 0, 0, 0)
        #     for registro in listado:
        #         entrada = registro[1][0][0]
        #         salida = registro[1][0][1]
        #         semana = datetime.datetime(
        #             entrada[0], entrada[1], entrada[2]).isocalendar()[1]
        #         if semana == i:
        #             semanal.append(registro)
        #     print(f"Semana {i}:")
        #     for caso in semanal:
        #         trabajador = caso[0]
        #         if trabajador not in curris_semana:
        #             curris_semana.append(trabajador)
        #         entrada = caso[1][0][0]
        #         entrada = datetime.datetime(
        #             entrada[0], entrada[1], entrada[2], entrada[3], entrada[4])
        #         salida = caso[1][0][1]
        #         salida = datetime.datetime(
        #             salida[0], salida[1], salida[2], salida[3], salida[4])
        #         horas = salida-entrada
        #         totales = totales + horas
        #         horas, minutos, segundos = utilidades.convert_timedelta(horas)
        #         print(
        #             f"Trabajador num {trabajador}: horas = {horas}:{minutos}")
        #     totales_horas, totales_min, totales_seg = utilidades.convert_timedelta(
        #         totales)
        #     print(
        #         f"Trabajadores: {len(curris_semana)} - Horas totales: {totales_horas}h y {totales_min}min")

    def guardar(self):
        ''' Guarda el directorio en formato json en "directorio.json"
            dentro de la misma carpeta en la que esté "directorio.py" '''
        stream = "{\"empleados\":["
        for empleado in self.empleados:
            procesado = empleado.to_json()
            if self.empleados.index(empleado) != len(self.empleados)-1:
                procesado = procesado + ","
            stream = stream + procesado
        stream = stream + "]}"
        utilidades.escribir("directorio.json", "w", stream)

    def cargar(self):
        ''' Intenta leer el fichero "directorio.json" de la misma carpeta
        la que esté "directorio.py" y carga los datos leidos
        en el directorio '''
        guardados = utilidades.leer("directorio.json")
        if guardados:
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
                    empleado['activo'],
                    empleado['servicios'])
                self.add_empleado(nuevo_empleado)
