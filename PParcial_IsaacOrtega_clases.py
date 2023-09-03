from abc import ABC, abstractmethod

class Accionable:
    @abstractmethod
    def jugar():
        pass
    
    @abstractmethod
    def descansar():
        pass

class Empleado(Accionable):
    def __init__(self, nombre, barra_cansancio):
        self.nombre = nombre
        self.barra_cansancio = barra_cansancio
    
    @abstractmethod
    def limpiar():
        pass

class Cajero(Empleado):
    '''Es el empleado con el que interactuan los clientes, pueden limpiar, atender a los clientes, entre otras cosas'''
    def __init__(self, nombre, barra_cansancio):
        super().__init__(nombre, barra_cansancio)

    #implementar mejor con el objeto sofa
    def descansar(self):
        if self.barra_cansancio == 0:
            print('El cajero está completamente descansado')
        elif self.barra_cansancio > 10:
            self.barra_cansancio -= 1
            print('El cajero está punto de colapsar')
        else: 
            self.barra_cansancio -= 1

    def limpiar(self):
        pass

    def sugerir_accion(self):
        pass

    def atender_fila(self):
        pass


class Cocinero(Empleado):
    '''Es el empleado encargado de cocinar para los clientes, reciben los pedidos que les pasan los cajeros, de acuerdo a su nivel de cansancio, es más rentable o no que cocinen ciertas comidas de seguido'''
    def __init__(self, nombre, barra_cansancio, pedidos):
        super().__init__(nombre, barra_cansancio)
        self.pedidos = pedidos    #implementar una lista enlazada

    #seguir implementando
    def cocinar(self):
        for self.pedidos in self.pedidos:
            if(self.pedidos == None):
                print('no hay pedidos')
            else:
                pass

    def limpiar(self):
        pass

    def descansar(self):
        if self.barra_cansancio == 0:
            print('El cocinero está completamente descansado')
        elif self.barra_cansancio > 10:
            self.barra_cansancio -= 1
            print('El cocinero está punto de colapsar')
        else: 
            self.barra_cansancio -= 1 

    def entregar_comida(self):
        pass

class Cliente(Accionable):
    ''''''
    def __init__(self, nombre, entusiasmo, estado_animo, hambre):
        self.nombre = nombre
        self.entusiasmo = entusiasmo
        self.estado_animo = estado_animo
        self.hambre = hambre

    #implementar con la matriz de mapa
    def recorrer(self):
        pass

    #implementar con el objeto sofa
    def descansar(self):
        pass

    def jugar(self):
        pass

    def comer(self):
        pass

    def entrar_fila(self):
        pass

class Comedor:
    ''''''
    def __init__(self, caja, cocina, clientes, consolas, zona_relax):
        self.caja = caja
        self.cocina = cocina
        self.clientes = clientes
        self.consolas = consolas
        self.zona_relax = zona_relax

    #implmementar la creacion del mapa
    def recorrer(self):
        pass


class Sofa:
    ''''''
    def __init__(self, color, nivel_comodidad):
        self.color = color
        self.nivel_comodidad = nivel_comodidad
        self.disponible = True

    #implementar prestandole a cliente
    def descansar(self, disponible):
        if disponible:
            #prestar al cliente
            pass
        else:
            self.disponible = False

class Consola:
    ''''''
    def __init__(self, nombre):
        self.nombre = nombre
        self.disponible = True

    def jugar(self):
        pass

class Comida:
    def __init__(self, nombre, nivel_sabor, nivel_complejidad):
        self.nombre = nombre
        self.nivel_sabor = nivel_sabor
        self.nivel_complejidad = nivel_complejidad
