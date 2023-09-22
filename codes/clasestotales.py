from abc import ABC, abstractmethod

class Accionable:
    '''pequeña clase abstracta, donde definimos 2 clases a utilizar en distintos tipos, por el que ocurre el simple polimorfismo'''
    @abstractmethod
    def jugar():
        pass
    
    @abstractmethod
    def descansar():
        pass

class Empleado(Accionable):
    '''Es la clase abstracta con la que definimos los empleados del local'''
    
    @abstractmethod
    def limpiar():
        pass




class Cajero(Empleado):
    '''Es el empleado con el que interactuan los clientes, pueden limpiar, atender a los clientes, entre otras cosas'''
    def __init__(self, nombre, barra_cansancio):
        self.nombre = nombre
        self.barra_cansancio = barra_cansancio

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

    def jugar(self):
        '''La barra de cansancio disminuye cuando el cajero juega'''
        
        print('jugando cajero')
        if self.barra_cansancio > 0:
            self.barra_cansancio -= 1
        else:
            print('jugando cajero sin motivo alguno')    




class Cocinero(Empleado):
    '''Es el empleado encargado de cocinar para los clientes, reciben los pedidos que les pasan los cajeros, de acuerdo a su nivel de cansancio, es más rentable o no que cocinen ciertas comidas de seguido'''
    def __init__(self, nombre, barra_cansancio):
        self.nombre = nombre
        self.barra_cansancio = barra_cansancio
        self.pedidos = []    #implementar una lista enlazada

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
    '''Los clientes son el objeto que más interactúa con otros objetos, sus estados cuando se crean son randomizados'''
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
        if self.estado_animo <=3:
            self.estado_animo += 2
        elif self.estado_animo >=3 and self.estado_animo<6:
            self.estado_animo += 1
        else:
            print('Está eufórico, no descansará aunque le obliguen')

    #implementar con el objeto consola
    def jugar(self, Consola):
            if Consola.disponible == False:
                print('Esa consola no está disponible')
            else:
                if self.estado_animo < 3:
                    print('El cliente no jugará ni aunque le obliguen')
                    return False
                elif self.estado_animo >= 3 and self.estado_animo < 6:
                    print(f'El cliente {self.nombre} está jugando a la consola {Consola.nombre}')
                    self.entusiasmo += 1
                    return False
                else:
                    print(f'El cliente {self.nombre} está jugando a la consola {Consola.nombre}')
                    self.entusiasmo += 3
                    return False

    # def jugar(self):
    #     print('jugando cliente')

    #implementar con el objeto comida y objeto mesa
    def comer(self):
        pass

    #implementar con 
    def entrar_fila(self):
        pass




#a partir de acá, vienen todas las clases no referentes a personas interactuables, pero si objetos con
#los que las personas pueden interactuar

class Comedor:
    '''Es el objeto de el lugar en si, donde almacenamos la caja donde están los cajeros,
    la cocina donde están los cocinceros, a los clientes que vienen a interactuar, las consolas y los sofás'''
    def __init__(self, nombre):
        self.nombre = nombre
        self.caja = []          #array de cajeros
        self.cocina = []        #array de cocineros
        self.clientes = []      #array de clientes
        self.consolas = []      #array de consolas
        self.zona_relax = []    #array de sofás
        self.total_accionable = []

    #acá agregamos a los arrays de cada tipo de trabajador de acuerdo al tipo de objeto que nos pasen
    def agregar_trabajador(self, trabajador):
        if isinstance(trabajador, Cajero):
            self.caja.append(trabajador)
        elif isinstance(trabajador, Cocinero):
            self.caja.append(trabajador)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    #esto es solo para probar si funciona mi reconexón polimorfa
    def agregar_personas(self):
        self.total_accionable = self.caja

    #implmementar la creacion del mapa
    def recorrer(self):
        pass


class Sofa:
    '''Objeto con el que los objetos que heredan de "Accionable" pueden descansar'''
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
    '''Las consolas con las que los clientes/cajeros pueden jugar, cambian su disponibilidad si alguno las está usando, cambian los estados de las personas'''
    def __init__(self, nombre, disponible = True):
        self.nombre = nombre
        self.disponible = disponible

    #el print es distinto si la consola está en uso o no
    def jugar(self):
        if self.disponible == False:
            print(f'La consola{self.nombre} está ocupada')
        else:
            self.disponible = False
            print(f'Jugando en la consola {self.nombre}')

class Comida:
    '''Las comidas cambian el estado de hambre de los clientes'''
    def __init__(self, nombre, nivel_sabor, nivel_complejidad):
        self.nombre = nombre
        self.nivel_sabor = nivel_sabor
        self.nivel_complejidad = nivel_complejidad

    def comer(self):
        pass


class Mesa:
    '''Las mesas son utilizadas por los clientes cuando comen, cambian su disponibilidad cuando algún cliente las usa'''
    def __init__(self, numero_mesa):
        self.numero_mesa = numero_mesa
        self.disponible = True

    def sentarse(self):
        if(self.disponible == False):
            print('la mesa está ocupada')
        else:
            print(f'El cliente está sentado en la mesa {self.numero_mesa}')