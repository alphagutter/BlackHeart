#a partir de acá, vienen todas las clases no referentes a personas interactuables, pero si objetos con
#los que las personas pueden interactuar
from abc import ABC, abstractmethod
from humanos import *
from interactuables import *

class Comedor:
    '''Es el objeto de el lugar en si, donde almacenamos la caja donde están los cajeros,
    la cocina donde están los cocinceros, a los clientes que vienen a interactuar, las consolas y los sofás'''
    def __init__(self, nombre):
        self.nombre = nombre
        self.caja = None           #caja, donde están los cajeros y la fila a atender
        self.clientes = []              #array de clientes
        self.consolas = []              #array de consolas
        self.zona_relax = []            #array de sofás
        self.clientes_en_local = []
        self.ya_entraron = []           #clientes que ya entraron en el dia y no pueden entrar de vuelta

    def agregar_trabajador(self, trabajador):
        '''agregamos a los arrays de cada tipo de trabajador de acuerdo al tipo de objeto que nos pasen'''
        if isinstance(trabajador, Cajero):
            self.caja.cajeros.append(trabajador)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    #se agregarán las personas que vayan entrando al local, o irán saliendo respectivamente
    def personas_en_el_local(self, persona_nueva, meter):
        
        if meter == True:
            self.clientes_en_local.append(persona_nueva)
            print(f'Se introdujo al cliente {persona_nueva.nombre}')
        else:
            #guardar el lugar para devolver al estado en como se quedan al array de clientes
            lugar = self.clientes_en_local.indexOf(persona_nueva)
            if lugar >= 0:
                eliminado = self.clientes_en_local.remove(persona_nueva)
                print(f'El cliente {eliminado.nombre} salió')

    


    def agregar_sofas(self, Sofa):
        self.zona_relax.append(Sofa)

    def agregar_consolas(self, Consola):
        self.consolas.append(Consola)


class Caja:

    def __init__(self):
        self.cajeros = []       #array de cajeros
        self.fila = []          #array de clientes

    