class Persona:
    def __init__(self, nombre, edad, descripcion):
        self.nombre = nombre
        self.edad = edad
        self.descripcion = descripcion

    def trabajar(self):
        pass

    def descansar(self):
        pass

    def jugar(self):
        pass

    def pago(self):
        pass

class Gerente(Persona):

    def __init__(self):
        super().__init__()

    def manejar_cajero(self):
        pass

    def manejar_cocinero(self):
        pass

    def gestionar_costos(self):
        pass


class Cliente(Persona):
    def __init__(self, nivel_emocion, accion_actual, estado_animo):
        super().__init__
        self.nivel_emocion = nivel_emocion
        self.accion_actual = accion_actual
        self.estado_animo = estado_animo

    def descansar(self):
        pass

    def jugar(self):
        pass

    def pago(self):
        pass


    def comer(self):
        pass

    def recorrer(self):
        pass


class cajero(Persona):

    def __init__(self, nivel_felicidad, accion_actual, barra_cansancio):
        super().__init__()
        self.nivel_felicidad = nivel_felicidad
        self.accion_actual = accion_actual
        self.barra_cansancio = barra_cansancio
    

    def trabajar(self):
        pass

    def jugar(self):
        pass

    def pago(self):
        pass


    def interactuar_clientes(self):
        pass

    def limpiar(self):
        pass

class Cocinero(Persona):
    def __init__(self, barra_cansancio):
        super().__init__()
        self.barra_cansancio = barra_cansancio

    def trabajar(self):
        pass

    def descansar(self):
        pass

    def entregar_comida(self):
        pass
